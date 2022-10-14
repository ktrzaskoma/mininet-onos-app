from math import sin, cos, sqrt, atan2, radians

def disclaculator(lat1, lon1, lat2, lon2):
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
    'berlin': (52.5243700, 13.4105300),
    'hamburg': (53.5753200, 10.0153400),
    'hanover': (52.3705200, 9.7332200),
    'munich': (48.1374300, 11.5754900),
    'cologne': (50.9333300, 6.9500000),
    'frankfurt': (50.1155200, 8.6841700),
    'stuttgart': (48.7823200, 9.1770200),
    'dortmund': (51.5149400, 7.4660000),
    'leipzig': (51.3396200, 12.3712900),
    'bremen': (53.0751600, 8.8077700),
}

# fast
print(disclaculator(city['hanover'][0], city['hanover'][1], city['berlin'][0], city['berlin'][1]) / 200)
print(disclaculator(city['hanover'][0], city['hanover'][1], city['hamburg'][0], city['hamburg'][1]) / 200)
print(disclaculator(city['hanover'][0], city['hanover'][1], city['dortmund'][0], city['dortmund'][1]) / 200)
print(disclaculator(city['hanover'][0], city['hanover'][1], city['frankfurt'][0], city['frankfurt'][1]) / 200)
print(disclaculator(city['berlin'][0], city['berlin'][1], city['leipzig'][0], city['leipzig'][1]) / 200)
print(disclaculator(city['dortmund'][0], city['dortmund'][1], city['cologne'][0], city['cologne'][1]) / 200)
print(disclaculator(city['frankfurt'][0], city['frankfurt'][1], city['stuttgart'][0], city['stuttgart'][1]) / 200)
print(disclaculator(city['stuttgart'][0], city['stuttgart'][1], city['munich'][0], city['munich'][1]) / 200)
print(disclaculator(city['hamburg'][0], city['hamburg'][1], city['bremen'][0], city['bremen'][1]) / 200)




