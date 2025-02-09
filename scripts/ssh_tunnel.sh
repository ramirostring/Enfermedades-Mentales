#!/bin/bash
ssh -L 8080:10.0.0.1:7001 -i /ruta/a/tu/llave.pem usuario@10.0.0.1 -N -v
