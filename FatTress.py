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

        core_counter = 1
        aggr_counter = 1
        edge_counter = 1
        
        coreSwitches = [self.addSwitch('Core-S{}'.format(i + 1), dpid='000000000000000{}'.format(core_counter + i)) for i in range(numCoreSwitches)]
        core_counter += numCoreSwitches

        for p in range(1, numPods + 1):
            aggrSwitches = [self.addSwitch('Agg-S{}'.format((p-1)*2 + i + 1), dpid='010000000000000{}'.format(aggr_counter + i)) for i in range(numAggrSwitchesPerPod)]
            aggr_counter += numAggrSwitchesPerPod
            edgeSwitches = [self.addSwitch('Acc-S{}'.format((p-1)*2 + i + 1), dpid='020000000000000{}'.format(edge_counter + i)) for i in range(numEdgeSwitchesPerPod)]
            edge_counter += numEdgeSwitchesPerPod

            for i, aggr in enumerate(aggrSwitches):
                for j, core in enumerate(coreSwitches):
                    if (j // numAggrSwitchesPerPod) % numAggrSwitchesPerPod == i:
                        self.addLink(aggr, core)

            for edge in edgeSwitches:
                for aggr in aggrSwitches:
                    self.addLink(edge, aggr)

                for _ in range(numHostsPerEdgeSwitch):
                    host = self.addHost('h{}'.format(FatTreeTopo.hostcount))
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
