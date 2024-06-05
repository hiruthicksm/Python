from replit import clear

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
dic={}
track=False
while not track:  
  name=input("What is your name?: ")
  amount=int(input("What's your bid?:$ "))
  dic[name]=amount
  bidding=input("Are there any other bidders? Type 'yes' or 'no'")
  clear()
  if bidding=='no':
    track=True
    list=[]
    for i in dic:
      list.append(dic[i])
print(dic)
max_amt=max(list)
ind=list.index(max_amt)
k_list=[]
for i in dic:
  k_list.append(i)
win_name=k_list[ind]
print(f"The winner is {win_name} with a bid of ${max_amt}")
