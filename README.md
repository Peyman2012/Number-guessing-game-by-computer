# Number-guessing-game-by-computer

![logo](https://github.com/Peyman2012/Number-guessing-game-by-computer/assets/88220773/c7e44beb-9c49-4f3e-bf95-671453cbe578)



This program is written using the Random library:

    import random

It randomly selects the numbers from 0 to 100:

    rand = random.randint(1,100)

Every time he guesses a number, if it was not the number we wanted, the word "b" because the guessed number was bigger than our number, and the word "k" because the guessed number was smaller than our number, and "ok" because If the guessed number is the same as the number guessed by the program, it will be exited from the infinite loop with the "break" command:

     ent = " "
     a = True
     while a:
         if ent == "b":
            rand = random.randint(rand, 100)
            print(rand)
         elif ent == "k":
            rand = random.randint(1, rand)
            print(rand)
         elif ent == "ok":
             print("pc is good!!!!")
             break
         ent = input("Enter b or k : ")
