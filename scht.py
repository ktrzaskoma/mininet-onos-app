import sys

from mininet.topo import Topo
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
    'munich': (48.1374300, 11.5754900),
    'cologne': (50.9333300, 6.9500000),
    'frankfurt': (50.1155200, 8.6841700),
    'stuttgart': (48.7823200, 9.1770200),
    'dortmund': (51.5149400, 7.4660000),
    'leipzig': (51.3396200, 12.3712900),
    'essen': (51.4565700, 7.0122800),
    'bremen': (53.0751600, 8.8077700)
}

# fast
d1 = disclaculator(city['berlin'][0], city['berlin'][1], city['hamburg'][0], city['hamburg'][1]) / 200
d2 = disclaculator(city['berlin'][0], city['berlin'][1], city['dortmund'][0], city['dortmund'][1]) / 200
d3 = disclaculator(city['berlin'][0], city['berlin'][1], city['frankfurt'][0], city['frankfurt'][1]) / 200
d4 = disclaculator(city['berlin'][0], city['berlin'][1], city['munich'][0], city['munich'][1]) / 200
d5 = disclaculator(city['munich'][0], city['munich'][1], city['bremen'][0], city['bremen'][1]) / 200
d6 = disclaculator(city['munich'][0], city['munich'][1], city['stuttgart'][0], city['stuttgart'][1]) / 200
d7 = disclaculator(city['stuttgart'][0], city['stuttgart'][1], city['cologne'][0], city['cologne'][1]) / 200
d8 = disclaculator(city['stuttgart'][0], city['stuttgart'][1], city['frankfurt'][0], city['frankfurt'][1]) / 200
d9 = disclaculator(city['frankfurt'][0], city['frankfurt'][1], city['dortmund'][0], city['dortmund'][1]) / 200
d10 = disclaculator(city['frankfurt'][0], city['frankfurt'][1], city['hamburg'][0], city['hamburg'][1]) / 200
d11 = disclaculator(city['hamburg'][0], city['hamburg'][1], city['essen'][0], city['essen'][1]) / 200

# slow
d12 = disclaculator(city['berlin'][0], city['berlin'][1], city['leipzig'][0], city['leipzig'][1]) / 100
d13 = disclaculator(city['leipzig'][0], city['leipzig'][1], city['stuttgart'][0], city['stuttgart'][1]) / 100
d14 = disclaculator(city['leipzig'][0], city['leipzig'][1], city['hamburg'][0], city['hamburg'][1]) / 100
d15 = disclaculator(city['frankfurt'][0], city['frankfurt'][1], city['munich'][0], city['munich'][1]) / 100
d16 = disclaculator(city['cologne'][0], city['cologne'][1], city['dortmund'][0], city['dortmund'][1]) / 100
d17 = disclaculator(city['cologne'][0], city['cologne'][1], city['essen'][0], city['essen'][1]) / 100
d18 = disclaculator(city['essen'][0], city['essen'][1], city['dortmund'][0], city['dortmund'][1]) / 100
d19 = disclaculator(city['essen'][0], city['essen'][1], city['bremen'][0], city['bremen'][1]) / 100
d20 = disclaculator(city['bremen'][0], city['bremen'][1], city['hamburg'][0], city['hamburg'][1]) / 100


class Project(Topo):

    def __init__(self):
        Topo.__init__(self)

        h1 = self.addHost('berlin')
        h2 = self.addHost('hamburg')
        h3 = self.addHost('munich')
        h4 = self.addHost('cologne')
        h5 = self.addHost('frankfurt')
        h6 = self.addHost('stuttgart')
        h7 = self.addHost('dortmund')
        h8 = self.addHost('leipzig')
        h9 = self.addHost('hanover')
        h10 = self.addHost('bremen')

        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')
        s6 = self.addSwitch('s6')
        s7 = self.addSwitch('s7')
        s8 = self.addSwitch('s8')
        s9 = self.addSwitch('s9')
        s10 = self.addSwitch('s10')

        self.addLink(h1, s1)
        self.addLink(h2, s2)
        self.addLink(h3, s3)
        self.addLink(h4, s4)
        self.addLink(h5, s5)
        self.addLink(h6, s6)
        self.addLink(h7, s7)
        self.addLink(h8, s8)
        self.addLink(h9, s9)
        self.addLink(h10, s10)

        # dziala
        link_1 = self.addLink(s1, s2, bw=200, delay='1.8ms', loss=0)
        link_2 = self.addLink(s1, s7, bw=200, delay='3ms', loss=0)
        link_3 = self.addLink(s1, s5, bw=200, delay='3ms', loss=0)
        link_4 = self.addLink(s1, s3, bw=200, delay='3.6ms', loss=0)
        link_5 = self.addLink(s3, s10, bw=200, delay='4.2ms', loss=0)
        link_6 = self.addLink(s3, s6, bw=200, delay='1.3ms', loss=0)
        link_7 = self.addLink(s6, s4, bw=200, delay='2ms', loss=0)
        # nie dziala
        # link_8 = self.addLink(s6, s5, bw=200, delay='1.07ms', loss=0)
        # link_9 = self.addLink(s5, s7, bw=200, delay='1.25ms', loss=0)
        # link_10 = self.addLink(s5, s2, bw=200, delay='2.79ms', loss=0)
        # link_11 = self.addLink(s2, s9, bw=200, delay='2.2ms', loss=0)
        # link_12 = self.addLink(s1, s8, bw=100, delay='2.11ms', loss=0)
        # link_13 = self.addLink(s8, s6, bw=100, delay='5.15ms', loss=0)
        # link_14 = self.addLink(s8, s2, bw=100, delay='4.18ms', loss=0)
        # link_15 = self.addLink(s3, s5, bw=100, delay='4.3ms', loss=0)
        # link_16 = self.addLink(s4, s7, bw=100, delay='1.04ms', loss=0)
        # link_17 = self.addLink(s4, s9, bw=100, delay='0.82ms', loss=0)
        # link_18 = self.addLink(s9, s7, bw=100, delay='0.45ms', loss=0)
        # link_19 = self.addLink(s9, s10, bw=100, delay='3.07ms', loss=0)
        # link_20 = self.addLink(s10, s2, bw=100, delay='1.38ms', loss=0)


topos = {'project': (lambda: Project())}