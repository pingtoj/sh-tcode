import numpy as np

alphabets= [['a','b','c','d'],['e','f','g','h'],['i','k','l','m'],['n','o','p','q'],['r','s','t','u'],['v','w','x','y']]

flattened_ = np.array(alphabets).flatten()

def guess():     
    print("Which do you think is normal?")    
    correct_guess =['j', 'z']
    valid_characters = np.append(flattened_, ['j', 'z'])    
    while True:
        guess = input("Enter your guess: ").lower()
        if len(guess) != 1
        
            print("Please enter only one character.")
            continue        
        elif guess not in valid_characters:
            print(f"Invalid input! Please guess a character from the alphabet set.")
            continue         
        elif guess in correct_guess == correct_guess:
            print(f"{guess} is definitively a normal variable.")
            break  
        else:
            print(f"Keep guessing. {guess} is not correct!")

