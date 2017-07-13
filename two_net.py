'''
Created on Jun 19, 2017

@author: ravel
'''

from mininet.topo import Topo


class CustomTopo(Topo):
    def __init__(self):  
        Topo.__init__( self )
	h1 = self.addHost('h1')
        h2 = self.addHost('h2')
	h3 = self.addHost('h3')
	h4 = self.addHost('h4')
 	s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
 	s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')

	self.addLink(s1,h1)
	self.addLink(s2,h2)
	self.addLink(s1,s2)

	self.addLink(s3,h3)
	self.addLink(s4,h4)
	self.addLink(s3,s4)

topos = { 'two_net': ( lambda: CustomTopo() ) }
