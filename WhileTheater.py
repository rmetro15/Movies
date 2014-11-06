def movies():
        total = 0
        weather = input("Is it raining?:    ")
        if weather.upper() == "YES":
                return "We're closed, sorry"
        amntPpl = eval(input("How many people are there?:   "))
        for i in range(amntPpl):
            print("Person " + str(i+1) + ":")
            price = 5
            ID = input("Are you a student, veteran, or nurse?:  ")
            if ID.upper() == "YES":
                ID = input("Which one?: ")
            age = eval(input("What is your age?:  "))
            if weather.upper() == "NO":
                price = price
            if(age < 12):
                price = 0
            if(age < 60):
                price = 12
            if(age > 60):
                price = 7
            if ID.upper() == "STUDENT":
                price = price *.7
            if ID.upper() == "NURSE":
                price = price *.65
            if ID.upper() == "VETERAN":
                price = price *.6
            total += price
            print("Your ticket costs: $" + str(price))
            
