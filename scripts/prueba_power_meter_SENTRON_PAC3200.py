# --------------------------------------------------------------------------- # 
# Obtener datos del Analizador de Red SENTRON PAC3200 de Siemens mediante modbus TCP con python
# - Analizador: https://w5.siemens.com/spain/web/es/ic/building_technologies/sp_baja_tension/analizadores_sentron/SENTRONPAC3200/Pages/PAC3200.aspx
# - Datasheet: https://www.automation.siemens.com/cd-static/material/info/e20001-a112-l300-x-7800.pdf
# - Manual de Producto: https://cache.industry.siemens.com/dl/files/150/26504150/att_906556/v1/A5E01168664D-02_ES_122016_201612221316330094.pdf
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
# --------------------------------------------------------------------------- #

import logging
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.DEBUG)


ip = '192.168.1.10'
client = ModbusTcpClient(ip, port=502, timeout=3)
client.connect()
log.debug("Reading Registers") #debug mode on
parametros = ['Tensión UL1-N','Tensión UL2-N','Tensión UL3-N','Tensión UL1-L2','Tensión UL2-L3','Tensión UL3-L1',\
              'Corriente L1','Corriente L2','Corriente L3','Potencia aparente L1','Potencia aparente L2',\
              'Potencia aparente L3','Potencia activa L1','Potencia activa L2','Potencia activa L3']
unidades = ['V','V','V','V','V','V','A','A','A','VA','VA','VA','W','W','W']

for i in range(len(parametros)):
    result = client.read_holding_registers(i*2+1, 2, unit = 1)
    print(hex(result.registers[0]),hex(result.registers[1]))
    value = struct.pack('>I',(result.registers[0]<<16)|result.registers[1]) #4 bytes concatenacion de 2 bytes entero  + 2 bytes enteros
    valor_float = struct.unpack('!f', value)[0] #lo paso a float
    print(parametros[i] + " -->" + str(round(valor_float,2)) + " " +unidades[i])

client.close()
