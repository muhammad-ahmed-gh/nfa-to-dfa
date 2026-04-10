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

def epsilonClosure(states, nfa):
    closure = set(states) # initial value = {q0, q1, ...}

    changed = True
    while changed:
        changed = False

        for state in list(closure):
            for nextState in nfa["transitions"].get(state, {}).get("ε", []):
                if nextState not in closure:
                    closure.add(nextState) # add q2 and it will be gone through later
                    changed = True

    return frozenset(closure)


def buildDFA(NFA):
    start = epsilonClosure([NFA["start"]], NFA) # initial value = start + its closure
    states = [start]
    transitions = {}

    for state in states:
        current = state
        transitions[current] = {}

        for symbol in NFA["alphabet"]:
            nextState = set()

            for s in current:
                nextState.update(NFA["transitions"].get(s, {}).get(symbol, []))

            nextState = epsilonClosure(nextState, NFA)

            transitions[current][symbol] = nextState

            if nextState not in states:
                states.append(nextState)

    return states, transitions


def DFA(NFA):
    states, transitions = buildDFA(NFA)

    names = {s: chr(65 + i) for i, s in enumerate(states)}

    startState = epsilonClosure([NFA["start"]], NFA)

    DFA = {
        "states": list(names.values()),
        "alphabet": NFA["alphabet"],
        "start": names[startState],
        "accepting": [],
        "transitions": {}
    }

    for s in states:
        name = names[s]
        DFA["transitions"][name] = {}

        for x in s:
            if x in NFA["accepting"]:
                DFA["accepting"].append(name)
                break

        for sym in NFA["alphabet"]:
            DFA["transitions"][name][sym] = names[transitions[s][sym]]

    return DFA