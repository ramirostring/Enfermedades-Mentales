from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import json
import os
from keras_nlp.models import DebertaV3Preprocessor, DebertaV3Classifier

app = FastAPI(title="Mental Health Classification API")

model = None
preprocessor = None
label_map = None

@app.on_event("startup")
async def load_model():
    global model, preprocessor, label_map
    
    try:
        # 1. Cargar preprocesador
        preprocessor = DebertaV3Preprocessor.from_preset(
            "deberta_v3_extra_small_en", 
            sequence_length=113
        )
        
        # 2. Construir modelo con preprocesador integrado
        model = DebertaV3Classifier.from_preset(
            "deberta_v3_extra_small_en",
            preprocessor=preprocessor,
            num_classes=7,
            activation='softmax'
        )
        
        # 3. Cargar pesos desde archivo .keras
        model.load_weights(os.path.join("model", "classifier_weights.keras"))
        
        # 4. Cargar etiquetas
        with open(os.path.join("model", "label_mapping.json")) as f:
            label_map = json.load(f)
            
        # 5. Warm-up inference
        _ = model.predict(["Test input"])
            
    except Exception as e:
        raise RuntimeError(f"Error loading model: {str(e)}")

class TextRequest(BaseModel):
    text: str

class PredictionResponse(BaseModel):
    prediction: str
    confidence: float
    status: str

@app.post("/predict", response_model=PredictionResponse)
async def predict(request: TextRequest):
    try:
        prediction = model.predict([request.text])
        class_id = np.argmax(prediction)
        confidence = float(np.max(prediction))
        
        return {
            "prediction": label_map[str(class_id)],
            "confidence": round(confidence, 4),
            "status": "success"
        }
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction error: {str(e)}"
        )

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
