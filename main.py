from input import getInfo
from validation import validate
from processing import toDFA
from output import displayResult

info = getInfo()

if(validate(info)):
  displayResult(toDFA(info))
else:
  print("ERROR: invalid input")