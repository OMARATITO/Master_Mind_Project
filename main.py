import random

COLORS = ["R","G","B","W","O","Y"]
TRIES = 10
CODE_WIDTH = 4

def generate_code():
    code = []
    for _ in range(CODE_WIDTH):
        color = random.choice(COLORS)
        code.append(color)
    return code        

def guess_code():

    while True:
        guess = input("please enter your guess: ").upper().split(" ")

        if len(guess) != CODE_WIDTH:
            print(f"you must guess {CODE_WIDTH} colors !")
            continue

        for i in guess:
            if i not in COLORS:
                print(f"Invalid Color: {i} please try again !")
                break
        else:
            break
    return guess

def check_code(guess, real_code):
    color_count = {}
    correct_pos = 0
    incorrect_pos = 0

    for i in real_code:
        if i not in color_count:
            color_count[i] = 0
        color_count[i] += 1
    
    for guess_code , real in zip(guess,real_code):
        if guess_code == real:
            correct_pos += 1
            color_count[guess_code] -= 1

    for guess_code , real in zip(guess,real_code):
        if guess_code  in color_count and color_count[guess_code]>0:
            incorrect_pos += 1
            color_count[guess_code] -= 1
    return correct_pos , incorrect_pos

def game():
    print(f"welcome to 'Master Mind Game' you have {TRIES} Attempts")
    print("the valid colors are ", *COLORS)
    
    code = generate_code()
    for i in range(1,TRIES +1):
        guess = guess_code()
        correct_pos , incorrect_pos = check_code(guess,code)

        if correct_pos == CODE_WIDTH:
            print(f"you guessed the code in {i} tries")
            break

        print(f"correct position: {correct_pos} | incorrect position: {incorrect_pos}")

    else:
        print(f"you ran out of tries the code was " , *code)

if __name__=="__main__":
    game()

# this is my MASTER_MIND_PROJECT


