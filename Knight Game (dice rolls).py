import random
 
def main():

    roll = 0
    rounds = 1
    apples = 0
    mushrooms = False
    
    player_HP = 100

    while rounds != 11:
        print("\n")
        print("Round " + str(rounds))
        roll = dice_roll()
        

        if roll >= 1 and roll <= 6:
            print ("Prepare for COMBAT!")
            print ("HP: ", player_HP)
            

        elif roll == 7:
            print("You have recieved a BOON: 1 apple \nDo you want to eat it? \n [1] Yes\n [2] No\n")
            choice = 0
            
            while choice < 1 or choice > 2:
                choice = int(input("(Enter the number of the corresponding option)\n"))

            if choice == 1:
                player_HP = player_HP + 10 
            
            else:
                apples = apples + 1
                

        elif roll == 8:
            print("You have recieved a BOON: 2 apples \nDo you want to eat it? \n [1] Yes\n [2] No\n")
            choice = 0
            
            while choice < 1 or choice > 2:
                choice = int(input("(Enter the number of the corresponding option)\n"))

            if choice == 1:
                player_HP = player_HP + 20 
            
            else:
                apples = apples + 2
                

        elif roll == 9:
            print("You have recieved a BOON: 3 apples \nDo you want to eat it? \n [1] Yes\n [2] No\n")
            choice = 0
            
            while choice < 1 or choice > 2:
                choice = int(input("(Enter the number of the corresponding option)\n"))

            if choice == 1:
                player_HP = player_HP + 30 
            
            else:
                apples = apples + 3 


        elif roll == 10:
            print("You have recieved a BOON: 4 apples \nDo you want to eat it? \n [1] Yes\n [2] No\n")
            choice = 0
            
            while choice < 1 or choice > 2:
                choice = int(input("(Enter the number of the corresponding option)\n"))

            if choice == 1:
                player_HP = player_HP + 40 
            
            else:
                apples = apples + 4


        elif roll == 11:
            print ("You have received a BOON: 1 mushroom")
            mushroom = True
            print ("HP: ", player_HP)
             
            
        elif roll == 12:
            print ("You have arrived at a CAMPSITE!")
            if player_HP < 100:
                return hp == 100
            print ("HP: ", player_HP)
        

        rounds = rounds + 1
        
        
def dice_roll():
    diceRoll = random.randint(1, 12)
    return diceRoll

     
main()











