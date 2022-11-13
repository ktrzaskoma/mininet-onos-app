from math import sin, cos, sqrt, atan2, radians

def discalculator(lat1, lon1, lat2, lon2):
    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    R = 6373.0
    distance = R * c

    return distance * sqrt(2)

city = {
    'paris': (48.8534100, 2.3488000),
    'lille': (50.6329700, 3.0585800),
    'strasbourg': (48.5839200, 7.7455300),
    'nantes': (47.2172500, -1.5533600),
    'rennes': (48.1119800, -1.6742900),
    'bordeaux': (44.8404400, -0.5805000),
    'dijon': (47.3166700, 5.0166700),
    'lyon': (45.7484600, 4.8467100),
    'toulouse': (43.6042600, 1.4436700),
    'marseille': (43.2969500, 5.3810700),
}

# fast
print(discalculator(city['paris'][0], city['paris'][1], city['strasbourg'][0], city['strasbourg'][1]) / 200)
print(discalculator(city['paris'][0], city['paris'][1], city['lille'][0], city['lille'][1]) / 200)
print(discalculator(city['paris'][0], city['paris'][1], city['nantes'][0], city['nantes'][1]) / 200)
print(discalculator(city['nantes'][0], city['nantes'][1], city['rennes'][0], city['rennes'][1]) / 200)
print(discalculator(city['nantes'][0], city['nantes'][1], city['bordeaux'][0], city['bordeaux'][1]) / 200)
print(discalculator(city['paris'][0], city['paris'][1], city['dijon'][0], city['dijon'][1]) / 200)
print(discalculator(city['dijon'][0], city['dijon'][1], city['lyon'][0], city['lyon'][1]) / 200)
print(discalculator(city['lyon'][0], city['lyon'][1], city['toulouse'][0], city['toulouse'][1]) / 200)
print(discalculator(city['lyon'][0], city['lyon'][1], city['marseille'][0], city['marseille'][1]) / 200)
# added to test test-example controller
print('test-example things')
print(discalculator(city['toulouse'][0], city['toulouse'][1], city['bordeaux'][0], city['bordeaux'][1]) / 200)       #10
print(discalculator(city['toulouse'][0], city['toulouse'][1], city['marseille'][0], city['marseille'][1]) / 200)     #11
print(discalculator(city['marseille'][0], city['marseille'][1], city['strasbourg'][0], city['strasbourg'][1]) / 200) #12
print(discalculator(city['strasbourg'][0], city['strasbourg'][1], city['lille'][0], city['lille'][1]) / 200)         #13
print(discalculator(city['lille'][0], city['lille'][1], city['rennes'][0], city['rennes'][1]) / 200)                 #14
print(discalculator(city['bordeaux'][0], city['bordeaux'][1], city['paris'][0], city['paris'][1]) / 200)             #15

