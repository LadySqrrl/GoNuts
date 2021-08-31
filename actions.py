import random

def NotAChoice(action):
    print('\n', '*' * 12)
    print(f"{action} is not a choice, silly!")

def BacktoNest():
    print('\n', '*' * 12, "\nYou scamper back to your nest to hide.")
    return 'nest'

def CheckStash(nut_stash):
    print('\n', '*' * 12, '\n')
    print(f"You have {len(nut_stash)} nuts in your stash")
    
def IsNut():
    random.seed()
    a = random.randint(0, 15)
    
    if (a % 3) == 0:
        return True
    else:
        return False

def FindaNut(stash):
    #Need to add a random chance of finding a nut
    print('\n', '*' * 12, "\nCongratulations! You found a nut!")
    stash.append("nut")

def ClimbTree1(stash):
    print("You scamper up the trunk of the tree")
    print("When you reach the first limb you have a choice: go up or to the right?")
    print("The branch to the right looks a little sketchy, but it loosk like there might be a nut there.")

    action = ('\n>>')

    if action == 'right':
        Tree1Climb1Up(stash)
    elif action == 'up':
        print("You scamper to the right and up into the branches.")
        FindaNut(stash)
    
def Tree1Climb1Up(stash):
    print("You carfully make your way to the branch on the right and look around.") 
    print("Out on the end of the limb is a nut hanging from a twig")
    print("The limb looks pretty old and thin, do you want to go out on it and get the nut? Yes/No")
    action = ('\n>>')
    
    if action == 'yes':
        print("""You wiggle your way out to the end of the branch on your tummy. Right as you grab the nut, 
        the branch breaks and you fall to the ground""")
        print("""Good things squirrels are good at changing position in flight! 
        You land on your feet in the front yard and find the nut laying next to you""")
        FindaNut(stash)
    return
