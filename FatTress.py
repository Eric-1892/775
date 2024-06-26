from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import OVSSwitch
from mininet.link import TCLink
from mininet.log import setLogLevel
from mininet.cli import CLI
import os

class FatTreeTopo(Topo):
    hostcount = 1

    def build(self, k=4):
        # Topology parameters
        numPods = k
        numHostsPerEdgeSwitch = k // 2
        numEdgeSwitchesPerPod = k // 2
        numAggrSwitchesPerPod = k // 2
        numCoreSwitches = (k // 2) ** 2
        
        # Add Core Switches
        coreSwitches = [self.addSwitch('Core-S{}'.format(i + 1)) for i in range(numCoreSwitches)]

        for p in range(1, numPods + 1):
            # Add Aggregation and Edge Switches for each Pod
            aggrSwitches = [self.addSwitch('Agg-S{}'.format((p-1)*2 + i + 1)) for i in range(numAggrSwitchesPerPod)]
            edgeSwitches = [self.addSwitch('Acc-S{}'.format((p-1)*2 + i + 1)) for i in range(numEdgeSwitchesPerPod)]

            # Link Aggregation Switches to Core Switches
            for i, aggr in enumerate(aggrSwitches):
                for j, core in enumerate(coreSwitches):
                    if (j // numAggrSwitchesPerPod) % numAggrSwitchesPerPod == i:
                        self.addLink(aggr, core)

            # Link Edge Switches to Aggregation Switches and Hosts
            for edge in edgeSwitches:
                for aggr in aggrSwitches:
                    self.addLink(edge, aggr)

                # Connecting hosts to edge switches
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
