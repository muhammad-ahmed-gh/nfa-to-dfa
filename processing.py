# example input json
# {
#   "states": ["q0", "q1", "q2"],
#   "alphabet": ["0", "1"],
#   "start": "q0",
#   "accepting": ["q1", "q2"]
#   "transitions": {
#     "q0": {
#       "0": ["q0", "q1"],
#       "1": ["q0"]
#     },
#     "q1": {
#       "0": ["q1"],
#       "1": ["q1", "q2"]
#     },
#     "q2": {
#       "0": ["q0", "q1"],
#       "1": ["q0"]
#     },
#   }
# }
# 
# output json
# {
#   "states": ["A", "B", "C"],
#   "alphabet": ["0", "1"],
#   "start": "A",
#   "accepting": ["B", "C"]
#   "transitions": {
#     "A": {
#       "0": "A",
#       "1": "C"
#     }, ...
#   }
# }


def build_dfa(nfa):
    states = [frozenset([nfa["start"]])] # {"q0"}
    transitions = {}

    for i in range(len(states)):
        current = states[i]
        transitions[current] = {}

        for symbol in nfa["alphabet"]:
            next_state = set()

            for s in current:
                next_state.update(nfa["transitions"].get(s, {}).get(symbol, []))

            next_state = frozenset(next_state)
            transitions[current][symbol] = next_state

            if next_state not in states:
                states.append(next_state)

    return states, transitions


def dfa(nfa):
    states, transitions = build_dfa(nfa)

    names = {s: chr(65+i) for i, s in enumerate(states)}

    dfa = {
        "states": list(names.values()),
        "alphabet": nfa["alphabet"],
        "start": names[frozenset([nfa["start"]])],
        "accepting": [],
        "transitions": {}
    }

    for s in states:
        name = names[s]
        dfa["transitions"][name] = {}

        for x in s:
            if x in nfa["accepting"]:
                dfa["accepting"].append(name)
                break

        for sym in nfa["alphabet"]:
            dfa["transitions"][name][sym] = names[transitions[s][sym]]

    return dfa