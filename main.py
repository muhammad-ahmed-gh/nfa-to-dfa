from input import getNFA
from validation import validate
from processing import DFA
from output import displayResult

NFA = getNFA()
isValid, errMsg = validate(NFA)

if(isValid):
    displayResult(DFA(NFA))
else:
    print(errMsg)