logo = """
 _____________________
|  _________________  |
| | Python          | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(a,b):
  return a+b
def sub(a,b):
  return a-b
def mul(a,b):
  return a*b
def div(a,b):
  return a/b

operations={"+":add,
            "-":sub,
            "*":mul,
            "/":div
           }
def calculator():
  print(logo)
  a=float(input("Enter the first number: ")) 
  flag=True
  while flag:
    for i in operations:
      print(i)
    ope=input("Select any one operation above: ")
    b=float(input("Enter the next number: "))
    
    calc=operations[ope]
    answer=calc(a,b)
   
    print(f"{a} {ope} {b} ={answer}")
    
    choice=input(f"Type 'y' to continue calculate with {answer} or type 'n' to start a new calculation : ")
    if choice=='y':
     a=answer
     
    if choice=='n':
      flag=False
      calculator()
      
calculator()
