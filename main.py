import struct
from pymodbus.client.sync import ModbusTcpClient
import psycopg2
from config import *

# Connect to the PostgreSQL DB
connection = psycopg2.connect(**DB_PARAMS)

# Create a cursor to perform database operations
cursor = connection.cursor()

for MULTIMETER in MULTIMETERS:
    
    # Connect to the multimeter by Modbus
    client = ModbusTcpClient( MULTIMETER["ip"], port = MULTIMETER['port'], timeout = MULTIMETER['timeout'] )
    if not client.connect():
        continue

    client.read_holding_registers( 1, 2, unit = 1 )

    for MEASUREMENT in MULTIMETER["measurements"]:
        response = client.read_holding_registers( MEASUREMENT["offset"], 2 if MEASUREMENT["format"] == "Float" else 4 , unit = 1 )

        if MEASUREMENT["format"] == "Float":
            value = struct.pack('>I',(response.registers[-2]<<16)|response.registers[-1]) # 4 bytes concat with 2 bytes + 2 bytes
            float_value = struct.unpack('!f', value)[0] # convert to float

        else:
            value = struct.pack('>Q',(response.registers[-4]<<48)|(response.registers[-3]<<32)|(response.registers[-2]<<16)|response.registers[-1]) # 8 bytes concat
            float_value = struct.unpack('!d', value)[0] # convert to float

        cursor.execute("""
                        INSERT INTO {}
                            (datetime, device, measurement, value)
                        VALUES
                            (NOW(), '{}', '{}', {});
                        """.format(TABLE_NAME, MULTIMETER["device"], MEASUREMENT["measurement"], float_value))
        
    connection.commit()

connection.close()
client.close()