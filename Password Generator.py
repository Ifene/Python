def Password_Gen():
    #Password Generator Project
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    nr_letters= int(input("How many letters would you like in your password?\n")) 
    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    #Eazy Level - Order not randomised:
    #e.g. 4 letter, 2 symbol, 2 number = JduE&!91


    #Hard Level - Order of characters randomised:
    #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P



    #Randomly choosing from the lists
    # Ran_L = random.choice(letters)
    # Ran_N = random.choice(numbers)
    # Ran_S = random.choice(symbols)

    #Easy Mode
    # password = ""

    # #nr_letters = 4 in this instance:
    # for RandomL in range(1, nr_letters + 1):
    #   password += random.choice(letters)

    # for RandomN in range(1, nr_numbers + 1):
    #   password += random.choice(numbers)
    
    # for RandomS in range(1, nr_symbols + 1):
    #   password += random.choice(symbols)

    # print(password)

    #Hard Mode
    #Instead of a string we'll be adding it all to a list
    password_list = []

    #nr_letters = 4 in this instance:
    for RandomL in range(1, nr_letters + 1):
        password_list += random.choice(letters)

    for RandomN in range(1, nr_numbers + 1):
    #Another way to do it is with append. Adds to a list
        password_list.append(random.choice(numbers))
    
    for RandomS in range(1, nr_symbols + 1):
        password_list += random.choice(symbols)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    print(f'Your password is: {password}')