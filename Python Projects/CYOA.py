#choose your own adventure
name = input('Typre youe name: ')
print('Welcome', name, 'to this adventure.')

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way you would like to go? ").lower()

if answer == 'left':
    answer = input('You have arrived to a river.There is two ways around it, walk around it through the jungle or swim across? Type walk to walk around and swim ti swim across: ')

    if answer == 'swim':
        print("You swam across and were eaten by an aligator.")
    elif answer == 'walk':
        print('You walked for many miles.Trying to find the way across but instead got lost in the jungle and later got eaten by a Lion')
    else:
        print('Not a valid option.You lose.')


elif answer == 'right':
    answer = input('You came across a bridge, it looks wobbly due to high speed of wind, do you want to cross it or head back?(cross/back) ')

    if answer == 'back':
        print("You lose. Next time you see a word adventure aleast show some courage.")
    elif answer == 'cross':
        answer = input('You crossed the bridge successfully and there you see stranger. Do you wanna talk to him?(Yes/No) ')

        if answer == 'yes':
            print('The stranger was the old man who claims he had a map of a godly teasure which you have to find.He said the gods have have you. Are you ready for a thriller adventure to find this treasure or are you gonna back down from the challenges you gonna face on this sdventure?(yes/no) ')
        elif answer == 'no':
            print('The stranger was mental hospital patient who escaped from the hospital few hours ago. And you ignored him which made him angry with resulted him throwing a rock behind your head and you died.')
        else:
            print('Not a valid option. You lose!')
    else:
        print('Not a valid option.You lose.')



else:
    print('Not a valid option. you lose :/')

print('Thank you for playing. hope you enjoyed this.')