# example input
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
#output
# Alphabet: ['0', '1']
# States: ['A', 'B', 'C']
# Start state: A
# Accept state: ['B', 'C']
# Transitions:
# →A ——— 0 ——» →A
# →A ——— 1 ——» C
def displayResult(result_DFA):
    print(f"---------DFA Table---------")
    print(f"Alphabet: {result_DFA['alphabet']}")
    print(f"States: {result_DFA['states']}")
    print(f"Start state: {result_DFA['start']}")
    print(f"Accept state: {result_DFA['accepting']}")
    print(f"Transitions:")
    for state,transition in result_DFA['transitions'].items():
        prefix=""
        if(state == result_DFA['start']):
            prefix+="→"
        if(state == result_DFA['accepting']):
            prefix+="*"
        for symbol,Nextstate in transition.items():
            prefixnext=""
            if(Nextstate == result_DFA['start']):
                prefixnext+="→"
            if(Nextstate == result_DFA['accepting']):
                prefixnext+="*"

            print(f"{prefix}{state} ——— {symbol} ——» {prefixnext}{Nextstate}")
        print("\n")