import random

def word():
    infile = open("Word.py",'r')
    num = random.randint(0,297)
    for i in range(num):
        word = infile.readline()
    infile.close()
    return word

def man(x,Word):
    if x == 0:
        print("      __________")
        print("     |         |")
        print("     |         |")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("     __________|__________")
    if x == 1:
        print("      __________")
        print("     |         |")
        print("     |         |")
        print("    ---        |")
        print("   |___|       |")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("     __________|__________")
    if x == 2:
        print("      __________")
        print("     |         |")
        print("     |         |")
        print("    ---        |")
        print("   |___|       |")
        print("     |         |")
        print("     |         |")
        print("     |         |")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("     __________|__________")
    if x == 3:
        print("      __________")
        print("     |         |")
        print("     |         |")
        print("    ---        |")
        print("   |___|       |")
        print("     |         |")
        print("     |\        |")
        print("     |         |")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("     __________|__________")
    if x == 4:
        print("      __________")
        print("     |         |")
        print("     |         |")
        print("    ---        |")
        print("   |___|       |")
        print("     |         |")
        print("    /|\        |")
        print("     |         |")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("     __________|__________")
    if x == 5:
        print("      __________")
        print("     |         |")
        print("     |         |")
        print("    ---        |")
        print("   |___|       |")
        print("     |         |")
        print("    /|\        |")
        print("     |         |")
        print("      \        |")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("     __________|__________")
    if x == 6:
        print("      __________")
        print("     |         |")
        print("     |         |")
        print("    ---        |")
        print("   |___|       |")
        print("     |         |")
        print("    /|\        |")
        print("     |         |")
        print("    / \        |")
        print("               |")
        print("               |")
        print("               |")
        print("               |")
        print("     __________|__________")
        print("=="*20)
        print()
        print("GAME OVER")
        print("Word =",Word)
        print("=="*20)
        


def check(guess,Word):
    correct = []
    count = 0
    for i in range(0,len(Word)-1,1):
        if guess == Word[i]:
            count +=1
            correct.append(Word[i])
        else:
            correct.append("-" )
        
    if count == 0:
        return correct,False
    else:
        return correct,True
    
def let(correct,old,Word):
    correct_2 = []
    for i in range(0,len(Word)-1,1):
        if old[i] == '-':
            correct_2.append(correct[i])
        else:
            correct_2.append(old[i])
    return correct_2

def win(old,letters):
    for i in range(0,letters,1):
        if old[i] == '-':
            return False
    return True
    
        
def main():
    start = 0
    while start == 0:
        print()
        start = eval(input("Type '1' to play.: "))
        if start == 1:
            while start == 1:
                Word = word()
                #print(Word)
                letters = len(Word)-1
                old = 20*['-']
                x = 0
                print("Word = [","'_' "* letters,"]")
                all_guess = []
                while x != 8:
                    
                    man(x,Word)
                    if x == 6:
                        break
                    guess = input("Guess a letter: ")
                    all_guess.append(guess)
                    print("Guess:",all_guess)
                    correct,count = check(guess,Word)
                    
                    correct_2 = let(correct,old,Word)
                    if correct_2 != old:
                        old = correct_2
                    print("Word =", old)
                    if count == False:
                        x += 1
                    w_l = win(old,letters)
                    if w_l == True:
                        print("=="*20)
                        print()
                        print("You Won!!!!!!")
                        print("Word =",Word)
                        print("=="*20)
                        break   
                start = 0
                
        else:
            print()
            print("Try again")
            start = 0
main()
