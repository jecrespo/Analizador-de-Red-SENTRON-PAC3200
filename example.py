# --------------------------------------------------------------------------- # 
# Obtener datos del multímetro SENTRON PAC3200 de Siemens mediante modbus TCP con Python.
# - Analizador: https://w5.siemens.com/spain/web/es/ic/building_technologies/sp_baja_tension/analizadores_sentron/SENTRONPAC3200/Pages/PAC3200.aspx
# - Datasheet: https://www.automation.siemens.com/cd-static/material/info/e20001-a112-l300-x-7800.pdf
# - Manual de Producto: https://cache.industry.siemens.com/dl/files/150/26504150/att_906556/v1/A5E01168664D-02_ES_122016_201612221316330094.pdf
# --------------------------------------------------------------------------- # 

# --------------------------------------------------------------------------- #
# Librerías:
# - struct: https://docs.python.org/3/library/struct.html
# - comando instalación: pip install pymodbus==2.5.3
# - pymodbus instalación: https://pypi.org/project/pymodbus/
# - pymodbus: https://pymodbus.readthedocs.io/en/latest/
# --------------------------------------------------------------------------- # 

import struct # Para decodificar los datos
from pymodbus.client.sync import ModbusTcpClient # Para la conexión

# Realizar la conexión
ip = '192.168.x.x' # Coloca la dirección IP de tu multímetro
client = ModbusTcpClient(ip, port=502, timeout=3)
client.connect()

#Puedes comprobar la conexión con el multímetro con
#client.connected

# Descargar datos con una instrucción 0x03
raw_value = client.read_holding_registers(address=1, count=2, unit = 1)
""" address es el registro que quieres leer. La dirección 1 corresponde 
    a la Tensión entre Línea 1 y Neutro.
    En la página 41 del manual del producto encontrarás una tabla con
    la dirección de todos los registros del multímetro. La dirección es
    la columna offset. Cambia este valor por la magnitud que quieras
    obtener.
    
    count es la cantidad de registros donde se almancena el valor.
    En la tabla de magnitudes del manual viene indicado en la columna
    Número de registros."""

# Si el valor está almacenado en dos registros y está en formato Float
# decodificamos:
packed_value = struct.pack('>I',(raw_value.registers[0]<<16)|raw_value.registers[1]) 
value = struct.unpack('!f', packed_value)[0] 
print(value)

# Si el valor está almacenado en cuatro registros y está en formato Double
# decodificamos:
# packed_value = struct.pack('>Q',(raw_value.registers[0]<<48)|(raw_value.registers[1]<<32)|(raw_value.registers[2]<<16)|raw_value.registers[3])
# value = struct.unpack('!d', value)[0]
# print(value)

# Cerramos la conexión
client.close()