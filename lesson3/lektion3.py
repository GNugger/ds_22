

def my_function(name):
    print("in my function")
    return "hej"+ name

# my_function ("")
#print(my_function("Fay"))

def a_general_function(*args,**kwargs): # en asterisk det är postional arguments och två är keywords arguments
        a,b,c,d,e,f,g=args # position spelar roll
        print 
        print(a,g)
        print(args,kwargs)
        
a_general_function("a","b",1,2,3,True,False, name="Fay") ## kan inte lika keywe