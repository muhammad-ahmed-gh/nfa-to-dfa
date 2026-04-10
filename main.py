from input import getNFA
from validation import validate
from processing import DFA
from output import displayResult

NFA = getNFA()

if(validate(NFA)):
  displayResult(DFA(NFA))
else:
  print("ERROR: invalid input")