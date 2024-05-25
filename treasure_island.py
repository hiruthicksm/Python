print("Welcome to Treasure Island.")

print("Your mission is to find the treasure.")

path1=input("There are two ways in front of you which one will you choose, left or right ")

if path1=="left":
  path2=input('There is a river upcoming,whether you want to wait for the boat or you want to swim? or anything else ')
  if path2=="wait":
    path3=input("There are three coloured doors in front of you which one would you choose,red or blue or yellow or anything else ")
    if path3=="yellow":
      print("You Win!")
    elif path3=="red":
      print("Burned by fire.Game Over.")
    elif path3=="blue":
      print('Eaten by beasts')
    else:
      print("Game over")
  else:
    print("Attacked by trout.Game Over")
else:
  print("Fall into a hole.Game Over")
