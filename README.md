# Multímetro Siemens SENTRON PAC3200 con Python

Obtener datos del multímetro SENTRON PAC3200 de Siemens mediante modbus TCP con Python.

## ¿Cómo configurar?

En el [manual del producto]([README.md](https://cache.industry.siemens.com/dl/files/150/26504150/att_906556/v1/A5E01168664D-02_ES_122016_201612221316330094.pdf)) podrás encontrar los pasos para configurar el medidor. Importante:
* Debes configurar el dispositivo correctamente para que desde la PC donde corras el script de Python pueda acceder a la dirección IP del medidor.
* Debes configurar el medidor en modo Modbus.

En el archivo **example.py** encontrarás un script de ejemplo para obtener los datos del medidor.

## Enlaces de interés:

Analizador: https://w5.siemens.com/spain/web/es/ic/building_technologies/sp_baja_tension/analizadores_sentron/SENTRONPAC3200/Pages/PAC3200.aspx

Datasheet: https://www.automation.siemens.com/cd-static/material/info/e20001-a112-l300-x-7800.pdf

Manual de Producto: https://cache.industry.siemens.com/dl/files/150/26504150/att_906556/v1/A5E01168664D-02_ES_122016_201612221316330094.pdf

## Extras:

* Este proyecto utiliza la versión de la librería pymodbus 2.5.3. Con versiones más recientes no funciona. Esto se puede instalar con el comando:

    `pip install pymodbus==2.5.3`