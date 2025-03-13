from random import randint
import snakes.plugins
from snakes.nets import *

snakes.plugins.load('gv', 'snakes.nets', 'snk')
from snk import *

# Initialize PetriNet
cpn = PetriNet('Packet Transmission')

# Subnetwork 1 - Packet Type Selection
# Places for file creation and breakdown
cpn.add_place(Place('Created_File', []))
cpn.add_place(Place('Created_Packets', []))

# Places for router selection
# Router A
cpn.add_place(Place('Router_A_Queue', []))
cpn.add_place(Place('Router_A', []))  # TCP only
# Router B
cpn.add_place(Place('Router_B_Queue', []))
cpn.add_place(Place('Router_B', []))  # TCP only
# Router C
cpn.add_place(Place('Router_C_Queue', []))
cpn.add_place(Place('Router_C', []))  # TCP/UDP
# Router D
cpn.add_place(Place('Router_D_Queue', []))
cpn.add_place(Place('Router_D', []))  # TCP/UDP

# Places for path selection
# cpn.add_place(Place('Path_Selection', []))
# cpn.add_place(Place('Transmission', []))

# Transitions
cpn.add_transition(Transition('Break_Down_File'))
cpn.add_transition(Transition('Select_Router_A', guard=Expression("p[1] == 'TCP'")))
cpn.add_transition(Transition('Select_Router_B', guard=Expression("p[1] == 'TCP'")))
cpn.add_transition(Transition('Select_Router_C'))
cpn.add_transition(Transition('Select_Router_D'))
cpn.add_transition(Transition('Router_A_Packet_Transmit'))
cpn.add_transition(Transition('Router_B_Packet_Transmit'))
cpn.add_transition(Transition('Router_C_Packet_Transmit'))
cpn.add_transition(Transition('Router_D_Packet_Transmit'))
# cpn.add_transition(Transition('Transmit_Packet'))
# cpn.add_transition(Transition('Select_Path'))

# Arcs
# File break down to N packets
N = 5
cpn.add_input('Created_File', 'Break_Down_File', Variable('f'))
cpn.add_output('Created_Packets', 'Break_Down_File',
               MultiArc([Expression("(f[0], 'UDP' if f[1] == 'media' else 'TCP')") for i in range(N)]))

# Router selection for each packet
cpn.add_input('Created_Packets', 'Select_Router_A', Variable('p'))
cpn.add_output('Router_A_Queue', 'Select_Router_A', Expression('p'))
cpn.add_input('Router_A_Queue', 'Router_A_Packet_Transmit', Variable('p'))
cpn.add_output('Router_A', 'Router_A_Packet_Transmit', Variable('p'))

cpn.add_input('Created_Packets', 'Select_Router_B', Variable('p'))
cpn.add_output('Router_B_Queue', 'Select_Router_B', Expression('p'))
cpn.add_input('Router_B_Queue', 'Router_B_Packet_Transmit', Variable('p'))
cpn.add_output('Router_B', 'Router_B_Packet_Transmit', Variable('p'))

cpn.add_input('Created_Packets', 'Select_Router_C', Variable('p'))
cpn.add_output('Router_C_Queue', 'Select_Router_C', Expression('p'))
cpn.add_input('Router_C_Queue', 'Router_C_Packet_Transmit', Variable('p'))
cpn.add_output('Router_C', 'Router_C_Packet_Transmit', Variable('p'))

cpn.add_input('Created_Packets', 'Select_Router_D', Variable('p'))
cpn.add_output('Router_D_Queue', 'Select_Router_D', Expression('p'))
cpn.add_input('Router_D_Queue', 'Router_D_Packet_Transmit', Variable('p'))
cpn.add_output('Router_D', 'Router_D_Packet_Transmit', Variable('p'))

# cpn.add_input('Router_A_Queue', 'Router_A_Packet_Transmit', Variable('p'))
# cpn.add_output('Router_A', 'Router_A_Packet_Transmit', Variable('p'))
# cpn.add_input('Router_B_Queue', 'Router_B_Packet_Transmit', Variable('p'))
# cpn.add_output('Router_B', 'Router_B_Packet_Transmit', Variable('p'))
# cpn.add_input('Router_C_Queue', 'Router_C_Packet_Transmit', Variable('p'))
# cpn.add_output('Router_C', 'Router_C_Packet_Transmit', Variable('p'))
# cpn.add_input('Router_D_Queue', 'Router_D_Packet_Transmit', Variable('p'))
# cpn.add_output('Router_D', 'Router_D_Packet_Transmit', Variable('p'))

# cpn.add_input('Router_A_B', 'Select_Router', Variable('p'))
# cpn.add_input('Router_C_D', 'Select_Router', Variable('p'))
# cpn.add_output('Path_Selection', 'Select_Router', Expression('p'))
#
# cpn.add_input('Path_Selection', 'Select_Path', Variable('p'))
# cpn.add_output('Transmission', 'Select_Path', Expression('p'))
#
# cpn.add_input('Transmission', 'Transmit_Packet', Variable('p'))

# Subnetwork 2 - Packet Transfer
# cpn.add_place(Place('Path_1', []))  # TCP Path 1
# cpn.add_place(Place('Path_2', []))  # TCP Path 2
# cpn.add_place(Place('Path_3', []))  # UDP Path
# cpn.add_place(Place('Arrival', []))
#
# cpn.add_transition(Transition('Check_Traffic'))
# cpn.add_transition(Transition('Move_Packet'))
# cpn.add_transition(Transition('Verify_Completion'))

# Arcs for congestion control (Max 200 packets per path)
# cpn.add_input('Transmission', 'Check_Traffic', Variable('p'))
# cpn.add_output('Path_1', 'Check_Traffic', Expression('p') if "TCP" in "p" else MultiSet([]))
# cpn.add_output('Path_2', 'Check_Traffic', Expression('p') if "TCP" in "p" else MultiSet([]))
# cpn.add_output('Path_3', 'Check_Traffic', Expression('p') if "UDP" in "p" else MultiSet([]))
#
# cpn.add_input('Path_1', 'Move_Packet', Variable('p'))
# cpn.add_input('Path_2', 'Move_Packet', Variable('p'))
# cpn.add_input('Path_3', 'Move_Packet', Variable('p'))
# cpn.add_output('Arrival', 'Move_Packet', Expression('p'))
#
# cpn.add_input('Arrival', 'Verify_Completion', Variable('p'))

image_path = './images/'
routers = ['A', 'B', 'C', 'D']
# Simulation
# Initial Tokens
cpn.place('Created_File').tokens = MultiSet([(1, 'media'), (2, 'non-media')])  # Example files

# State 1
print("Initial State:")
print(cpn.get_marking())
cpn.draw(f"{image_path}1.png")
for sub in cpn.transition('Break_Down_File').modes():
    cpn.transition('Break_Down_File').fire(sub)

# State 2
print("After Packet Creation:")
print(cpn.get_marking())
cpn.draw(f"{image_path}2.png")
for router in routers:
    transition = f'Select_Router_{router}'
    for sub in cpn.transition(transition).modes():
        cpn.transition(transition).fire(sub)

# State 3
print("After Router Selection:")
print(cpn.get_marking())
cpn.draw(f"{image_path}3.png")
for router in routers:
    transition = f'Router_{router}_Packet_Transmit'
    for sub in cpn.transition(transition).modes():
        cpn.transition(transition).fire(sub)

# State 4
print("After packet transmission:")
print(cpn.get_marking())
cpn.draw(f"{image_path}4.png")