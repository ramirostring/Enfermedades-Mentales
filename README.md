# Proyecto de Predicción de Enfermedades Mentales

## Instrucciones

1. **Puente SSH**:
   ```bash
   bash scripts/ssh_tunnel.sh
   ```

2. **Para instalar RPM con Ansible**:
   ```bash
   ansible-playbook -i ansible/inventory ansible/instalar_rpm.yml
   ```

3. **Desplegar API**:
   ```bash
   cd api
   docker-compose up --build
   ```

4. **Pruebas E2E**:
   ```bash
   python3 tests/test_api.py
   ```

5. **Probar desde el terminal de Linux**:
   ```bash
   curl -X POST "http://localhost:8000/predict" \
   -H "Content-Type: application/json" \
   -d '{"text": "I have persistent thoughts about ending my life"}'
