# In this file you cand find all the measured quantities available in the Siemens Sentron PAC3200.
# You can find more information in the user manual:
# https://cache.industry.siemens.com/dl/files/150/26504150/att_906556/v1/A5E01168664D-02_ES_122016_201612221316330094.pdf

# Table of measurements: --------------

# Voltage Va-n
# Voltage Vb-n
# Voltage Vc-n
# Voltage Va-b
# Voltage Vb-c
# Voltage Vc-a
# Current a
# Current b
# Current c
# Apparent Power a
# Apparent Power b
# Apparent Power c
# Active Power a
# Active Power b
# Active Power c
# Reactive Power a
# Reactive Power b
# Reactive Power c
# Power Factor a
# Power Factor b
# Power Factor c
# THD-R Voltage a
# THD-R Voltage b
# THD-R Voltage c
# THD-R Current a
# THD-R Current b
# THD-R Current c
# Frequency
# Avg. Voltage Vph-n
# Avg. Voltage Vph-ph
# Avg. Current
# Total Apparent Power
# Total Active Power
# Total Reactive Power
# Total Power Factor
# Amplitude Unbalance - Voltage
# Amplitude Unbalance - Current
# Max. Voltage Va-n
# Max. Voltage Vb-n
# Max. Voltage Vc-n
# Max. Voltage Va-b
# Max. Voltage Vb-c
# Max. Voltage Vc-a
# Max. Current a
# Max. Current b
# Max. Current c
# Max. Apparent Power a
# Max. Apparent Power b
# Max. Apparent Power c
# Max. Active Power a
# Max. Active Power b
# Max. Active Power c
# Max. Reactive Power a
# Max. Reactive Power b
# Max. Reactive Power c
# Max. Power Factor a
# Max. Power Factor b
# Max. Power Factor c
# Max. THD-R Voltage a
# Max. THD-R Voltage b
# Max. THD-R Voltage c
# Max. THD-R Current a
# Max. THD-R Current b
# Max. THD-R Current c
# Max. Frequency
# Max. Avg. Voltage Vph-n
# Max. Avg. Voltage Vph-ph
# Max. Avg. Current
# Max. Total Apparent Power
# Max. Total Active Power
# Max. Total Reactive Power
# Max. Total Power Factor
# Min. Voltage Va-n
# Min. Voltage Vb-n
# Min. Voltage Vc-n
# Min. Voltage Va-b
# Min. Voltage Vb-c
# Min. Voltage Vc-a
# Min. Current a
# Min. Current b
# Min. Current c
# Min. Apparent Pwr a
# Min. Apparent Pwr b
# Min. Apparent Pwr c
# Min. Active Power a
# Min. Active Power b
# Min. Active Power c
# Min. Reactive Pwr a
# Min. Reactive Pwr b
# Min. Reactive Pwr c
# Min. Power Factor a
# Min. Power Factor b
# Min. Power Factor c
# Min. Frequency
# Min. Avg. Volt Vph-n
# Min. Avg. Volt Vph-ph
# Min. Avg. Current
# Min. Total App. Pwr
# Min. Total Act. Pwr
# Min. Total Reac. Pwr
# Min. Total Pwr Fact.
# Demand Act. Pwr Imp
# Demand Reac. Pwr Imp
# Demand Act. Pwr Exp
# Demand Reac. Pwr Exp
# Max. Act. Pwr
# Min. Act. Pwr
# Max. Reactive Pwr
# Min. Reactive Pwr
# Act. Nrg Import T1
# Act. Nrg Import T2
# Act. Nrg Export T1
# Act. Nrg Export T2
# React. Nrg Import T1
# React. Nrg Import T2
# React. Nrg Export T1
# React. Nrg Export T2
# Apparent Nrg T1
# Apparent Nrg T2

PAC3200_MEASUREMENTS = {
    'Voltage Va-n': {
        'measurement': 'Voltage Va-n',
        'offset': 1,
        'registers': 2,
        'format': 'Float',
        'unit': 'V'},
    'Voltage Vb-n': {
        'measurement': 'Voltage Vb-n',
        'offset': 3,
        'registers': 2,
        'format': 'Float',
        'unit': 'V'},
    'Voltage Vc-n': {
        'measurement': 'Voltage Vc-n',
        'offset': 5,
        'registers': 2,
        'format': 'Float',
        'unit': 'V'},
    'Voltage Va-b': {
        'measurement': 'Voltage Va-b',
        'offset': 7,
        'registers': 2,

        'format': 'Float',
        'unit': 'V'},
    'Voltage Vb-c': {
        'measurement': 'Voltage Vb-c',
        'offset': 9,
        'registers': 2,
        'format': 'Float',
        'unit': 'V'},
    'Voltage Vc-a': {
        'measurement': 'Voltage Vc-a',
        'offset': 11,
        'registers': 2,
        'format': 'Float',
        'unit': 'V'},
    'Current a': {
        'measurement': 'Current a',
        'offset': 13,
        'registers': 2,
        'format': 'Float',
        'unit': 'A'},
    'Current b': {
        'measurement': 'Current b',
        'offset': 15,
        'registers': 2,
        'format': 'Float',
        'unit': 'A'},
    'Current c': {
        'measurement': 'Current c',
        'offset': 17,
        'registers': 2,
        'format': 'Float',
        'unit': 'A'},
    'Apparent Power a': {
        'measurement': 'Apparent Power a',
        'offset': 19,
        'registers': 2,
        'format': 'Float',
        'unit': 'VA'},
    'Apparent Power b': {
        'measurement': 'Apparent Power b',
        'offset': 21,
        'registers': 2,
        'format': 'Float',
        'unit': 'VA'},
    'Apparent Power c': {
        'measurement': 'Apparent Power c',
        'offset': 23,
        'registers': 2,
        'format': 'Float',
        'unit': 'VA'},
    'Active Power a': {
        'measurement': 'Active Power a',
        'offset': 25,
        'registers': 2,
        'format': 'Float',
        'unit': 'W'},
    'Active Power b': {
        'measurement': 'Active Power b',
        'offset': 27,
        'registers': 2,
        'format': 'Float',
        'unit': 'W'},
    'Active Power c': {
        'measurement': 'Active Power c',
        'offset': 29,
        'registers': 2,
        'format': 'Float',
        'unit': 'W'},
    'Reactive Power a': {
        'measurement': 'Reactive Power a',
        'offset': 31,
        'registers': 2,
        'format': 'Float',
        'unit': 'var'},
    'Reactive Power b': {
        'measurement': 'Reactive Power b',
        'offset': 33,
        'registers': 2,
        'format': 'Float',
        'unit': 'var'},
    'Reactive Power c': {
        'measurement': 'Reactive Power c',
        'offset': 35,
        'registers': 2,
        'format': 'Float',
        'unit': 'var'},
    'Power Factor a': {
        'measurement': 'Power Factor a',
        'offset': 37,
        'registers': 2,
        'format': 'Float',
        'unit': ''},
    'Power Factor b': {
        'measurement': 'Power Factor b',
        'offset': 39,
        'registers': 2,
        'format': 'Float',
        'unit': ''},
    'Power Factor c': {
        'measurement': 'Power Factor c',
        'offset': 41,
        'registers': 2,
        'format': 'Float',
        'unit': ''},
    'THD-R Voltage a': {
        'measurement': 'THD-R Voltage a',
        'offset': 43,
        'registers': 2,
        'format': 'Float',
        'unit': '%'},
    'THD-R Voltage b': {
        'measurement': 'THD-R Voltage b',
        'offset': 45,
        'registers': 2,
        'format': 'Float',
        'unit': '%'},
    'THD-R Voltage c': {
        'measurement': 'THD-R Voltage c',
        'offset': 47,
        'registers': 2,
        'format': 'Float',
        'unit': '%'},
    'THD-R Current a': {
        'measurement': 'THD-R Current a',
        'offset': 49,
        'registers': 2,
        'format': 'Float',
        'unit': '%'},
    'THD-R Current b': {
        'measurement': 'THD-R Current b',
        'offset': 51,
        'registers': 2,
        'format': 'Float',
        'unit': '%'},
    'THD-R Current c': {
        'measurement': 'THD-R Current c',
        'offset': 53,
        'registers': 2,
        'format': 'Float',
        'unit': '%'},
    'Frequency': {
        'measurement': 'Frequency',
        'offset': 55,
        'registers': 2,
        'format': 'Float',
        'unit': 'Hz'},
    'Avg. Voltage Vph-n': {
        'measurement': 'Avg. Voltage Vph-n',
        'offset': 57,
        'registers': 2,
        'format': 'Float',
        'unit': 'V'},
    'Avg. Voltage Vph-ph': {
        'measurement': 'Avg. Voltage Vph-ph',
        'offset': 59,
        'registers': 2,
        'format': 'Float',
        'unit': 'V'},
    'Avg. Current': {
        'measurement': 'Avg. Current',
        'offset': 61,
        'registers': 2,
        'format': 'Float',
        'unit': 'A'},
    'Total Apparent Power': {
        'measurement': 'Total Apparent Power',
        'offset': 63,
        'registers': 2,
        'format': 'Float',
        'unit': 'VA'},
    'Total Active Power': {
        'measurement': 'Total Active Power',
        'offset': 65,
        'registers': 2,
        'format': 'Float',
        'unit': 'W'},
    'Total Reactive Power': {
        'measurement': 'Total Reactive Power',
        'offset': 67,
        'registers': 2,
        'format': 'Float',
        'unit': 'var'},
    'Total Power Factor': {
        'measurement': 'Total Power Factor',
        'offset': 69,
        'registers': 2,
        'format': 'Float',
        'unit': ''},
    'Amplitude Unbalance - Voltage': {
        'measurement': 'Amplitude Unbalance - Voltage',
        'offset': 71,
        'registers': 2,
        'format': 'Float',
        'unit': '%'},
    'Amplitude Unbalance - Current': {
        'measurement': 'Amplitude Unbalance - Current',
        'offset': 73,
        'registers': 2,
        'format': 'Float',
        'unit': '%'},
    'Max. Voltage Va-n': {
        'measurement': 'Max. Voltage Va-n',
        'offset': 75,
        'registers': 2,
        'format': 'Float',
        'unit': 'V'},
    'Max. Voltage Vb-n':
    {
        'measurement': 'Max. Voltage Vb-n',
        'offset': 77,
        'registers': 2,
        'format': 'Float',
        'unit': 'V'},
    'Max. Voltage Vc-n': {
        'measurement': 'Max. Voltage Vc-n',
        'offset': 79,
        'registers': 2,
        'format': 'Float',
        'unit': 'V'},
    'Max. Voltage Va-b': {
        'measurement': 'Max. Voltage Va-b',
        'offset': 81,
        'registers': 2,
        'format': 'Float',
        'unit': 'V'},
    'Max. Voltage Vb-c': {
        'measurement': 'Max. Voltage Vb-c',
        'offset': 83,
        'registers': 2,
        'format': 'Float',
        'unit': 'V'},
    'Max. Voltage Vc-a': {
        'measurement': 'Max. Voltage Vc-a',
        'offset': 85,
        'registers': 2,
        'format': 'Float',
        'unit': 'V'},
    'Max. Current a': {
        'measurement': 'Max. Current a',
        'offset': 87,
        'registers': 2,
        'format': 'Float',
        'unit': 'A'},
    'Max. Current b': {
        'measurement': 'Max. Current b',
        'offset': 89,
        'registers': 2,
        'format': 'Float',
        'unit': 'A'},
    'Max. Current c': {
        'measurement': 'Max. Current c',
        'offset': 91,
        'registers': 2,
        'format': 'Float',
        'unit': 'A'},
    'Max. Apparent Power a': {
        'measurement': 'Max. Apparent Power a',
        'offset': 93,
        'registers': 2,
        'format': 'Float',
        'unit': 'VA'},
    'Max. Apparent Power b': {
        'measurement': 'Max. Apparent Power b',
        'offset': 95,
        'registers': 2,
        'format': 'Float',
        'unit': 'VA'},
    'Max. Apparent Power c': {
        'measurement': 'Max. Apparent Power c',
        'offset': 97,
        'registers': 2,
        'format': 'Float',
        'unit': 'VA'},
    'Max. Active Power a': {
        'measurement': 'Max. Active Power a',
        'offset': 99,
        'registers': 2,
        'format': 'Float',
        'unit': 'W'},
    'Max. Active Power b': {
        'measurement': 'Max. Active Power b',
        'offset': 101,
        'registers': 2,
        'format': 'Float',
        'unit': 'W'},
    'Max. Active Power c': {
        'measurement': 'Max. Active Power c',

        'offset': 103,
        'registers': 2,
        'format': 'Float',
        'unit': 'W'},
    'Max. Reactive Power a': {
        'measurement': 'Max. Reactive Power a',
        'offset': 105,
        'registers': 2,
        'format': 'Float',
        'unit': 'var'},
    'Max. Reactive Power b': {
        'measurement': 'Max. Reactive Power b',
        'offset': 107,
        'registers': 2,
        'format': 'Float',
        'unit': 'var'},
    'Max. Reactive Power c': {
        'measurement': 'Max. Reactive Power c',
        'offset': 109,
        'registers': 2,
        'format': 'Float',
        'unit': 'var'},
    'Max. Power Factor a': {
        'measurement': 'Max. Power Factor a',
        'offset': 111,
        'registers': 2,
        'format': 'Float',
        'unit': ''},
    'Max. Power Factor b': {
        'measurement': 'Max. Power Factor b',
        'offset': 113,
        'registers': 2,
        'format': 'Float',
        'unit': ''},
    'Max. Power Factor c': {
        'measurement': 'Max. Power Factor c',
        'offset': 115,
        'registers': 2,
        'format': 'Float',
        'unit': ''},
    'Max. THD-R Voltage a': {
        'measurement': 'Max. THD-R Voltage a',
        'offset': 117,
        'registers': 2,
        'format': 'Float',
        'unit': '%'},
    'Max. THD-R Voltage b': {
        'measurement': 'Max. THD-R Voltage b',
        'offset': 119,
        'registers': 2,
        'format': 'Float',
        'unit': '%'},
    'Max. THD-R Voltage c': {
        'measurement': 'Max. THD-R Voltage c',
        'offset': 121,
        'registers': 2,
        'format': 'Float',
        'unit': '%'},
    'Max. THD-R Current a': {
        'measurement': 'Max. THD-R Current a',
        'offset': 123,
        'registers': 2,
        'format': 'Float',
        'unit': '%'},
    'Max. THD-R Current b': {
        'measurement': 'Max. THD-R Current b',
        'offset': 125,
        'registers': 2,
        'format': 'Float',
        'unit': '%'},
    'Max. THD-R Current c': {
        'measurement': 'Max. THD-R Current c',
        'offset': 127,
        'registers': 2,
        'format': 'Float',
        'unit': '%'},
    'Max. Frequency': {
        'measurement': 'Max. Frequency',
        'offset': 129,
        'registers': 2,
        'format': 'Float',
        'unit': 'Hz'},
    'Max. Avg. Voltage Vph-n': {
        'measurement': 'Max. Avg. Voltage Vph-n',
        'offset': 131,
        'registers': 2,
        'format': 'Float',
        'unit': 'V'},
    'Max. Avg. Voltage Vph-ph': {
        'measurement': 'Max. Avg. Voltage Vph-ph',
        'offset': 133,
        'registers': 2,
        'format': 'Float',
        'unit': 'V'},
    'Max. Avg. Current': {
        'measurement': 'Max. Avg. Current',
        'offset': 135,
        'registers': 2,
        'format': 'Float',
        'unit': 'A'},
    'Max. Total Apparent Power': {
        'measurement': 'Max. Total Apparent Power',
        'offset': 137,
        'registers': 2,
        'format': 'Float',
        'unit':
        'VA'},
    'Max. Total Active Power': {
        'measurement': 'Max. Total Active Power',
        'offset': 139,
        'registers': 2,
        'format': 'Float',
        'unit': 'W'},
    'Max. Total Reactive Power': {
        'measurement': 'Max. Total Reactive Power',
        'offset': 141,
        'registers': 2,
        'format': 'Float',
        'unit': 'var'},
    'Max. Total Power Factor': {
        'measurement': 'Max. Total Power Factor',
        'offset': 143,
        'registers': 2,
        'format': 'Float',
        'unit': ''},
    'Min. Voltage Va-n': {
        'measurement': 'Min. Voltage Va-n',
        'offset': 145,
        'registers': 2,
        'format': 'Float',
        'unit': 'V'},
    'Min. Voltage Vb-n': {
        'measurement': 'Min. Voltage Vb-n',
        'offset': 147,
        'registers': 2,
        'format': 'Float',
        'unit': 'V'},
    'Min. Voltage Vc-n': {
        'measurement': 'Min. Voltage Vc-n',
        'offset': 149,
        'registers': 2,
        'format': 'Float',
        'unit': 'V'},
    'Min. Voltage Va-b': {
        'measurement': 'Min. Voltage Va-b',
        'offset': 151,
        'registers': 2,
        'format': 'Float',
        'unit': 'V'},
    'Min. Voltage Vb-c': {
        'measurement': 'Min. Voltage Vb-c',
        'offset': 153,
        'registers': 2,
        'format': 'Float',
        'unit': 'V'},
    'Min. Voltage Vc-a': {
        'measurement': 'Min. Voltage Vc-a',
        'offset': 155,
        'registers': 2,
        'format': 'Float',
        'unit': 'V'},
    'Min. Current a': {
        'measurement': 'Min. Current a',
        'offset': 157,
        'registers': 2,
        'format': 'Float',
        'unit': 'A'},
    'Min. Current b': {
        'measurement': 'Min. Current b',
        'offset': 159,
        'registers': 2,
        'format': 'Float',
        'unit': 'A'},
    'Min. Current c': {
        'measurement': 'Min. Current c',
        'offset': 161,
        'registers': 2,
        'format': 'Float',
        'unit': 'A'},
    'Min. Apparent Pwr a': {
        'measurement': 'Min. Apparent Pwr a',
        'offset': 163,
        'registers': 2,
        'format': 'Float',
        'unit': 'VA'},
    'Min. Apparent Pwr b': {
        'measurement': 'Min. Apparent Pwr b',
        'offset': 165,
        'registers': 2,
        'format': 'Float',
        'unit': 'VA'},
    'Min. Apparent Pwr c': {
        'measurement': 'Min. Apparent Pwr c',
        'offset': 167,
        'registers': 2,
        'format': 'Float',
        'unit': 'VA'},
    'Min. Active Power a': {
        'measurement': 'Min. Active Power a',
        'offset': 169,
        'registers': 2,
        'format': 'Float',
        'unit': 'W'},
    'Min. Active Power b': {
        'measurement':
        'Min. Active Power b',
        'offset': 171,
        'registers': 2,
        'format': 'Float',
        'unit': 'W'},
    'Min. Active Power c': {
        'measurement': 'Min. Active Power c',
        'offset': 173,
        'registers': 2,
        'format': 'Float',
        'unit': 'W'},
    'Min. Reactive Pwr a': {
        'measurement': 'Min. Reactive Pwr a',
        'offset': 175,
        'registers': 2,
        'format': 'Float',
        'unit': 'var'},
    'Min. Reactive Pwr b': {
        'measurement': 'Min. Reactive Pwr b',
        'offset': 177,
        'registers': 2,
        'format': 'Float',
        'unit': 'var'},
    'Min. Reactive Pwr c': {
        'measurement': 'Min. Reactive Pwr c',
        'offset': 179,
        'registers': 2,
        'format': 'Float',
        'unit': 'var'},
    'Min. Power Factor a': {
        'measurement': 'Min. Power Factor a',
        'offset': 181,
        'registers': 2,
        'format': 'Float',
        'unit': ''},
    'Min. Power Factor b': {
        'measurement': 'Min. Power Factor b',
        'offset': 183,
        'registers': 2,
        'format': 'Float',
        'unit': ''},
    'Min. Power Factor c': {
        'measurement': 'Min. Power Factor c',
        'offset': 185,
        'registers': 2,
        'format': 'Float',
        'unit': ''},
    'Min. Frequency': {
        'measurement': 'Min. Frequency',
        'offset': 187,
        'registers': 2,
        'format': 'Float',
        'unit': 'Hz'},
    'Min. Avg. Volt Vph-n': {
        'measurement': 'Min. Avg. Volt Vph-n',
        'offset': 189,
        'registers': 2,
        'format': 'Float',
        'unit': 'V'},
    'Min. Avg. Volt Vph-ph': {
        'measurement': 'Min. Avg. Volt Vph-ph',
        'offset': 191,
        'registers': 2,
        'format': 'Float',
        'unit': 'V'},
    'Min. Avg. Current': {
        'measurement': 'Min. Avg. Current',
        'offset': 193,
        'registers': 2,
        'format': 'Float',
        'unit': 'A'},
    'Min. Total App. Pwr': {
        'measurement': 'Min. Total App. Pwr',
        'offset': 195,
        'registers': 2,
        'format': 'Float',
        'unit': 'VA'},
    'Min. Total Act. Pwr': {
        'measurement': 'Min. Total Act. Pwr',
        'offset': 197,
        'registers': 2,
        'format': 'Float',
        'unit': 'W'},
    'Min. Total Reac. Pwr': {
        'measurement': 'Min. Total Reac. Pwr',
        'offset': 199,
        'registers': 2,
        'format': 'Float',

        'unit': 'var'},
    'Min. Total Pwr Fact.': {
        'measurement': 'Min. Total Pwr Fact.',
        'offset': 201,
        'registers': 2,
        'format': 'Float',
        'unit': 'var'},
    'Demand Act. Pwr Imp': {
        'measurement': 'Demand Act. Pwr Imp',
        'offset': 501,
        'registers': 2,
        'format': 'Float',
        'unit': 'W'},
    'Demand Reac. Pwr Imp': {
        'measurement': 'Demand Reac. Pwr Imp',
        'offset': 503,
        'registers': 2,
        'format': 'Float',
        'unit': 'var'},
    'Demand Act. Pwr Exp': {
        'measurement': 'Demand Act. Pwr Exp',
        'offset': 505,
        'registers': 2,
        'format': 'Float',
        'unit': 'W'},
    'Demand Reac. Pwr Exp': {
        'measurement': 'Demand Reac. Pwr Exp',
        'offset': 507,
        'registers': 2,
        'format': 'Float',
        'unit': 'var'},
    'Max. Act. Pwr': {
        'measurement': 'Max. Act. Pwr',
        'offset': 509,
        'registers': 2,
        'format': 'Float',
        'unit': 'W'},
    'Min. Act. Pwr': {
        'measurement': 'Min. Act. Pwr',
        'offset': 511,
        'registers': 2,
        'format': 'Float',
        'unit': 'W'},
    'Max. Reactive Pwr': {
        'measurement': 'Max. Reactive Pwr',
        'offset': 513,
        'registers': 2,
        'format': 'Float',
        'unit': 'var'},
    'Min. Reactive Pwr': {
        'measurement': 'Min. Reactive Pwr',
        'offset': 515,
        'registers': 2,
        'format': 'Float',
        'unit': 'var'},
    'Act. Nrg Import T1': {
        'measurement': 'Act. Nrg Import T1',
        'offset': 801,
        'registers': 4,
        'format': 'Double',
        'unit': 'Wh'},
    'Act. Nrg Import T2': {
        'measurement': 'Act. Nrg Import T2',
        'offset': 805,
        'registers': 4,
        'format': 'Double',
        'unit': 'Wh'},
    'Act. Nrg Export T1': {
        'measurement': 'Act. Nrg Export T1',
        'offset': 809,
        'registers': 4,
        'format': 'Double',
        'unit': 'Wh'},
    'Act. Nrg Export T2': {
        'measurement': 'Act. Nrg Export T2',
        'offset': 813,
        'registers': 4,
        'format': 'Double',
        'unit': 'Wh'},
    'React. Nrg Import T1': {
        'measurement': 'React. Nrg Import T1',
        'offset': 817,
        'registers': 4,
        'format': 'Double',
        'unit': 'varh'},
    'React. Nrg Import T2': {
        'measurement': 'React. Nrg Import T2',
        'offset': 821,
        'registers': 4,
        'format': 'Double',
        'unit': 'varh'},
    'React. Nrg Export T1': {
        'measurement': 'React. Nrg Export T1',
        'offset': 825,
        'registers': 4,
        'format': 'Double',
        'unit': 'varh'},
    'React. Nrg Export T2': {
        'measurement': 'React. Nrg Export T2',
        'offset': 829,
        'registers': 4,
        'format': 'Double',
        'unit': 'varh'},
    'Apparent Nrg T1': {
        'measurement': 'Apparent Nrg T1',
        'offset': 833,
        'registers': 4,
        'format': 'Double',
        'unit': 'VAh'},
    'Apparent Nrg T2': {
        'measurement': 'Apparent Nrg T2',
        'offset': 837,
        'registers': 4,
        'format': 'Double',
        'unit': 'VAh'}
        }