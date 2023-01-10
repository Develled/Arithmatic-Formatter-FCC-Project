import re

def arithmetic_arranger(problems, solve = False):   
    
  firstNum = ''
  secondNum = ''
  equalsSign = ''
  answer = ''  

  ## creating errors
  if len(problems) > 5:
      return 'Error: Too many problems.'
  
  for problem in problems:
      if(re.search("[^\s0-9.+-]", problem)):
          if(re.search("[/]", problem) or re.search ("[*]", problem)):
             return "Error: Operator must be '+' or '-'."            
          return "Error: Numbers must only contain digits."
             
      topNum = problem.split()[0]
      bottomNum = problem.split()[2]
      operator = problem.split()[1]
      
      if (len(topNum) > 4 or len(bottomNum) > 4):
          return 'Error: Numbers cannot be more than four digits.'
      
      sums =''
      if (operator == '+'):
        sums = str(int(topNum)+int(bottomNum))
      elif (operator == '-'):
        sums = str(int(topNum)-int(bottomNum))
    
      length = max(len(topNum), len(bottomNum)) + 2
      top = str(topNum).rjust(length)
      bottom = operator + str(bottomNum).rjust(length - 1)
      line = ''
      res = str(sums).rjust(length)
      for s in range(length):
          line += '-'
      # add to the overall string
      if problem != problems[-1]:
        firstNum += top + '    '
        secondNum += bottom + '    '
        equalsSign += line + '    '
        answer += res + '    '
      else:
        firstNum += top
        secondNum += bottom
        equalsSign += line
        answer += res
    
  if solve:
    arranged_problems = firstNum + '\n' + secondNum + '\n' + equalsSign + '\n' + answer
  else:
      arranged_problems = firstNum + '\n' + secondNum + '\n' + equalsSign
  return arranged_problems
      
