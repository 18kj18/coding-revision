import random

while True:
    #Inputs
    s_name=input("Enter your surname\n---> ")    
    f_name=input("Enter your first name\n---> ")
    age = int(input("Enter your age\n---> "))
    eircode = input("Enter your eircode\n---> ")
    choice = input('Would you like to try free super vaccine. type YES please please please\n---> ').lower()

    #Check eircode
    if int(eircode[-1]) % 2 == 0:
        place = "Northfield"
    else:
        place = "Eastwood"

    #Check age
    if age >= 12 and age <= 49:
        vaccine = 'MRNA'
    elif age >= 50:
        vaccine = 'ADENO'
    else:
        vaccine = 'None'
        
    #Super vaccine randomiser
    super_list = ['Super Vaccine A', 'Super Vaccine B', 'Super Vaccine C']
    if choice in ['yes', 'yeah', 'yea', 'please'. 'please give me the vaccine']:
        rand_vaccine = 'You will recieve ' + str(random.choice(super_list))
    else:
        rand_vaccine = ''
        
    
    #The print statements
    for i in range(0, 15, 1):
            print(' ')
    print("Hello", f_name, s_name, "you are, ", age, "years old")
    print("Eircode is, ", eircode)
    print("You must attend ", place, " for your vaccine")
    print(f_name, ", you will recieve the ", vaccine, " vaccine")
    print(rand_vaccine)
        
    if input("\ntype hi to end program\n---> ") == 'hi':
        quit()
    else:
        for i in range(0, 15, 1):
            print(' ')
    
