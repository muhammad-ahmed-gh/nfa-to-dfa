from input import getNFA
from validation import validate
from processing import DFA
from output import displayResult

print("-----------------------------------------")
print("        -- NFA to DFA Converter --")
print("-----------------------------------------")

NFA = getNFA()
isValid, errMsg = validate(NFA)

if(isValid):
    displayResult(DFA(NFA))
else:
    print(errMsg)