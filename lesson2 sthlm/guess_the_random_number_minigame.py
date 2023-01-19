import random

min:int=int(1)
max:int=int(100)

tries = 0
random_num = random.randint(min, max)

while True:
    guess = input("Guess the number between 1-100 you have 10 tries. Or press 0 to exit the program: ")
    guess = int(guess)
    
    if guess == 0:
        print("Exit Program")
        break
    
    print ("you have", 9-tries, "tries left")
    
    if guess >= random_num+1:
        print ("you guess is too high")
        tries +=1
    elif guess <= random_num-1:
        print ("you guess is too low")
        tries +=1
    if guess == random_num:
       print("you guess correct, the number is:", random_num)
       tries +=1
       print("It took you", tries, "tries")
       break
    if tries ==10:
        print("you used up your tries the number was:", random_num,".")
        break
    
       
   

