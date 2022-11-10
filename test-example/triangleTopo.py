from mininet.topo import Topo

class TriangleTopo(Topo):

    def __init__(self):
        Topo.__init__(self)

        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')

        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')


        self.addLink(h1, s1)
        self.addLink(h2, s2)
        self.addLink(h3, s3)


        # dziala
        link_1 = self.addLink(s1, s2, bw=200, delay='2.8078196440920307ms', loss=0)
        link_2 = self.addLink(s2, s3, bw=200, delay='1.4453722915453864ms', loss=0)
        link_3 = self.addLink(s3, s1, bw=200, delay='2.4218562396222607ms', loss=0)




topos = {'project': (lambda: TriangleTopo())}