#!/usr/bin/python3
# -*- coding: utf-8 -*-

# --------------------------------------------------------------------------- # 
# Obtener datos del Analizador de Red SENTRON PAC3200 de Siemens mediante modbus TCP con python
# - Analizador: https://w5.siemens.com/spain/web/es/ic/building_technologies/sp_baja_tension/analizadores_sentron/SENTRONPAC3200/Pages/PAC3200.aspx
# - Datasheet: https://www.automation.siemens.com/cd-static/material/info/e20001-a112-l300-x-7800.pdf
# - Manual de Producto: https://cache.industry.siemens.com/dl/files/150/26504150/att_906556/v1/A5E01168664D-02_ES_122016_201612221316330094.pdf
# --------------------------------------------------------------------------- # 
# --------------------------------------------------------------------------- #
# Ejecutado en CRON cada un minuto para guardar datos en una BBDD MySQL
# --------------------------------------------------------------------------- #

# --------------------------------------------------------------------------- #
# Librerías:
# - struct: https://docs.python.org/3/library/struct.html
# - comando instalación: pip install pymodbus
# - pymodbus instalación: https://pypi.org/project/pymodbus/
# - pymodbus: https://pymodbus.readthedocs.io/en/latest/
# --------------------------------------------------------------------------- # 

import struct
from pymodbus.client.sync import ModbusTcpClient

# --------------------------------------------------------------------------- # 
# configure the client logging debug:
#
# import logging
# logging.basicConfig()
# log = logging.getLogger()
# log.setLevel(logging.DEBUG)
# --------------------------------------------------------------------------- # 

# --------------------------------------------------------------------------- # 
# configure BBDD
# instalar como administrador: pip install mysql-connector-python (https://pypi.org/project/mysql-connector-python/)
# conector: https://dev.mysql.com/downloads/connector/python/8.0.html
# documentación: https://dev.mysql.com/doc/connector-python/en/
# --------------------------------------------------------------------------- # 
import mysql.connector as my_dbapi

ip = '192.168.1.10'
client = ModbusTcpClient(ip, port=502, timeout=3)
client.connect()
parametros = ['Tensión UL1-N','Tensión UL2-N','Tensión UL3-N','Tensión UL1-L2','Tensión UL2-L3','Tensión UL3-L1',\
              'Corriente L1','Corriente L2','Corriente L3','Potencia aparente L1','Potencia aparente L2',\
              'Potencia aparente L3','Potencia activa L1','Potencia activa L2','Potencia activa L3', \
              'Potencia reactiva L1','Potencia reactiva L2','Potencia reactiva L3', \
              'Factor de potencia L1','Factor de potencia L2','Factor de potencia L3','Frecuencia', \
              'Tensión media UL-N','Tensión media UL-L','Corriente media','Potencia aparente total', \
              'Potencia activa total','Potencia reactiva total','Factor de potencia total',\
              'Tensión máxima UL1-N','Tensión máxima UL2-N','Tensión máxima UL3-N', \
              'Tensión máxima UL1-L2','Tensión máxima UL2-L3','Tensión máxima UL3-L1', \
              'Corriente máxima L1','Corriente máxima L2','Corriente máxima L3', \
              'Potencia aparente máxima L1','Potencia aparente máxima L2','Potencia aparente máxima L3', \
              'Potencia activa máxima L1','Potencia activa máxima L2','Potencia activa máxima L3', \
              'Potencia reactiva máxima L1','Potencia reactiva máxima L2','Potencia reactiva máxima L3', \
              'Frecuencia máxima','Tensión media máxima UL-N','Tensión media máxima UL-L','Corriente media máxima', \
              'Potencia aparente total máxima','Potencia activa total máxima','Potencia reactiva total máxima', \
              'Factor de potencia total máximo','Frecuencia mínima','Corriente media mínima','Potencia aparente total mínima', \
              'Potencia activa total mínima','Potencia reactiva total mínima','Factor de potencia total mínimo']

offset = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,55,57,59,61,63,65,67,69,75,77,79,81,\
          83,85,87,89,91,93,95,97,99,101,103,105,107,109,129,131,133,135,137,139,141,143,187,193,195,197,199,201]
unidades = ['V','V','V','V','V','V','A','A','A','VA','VA','VA','W','W','W','var','var','var','','','','Hz', \
            'V', 'V','A','VA','W','var','','V','V','V','V','V','V','A','A','A','VA','VA','VA','W','W','W','var','var','var',\
            'Hz','V','V','A','VA','W','var','','Hz','A','VA','W','var','']
datos = []

for i in range(len(parametros)):
    result = client.read_holding_registers(offset[i], 2, unit = 1)
    #print(hex(result.registers[0]),hex(result.registers[1]))
    value = struct.pack('>I',(result.registers[0]<<16)|result.registers[1]) #4 bytes concatenacion de 2 bytes entero  + 2 bytes enteros
    valor_float = struct.unpack('!f', value)[0] #lo paso a float
    
    datos.append(round(valor_float,2))
    print(parametros[i] + " -->" + str(round(datos[i],2)) + " " +unidades[i])

client.close()

#conexión a BBDD
cnx_my = my_dbapi.connect(user='pon_tu_usuario', password='pon_tu_password', host='192.168.1.100', database='Power')
cursor_my = cnx_my.cursor()
query_my = "INSERT INTO Power (Tension_UL1_N,Tension_UL2_N,Tension_UL3_N,Potencia_activa_L1,Potencia_activa_L2,Potencia_activa_L3," \
           "Potencia_activa_total,Potencia_activa_total_máxima,Tensión_media_máxima_UL_N) VALUES ("\
           + str(round(datos[0],2)) + "," + str(round(datos[1],2)) + "," + str(round(datos[2],2)) + "," \
           + str(round(datos[12]/1000,2)) + "," + str(round(datos[13]/1000,2)) + "," + str(round(datos[14]/1000,2)) + "," \
           + str(round(datos[26]/1000,2)) + "," + str(round(datos[52]/1000,2)) + "," + str(round(datos[48],2)) + ")"

cursor_my.execute(query_my)
cnx_my.commit()
cnx_my.close()