import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

print('What do you choose? Type 0 for Rock,1 for Paper or 2 for Scissors.')
images=[rock,paper,scissors]
choice=int(input())
list=["rocks","papers","scissorss"]
length=len(list)
print(images[choice])

com=random.randint(0,length-1)
print("Computer choose: ")
print(images[com])

if choice==0 and com==0:
    print("match draw")
elif choice==0 and com==1:
    print("computer wins")
elif choice==0 and com==2:
    print("You win")
elif choice==1 and com==0:
     print("you win")
elif choice==1 and com==1:
    print("draw")
elif choice==1 and com==2:
    print("Computer Wins")
elif choice==2 and com==0:
    print("Computer Wins")
elif choice==2 and com==1:
    print("You Win")
else:
    print("Draw")
        

