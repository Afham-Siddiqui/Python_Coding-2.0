print("Find the best movies for your taste!!!\n")
name = str(input("Enter your name...\n"))
print("Welcome", name, "\n")

pass_1 = (input("Enter your password (password is your name).."))

if pass_1 == name:
    print("you have successfully logged in!\n")

    choice = int(input("Enter category of movie(please write category no.) \n1.action, \n2.adventurous, \n"
                       "3.comedy, \n4.horror \n"))

    if choice == 1:
        print("1.AVENGERS ENDGAME\n"
              "2.AVENGERS INFINITY WAR\n"
              "3.THE AVENGERS CAPTAIN MARVEL\n"
              "4.Black Panther (2018)\n"
              "5.MISSION: IMPOSSIBLE (FALL OUT)\n"
              "6.MISSION: IMPOSSIBLE (GHOST PROTOCOL)\n"
              "7.HARRY POTTER AND DEATH VALLEY\n"
              "8.WONDER WOMAN\n"
              "9.TERMINATOR: DARK FATE\n"
              "10TERMINATOR 2: JUDGMENT DAY\n"
              "11.EDGE OF TOMORROW\n"
              "12.FAST ANS FURIOUS: (HOBBS AND SHAW)\n"
              "13.THE DARK KNIGHT \n"
              "14.THE DARK KNIGHT RISES\n"
              "15.GUARDIANS OF THE GALAXY")

    if choice == 2:
        print("1.JURASSIC WORLD\n"
              "2.ANT-MAN (THE WASP)\n"
              "3.JOURNEY TO THE CENTER OF THE EARTH\n"
              "4.JOURNEY TO THE MYSTERIOUS ISLAND\n"
              "5.STAR TREK INTO DARKNESS\n"
              "6.LIFE OF PIE\n"
              "7.JURASSIC PARK\n"
              "8.PIRATES OF THE CARIBBEAN: (CURSE OF BLACK PEARL)\n"
              "9.AVATAR\n"
              "10.NATIONAL TREASURE\n"
              "11.THE HOBBIT: (AN UNEXPECTED JOURNEY)\n"
              "12.THE HOBBIT: (THE DESOLATION OF SMAUG\n"
              "13.SHERLOCK HOLMES: (THE GAME OF SHADOWS)\n"
              "14.PIRATES OF THE CARIBBEAN: (AT WORLD'S\n"
              "15.NIGHT AT THE MUSEUM: (SECRET OF THE TOMB)")

    if choice == 3:
        print("1.Books Mart\n"
              "2.Game Night\n"
              "3.21 Street Jump\n"
              "4.22 Street Jump\n"
              "5.The Hangover\n"
              "6.Airplane!\n"
              "7.Anchorman: The Legend of Ron Burgundy\n"
              "8.Best in Show \n"
              "9.Big \n"
              "10.Bridesmaids \n"
              "11.Clueless \n"
              "12.Coming to America \n"
              "13.Dr. Strangelove \n"
              "14.Old School\n"
              "15.Scary Movie")

    if choice == 4:
        print("1.A Quite Place\n"
              "2.Hereditary\n"
              "3.The Nun\n"
              "4. Get Out\n"
              "5. It\n"
              "6.It Chapter Two\n"
              "7.The Witch\n"
              "8.The Conjuring\n"
              "9.The Conjuring 2\n"
              "10.A Cabin In The Woods\n"
              "11.Annabelle\n"
              "12.It Comes At Night\n"
              "13.Let The Right One In\n"
              "14.A Nightmare On Elm Street\n"
              "15.It Follows")

else:
    print("wrong password")