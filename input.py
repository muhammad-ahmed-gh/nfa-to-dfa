def getNFA():
    NFA = {}
    print("Enter the following separated with commas\n")

    NFA['states'] = input("States of the NFA: ").split(",")
    NFA['alphabet'] = input("Alphabet of the NFA: ").split(",")
    NFA['start'] = input("Start state of the NFA: ")
    NFA['accepting'] = input("Accepting states of the NFA: ").split(",")
    NFA['transitions'] = {}

    for state in NFA['states']:
        NFA['transitions'][state] = {}
        for symbol in NFA['alphabet']:
            next_states = input(f"{state} at {symbol} -> ").split(",")
            NFA['transitions'][state][symbol] = next_states

        eps = input(f"{state} at ε -> ")
        if eps.strip() == "":
            NFA['transitions'][state]["ε"] = []
        else:
            NFA['transitions'][state]["ε"] = eps.split(",")

    return NFA
