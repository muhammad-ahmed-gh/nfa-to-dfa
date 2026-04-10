import json

def validate(data):
    """
    Validates the structure and logic of an NFA/DFA JSON object.
    Returns (is_valid, error_message).
    """
    required_keys = {"states", "alphabet", "start", "accepting", "transitions"}
    
    # 1. Check for missing top-level keys
    if not required_keys.issubset(data.keys()):
        #That means there are missing keys like start,accepting or alphabet 
        # and we want to know which is missing so make variable missing
        missing = required_keys - data.keys()
        return False, f"Missing required keys: {missing}"
    
    states = set(data["states"])
    alphabet = set(data["alphabet"])
    accepting = set(data["accepting"])
    transitions = data["transitions"]

    # 2. Validate 'start' state
    if data["start"] not in states:
        return False, f"Start state '{data['start']}' is not in the states list."

    # 3. Validate 'accepting' states
    for acc in accepting:
        if acc not in states:
            return False, f"Accepting state '{acc}' is not in the states list."

    # 4. Validate 'transitions'
    #note transition is sub json object that has state as key and value is another json object
    for state, paths in transitions.items():
        # Check if the transition source state exists
        if state not in states:
            return False, f"Transition defined for unknown state: '{state}'"
        #path is json object
        for symbol, targets in paths.items():
            # Check if the symbol is in the alphabet
            if str(symbol) not in alphabet:
                return False, f"Symbol '{symbol}' in transitions not in alphabet."
            
            # For NFA (Input style): targets is a list as nfa state can have multiple transitions for same symbol
      
            if isinstance(targets, list):
                for target in targets:
                    if target not in states:
                        return False, f"Target state '{target}' does not exist."
            # For DFA (Output style): targets is a single string 
            # as dfa state can have only one transition for same symbol
            elif isinstance(targets, str):
                if targets not in states:
                    return False, f"Target state '{targets}' does not exist."
            else:
                return False, f"Invalid target format for symbol '{symbol}' in state '{state}'."
# If all checks pass, the input is valid
    return True, "Valid Automaton"

# # --- Example Usage ---
# nfa_input = {
#     "states": ["q0", "q1", "q2"],
#     "alphabet": ["0", "1"],git checkout -b my-new-branch
#     "start": "q0",
#     "accepting": ["q1", "q2"],
#     "transitions": {
#         "q0": {
#             "0": ["q0", "q1"],
#             "1": ["q0"]
#         }
#     }
# }

# is_valid, msg = validate(nfa_input)
# print(f"Is Valid: {is_valid} | Result: {msg}")
