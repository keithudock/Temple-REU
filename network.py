'''
Created on Jun 19, 2017

@author: ravel
'''

from mininet.topo import Topo



class CustomTopo(Topo):
    def __init__(self):  
        Topo.__init__( self )
        network = raw_input('Please enter the desired network topology: ')
        if network == 'diamond':
            h1 = self.addHost('h1')
            h2 = self.addHost('h2')
            s1 = self.addSwitch('s1')
            s2 = self.addSwitch('s2')
            s3 = self.addSwitch('s3')
            s4 = self.addSwitch('s4')

            self.addLink(s1,h1)
	    
            self.addLink(s4,h2)
            self.addLink(s1,s2)
            self.addLink(s1,s3)
            self.addLink(s2,s4)
            self.addLink(s3,s4)

	    
		
	elif network == 'mytopo':
		leftHost = self.addHost( 'h1' )
        	rightHost = self.addHost( 'h2' )
        	leftSwitch = self.addSwitch( 's3' )
        	rightSwitch = self.addSwitch( 's4' )

        	# Add links
        	self.addLink( leftHost, leftSwitch )
		self.addLink( leftSwitch, rightSwitch )
		self.addLink( rightSwitch, rightHost )
	
	elif network == 'fattree':

        	self.size = int(input('Please enter the number of pods in the tree: '))

        	cores = (self.size/2)**2
        	aggs = (self.size/2) * self.size
        	edges = (self.size/2) * self.size
        	hosts = (self.size/2)**2 * self.size

        	switches = {}

		for pod in range(0, self.size):
		    agg_offset = cores + self.size/2 * pod
		    edge_offset = cores + aggs + self.size/2 * pod
		    host_offset = cores + aggs + edges + (self.size/2)**2 * pod

		    for agg in range(0, self.size/2):
		        core_offset = agg * self.size/2
		        aggname = "a{0}".format(agg_offset + agg)
		        agg_sw = self.addSwitch(aggname)
		        switches[aggname] = agg_sw

		        # connect core and aggregate switches
		        for core in range(0, self.size/2):
		            corename = "c{0}".format(core_offset + core)
		            core_sw = self.addSwitch(corename)
		            switches[corename] = core_sw
		            self.addLink(agg_sw, core_sw)

		        # connect aggregate and edge switches
		        for edge in range(0, self.size/2):
		            edgename = "e{0}".format(edge_offset + edge)
		            edge_sw = self.addSwitch(edgename)
		            switches[edgename] = edge_sw
		            self.addLink(agg_sw, edge_sw)

		    # connect edge switches with hosts
		    for edge in range(0, self.size/2):
		        edgename = "e{0}".format(edge_offset + edge)
		        edge_sw = switches[edgename]

		        for h in range(0, self.size/2):
		            hostname = "h{0}".format(host_offset + self.size/2 * edge + h)
		            hostobj = self.addHost(hostname)
		            self.addLink(edge_sw, hostobj)

	elif network == 'single':
		"k: number of hosts"
		k = int(input('Enter the # of hosts connected to a single switch: '))
		switch = self.addSwitch( 's1' )
		for h in irange( 1, k ):
		    host = self.addHost( 'h%s' % h )
		    self.addLink( host, switch )

	else:
		print("Invalid Topology")
		

        
topos = { 'network': ( lambda: CustomTopo() ) }
