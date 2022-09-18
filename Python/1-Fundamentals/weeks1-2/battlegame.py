#Basic battle game using Python fundamentals. This will use loops and conditionals to make a battle between a chosen character and a dragon

#step 1: establish characters with type, health, and damage
wizard = "Wizard"
elf = "Elf"
human = "Human"
master_cheif = "Master Cheif"

wizard_hp = 70
elf_hp = 100
human_hp = 150

wizard_damage = 150
elf_damage = 100
human_damage = 20

master_Cheif_hp = 500
master_cheif_damage = 65

#step 2: create a dragon with health, damage and type

dragon_hp = 300
dragon_damage = 50
#step 3: character selection while loop
while(True):
    print("For the best experience, please make your terminal fullscreen :)")
    while(True):
        print(f"1) {wizard}")
        print(f"2) {elf}")
        print(f"3) {human}")
        print(f"4) {master_cheif}")
        print("5) EXIT" )
        print("Choose your hero:")
        character_choice = input()
        if(character_choice == "1" or character_choice.lower()== "wizard"):
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            break
        elif(character_choice == "2" or character_choice.lower() == "elf"):
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            break
        elif(character_choice == "3" or character_choice.lower() == "human"):
            character = human
            my_hp = human_hp
            my_damage = human_damage
            break
        elif(character_choice == "4" or character_choice.lower() == "master cheif" or character_choice.lower() == "mastercheif"):
            character = master_cheif
            my_hp = master_Cheif_hp
            my_damage = master_cheif_damage
            print("An ODST drop pod comes down from the sky. Master cheif has joined the battle.")
            break
        elif(character_choice == "5" or character_choice.lower() == "exit"):
            print("Good Bye")
            quit()
        else:
            print("Invalid option. Please select 1, 2, or 3")

    print("Character: " + character)
    print("HP: " +  str(my_hp))
    print("Damage: " + str(my_damage))

    # this artwork is not mine, I found it on the Internet, But I thought it was super cool, If needed, I can resubmit without the artwork :) Source: https://asciiart.cc/view/12177
    print('''
                                                    /===-_---~~~~~~~~~------____
                                                    |===-~___                _,-'
                    -==\\                         `//~\\   ~~~~`---.___.-~~
                ______-==|                         | |  \\           _-~`
            __--~~~  ,-/-==\\                        | |   `\        ,'
        _-~       /'    |  \\                      / /      \      /
    .'        /       |   \\                   /' /        \   /'
    /  ____  /         |    \`\.__/-~~ ~ \ _ _/'  /          \/'
    /-'~    ~~~~~---__  |     ~-/~         ( )   /'        _--~`
                    \_|      /        _)   ;  ),   __--~~
                        '~~--_/      _-~/-  / \   '-~ |
                        {\__--_/}    / \\_&gt;- )&lt;__\      \
                        /'   (_/  _-~  | |__&gt;--&lt;__|      |
                    |0  0 _/) )-~     | |__&gt;--&lt;__|     |
                    / /~ ,_/       / /__&gt;---&lt;__/      |
                    o o _//        /-~_&gt;---&lt;__-~      /
                    (^(~          /~_&gt;---&lt;__-      _-~
                    ,/|           /__&gt;--&lt;__/     _-~
                ,//('(          |__&gt;--&lt;__|     /                  .----_
                ( ( '))          |__&gt;--&lt;__|    |                 /' _---_~\
            `-)) )) (           |__&gt;--&lt;__|    |               /'  /     ~\`\
            ,/,'//( (             \__&gt;--&lt;__\    \            /'  //        ||
        ,( ( ((, ))              ~-__&gt;--&lt;_~-_  ~--____---~' _/'/        /'
        `~/  )` ) ,/|                 ~-_~&gt;--&lt;_/-__       __-~ _/
    ._-~//( )/ )) `                    ~~-'_/_/ /~~~~~~~__--~
        ;'( ')/ ,)(                              ~~~~~~~~~~
    ' ') '( (/
        '   '  `
    
    ''')
    print("A wild Dragon Appeared!")

    #Step 4 Battle loop! :) 

    while(True):
        dragon_hp = dragon_hp - my_damage
        if(dragon_hp < 0):
            dragon_hp = 0
        print("the " + character + " damaged the dragon!")
        print("the Dragon's HP is: " + str(dragon_hp) + ".")
        if dragon_hp <= 0:
            print("the Dragon has died.")
            break
        my_hp = my_hp - dragon_damage
        if(my_hp < 0):
            my_hp = 0
        print("The Dragon has attacked!")
        print(character + " has " + str(my_hp) + " HP.")
        if(my_hp <= 0):
            print("the " + character + " has been defeated. They died a heroic yet foolish death.")
            break
    print("want to play again?")
    print("1) yes")
    print("2) no")
    play_again = input()
    if(play_again == "1" or play_again.lower() == "yes"):
        print("Restarting program....")
    else:
        break
    
 