import struct
from pymodbus.client.sync import ModbusTcpClient
ip = '192.168.1.10'
client = ModbusTcpClient(ip, port=502, timeout=3)
client.connect()
parametros = ['Tensión UL1-N','Tensión UL2-N','Tensión UL3-N','Tensión UL1-L2','Tensión UL2-L3','Tensión UL3-L1',\
              'Corriente L1','Corriente L2','Corriente L3','Potencia aparente L1','Potencia aparente L2',\
              'Potencia aparente L3','Potencia activa L1','Potencia activa L2','Potencia activa L3']
unidades = ['V','V','V','V','V','V','A','A','A','VA','VA','VA','W','W','W']

for i in range(0,100):
    result = client.read_holding_registers(i*2+1, 2, unit = 1)
    print(hex(result.registers[0]),hex(result.registers[1]))
	value = struct.pack('>I',(result.registers[0]<<16)|result.registers[1]) #4 bytes concatenacion de 2 bytes entero  + 2 bytes enteros
    valor_float = struct.unpack('!f', value)[0] #lo paso a float
    print(parametros[i] + " -->" + str(round(valor_float,2)) + " " +unidades[i])

client.close()
