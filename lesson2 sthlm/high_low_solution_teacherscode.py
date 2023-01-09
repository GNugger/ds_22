import random

max = 10
min = 1

score = 0

# Returnerar en string

random_num = random.randint(min, max)

while True:
    print("Ditt nummer är: ", random_num)

    guess = input("Vad är din gissning högre eller lägre? (h/l) (exit): ")

    if guess != "h" and guess != "l" and guess != "exit": # om gissining är h eller l så kommmeer det köra koden 1 om man kör exit så stängs programmet 
        continue

    if guess == "exit": ## koden som stänger programmet och skriver ut resultatet
        print("Din score blev:", score,"total")
        print("Tack för att du spelade")
        break

    new_num = random.randint(min, max)
    #kod1 som jag kallar det här körs det om man väljer h eller l och det forstätters tills man skriver exit för att avslutat
    if new_num >= random_num and guess == "h":
        score += 1
        print("Rätt, din score är: ", score)
    elif new_num <= random_num and guess == "l":
        score += 1
        print("Rätt, din score är: ", score)
    else:
        print("Fel din score var: ", score)
        score = 0
        print("Prova igen")

    random_num = new_num