#Importing the time module
import time

#Ways the User might respond
answer_A = ['A','a']
answer_B = ['B','b']
answer_C = ['C','c']
yes = ['Y','y','yes']
no = ['N','n','no']

#Instruction
required = ('You are required to choose from the options given e.g A,B,C,D...')

#Introduction to the adventure
def intro():
    print('\nWith you still feeling dizzy, you woke earlier in the '
          'morning to urinate. Strangely, you found a venomous snake '
          'in the closet.\nWhat would you do?')
    
    time.sleep(2)
    print('\nA. Run out of the toilet out of fear\n'
          'B. Immediately flush the closet\n'
          'C. You\'d hit the snake with the toilet plunger')
    
    #The user would have to choose what he/she would do
    choice = input('>>> ')
    if choice in answer_A:
        print('You put the whole house in a messy danger. '
              '3 days later your sister got bitten by the '
              'snake from it\'s hiding place '
              'and she died few hours later\n\nYou lose!\n')
    elif choice in answer_B:
        print('Luckily the snake was flushed. '
              'Your family is safe.\nThat\'s a nice initiative! ')
    elif choice in answer_C:
        option_hit_1()
    else:
        print(required)
        intro()
        
def option_hit_1():
    print('Unfortunately, you hit the wrong part of the snake\'s body '
          'which was not effective because you use a rubber plunger '
          '\nWhat would you do next?\n ')
    
    time.sleep(2)
    print('A. Hit the snake strongly again\n'
          'B. Quickly run outside ')
    
    #User is to choose from the hit option
    choice = input('>>> ')
    
    if choice in answer_A:
        print('This time around the snake becomes weak.'
              'Would you take it out to kill properly? Y/N') 
        
        #User would have to choose either yes or no
        choice = input('>>> ')
        if choice in yes:
            option_hit_2()
        elif choice in no:
            print('You gave it enough time to revitalise,'
                  'you then got poisoned and died. \n\nYou lost!')

    elif choice in answer_B:
        option_run_outside()
    else:
        print(required)
        option_hit_1()

def option_hit_2():
    print('Fortunately, you were able to kill the snake properly and burnt it'
          '\nGood job!')
def option_run_outside():
    print('Did you quickly ran outside to get a stick to kill the snake? Y/N' )
    
    choice = input('>>> ')
    if choice in yes:
        print('You were able to grab a stick, which you '
              'used to kill the snake and disposed it.'
              '\n\nExcellent Initiative!')
    elif choice in no:
        print('You ran outside out of fear and kept '
              'your family in danger!'
              '\nYou Lose!!!')


intro()