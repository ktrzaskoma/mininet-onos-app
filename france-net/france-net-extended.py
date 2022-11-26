from mininet.topo import Topo


class Project(Topo):

    def __init__(self):
        Topo.__init__(self)

        h1 = self.addHost('paris')
        h2 = self.addHost('lille')
        h3 = self.addHost('strasbourg')
        h4 = self.addHost('nantes')
        h5 = self.addHost('rennes')
        h6 = self.addHost('bordeaux')
        h7 = self.addHost('dijon')
        h8 = self.addHost('lyon')
        h9 = self.addHost('toulouse')
        h10 = self.addHost('marseille')

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

        self.addLink(h1, s1)  # paris
        self.addLink(h2, s2)  # lille
        self.addLink(h3, s3)  # strasbourg
        self.addLink(h4, s4)  # nantes
        self.addLink(h5, s5)  # rennes
        self.addLink(h6, s6)  # bordeaux
        self.addLink(h7, s7)  # dijon
        self.addLink(h8, s8)  # lyon
        self.addLink(h9, s9)  # toulouse
        self.addLink(h10, s10)  # marseille

        # dziala
        link_1 = self.addLink(s1, s3, bw=200, delay='2.8078196440920307ms', loss=0)
        link_2 = self.addLink(s1, s2, bw=200, delay='1.4453722915453864ms', loss=0)
        link_3 = self.addLink(s1, s4, bw=200, delay='2.4218562396222607ms', loss=0)
        link_4 = self.addLink(s4, s5, bw=200, delay='0.7066264410307157ms', loss=0)
        link_5 = self.addLink(s4, s6, bw=200, delay='1.9433702026800423ms', loss=0)
        link_6 = self.addLink(s1, s7, bw=200, delay='1.8506687587742465ms', loss=0)
        link_7 = self.addLink(s7, s8, bw=200, delay='1.2368411863985722ms', loss=0)
        link_8 = self.addLink(s8, s9, bw=200, delay='2.542496989322984ms', loss=0)
        link_9 = self.addLink(s8, s10, bw=200, delay='1.9512774194128457ms', loss=0)
        # onos things
        link_10 = self.addLink(s9, s6, bw=200, delay='1.4989136372196574ms', loss=0)
        link_11 = self.addLink(s9, s10, bw=200, delay='2.260927572628282ms', loss=0)
        link_12 = self.addLink(s10, s3, bw=200, delay='4.354145322302172ms', loss=0)
        link_13 = self.addLink(s3, s2, bw=200, delay='2.880726317719385ms', loss=0)
        link_14 = self.addLink(s2, s5, bw=200, delay='3.1304550037846424ms', loss=0)
        link_15 = self.addLink(s6, s1, bw=200, delay='3.527074031698339ms', loss=0)



topos = {'franceTopo': (lambda: Project())}
