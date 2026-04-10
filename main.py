from input import getInfo
from validation import validate
from processing import dfa
from output import displayResult

info = getInfo()

if(validate(info)):
  displayResult(dfa(info))
else:
  print("ERROR: invalid input")