print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Willkommen zur Schatzsuche.")
print("Versuche den Schatz zu finden.")

choice1=input("Du bist mit deinem Schiff nach langer und gefährlicher Fahrt zu einer Insel gelangt, die genau so aussieht wie auf der Schatzkarte die du in einer alten Kiste in einer Höhle gefunden hast. \r\nAuf der Karte siehst du 2 Wege die von der Stelle am Strand an der du stehst wegführen. Der linke führt zu einem grossen Fluss in dem einige Krokodile eingezeichnet sind und auf der anderen Seite ein gelbes Haus steht. Der rechte Pfad führt zu einem schwarzen Kreis.\r\nWelchen Weg willst du folgen? Dem (l)inken oder (r)echten? ")
if choice1 == "l":
    choice2=input("Du folgst dem linken Pfad der dich nach etwa 40min zu einem grossen Fluss führt. Der Fluss ist sehr breit aber die Strömung scheint nicht stark zu sein. Du überlegst ob du (s)chwimmen oder erstmal (a)bwarten solltest. ")
    if choice2 == "a":
        choice3 = input("Du setzt dich an das Ufer des Flusses. Mit schrecken bemerkst du dunkle Schatten im Fluss. Doch nach einer Weile bemerkst du etwas flussaufwärts einige grosse Steine aus dem Fluss ragen. Schnell sprinst du so ohne nass zu werden über den Fluss ans andere Ufer. Dort bemerkst du ein würfelförmiges Gebilde. An drei Seiten sind eine gelbe, eine blaue und eine rote Tür. Gehst du durch die (r)ote oder (g)elbe oder (b)laue Tür? ")
        if choice3 == "r":
            print("Vorsichtig öffnest du die rote Tür und betrittst den Raum. Doch die Tür schlägt hinter dir zu und plötzlich ist der Raum in Flammen gehüllt die dich verzehren. GAME OVER")
        elif choice3 == "b":
            print("Du öffnest die blaue Tür, doch bevor sie richtig offen ist, sprint dich ein Raubtier an und vergräbt seine spitzen Zähne in deinen Leib. GAME OVER")
        elif choice3 == "g":
            print("Du öffnest die gelbe Tür, auf einem Altar steht eine grosse Kiste. Als du die Kiste öffnest ist sie voller Gold und Diamanten. DU HAST GEWONNEN!")
        else:
            print("Du traust den Türen nicht und kehrst zum Schiff ohne den Schatz zurück. ENDE")

    else:
        print("Du beginnst den Fluss zu durchschwimmen. Du kommst gut voran, doch in der hälfte des Flusses bemerkst du plötzlich einen dunklen Schatten der dich verfolgt. Du schwimmst so schnell du kannst doch der Schatten holt dich ein und ein grosses Krokodilmaul packt eines deiner Beine und zieht dich unter die Wasseroberfläche. GAME OVER")

else:
    print("Du folgst dem rechten Pfad. Nach einigen Minuten spürst du plötzlich wie der Boden nachgibt und du in ein Loch stürzt. GAME OVER")