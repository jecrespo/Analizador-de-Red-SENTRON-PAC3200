# You need to edit this file with the the correct parameters 
# of your network, your database and your multimeters.
# ---------------------------------------------------------

from libs.sentron_pac3200 import PAC3200_MEASUREMENTS

# DATABASE PARAMETERS

DB_PARAMS = { 
    "host": "localhost",                # E.g., "localhost" or "127.0.0.1"
    "database": "energy_measurements",  # The name of your database
    "user": "postgres",                 # The database user
    "password": "your_password"            # The password for the database user
}

TABLE_NAME = "sentron_pac3200_measurements" # The name of the table in the db

# MULTIMETERS PARAMETERS

MULTIMETERS = [
    {
        "device": "device_1",           # Some name to the multimeter. Max. 20 characters.
        "ip": "192.168.1.x",            # The IP that you set in the multimeter
        "port": 502,                    # In general, you don't need to change this parameter
        "timeout": 3,                   # The same
        "measurements": [               # Add all the measurements you want. In the file libs/sentron_pac3200.py you can find the table of the measurements
            PAC3200_MEASUREMENTS['Voltage Va-n'],
            PAC3200_MEASUREMENTS['Voltage Vb-n'],
            PAC3200_MEASUREMENTS['Voltage Vc-n']
        ]
    },
    # You can add more multimeters copy this dictionary, one for each multimeter, E.g.
    {
        "device": "device_2",           # Some name to the multimeter. Max. 20 characters.
        "ip": "192.168.1.x",            # The IP that you set in the multimeter
        "port": 502,                    # In general, you don't need to change this parameter
        "timeout": 3,                   # The same
        "measurements": [               # Add all the measurements you want. In the file libs/sentron_pac3200.py you can find the table of the measurements
            PAC3200_MEASUREMENTS['Voltage Va-n'],
            PAC3200_MEASUREMENTS['Voltage Vb-n'],
            PAC3200_MEASUREMENTS['Voltage Vc-n']
        ]
    }
]