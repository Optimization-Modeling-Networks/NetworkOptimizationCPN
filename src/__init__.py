import snakes.plugins
snakes.plugins.load('gv', 'snakes.nets', 'snk')
from snk import *

# Initialize PetriNet
pn = PetriNet('First net')

# Add places
pn.add_place(Place('p1', [0]))

# Add transitions
pn.add_transition(Transition('t1', Expression('x<5')))

# Add arcs
pn.add_input('p1', 't1', Variable('x'))
pn.add_output('p1', 't1', Expression('x+1'))

subs = pn.transition('t1').modes()
print(subs)
# output: [Substitution(x=0)]
# shows the mapping between arcs variable and place's token {Variable('x') = 0, lines 7 and 13}

pn.transition('t1').fire(subs[0])
# fires a transition with the specified substitution

tokens = pn.place('p1').tokens
print(tokens)
# output: MultiSet([1])
# shows place's tokens

net_marking = pn.get_marking()
print(net_marking)
# output: Marking({'p': MultiSet([1])})
# shows marking of the whole net

pn.draw("pn.png")
