import random
min = 1
max = 6
roll_again = "yes"
while roll_again == "yes" or roll_again == "y":

  print ("Rolling the dices...")
  number = (random.randint(min, max))
  print (number)  
    # if random(min, max) == 1:
    #   print ("Owh Sorry!!")

  if number == 6:
    print("wow you WIN \n GOOD LUCK")
  roll_again = input("Roll the dices again? ")
