# List

print("______________List / String________________")
list1 = list()
list2 = list([1, "hello", True, None])

list3 = [] # list ska alltid skapas med square bracket eller har den inniut i () alltså ([]) som lista2 eller som list1 = list()
list4 = [2, "World", False, 2, 2, 2, 2, "World", False, False]
list5 = [list2, list4] # kan också göra som dict dock ju mer det finns i en lista desto mer compliserad det blir och mer minne och svårare att ittererar listan.

list6 = list2.copy() # för att koperierar list2 värde till list6 för att kunna antingen göra ändringar i list6 istället för att ändra list2 värden

print(list1)
print(list2)
print(list3)
print(list4)
print(list5)
print(list6)
list6.append("Fiskmås")
print(hex(id(list2)))
print(hex(id(list6)))


print(list2[1] + " " + list4[1]) # för sträng 
# print(list2[1] + " " + str(list4[0])) # gemon att avända str(listX[0]) där index är INT så konverterar det om INT till STR
# print(list2[1], list4[1]) # skrivs bara ut vad indexen har med komma täcken 

length = len(list2)
print(length)

print(list2[len(list2)-1])
print(list2[-1])

string = "Anton"
string_length = len(string) 

print(string_length) # hur många bokstäver en string innehåller

print(string[0]) # index 0 bokstav

list2[-1] = string # för att kunna andra list2 -1 alltså "None" till "Anton"
print(list2)

# Funkar inte då strängar är immutable.
# string[2] = "d"
# print(string)

sliced_list2 = list2[1:3] # lista från index1 till 3
print(sliced_list2)

sliced_string = string[1:3] # string från index 1 till 3
print(sliced_string)

# appened är för att lägga till en visst typ av data i en lista så som i vår lista list1 så har det ingen data i sig
list1.append("Hello, world!") 
list1.append("Hello, world Again!")
print(list1)

list1.insert(1, "my")  # insert är lägga till en till men i index position som "my" är inlagd på index 1 i list1
print(list1)

# Set är en lista med unika värden 
print("")
print("______________SET________________")

set1 = {1, 2, 3, 4}
set2 = {} # när den är tom så blir det en dictionaries 
set3 = set()
set4 = set(list4) # skapar en set utav en lista som är redan skapat

print(set1, type(set1))
print(set2, type(set2))
print(set4, type(set4))

# pop är för att gå igenom set som innehåller dubbleter och ta bort tills det inte finns några dubbleter så om i set4 har 3 värden så kommer vi behöva använda pop tre gånger för att det hämta det 3 första unika värden
print(set4.pop())
print(set4.pop())
print(set4.pop())

# bra för unika värden men inte bra till att avända som en struktuerad lista då det inte går att "slica" set listor

# Tuple
print("")
print("______________Tuple________________")

tuple1 = () # skapas med bara paranteser 
tuple2 = tuple()

tuple3 = (1, 2, 3, "Hello", "World", False)
tuple4 = tuple((4, 5, 6, "Goodbye", "Hell", True))

print(tuple1)
print(tuple2)
print(tuple3)
print(tuple4)

a, b, c, d, e, f = tuple3 #unpacking för att orginizerad värden så många du har så ska du ha så många variable till världen

print(d, e)

# tuples är immutable så det går inte att ändra

# Dictionaries kan sees om object 
# key, value
print("")
print("______________Dict________________")

dict1 = {}
dict2 = dict()

dict3 = {"name": "Anton", "age": 30}
dict4 = dict({"name": "Björne", "age": 50, (1, 2, 3): "korv", 1: "stroganoff"})

print(dict3)
print(dict4)

print(dict3["name"]) # name är en "key" för att få ut värden det kan vara vad som helst som är immutable value
print(dict4.get("name")) # .get är en metod som gör lite sammasak 
# dock den första som inte använder .get metoden så kommer det ger error 

# Funkar inte ger error
# print(dict3["fisk"])

# Ger None om det inte finns stoppar inte programmet
print(dict4.get("fisk"))

print(dict4.get((1, 2, 3))) #tuple immutable så det går att använda det 
print(dict4.get(1)) #int immutable

dict3["nationality"] = "SWEDISH" # för att lägga till en dict som är redan skapat

pet_dict1 = {"name": "Shirokumakun", "color": "White"}
pet_dict2 = {"name": "Biffen", "color": "Brown"}

company = {"name": "Mujina", "logo": "url", "employees": {"name": "Erik"}}

print(pet_dict1, pet_dict2)

dict3["pets"] = [pet_dict1, pet_dict2] 

print(dict3)

dict3["company"] = company

print(dict3)
print(dict3["company"])
print(dict3["pets"])

dict5 = dict4.copy()
print(dict5)
print(dict4)

dict5["name"] = "Sven"
print(dict5)
print(dict4)

print(hex(id(dict5)))
print(hex(id(dict4)))

#för att kunna see dicts olika keys och värden 
dict_keys = dict5.keys()
dict_values = dict5.values()

print(dict_keys) 
print(dict_values)