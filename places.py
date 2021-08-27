import actions
import phrases
import avail_nut

class Nest(object):
    def enter(self, stash):
        print(phrases.nest_welcome)
        print(phrases.nest_options)

        action = input("\n>> ")

        if 'leave' in action:
            return 'front_yard'
        elif 'check' in action or 'stash' in action:
            actions.CheckStash(stash)
            return 'nest'
        else:
            actions.NotAChoice(action)
            return 'nest'

class FrontYard(object):
    def enter(self, stash):
        print('\n', '*' * 12, '\n', phrases.front_yard_welcome)
        print(phrases.front_yard_options)

        action = input("\n>> ")

        if action == 'tree':
            return 'tree_1'
        elif action == 'front porch':
            return 'front_porch'
        elif action == 'flower bed':
            return 'flower_bed'
        elif action == 'backyard':
            return 'back_yard'
        elif 'check' in action or 'stash' in action:
            actions.CheckStash(stash)
        else:
            actions.NotAChoice(action)
        return 'front_yard'

class Tree1(object):
    def enter(self, stash):
        print('\n', '*' * 12, '\n',phrases.tree_1_welcome)
        print(phrases.tree_1_options)

        action = input("\n>> ")

        if 'circle' in action:
            if avail_nut.tree1_circle == True:
                print('\n', '*' * 12, '\n', phrases.circle_description1)
                actions.FindaNut(stash)
                avail_nut.tree1_circle = False
            else:
                print('\n', '*' * 12, '\n', phrases.circle_description2)    
        elif 'dig' in action:
            if avail_nut.tree1_dig == True:
                print('\n', '*' * 12, '\n', phrases.dig_description1)
                actions.FindaNut(stash)
                avail_nut.tree1_dig = False
            else:
                print('\n', '*' * 12, '\n', phrases.dig_description2)
        elif 'climb' in action:
            actions.ClimbTree1(stash)
        elif 'back' in action or 'front' in action:
            return 'front_yard'
        elif 'check' in action or 'stash' in action:
            actions.CheckStash(stash)
        else:
            actions.NotAChoice(action)
        return 'tree_1'

class FrontPorch(object):
    def enter(self, stash):
        print('\n', '*' * 12, '\n', phrases.front_porch_welcome)
        print(phrases.front_porch_options)

        action = input("\n>> ")

        if 'climb' in action:
            print('\n', '*' * 12, '\n', phrases.frontporch_chair1)
            print('\n', '*' * 12, '\n', "Would you like to jump up again? Yes or No?")
            jump_again = input("\n>> ")
            if jump_again == "Yes" or jump_again == "yes" or jump_again == 'y': 
                if avail_nut.frontporch_chair == True:
                    print('\n', '*' * 12, '\n', phrases.frontporch_chair2)
                    actions.FindaNut(stash)
                    avail_nut.frontporch_chair = False
                else:
                    print('\n', '*' * 12, '\n', phrases.circle_description2)
            else:
                return 'front_porch' 
        elif 'dig' in action:
            pass
            #you find a nut!
        elif 'search' in action:
            print("The floor is dirty! They need to sweep out here!")
            return 'front_porch'
        elif 'back' in action or 'front' in action:
            return 'front_yard'
        elif 'check' in action or 'stash' in action:
            actions.CheckStash(stash)
        else:
            actions.NotAChoice(action)
        return 'front_porch'

class FlowerBed(object):
    def enter(self, stash):
        print("Stuff")
        print("options")
        
        action = input("\n>> ")

        if 'climb' in action:
            pass
            #you find a nut!
        elif 'dig' in action:
            pass
            #you find a nut!
            return 'front_porch'
        elif 'search' in action:
            print("The floor is dirty! They need to sweep out here!")
            return 'front_porch'
        elif 'check' in action or 'stash' in action:
            actions.CheckStash(stash)
        else:
            actions.NotAChoice(action)
            return 'flower_bed'


class BackYard(object):
    def enter(self, stash):
        print("Stuff")
        print("options")
        
        action = input("\n>> ")

        if 'climb' in action:
            pass
            #you find a nut!
        elif 'dig' in action:
            pass
            #you find a nut!
            return 'front_porch'
        elif 'search' in action:
            print("The floor is dirty! They need to sweep out here!")
            return 'front_porch'
        elif 'check' in action or 'stash' in action:
            actions.CheckStash(stash)
        else:
            actions.NotAChoice(action)
            return 'flower_bed'

class Tree2(object):
    def enter(self, stash):
        print("Stuff")
        print("options")
        
        action = input("\n>> ")

        if 'climb' in action:
            pass
            #you find a nut!
        elif 'dig' in action:
            pass
            #you find a nut!
            return 'front_porch'
        elif 'search' in action:
            print("The floor is dirty! They need to sweep out here!")
            return 'front_porch'
        elif 'check' in action or 'stash' in action:
            actions.CheckStash(stash)
        else:
            actions.NotAChoice(action)
            return 'flower_bed'

class Patio(object):
    def enter(self, stash):
        print("Stuff")
        print("options")
        
        action = input("\n>> ")

        if 'climb' in action:
            pass
            #you find a nut!
        elif 'dig' in action:
            pass
            #you find a nut!
            return 'front_porch'
        elif 'search' in action:
            print("The floor is dirty! They need to sweep out here!")
            return 'front_porch'
        elif 'check' in action or 'stash' in action:
            actions.CheckStash(stash)
        else:
            actions.NotAChoice(action)
            return 'flower_bed'

class VegetableGarden(object):
    def enter(self, stash):
        print("Stuff")
        print("options")
        
        action = input("\n>> ")

        if 'climb' in action:
            pass
            #you find a nut!
        elif 'dig' in action:
            pass
            #you find a nut!
            return 'front_porch'
        elif 'search' in action:
            print("The floor is dirty! They need to sweep out here!")
            return 'front_porch'
        elif 'check' in action or 'stash' in action:
            actions.CheckStash(stash)
        else:
            actions.NotAChoice(action)
            return 'flower_bed'

class Tree3(object):
    def enter(self, stash):
        print("Stuff")
        print("options")
        
        action = input("\n>> ")

        if 'climb' in action:
            pass
            #you find a nut!
        elif 'dig' in action:
            pass
            #you find a nut!
            return 'front_porch'
        elif 'search' in action:
            print("The floor is dirty! They need to sweep out here!")
            return 'front_porch'
        elif 'check' in action or 'stash' in action:
            actions.CheckStash(stash)
        else:
            actions.NotAChoice(action)
            return 'flower_bed'

class NeighborTree(object):
    def enter(self, stash):
        print("Stuff")
        print("options")
        
        action = input("\n>> ")

        if 'climb' in action:
            pass
            #you find a nut!
        elif 'dig' in action:
            pass
            #you find a nut!
            return 'front_porch'
        elif 'search' in action:
            print("The floor is dirty! They need to sweep out here!")
            return 'front_porch'
        elif 'check' in action or 'stash' in action:
            actions.CheckStash(stash)
        else:
            actions.NotAChoice(action)
            return 'flower_bed'
  
class NeighborBackyard(object):
    def enter(self, stash):
        print("Stuff")
        print("options")
        
        action = input("\n>> ")

        if 'climb' in action:
            pass
            #you find a nut!
        elif 'dig' in action:
            pass
            #you find a nut!
            return 'front_porch'
        elif 'search' in action:
            print("The floor is dirty! They need to sweep out here!")
            return 'front_porch'
        elif 'check' in action or 'stash' in action:
            actions.CheckStash(stash)
        else:
            actions.NotAChoice(action)
            return 'flower_bed'
        
class NeighborFlowerbed(self, stash):
        print("Stuff")
        print("options")
        
        action = input("\n>> ")

        if 'climb' in action:
            pass
            #you find a nut!
        elif 'dig' in action:
            pass
            #you find a nut!
            return 'front_porch'
        elif 'search' in action:
            print("The floor is dirty! They need to sweep out here!")
            return 'front_porch'
        elif 'check' in action or 'stash' in action:
            actions.CheckStash(stash)
        else:
            actions.NotAChoice(action)
            return 'flower_bed'
        
class NeighborDeck(self, stash):
        print("Stuff")
        print("options")
        
        action = input("\n>> ")

        if 'climb' in action:
            pass
            #you find a nut!
        elif 'dig' in action:
            pass
            #you find a nut!
            return 'front_porch'
        elif 'search' in action:
            print("The floor is dirty! They need to sweep out here!")
            return 'front_porch'
        elif 'check' in action or 'stash' in action:
            actions.CheckStash(stash)
        else:
            actions.NotAChoice(action)
            return 'flower_bed'        

class NeighborFrontYard(object):
    def enter(self, stash):
        print("Stuff")
        print("options")
        
        action = input("\n>> ")

        if 'climb' in action:
            pass
            #you find a nut!
        elif 'dig' in action:
            pass
            #you find a nut!
            return 'front_porch'
        elif 'search' in action:
            print("The floor is dirty! They need to sweep out here!")
            return 'front_porch'
        elif 'check' in action or 'stash' in action:
            actions.CheckStash(stash)
        else:
            actions.NotAChoice(action)
            return 'flower_bed'        

class NeighborBushes(object):
    def enter(self, stash):
        print("Stuff")
        print("options")
        
        action = input("\n>> ")

        if 'climb' in action:
            pass
            #you find a nut!
        elif 'dig' in action:
            pass
            #you find a nut!
            return 'front_porch'
        elif 'search' in action:
            print("The floor is dirty! They need to sweep out here!")
            return 'front_porch'
        elif 'check' in action or 'stash' in action:
            actions.CheckStash(stash)
        else:
            actions.NotAChoice(action)
            return 'flower_bed'        

class NeighborLawn(object):
    def enter(self, stash):
        print("Stuff")
        print("options")
        
        action = input("\n>> ")

        if 'climb' in action:
            pass
            #you find a nut!
        elif 'dig' in action:
            pass
            #you find a nut!
            return 'front_porch'
        elif 'search' in action:
            print("The floor is dirty! They need to sweep out here!")
            return 'front_porch'
        elif 'check' in action or 'stash' in action:
            actions.CheckStash(stash)
        else:
            actions.NotAChoice(action)
            return 'flower_bed'        
        
class Finished(object):
    def enter(self):
        print("Congratulations! You have all the nuts you need for the winter now!")
        return 'finished'
