from mininet.topo import Topo

class Project(Topo):

    def __init__(self):
        Topo.__init__(self)

        h1 = self.addHost('hanover')
        h2 = self.addHost('berlin')
        h3 = self.addHost('leipzig')
        h4 = self.addHost('hamburg')
        h5 = self.addHost('bremen')
        h6 = self.addHost('dortmund')
        h7 = self.addHost('cologne')
        h8 = self.addHost('frankfurt')
        h9 = self.addHost('stuttgart')
        h10 = self.addHost('munich')

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
        link_1 = self.addLink(s1, s2, bw=200, delay='1.7667523626592816ms', loss=0)
        link_2 = self.addLink(s1, s4, bw=200, delay='0.9569642143970305ms', loss=0)
        link_3 = self.addLink(s1, s6, bw=200, delay='1.2887792071956992ms', loss=0)
        link_4 = self.addLink(s1, s8, bw=200, delay='1.8472174741983094ms', loss=0)
        link_5 = self.addLink(s2, s3, bw=200, delay='1.059359275529652ms', loss=0)
        link_6 = self.addLink(s6, s7, bw=200, delay='0.5233099952212235ms', loss=0)
        link_7 = self.addLink(s8, s9, bw=200, delay='1.07843150845552ms', loss=0)
        link_8 = self.addLink(s9, s10, bw=200, delay='1.349814048911974ms', loss=0)
        link_9 = self.addLink(s4, s5, bw=200, delay='0.6903084168350831ms', loss=0)



topos = {'project': (lambda: Project())}