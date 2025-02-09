# Questionario para sección prácica


## Pregunta 1: Escribe el comando para un puente ssh entre el puerto 8080 (tu maquina) y el puerto 7001 del servidor 10.0.0.1, utilizando una llave pem como autenticación al servidor

**Respuesta:** ssh -L 8080:10.0.0.1:7001 -i ruta usuario@10.0.0.1 -N -v 
1. Aquí 'ruta' es la ruta del archivo llave.pem
2. '-L 8080:10.0.0.1:7001' es un mapeo entre el puerto local 8080 y el puerto 7001 de un servidor remoto 
3. '-i' Declara la llave PEM de autenticación
4. '-N' Impide accionar comandos remotos 
5. '-v' Arroja información descriptiva al respecto de la construcción del puente SSH
