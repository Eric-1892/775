from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSSwitch
from mininet.link import TCLink
from mininet.log import setLogLevel
from mininet.cli import CLI
import os

class FatTreeTopo(Topo):
    hostcount = 1

    def __init__(self, k=4):
        super(FatTreeTopo, self).__init__()
        self.k = k
        self.build(k)

    def build(self, k):
        numPods = k
        numHostsPerEdgeSwitch = k // 2
        numEdgeSwitchesPerPod = k // 2
        numAggrSwitchesPerPod = k // 2
        numCoreSwitches = (k // 2) ** 2
        
        coreSwitches = [self.addSwitch('Core-S{}'.format(i + 1), dpid='010000000000{:02x}'.format(i)) for i in range(numCoreSwitches)]

        aggr_dpid_suffix = 0
        edge_dpid_suffix = 0

        for p in range(1, numPods + 1):
            aggrSwitches = [self.addSwitch('Agg-S{}'.format((p-1)*2 + i + 1), dpid='020000000000{:02x}'.format(aggr_dpid_suffix + i)) for i in range(numAggrSwitchesPerPod)]
            aggr_dpid_suffix += numAggrSwitchesPerPod
            
            edgeSwitches = [self.addSwitch('Acc-S{}'.format((p-1)*2 + i + 1), dpid='030000000000{:02x}'.format(edge_dpid_suffix + i)) for i in range(numEdgeSwitchesPerPod)]
            edge_dpid_suffix += numEdgeSwitchesPerPod
            
            for i, aggr in enumerate(aggrSwitches):
                for j, core in enumerate(coreSwitches):
                    if (j // numAggrSwitchesPerPod) % numAggrSwitchesPerPod == i:
                        self.addLink(aggr, core)

            for edge in edgeSwitches:
                for aggr in aggrSwitches:
                    self.addLink(edge, aggr)

                for _ in range(numHostsPerEdgeSwitch):
                    host = self.addHost('h{}'.format(FatTreeTopo.hostcount), dpid='040000000000{:02x}'.format(FatTreeTopo.hostcount))
                    self.addLink(edge, host)
                    FatTreeTopo.hostcount += 1

topos = {'FatTree': (lambda: FatTreeTopo())}

def run():
    os.system('sudo mn -c')

    topo = FatTreeTopo(k=4)
    net = Mininet(topo=topo, switch=OVSSwitch, link=TCLink, controller=None)
    net.start()
    
    CLI(net)
    net.stop()
    os.system('sudo mn -c')
    
if __name__ == '__main__':
    setLogLevel('info')
    run()
