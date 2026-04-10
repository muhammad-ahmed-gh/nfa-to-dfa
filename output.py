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
# ---------DFA Table---------
# Alphabet: ['0', '1']
# States: ['A', 'B', 'C']
# Start state: A
# Accept state: ['B', 'C']
# Transitions Table:
# ---------------------------
# State    |input(0) |input(1) |
# ---------------------------
#  →A      | →A      | *C      |
#...
def displayResult(result_DFA):
    print(f"\n---------DFA Table---------")
    print(f"Alphabet: {result_DFA['alphabet']}")
    print(f"States: {result_DFA['states']}")
    print(f"Start state: {result_DFA['start']}")
    print(f"Accept state: {result_DFA['accepting']}")
    print(f"Transitions Table:")
    print("---------"+"----------"*len(result_DFA['alphabet']))
    print("State",end="    |")
    for alpha in result_DFA['alphabet']:
        print(f"{alpha}       ", end=" |")
    print("\n---------"+"----------"*len(result_DFA['alphabet']))
    for state in result_DFA['states']:
        prefix="  "
        if(state in result_DFA['accepting']) and (state in result_DFA['start']):
            prefix="→*"
        elif(state in result_DFA['accepting']):
            prefix=" *"
        elif(state in result_DFA['start']):
            prefix=" →"       
        print(f"{prefix}{state:<4}", end="")
        if state in result_DFA['transitions']:
            transition = result_DFA['transitions'][state]
            print(end="   |")
            for symbol in result_DFA['alphabet']:
                if symbol in transition:
                    Nextstate = transition[symbol]                    
                    prefixnext="  "
                    if(Nextstate in result_DFA['start']) and (Nextstate in result_DFA['accepting']):
                        prefixnext="→*"

                    elif(Nextstate in result_DFA['accepting']):
                        prefixnext=" *"
                    elif(Nextstate in result_DFA['start']):
                        prefixnext=" →"

                    print(f"{prefixnext}{Nextstate:<7}", end="|")
        print(end="\n")