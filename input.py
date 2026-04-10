import json

def getNFA():
    nfa = {}
    
    nfa['states'] = [s.strip() for s in input("Enter states (comma separated, e.g., q0, q1): ").split(",") if s.strip()]
    nfa['alphabet'] = [a.strip() for a in input("Enter alphabet (comma separated, e.g., 0, 1): ").split(",") if a.strip()]
    nfa['start'] = input("Enter the start state: ").strip()
    nfa['accepting'] = [s.strip() for s in input("Enter accepting states (comma separated): ").split(",") if s.strip()]
    
    nfa['transitions'] = {}
    for state in nfa['states']:
        nfa['transitions'][state] = {}
        for symbol in nfa['alphabet']:
            prompt = f"Enter next states for ({state}, {symbol}) (comma separated, or press Enter for none): "
            user_input = input(prompt).strip()
            
            if not user_input:
                nfa['transitions'][state][symbol] = []
            else:
                nfa['transitions'][state][symbol] = [s.strip() for s in user_input.split(",")]
                
    return nfa

def save_to_json(data, filename="nfa_config.json"):
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"\nSuccess! NFA has been saved to '{filename}'.")
    except Exception as e:
        print(f"An error occurred while saving: {e}")

if __name__ == "__main__":
    nfa_data = getNFA()
    save_to_json(nfa_data)