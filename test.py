from mininet.topo import Topo

class Project(Topo):

    def __init__(self):
        Topo.__init__(self)

        h1 = self.addHost('berlin')
        h2 = self.addHost('hamburg')


        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')


        self.addLink(h1, s1)
        self.addLink(h2, s2)

        link_1 = self.addLink(s1, s2, bw=200, delay='100ms', loss=0)


topos = {'project': (lambda: Project())}