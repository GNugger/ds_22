# list

list1=([])
#list2=(1,"hello", True, None)# med () så är det en tuple // snabbare och inte mutable grunden är att det inte går att ändra
list2 = ([1,"hello", True, None]) # den här lista går det att ändrar på grund av square bracket innuit i brackets.
list3=[]
list4=[2,"world", False, "world", False, 2,2,2,2,2,2,2]# med [] så är det en "list" // långsamare och mutable tanken är att kunna ändra efterhand det har skapats 


print(list1)
print(list2)
print(list3)
print(list4)

# print(list2[1] + " " + str(list4[0])) # gemon att avända str(listX[0]) där index är INT så konverterar det om INT till STR
# print(list2[1], list4[1]) # skrivs bara ut vad indexen har med komma täcken 

lenght = len(list2)
print(lenght)

print(list2[len(list2)-1]) # standard 
print(list2[-1]) # python shortcut

name = "knnbccbddllm"
name_lenght = len(name) # hur många bokstäver det innehåller i en string

print(name_lenght)  # hur många bokstäver det innehåller i en string

print(name[0])  # första bokstäven i strängen
list2[-1] = name # för att ändrar list2 -1 alltså "None" till "Fay" det här är mutable 

print(list2)

# Funkar inte då pga en "string" är immutable vilket menars det går inte att ändra.
# name[0] = "d"
# print(name)


#
sliced_list = list2[0:] # från början till slut men då kan man bara skriva sliced_list1 = list2[0] istället
sliced_list1 = list2[1:3] #från index 1 till 3 funkar även för strings som sliced_string = string [1:3]
print(sliced_list)
print(sliced_list1)

# appened är för att lägga till en visst typ av data i en lista så som i vår lista list1 så har det ingen data i sig
list1.append("hello world!") 
list1.append("knnbccbdllm test")
print(list1)

list1.insert(1, " my") # insert är lägga till en till men i index position som "my" är inlagd på index 1 i list1
print(list1)

#set 

set1 = {1,2,3,4}
set2 = {}
set3 = set()
set4 = set(list4)

print(set1,type(set1))
print(set2,type(set2))
print(set4,type(set4))