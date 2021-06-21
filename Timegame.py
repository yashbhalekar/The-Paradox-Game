answer = input("Do you wanna play the game? (yes 👍/no 👎)")
answer = answer.lower().strip()

if answer == "yes":
    print("WELCOME TO THE TIME")
    answer = input("Choose your option ('s-start','e-exit')")

if answer == "start":
    name = input("Enter your Character Name : ")
    answer = input("Hello"+" "+ name +" "+ "Which mode would you like to play? (story/arcade)" )

if answer == "arcade":
    print('''
        Which Year You Wanna go ?
        1) 1985.
        2) 1935.
    ''')
    answer = input("Enter the year : ")


if answer == "1985":
    print("Hey" + name + "Now you are a part of A Secret Time Agency and you are a JTT now.")

    print("""Hello Roger! Your task is to go back in 1985 through a Time Machine and
            murder a 6ft tall man and get the briefcase from him.
            The briefcase contains some confidential data so you just have to
            take it and come back in 2021.
            
            NOTE : MAN WEARING A BLACK SUIT AND THE BRIEFCASE IS CHAINED TO HIS HAND
        """)
    answer = input("Launch the machine by pressing 'l':")
    answer = input('''You have successfully landed in 1985. 
                    Wait for the man to come at the attack point.
                    FaceOff between you and the man. Press 'g' to attack
                    the man :
                    ''')
    won = input("Well Done ! Roger, Mission Accomplished 💯"
                "Press enter to return")
    print("Roger as you have completed the mission, the general has asked you"
          "to read out the confidential data in the briefcase to him")

    answer = input("To open the file press o:")


    if answer =="o":
        print('''
        
                The man who you killed was your grandfather and as you
                killed your grandfather now your existence is no more.
                                 HOW ?
                GRANDFATHER GOT KILLED , SO HE WOULD NOT MARRY YOUR GRANDMOTHER
                AND AS THEY DON'T GET MARRIED YOUR FATHER WOULDN'T BE BORN AND 
                AS YOUR FATHER IS NOT THERE YOUR MOTHER WOULD MARRY SOMEONE ELSE
                AND THIS IS HOW YOU DON'T EXIST.
                
                THIS IS CALLED GRANDFATHER PARADOX.
        
        ''')

if answer == "1935":
    print("Hey" + name + "Now you are a part of A Secret Time Agency and you are a JTT now.")
    print('''Hello Roger! , your mission is to go back in 1935 and
            hand over a confidential data containing file to a man named 
             John Rix and come back.
        ''')
    answer = input("Launch the machine by pressing 'l':")
    answer = input('''You have successfully landed in 1935. 
                        Approach the man but don't reveal your name and just
                         hand the file over to him.
                         To hand over the file press h :
                        ''')
    print("Handed the file, MISSION ACCOMPLISHED!")
    print('''
            Roger congratulations on completing your trial mission.
            The reason behind this mission was to get you the knowledge
            of BOOTSTRAP PARADOX.
            
            What is Bootstrap Paradox ?
            
            THE FILE WHICH YOU HANDED OVER TO JOHN RIX CONTAINED THE INFORMATION
            ABOUT THIS SECRET TIME AGENCY AND JOHN WAS THE ONE WHO FOUNDED THIS AGENCY.
            YOU CAN SAY THAT "JOHN RIX IS THE FOUNDER OF THE STA".
            NOW AS YOU GAVE HIM THE IDEA ABOUT STA ,SO NOW THE MAIN QUESTION ARISES...
            
            THAT IS FROM WHERE DID THE IDEA OF STA ORIGINALLY CAME FROM ?
            
                        WHAT'S THE ORIGIN OF STA?
                        
            THIS IS WHAT WE CALL AS A BOOTSTRAP PARADOX.
               
            ''')

elif answer == "story":
    print("COMING SOON...")


elif answer == "no":
    print("Have a good Time , BYE!")


else:
    print("You entered something Invalid")