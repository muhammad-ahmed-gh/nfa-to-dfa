from input import getInfo
from validation import validate
from processing import DFA
from output import displayResult

info = getInfo()

if(validate(info)):
  displayResult(DFA(info))
else:
  print("ERROR: invalid input")