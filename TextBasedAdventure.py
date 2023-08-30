#Made by Max Benningfield

#Flee, rest, inventory in battle, do ability in battle

import random as rn


def clear():
    for i in range(50):
        print("\n")

def Start():
    clear()
    print("""
               _                           
              | |                          
 __      _____| | ___ ___  _ __ ___   ___  
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ 
  \ V  V /  __/ | (_| (_) | | | | | |  __/ 
   \_/\_/ \___|_|\___\___/|_| |_| |_|\___| """)
    
#Character Art
def character(piclass):
    if piclass == 1:
        print("""
   ,
  / \, A ,         
 |    =|= >       .--.
  \ /` | `       /.--.\
   `   |         |====|
       |         |`::`|
       |     .-`\..../`_.-^-._
      /\\/  /  |...::..|`   :   `|
      |:'\ |   /'''::''|   .:.   |
       \ /\-,/\   ::  |..:::::..|
       |\ <` >  >._::_.| ':::::' |
       |`""`   /   ^^  |   ':'   |
       |       |       \    :    /
       |       |        \   :   /
       |       |___/\___|`-.:.-`
       |        \_ || _/    `
       |        <_ >< _>
       |        |  ||  |
       |        |  ||  |
       |       _\.:||:./_
       |      /____/\____\)""")
    elif piclass == 2:
        print("""    ____
                  .'* *.'
               __/_*_*(_
              / _______ \
             _\_)/___\(_/_
            / _((\- -/))_ \
            \ \())(-)(()/ /
             ' \(((()))/ '
            / ' \)).))/ ' \
           / _ \ - | - /_  \
          (   ( .'''. .'  )
          _\"__ /    )\ __"/_
            \/  \   ' /  \/
             .'  '...' ' )
              / /  |  \ \
             / .   .   . \
            /   .     .   \
           /   /   |   \   \
         .'   /    b    '.  '.
     _.-'    /     Bb     '-. '-._
 _.-'       |      BBb       '-.  '-.
(________mrf\____.dBBBb.________)____))""")
    elif piclass == 3:
        print("""
                          ,dM
                         dMMP
                        dMMM'
                        \MM/
                        dMMm.
                       dMMP'_\---.
                      _| _  p 88`.
                    ,db p >  8P|  `.
                   (``T8b,__,'dP |   |
                   |   `Y8b..dP  _  |
                   |    |`T88P_ /  `\
                   :_.-~|d8P'`Y/    /
                    \_   TP       7`\
         ,,__        >   `._  /'  /   `\_
         `._ ""'"~~~~------|`\'      ,'
            "'"~~~-----~~~'\__[|' _.-'  `\
                    --..._     .-'-._     
                   /      /`~~"'   ,'`\_ ,/
                  _    /'        /    ,/
                  | `~-l             /
                  `\           /\.._|
                    \    \      \     \
                    /`---'      `----'
                   (     /
                    `---' """)                 
    elif piclass == 4:
        print("""
             _.--._
            _.JL___
            F"-/\_-7L
            | a/ e | \
           ,L,c,.='/,
        _,-S::S:' '--._
       . \s:::s: .'   /\
      /  \  ::::  /    /  \
     / ,  k S''S.'    j __,l
  ,---/| /  /S   /S '.   |'   
 ,Ljjj |/|.' s .' s   \  L    |
 LL,_ ]( \    /    '.  '.||   
 ||\ > /  -.'_.-.___\.-'(|=="(
 JJ," /   |_  [   ]     _]|   /
  LL\/   ,' '--'-'-----'  \  (
  ||           |          |  >
  JJ     |      |\         |,/
   LL    |      ||       ' |
   ||    |      ||       . |
   JJ    /_     ||       _|
    LL   L "==='|i======='_|
    ||    i----' '-------'
    JJ    '-----.------,-'
     LL     L_.__J,'---'
     ||      |   ,|    (
     JJ     .'=  (|  ,_|
      LL   /    .'L_    \
      ||   '---'    '.___>""")

    elif piclass == 5:
        print("""
                      .,.
                   '" \ \//
                 \|a (a|7 \//
                 j| ..  | ||/
                //'.--.')\-,/
              .-||- '' ||/  `-.
               | \ |/ |/ L.  ,|
             f\ |\| Y  || \ '._\
            j | \|     (| |   | |
           |  L_\         L.__: |
            \(  '-.,-,    |    |
             |'-.'.L_rr>  f--f  |
.-=,,______,--------- J-.   __
   ``"-,__   |  |      h  |  f  '--.__
       `----,_       h  f-j   |   __==-.
            / `-''-,,__J,'  \_..--:'-'     '
            | |    `' --L7//'-'`|
            | ,     ||  h    |  (
            |      | \ J    j   |
            | L__   | |  L_.'    |
            |   |'-.| L.'h  |  : |
            |  \     |  J  : : |
            | :  (    \  'L| : : |
            |    \'.--|    \  : |
            | | : \    \-, /`\ : |
            L-'-__\   \\ '  | | |
                       \\   |'L_j
                    _>  _|   |
                   <___/ /-  \
                        /    /
                        '---'""")                    
    elif piclass == 6:
        print("""
		             .---::-..`           :_-o
		         `:::shhhhhydhhh+        .| |
		    --:-:+-oddsssyh+ysshs/-+    `:  /.
		    :o:-+oyh+syds:..:ss+o-:s   ::.   -/.
		    `//:-oh+/-/ohh:-sh+/+//.  // ~~~--~ oo
		      .+:/+++.--h+..:+s.-+    ||~      ~ y
		      `/://oo..+:--////..o    -_________-
		       .-://o/.+y+ooss../o` .+hhhmy/:.
		         `++:+::oyssy::+/+/-hhhddd`
		      ``--/++/+::/++/////o-::yhmm:
		    `---....:+:+o//o/o/+-..-:/++/
		   .+-..::/..+:+://:/oo-/::... `  `
		   yhyyso/+..+/o:::::y/:+ `    `  `
		  .dhhdd-+:``-/o+++++y/.:.
		 .+hhhd-`+.```:hhsyhsm/`./
		shhhhhd-/:.```.ysosssh-`./
		sddddmy++-````-s++o++y.``+
		 -:++-`//-````+oo+s++y```+
		        `o++/+so`-y++s+o..
		        +++++so` :s++++s
		      .+++++oo   +s++++o
		   .:+yhhhyss/  .yyhhhyyo:`
		  /yyyyyyyhds`  `sdhyyyyyyy:
		  :oyhhy++:.      .:+oyhhyo-""")

#Draw the ascii art for enemies
def draw(type):
	if type == "Lion":
		print("""
======================================================================
                                                ,w.
                                              ,YWMMw  ,M  ,
                         _.---.._   __..---._.'MMMMMw,wMWmW,
                    _.-""        "'"           YP"WMMMMMMMMMb,
                 .-' __.'                   .'     MMMMW^WMMMM
     _,        .'.-'" `,       /`     .--""      :MMM[==MWMW^
  ,mM^"     ,-'.'   /               /   ,       MMMMb_wMW"  @|
 ,MM:.    .'.-'   .'          `\         `,     MMMMMMMW `"=./`-,
 WMMm__,-'.'     /      _.\      F"'"-+,,   _,_.dMMMMMMMM[,_ / `=_
 "^MP__.-'    ,-' _.--""   `-,          \   MMMMMMMMMMW^`` __|
            /   .'                      )  )`  \ `"^W^`,   \  :
           /  .'             /  (       .'  /     Ww._     `.  `"
          /  Y,              `,  `-,=,_         MMMP`""-,  `-._.-,
         (--, )                `,_ / `) \/"")      ^"      `-, -"\:
          `"""                     """   `"'                  `---"
======================================================================
        """)
	
	elif type == "Boar":
		print("""
============================================
              _,-"''"-..__
         |`,-'_. `  ` ``  `--'"'".
           ,'  | ``  ` `  ` ```  `.
       ,-' @ ..-' ` ` `` `  `` `  ` |==.
     ,'    ^    `  `    `` `  ` `.     |
    `_,-^-   _ .  ` \ `  ` __ `       #
       `"---"' `-`. ` \---""`.`.  `
                  \\`         `. `,
                   ||`      / / | |
                  //_`    ,_' ,_"
============================================
        """)
	
	elif type == "Spider":
		print("""
================================
        /\  .-"'"-.  /\\
       //\\/  ,,,  \//\\
       |/\| ,, |/\|
       //\\\-"'"-///\\
      //  \/   .   \/  \\
     (| ,-_| \ | / |_-, |)
       //`__\.-.-./__`\\
      // /.-( @ @ )-.\ \\
     (\ |)   '---'   (| /)
      ` (|           |) `
        \)           (/
================================
        """)
	
	elif type == "Wolf":
		print("""
=====================================
                          ,     ,
                          |\---/|
                         /  @ @ |
                    __.-'|   "  /
           __ ___.-'       '--'|
        .-'  '        :      _/
       / ,    .        .     |
      :      :        :   _/
      |  |   .'     __:   /
      |  :   /'----'| \  |
      \  |\  |      | /| |
       '.'| /       || \ |
       | /|.'       '.l \\_
       || ||             '-'
       '-''-'
=====================================
        """)

	elif type == "Elephant":
		print("""
=====================================================
              ___.-~"~-._   __....__
            .'    `    \ ~"~        ``-.
           /` _      )  `\              `\\
          /`  @)    /     |               `\\
         :`        /      |                 \\
    <`-._|`  .-.  (      /   .            `\\
     `-. `--'_.'-.\___/'   .      .       | \\
  _     /:--`     |        /     /        .'  \\
 ("\   /`/        |       '     '         /    :`
 `\'\_/`/         .\     /`~`=-.:        /     ``
   `._.'          /`\    |      `\      /(
                 /  /\   |        `Y   /  \\
                J  /  Y  |         |  /`\  \\
               /  |   |  |         |  |  |  |
              "---"  /___|        /___|  /__|
=====================================================
        """)
	elif type == "Slime":
		print("""
==================================
         , - ~ ~ ~ - ,
     , '               ' ,
   ,    !           !      ,
  ,                         ,
 ,               @@     @@   ,
 , !             @@     @@   ,
 ,        !                  ,
  ,                  []     ,
   ,              ------!  ,
     ,       !          , '
       ' - , _ _ _ ,  '
==================================
        """)

	elif type == "Bear":
		print("""
=====================================================
                                     _.--"''"--.._
                         _.""    .'       `-._
                       ."                  `-.
                      / /     .'                `.
                     /                          \\
                     :      :             :     `-.\\
                           :              `.      `
                    : :      :                \      :
                    : \      `:                \   `.
                     \ \      `                    
                      \ : .'                   |   
                       `>'     :              `.   )
                       / _.'               `.  / _(
                      ,'         `.        `.    `-.
                     ' .'   :    `. `.       / \, \ \ \\
                     :,'     :      `. `. \     \_/_/_/
                   .-=:.-"  -,-   "-.,=-.\ .
                   |(`.`     :       .')| \: `.
                    \\/      :       \//      \\
                     :      .:.       :  _/     
                                             |
                     :    _     _      /       
                      `.  \   /  .' .'       /
                        !  :   :  !_.'        /
                         `.:   :.'/\         
                           \ _ /  | :       :
                           "^"   | !       :
                         .-'      |        |
                        / / /    / /       /
                        \_\_\__.'-|       
                                  /      .'
                               .-'      (
                             / , ,  , |/
                            :\|  |  |v'
                            :::v-v-'
=====================================================
        """)
	
	elif type == "Fire Dragon":
		print("""
=====================================================
                                                /===-_---~~~~~~~~~------____
                                                |===-~___                _,-'
                 -==\\                         `//~\\   ~~~~`---.___.-~~
             ______-==|                         | |  \\           _-~`
       __--~~~  ,-/-==\\                        | |   `\        ,'
    _-~       /'    |  \\                      / /      \      /
  .'        /       |   \\                   /' /        \   /'
 /  ____  /         |    \`\.__/-~~ ~ \ _ _/'  /          \/'
/-'~    ~~~~~---__  |     ~-/~         ( )   /'        _--~`
                  \_|      /        _)     ),   __--~~
                    '~~--_/      _-~/-  / \   '-~ \\
                   \__--_/    / \\_>- )<__\      \\
                   /'   (_/  _-~  | |__>--<__|      |
                  |0  0 _/) )-~     | |__>--<__|      |
                  / /~ ,_/       / /__>---<__/      |
                 o o _//        /-~_>---<__-~      /
                 (^(~          /~_>---<__-      _-~
                ,/|           /__>--<__/     _-~
             ,//('(          |__>--<__|     /                  .----_
            ( ( '))          |__>--<__|    |                 /' _---_~\\
         `-)) )) (           |__>--<__|    |               /'  /     ~\`\\
        ,/,'//( (             \__>--<__\    \            /'  //        ||
      ,( ( ((, ))              ~-__>--<_~-_  ~--____---~' _/'/        /'
    `~/  )` ) ,/|                 ~-_~>--<_/-__       __-~ _/
  ._-~//( )/ )) `                    ~~-'_/_/ /~~~~~~~__--~
   '( ')/ ,)(                              ~~~~~~~~~~
  ' ') '( (/
    '   '  `
=====================================================
        """)
	
	elif type == "Ice Dragon":
		print("""
=====================================================
                         __
               __/\   _.-'.-'-.__
              /   .-'.       '-.'-._ __.--._
            -..'\,-,/..-  _         .'   \   '----._
            /). /_ _\' ( ' '.         '-  '/'-----._'-.__
           / '.<a a>.'     '-r   _      .-.       '-._ \\
          /  '.\. Y .).'\      ( .'  .      .\          '\'.
        _/   .-')'|'/'-. __     \)    )      '',_      _.c_.\\
       /       .<, ,>.     \    |   _/\        . ',   :   : \\
      /      |.' \_/ '.    |   /  .'   |          '.     .'  \)
     /    __/    ~~~~     /| / .-'    '-.        : \   _   ||
    |    /      ~~~~~~ __/  \/ /    _     \_      '.'\ ' /   ||
    |    |     ~~~~~~~~|  /.'   .'        \_      .|   \   \|
    |    |   ~~~~~~~~~~~~  / /   /      __.---'      '._    ||
   /    //        ...  \\ /.'  _:-.____< ,_           '.\ \  ||
               ......  // .-'     '-.__  '-'-\_      '.\/_ \|
     ................  ( ====.===-==='        '.    .  \\: \\
               /\       \\ '._        /          :   ,'   )\_ \\
             __  |       \\   '------/            \ .    /   )/
            /    |        \|        _|             )Y    |   /
           /      \         \\      \             .','   /  ,/
          |        \         \\    _/            /     _/
          |         \         \\   \           .'    .'
          |          |        '| '1          /    .'
          |          |         '. \        |:    /
         /            \           \ |       /', .'
                                   \(      ( z'
                                    \:      \ '(_
                                     \_,     '._ '-.___
                           snd                   '-' -.\\
=====================================================
        """)
	elif type == "Earth Dragon":
		print("""
=====================================================
                                      _   __,----'~~~~~~~~~`-----.__
                                   .  .    `//====-_             ___,-' `
                   -.            \_|// .   /||\\  `~~~~`---.___./
             ______-==.       _- @  \/    |||  \\           _,'`
       __,--'   ,=='||\=_    _--~/_-'|-   |`\   \\        ,'
    _-'        '    |  \\`.   ^-^~7  /-   /  ||   `\.     /
  .'                |   \\ \_    /  /-   /   ||      \   /
 / ----____         |     \\.`-_/  /|- _/   ,||       \ /
,-'        \----____ \     `==-/  `| \'--===-'       _/`
             ___       `-|      /|    )-'\~'      _,--~'
           //   \\        '-~~\_/ |    |   `\_   ,~             /\\
          //     \\            /  \     \__   \/~               `\__
        ..         ..    _,-' _/'\ ,-'~____-'`-/                 ``===\\
         \\       //    ((->/'    \|||' `.     ~`-/ ,                _||
          \\     //                \_     ~\      `^---|__i__i__\--~'_/
            _____               __-^-_    `)  \-.______________,-~'
                               //,-'~~`__--^-  |-------~~~~~'
                                  //,--~~`-\\
=====================================================
        """)
	elif type == "Air Dragon":
		print("""
=====================================================
                              )|
                              )|
                             _)|
                             )||                                  /X`
    --_-_-_-_---            _)||                                 //(
       -_-_-_              _) ||                                // (
        -_-_-             _)  ||                               // (
         -__-            _)   ||                              //  (
        _-_            __)    ||                             //   (
       _-            __)      ||                            //    /
        -            )        ||--_-_-_-_---               //    (
         --_       'X\        ||   -_-_-_                 //     (
        _-_         )\\       ||   -_-_-                 //      (
                    ) \\      ||    -__-                //       /
                     ) \\     ||   _-_                 //       (
                     )  \\    || _-                   //        (
                      \  \\   ||  -                  //         (_
                       )  \\  ||  --_               //           (_
                        )  \\ || _-_               //             (_
                        \   \\||                  //                \
                         )   >. )               _/(__________________X`
                         \  //||               (  .------------------.>  --_-_-_-_---
                         _)// ||                )/\\             __.-'      -_-_-_
                        _)//  ||               //  \\          _(           -_-_-
                        )//.. ||              //    \\       _(              -__-
                        X/'  \||             //      \\     (               _-_
                      ),,_,,,,||            //        \\   (              _-
                       )___)   )|           //.--------.\\ (               -
                         /  \'||   .--.__.//'-.________`\X'                --_
                        (   ,)||  <\--<_(//-/> \       `.                _-_
                         \ /(\||  /   ^.'/_/(\  \        `.
                         (   \|`./  ^.' /<   .-  \/\___    \
                          \ |/) | ^ /  /  \ /    /( \  `-.  \
                          ( `/  ^  ^   (  \/>   /(   \    \  \
                           >--) ^  L/     \(   /(     )    )  )
                         .(\  / ^/)/ \   ( / \ ((     /    /  /
                      .'  )\/ ^/(/  (    \)  `-\\   /\   /  /
                     /    > ^   /,   |  //      `\   /  ( .'              --_-_-_-_---
                    /    (=  =)).'  /  //,        ) (    \`.                 -_-_-_
                   /  ,  <, ,_>/    > '/',       /   >    \ )                -_-_-
                   ) '  _/ /\>'    / ~ )'    ___/ _>'     (/                  -__-
                  /  .-(^-^)/-.  / / /     (---. `--.                       _-_
                 /  (  (-^-(/   ) \' /       `   \ \--)                    _-
                /  /    )   )   ._/ /             `-)'                      -
                ) /    (   (   (-^. \-._           '                        --_
               /  >             `  \)`--)                                 _-_
              (   `--.             '   '
              / />----)
             / /\)   '
            (-'  `
             `
=====================================================
        """)
# 	elif type == "Earth Dragon":
# 		print("""
# =====================================================

# =====================================================
#         """)

# Displays the abilities
def getability(pclass, mana, inte, level):
	print("Choose an ability")
	if pclass == "Champion":# Champion Section
		cost = inte * level
		print("[1] Cleaving Strike ["+str(cost)+" mana]")
		print("[2] Melting Thrust ["+str(cost)+" mana]")
		print("[3] Critical Bash ["+str(cost)+" mana]")
		cost = inte * level + 1
		print("[4] Purify ["+str(cost)+" mana]")
		cost = inte * (level)
		choice = input()
		if choice == "1":
			ability = "cleaving strike"
			if (mana >= cost):
				mana = mana - cost
				return  ability, mana 
			
			else:
				ability = "none"
				return  ability, mana 
			
		
		elif choice == "2":
			ability = "melting thrust"
			if (mana >= cost):
				mana = mana - cost
				return  ability, mana 
			
			else :
				ability = "none"
				return  ability, mana 
			
		
		elif (choice == "3") :
			ability = "critical bash"
			if (mana >= cost) :
				mana = mana - cost
				return  ability, mana 
			
			else :
				ability = "none"
				return  ability, mana 
			
		
		elif (choice == "4"):
			ability = "purify"
			if (mana >= cost): 
				cost = inte * (level + 1)
				mana = mana - cost
				return  ability, mana 
			
			else:
				ability = "none"
				return  ability, mana 
			
		
		else:
			ability = "none"
			return  ability, mana 
		
	
	elif (pclass == "Wizard"): #Wizard Section
		cost = inte * (level)
		print("[1] Fireball ["+str(cost)+" mana]")
		print("[2] Acid Splash ["+str(cost)+" mana]")
		cost = inte * (level + 2)
		print("[3] Summon Storm ["+str(cost)+" mana]")
		print("[4] Spell of Healing ["+str(cost)+" mana]")
		cost = inte * (level)
		choice = input()
		if (choice == "1"):
			ability = "fireball"
			if (mana >= cost):
				mana = mana - cost
				return  ability, mana 
			
			else :
				ability = "none"
				return  ability, mana 
			
		
		elif (choice == "2"):
			ability = "acid spalsh"
			if (mana >= cost): 
				mana = mana - cost
				return  ability, mana 
			
			else: 
				ability = "none"
				return  ability, mana 
			
		
		elif (choice == "3"):
			ability = "summon storm"
			if (mana >= cost + 2):
				mana = mana - cost
				return  ability, mana 
			
			else:
				ability = "none"
				return  ability, mana 
			
		
		elif (choice == "4"):
			ability = "spell of healing"
			if (mana >= cost): 
				cost = inte * (level + 2)
				mana = mana - cost
				return  ability, mana 
			
			else:
				ability = "none"
				return  ability, mana 
			
		
		else:
			ability = "none"
			return  ability, mana 
		
	
	elif (pclass == "Assassin"):  # Assassin Section
		cost = inte * (level)
		print("[1] Back Stab ["+str(cost)+" mana]")
		print("[2] Headcrack ["+str(cost)+" mana]")
		print("[3] Poison ["+str(cost)+" mana]")
		cost = inte * 10
		print("[4] Assassinate ["+str(cost)+" mana]")
		cost = inte * (level)
		choice = input()
		if (choice == "1"):
			ability = "back stab"
			if (mana >= cost):
				mana = mana - cost
				return  ability, mana 
			
			else:
				ability = "none"
				return  ability, mana 
			
		
		elif (choice == "2"): 
			ability = "headcrack"
			if (mana >= cost): 
				mana = mana - cost
				return  ability, mana 
			
			else: 
				ability = "none"
				return  ability, mana 
			
		
		elif (choice == "3"):
			ability = "poison"
			if mana >= cost: 
				mana = mana - cost
				return  ability, mana 
			
			else:
				ability = "none"
				return  ability, mana 
			
		
		elif choice == "4": 
			ability = "assassinate"
			if mana >= cost: 
				cost = inte * 10
				mana = mana - cost
				return  ability, mana 
			
			else:
				ability = "none"
				return  ability, mana 
			
		
		else: 
			ability = "none"
			return  ability, mana 
		
	
	elif pclass == "Cleric":  # Cleric Section
		cost = inte * (level)
		print("[1] Smite ["+str(cost)+" mana]")
		print("[2] Enflame ["+str(cost)+" mana]")
		print("[3] Atonement ["+str(cost)+" mana]")
		print("[4] Flash Heal ["+str(cost)+" mana]")
		choice = input()
		if choice == "1": 
			ability = "smite"
			if mana >= cost: 
				mana = mana - cost
				return  ability, mana 
			
			else:
				ability = "none"
				return  ability, mana 
			
		
		elif choice == "2": 
			ability = "enflame"
			if mana >= cost: 
				mana = mana - cost
				return  ability, mana 
			
			else:
				ability = "none"
				return  ability, mana 
			
		
		elif choice == "3": 
			ability = "atonement"
			if mana >= cost: 
				mana = mana - cost
				return  ability, mana 
			
			else:
				ability = "none"
				return  ability, mana 
			
		
		elif choice == "4": 
			ability = "flash heal"
			if mana >= cost: 
				mana = mana - cost
				return  ability, mana 
			
			else:
				ability = "none"
				return  ability, mana 
			
		
		else:
			ability = "none"
			return  ability, mana 
		
	
	elif pclass == "Ranger": # Ranger Section
		cost = inte * (level)
		print("[1] Fire Arrow ["+str(cost)+" mana]")
		print("[2] Poision Arrow ["+str(cost)+" mana]")
		print("[3] Animal Attack ["+str(cost)+" mana]")
		print("[4] Healing Herbs ["+str(cost)+" mana]")
		input()
		if input == "1": 
			ability = "fire arrow"
			if mana >= cost: 
				mana = mana - cost
				return  ability, mana 
			
			else: 
				ability = "none"
				return  ability, mana 
			
		
		elif input == "2": 
			ability = "poision arrow"
			if mana >= cost: 
				mana = mana - cost
				return  ability, mana 
			
			else: 
				ability = "none"
				return  ability, mana 
			
		
		elif input == "3": 
			ability = "animal attack"
			if mana >= cost: 
				mana = mana - cost
				return  ability, mana 
			
			else: 
				ability = "none"
				return  ability, mana 
			
		
		elif input == "4": 
			ability = "healing herbs"
			if mana >= cost: 
				mana = mana - cost
				return  ability, mana 
			
			else:
				ability = "none"
				return  ability, mana 
			
		
		else: 
			ability = "none"
			return  ability, mana 
		
	
	elif pclass == "Alchemist":  # Alchemist Section
		cost = inte * (level)
		print("[1] Home-made Bomb ["+str(cost)+" mana]")
		print("[2] Poison Pot ["+str(cost)+" mana]")
		cost = inte * (level + 2)
		print("[3] Lightning-in-a-bottle ["+str(cost)+" mana]")
		print("[4] Healing Potion ["+str(cost)+" mana]")
		cost = inte * (level)
		choice = input()
		if choice == "1": 
			ability = "home-made bomb"
			if mana >= cost: 
				mana = mana - cost
				return  ability, mana 
			
			else:
				ability = "none"
				return  ability, mana 
			
		
		elif choice == "2": 
			ability = "poison pot"
			if mana >= cost: 
				mana = mana - cost
				return  ability, mana 
			
			else:
				ability = "none"
				return  ability, mana 
			
		
		elif choice == "3": 
			ability = "lightning-in-a-bottle"
			if mana >= cost + 2: 
				mana = mana - cost
				return  ability, mana 
			
			else:
				ability = "none"
				return  ability, mana 
			
		
		elif choice == "4": 
			ability = "healing potion"
			if mana >= cost: 
				cost = inte * (level + 2)
				mana = mana - cost
				return  ability, mana 
			
			else:
				ability = "none"
				return  ability, mana 
			
		
		else:
			ability = "none"
			return  ability, mana 
		
	
	else:
		ability = "none"
		return  ability, mana 

def game():
	clear()
	Start()
	print("Hello there, what is your name?")#Player's name
	global name
	name = input()
	print("Ahh, Welcome "+name+", I've been expecting you.")
     #players class
	clear()
	print("\n")
	print("Choose your Class")
	print("=================")
	print("[1] Champion")
	print("[2] Wizard")
	print("[3] Assassin")
	print("[4] Cleric")
	print("[5] Ranger")
	print("[6] Alchemist\n")
	choice = input()

	global pclass
	global piclass
	if (choice == "1"):
		pclass = "Champion"
		piclass = 1
	
	elif (choice == "2"):
		pclass = "Wizard"
		piclass = 2
	
	elif (choice == "3"):
		pclass = "Assassin"
		piclass = 3
	
	elif (choice == "4"):
		pclass = "Cleric"
		piclass = 4
	
	elif (choice == "5"):
		pclass = "Ranger"
		piclass = 5
	
	elif (choice == "6"): 
		pclass = "Alchemist"
		piclass = 6
	
	menu()

def menu():
	clear()
	
	character(piclass)
	print("""
            __       __
  /\/\     /__\   /\ \ \  /\ /\\
 /    \   /_\    /  \/ / / / \ \\
/ /\/\ \ /__    / /\  /  \ \_/ /
\/    \/ \__/   \_\ \/    \___/

""")

	print("\n"+pclass+" "+name)
	print("lives remaining: "+str(live)+"\n")
	print("[1] Encounter")
	print("[2] Inventory")
	print("[3] Rest (Returns you to full health/mana)")
	print("[4] Assign Skillpoints ["+str(skill)+" available]")
	print("[5] Shop")
	print("[99] Exit")
	choice = input()
	if (choice == "1"): 
		sarena()
	
	elif (choice == "99"): 
		leave()
	
	elif (choice == "2"): 
		inventory()
	
	elif (choice == "3"): 
		global mana, mmana, hp, mhp, stre, inte, dext, bhp, bphp
		mhp = stre * 20
		mmana = inte * 10
		hp = mhp
		hp = hp * (bphp + 1)
		hp = hp + bhp
		mana = mmana
		menu()
	
	elif (choice == "4"):
		askill()
	
	elif (choice == "5"): 
		shop()
	menu()

	# Setting Up Enemys
def sarena():
	global etype, elevel, mehp, mana, mmana, name, level, hp, mhp, stre, inte, dext, ehp, ice, fire, earth, spirt
	mmana = inte * 10
	shp = stre * 20
	mhp = stre * 20
	random = rn.randint(1, 11)
	if random == 1:
		etype = "Lion"
		random2 = rn.random() % 2 + 1
		eability = "gnaw"
		if (random2 == 1): 
			ehp = shp + rn.random() % (level * 5)
		
		else: 
			ehp = shp - rn.random() % (level * 5)
		
		mehp = ehp
		

	elif random == 2:		
		etype = "Boar"
		random2 = rn.random() % 2 + 1
		eability = "goar"
		if (random2 == 1): 
			ehp = shp + rn.random() % (level * 3)
		
		else: 
			ehp = shp - rn.random() % (level * 3)
		
		mehp = ehp
		

	elif random ==3:
		etype = "Spider"
		random2 = rn.random() % 2 + 1
		eability = "webspin"
		elevel = rn.random() % (level + 3) + 1
		if (random2 == 1): 
			ehp = shp + rn.random() % (level * 2)
		
		else: 
			ehp = shp - rn.random() % (level * 2)
		
		mehp = ehp
		

	elif random ==4:
		etype = "Wolf"
		random2 = rn.random() % 2 + 1
		eability = "growl"
		elevel = rn.random() % (level + 3) + 1
		if (random2 == 1): 
			ehp = shp + rn.random() % (level * 4)
		
		else: 
			ehp = shp - rn.random() % (level * 4)
		
		mehp = ehp
		

	elif random ==5:
		etype = "Elephant"
		random2 = rn.random() % 2 + 1
		eability = "stomp"
		if (random2 == 1): 
			ehp = shp + rn.random() % (level * 6)
		
		else: 
			ehp = shp - rn.random() % (level * 3)
		
		mehp = ehp
		

	elif rn.random ==6:
		etype = "Bear"
		random2 = rn.random() % 2 + 1
		eability = "Claw"
		if (random2 == 1): 
			ehp = shp + rn.random() % (level * 7)
		
		else: 
			ehp = shp - rn.random() % (level * 2)
		
		mehp = ehp
		
	elif random ==7:
		if ((level < 1) or (fire == True)):
		
			etype = "Wolf"
			random2 = rn.random() % 2 + 1
			eability = "growl"
			elevel = rn.random() % (level + 3) + 1
			if (random2 == 1): 
				ehp = shp + rn.random() % (level * 4)
			
			else: 
				ehp = shp - rn.random() % (level * 4)
			
			mehp = ehp
			
		elif ((level >= 1) and (fire == False)):
		
			etype = "Fire Dragon"
			random2 = rn.random() % 2 + 1
			eability = "Fire Breath"
			if (random2 == 1): 
				ehp = shp + rn.random() % (level * 9)
			
			else:
				ehp = shp - rn.random() % (level * 9)
			
			mehp = ehp
			
		
	elif random ==8:
		if ((level < 2) or (ice == True)):
		
			etype = "Bear"
			random2 = rn.random() % 2 + 1
			eability = "Claw"
			elevel = rn.random() % (level + 3) + 1
			if (random2 == 1):
				ehp = shp + rn.random() % (level * 7)
			
			else:
				ehp = shp - rn.random() % (level * 2)
			
			mehp = ehp
			
		
		elif ((level >= 2) and (ice == False)):
		
			etype = "Ice Dragon"
			random2 = rn.random() % 2 + 1
			eability = "Ice Breath"
			if (random2 == 1):
				ehp = shp + rn.random() % (level *11)
			
			else:
				ehp = shp - rn.random() % (level * 11)
			
			mehp = ehp
			
		
	elif random ==9:
		if ((level < 3) or (earth == True)):
		
			etype = "Elephant"
			random2 = rn.random() % 2 + 1
			eability = "Stomp"
			elevel = rn.random() % (level + 3) + 1
			if (random2 == 1):
				ehp = shp + rn.random() % (level * 6)
			
			else:
				ehp = shp - rn.random() % (level * 3)
			
			mehp = ehp
			
		
		elif ((level >= 3) and (earth == False)):
		
			etype = "Earth Dragon"
			random2 = rn.random() % 2 + 1
			eability = "Earth Slam"
			if (random2 == 1): 
				ehp = shp + rn.random() % (level * 13)
			
			else: 
				ehp = shp - rn.random() % (level * 13)
			
			mehp = ehp
		
	elif random == 10:
		if ((level < 4) or (air == True)):
		
			etype = "Spider"
			random2 = rn.random() % 2 + 1
			eability = "webspin"
			elevel = rn.random() % (level + 3) + 1
			if (random2 == 1):
				ehp = shp + rn.random() % (level * 2)
			
			else: 
				ehp = shp - rn.random() % (level * 2)
			
			mehp = ehp
			
		
		elif ((level >= 4) and (air == False)):
		
			etype = "Air Dragon"
			random2 = rn.random() % 2 + 1
			eability = "Air Blast"
			if (random2 == 1): 
				ehp = shp + rn.random() % (level * 15)
			
			else: 
				ehp = shp - rn.random() % (level * 15)
			
			mehp = ehp
			
		
	elif random == 11:
		if ((level < 5) or (spirt == True)):
		
			etype = "Lion"
			random2 = rn.random() % 2 + 1
			eability = "gnaw"
			if (random2 == 1):
				ehp = shp + rn.random() % (level * 5)
			
			else: 
				ehp = shp - rn.random() % (level * 5)
			
			mehp = ehp
			
		
		elif ((level >= 5) and (spirt == False)):
		
			etype = "Spirt Dragon"
			random2 = rn.random() % 2 + 1
			eability = "Soul Absorb"
			if (random2 == 1):
				ehp = shp + rn.random() % (level * 15)
			
			else: 
				ehp = shp - rn.random() % (level * 15)
			
			mehp = ehp
			
	elevel = rn.random() % (level + 3) + 1
	if ((elevel < (level - 3)) or (elevel >(level + 3))):
		elevel = level
	if ehp<0:
		ehp = mehp
	aarena()

	# Arena Main
def aarena():

	global etype, elevel, mehp, mana, mmana, name, level, hp, mhp, stre, inte, dext, ehp, fire, ice, earth, air, spirt
	clear()
	draw(etype)
	print("["+etype+" lvl: "+str(int(elevel))+"] >>> "+str(int(ehp))+"/"+str(int(mehp)))
	print("["+name+" "+str(level)+"] >>> "+str(int(hp))+"/"+str(int(mhp)))
	print("-Mana- >>> "+str(int(mana))+"/"+str(int(mmana)))
	print("[1] Attack")
	print("[2] Do ability")
	print("[3] Inventory")
	print("[99] Flee")
	choice = input()

	if (choice == "1"):
		dmg = (stre + inte) + rn.random() % dext * 2
		ehp = ehp - dmg
		deathCheck()		
		random2 = rn.random() % 2 + 1
		edmg = dmg
		# Setting up enemy damage
		if (random2 == 1):
			edmg = edmg + rn.random() % (dext * 2)
		
		else:
			edmg = edmg - rn.random() % (dext * 2)
		
		hp = hp - edmg
		# If player hp < 0 then
		if (hp <= 0):
			clear()
			live = live - 1
			if (live == 0): 
				print("""
       ___           __    ___  __    __
/\_/\ /___\/\ /\    / /   /___\/ _\  /__\\
\_ _//   // / \ \  / /    //  //\ \  /_\\
 / \/ \_//\ \_/ / / /___/ \_// _\ \/__
 \_/\___/  \___/  \____/\___/  \__/\__/
""")

				leave()
			
			print("[*] You Died")
			print("Type [1] to continue")
			input()

			menu()
		
		aarena()
	
	elif (choice == "99"):
		menu()
	
	elif (choice == "2"):
		darena()
	
	elif (choice == "3"):
		iarena()
	
	else:
		aarena()
	

	# Using items from Inventory
def deathCheck():
	global fire, ice, earth, etype, air, spirt, ehp
	# If enemy ehp < 0 then
	if (ehp <= 0):
		clear()
		print("[*] You killed the "+etype)
		print("Type [1] to continue")
		if (etype == "Fire Dragon"):
		
			fire = True
		
		if (etype == "Ice Dragon"):
		
			ice = True
		
		if (etype == "Earth Dragon"):
		
			earth = True
		
		if (etype == "Air Dragon"):
		
			air = True
		
		if (etype == "Spirt Dragon"):
		
			spirt = True
		
		input()
		if (fire == True and ice == True and earth == True and air == True and spirt == True):
		
			clear()
			print("""

       ___         __    __ _____    __
/\_/\ /___\/\ /\  / / /\ \ \\_   \/\ \ \\
\_ _///  // / \ \ \ \/  \/ / / /\/  \/ /
 / \/ \_//\ \_/ /  \  /\  /\/ /_/ /\  /
 \_/\___/  \___/    \/  \/\____/\_\ \/

            Made by: Max


""")
		rarena()
def iarena():
	clear()
	global rxp, rgold, xp, gold, level, xpb, xpl, skill, dext, inte, stre, level, mana, hp, etype, hpotion, mpotion, mmana, mhp
	print("Inventory")
	print("[1] Health Potion, "+str(hpotion)+" (Heals you to max health)")
	print("[2] Mana Potion, "+str(mpotion)+" (Restores you Mana to maximum)")
	print("[99] Exit")
	choice = input()
	if (choice == "1"):
		if (hpotion > 0):
			hpotion = hpotion - 1
			hp = mhp
		
	
	if (choice == "2"):
		if (mpotion > 0): 
			mpotion = mpotion - 1
			mana = mmana
		
	
	elif (choice == "99"): 
		aarena()
	
	iarena()

	# Picking spells and doing damage
def darena():
	global rxp, rgold, xp, gold, level, xpb, xpl, skill, dext, inte, stre, level, mana, hp, etype, ehp
	clear()
	action, mana = getability(pclass, mana, inte, level)
	# Champion spells
	edmg1 = 1
	if (action == "cleaving strike"): 
		dmg = (stre + inte + dext) + rn.random() % (dext * 2)
	
	elif (action == "melting thrust"): 
		dmg = (stre + inte + dext) + rn.random() % (stre * 2)
	
	elif (action == "critical bash"): 
		dmg = (stre + inte + dext) + rn.random() % (inte * 2)
	
	elif (action == "purify"): 
		hp = hp + inte * (level)+(rn.random() % inte)
		dmg = 0
		edmg1 = 0
		if (hp > mhp): 
			hp = mhp

	#Necromancer spells
	elif (action == "shadow strike"): 
		dmg = (stre + inte + dext) + rn.random() % (dext * 2)
	
	elif (action == "cripple"): 
		dmg = (stre + inte + dext) + rn.random() % (stre * 2)
	
	elif (action == "mutilate"): 
		dmg = (stre + inte + dext) + rn.random() % (inte * 2)
	
	elif (action == "life tap"): 
		dmg = (stre + inte) + rn.random() % (inte)
		hp = hp + dmg
		if (hp > mhp): 
			hp = mhp
		ehp = ehp - dmg

	#Assassin spells
	elif (action == "back stab"): 
		dmg = (stre + inte + dext) + rn.random() % (dext * 2)
	
	elif (action == "headcrack"): 
		dmg = (stre + inte + dext) + rn.random() % (stre * 2)
	
	elif (action == "poison"): 
		dmg = (stre + inte + dext) + rn.random() % (inte * 2)
	
	elif (action == "assassinate"):
		dmg = (stre + inte + dext) + rn.random() % ((inte + stre) * 3)
		ehp = ehp - dmg

	#Claric spells
	elif (action == "smite"): 
		dmg = (stre + inte + dext) + rn.random() % (dext)
	
	elif (action == "enflame"): 
		dmg = (stre + inte + dext) + rn.random() % (stre)
	
	elif (action == "atonement"):
		dmg = (stre + inte + dext) + rn.random() % (inte)
	
	elif (action == "flash heal"):
		hp = hp + ((stre * level) + (rn.random() % (inte * 2)))
		dmg = 0
		edmg1 = 0
		if (hp > mhp):
			hp = mhp

	#Ranger spells
	elif (action == "fire arrow"): 
		dmg = (stre + inte + dext) + rn.random() % (dext)
	
	elif (action == "poision arrow"): 
		dmg = (stre + inte + dext) + rn.random() % (stre)
	
	elif (action == "animal attack"): 
		dmg = (stre + inte + dext) + rn.random() % (inte)
	
	elif (action == "healing herbs"): 
		hp = hp + ((stre * level) + (rn.random() % (inte * 2)))
		if (hp > mhp): 
			hp = mhp
		dmg = 0
		edmg1 = 0
	
	else:
		dmg = int((stre + inte) + rn.random() % (dext * 2))
	ehp -= dmg
	deathCheck()
	# Setting up enemy damage
	random2 = rn.random() % 2 + 1
	if edmg1 == 0:
		edmg = 0
	elif (random2 == 1):
		edmg = dmg + rn.random() % (dext * 2)
	
	else:
		edmg = dmg - rn.random() % (dext * 2)
	hp = int(hp - edmg)
	# If player hp < 0 then
	if (hp <= 0):
		clear()
		print("[*] You Died")
		print("Type [1] to continue")
		input()
		menu()
	
	aarena()

	# Here you get arena awards
def rarena():
	global rxp, rgold, xp, gold, level, xpb, xpl, skill
	clear()
	rxp = int(rn.random() % (level * 2) + 5)
	rgold = rn.random()*5 + (level)
	rgold = int(rgold + goldb)

	print("""
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" ,  `"=._o." ,-""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` ` .". ,  "-._"-._               |
 _________|___________| `-.o`"=._ ." ` '`."\` . "-._ /_______________|_______
|                   | |o    `"-.o`"=._``  '` " ,__.--o   |
|___________________|_|      (#) `-.o `"=.`_.--"_o.- ___|___________________
____/______/______/___|o._    "      `".o|o_.--"    o____/______/______/____
/______/______/______/_"=._o--._         |          /______/______/______/_
____/______/______/______/__"=._o--._   o|o     _._o____/______/______/____
/______/______/______/______/____"=._o._ | _.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/_
*******************************************************************************
    """) 

	rrarena()

def rrarena():#reward arena
	global rxp, rgold, xp, gold, level, xpb, xpl, skill
	print("You recieved "+str(rxp)+" xp")
	print("You recieved "+str(rgold)+" gold")

	xp += rxp
	gold += rgold
	if (xp >= xpl):
		level = level + 1
		xpl = xpl + xpb
		xpb = xpb + 50
		skill = skill + 5
		print("You have leveled up to level "+str(level))
	
	print("Type [1] to continue to the menu")
	input()
	menu()

def inventory():
	clear()

	print("""
       ___
       )_(                                         _
       | |                                       [_ ]
     .-'-'-.       _                           .-'. '-.
    /-::_..-\    _[_]_                        /:/ _.-'\\
    )_     _(   /_   _\      [-]              |:._   .-|
    |::    |   )_`` '_(   .-' -'-.   (-)      |:._     |
    |::    |   |:     |   :-.. .-: .-'-'-.    |:._     |
    |::    |   |:     |   |:     | |-...-|    |:._     |
    |::-.._|   |:..  _|   |:..  _| |:. ._|    |:._     |
    `-.._..-'   `-...-'    `-...-'  `-...-'    `-.____.-'
    )""")
	levelalert()

def levelalert():
	global xp, xpl, skill, xpb 
	if (xp >= xpl):
		level = level + 1
		xpl = xpl + xpb
		xpb = xpb + 50
		skill = skill + 5
		levelalert()
	
	else:
		inventory2()
	

def inventory2():
	global level, xp, xpl, gold, hpotion, mpotion, fire, ice, earth, air, spirt
	print("[Level] >>> "+str(level))
	print("[XP] >>> "+str(int(xp))+"/"+str(xpl))
	print("[Gold] >>> "+str(int(gold)))
	print("[Healing Potions] >>> "+str(hpotion))
	print("[Mana Potions] >>> "+str(mpotion))
	print("==================================")
	if (fire == True):
	
		print("Fire Medal- acquired\n")
		print("==================================")
	elif (fire == False):
	
		print("Fire medal- Not acquired\n")
		print("==================================")
	
	if (ice == True):
	
		print("Ice Medal- acquired\n")
		print("==================================")
	elif (ice == False):
	
		print("Ice Medal- Not acquired\n")
		print("==================================")
	
	if (earth == True):
	
		print("Earth Medal- acquired\n")
		print("==================================")
	elif (earth == False):
	
		print("Earth Medal- Not acquired\n")
		print("==================================")
	
	if (air == True):
	
		print("Air Medal- acquired\n")
		print("==================================")
	
	elif (air == False):
	
		print("Air Medal- Not acquired\n")
		print("==================================")
	
	if (spirt == True):
	
		print("Spirt Medal- acquired\n")
		print("==================================")
	
	elif (spirt == False):
	
		print("Spirt Medal- Not acquired\n")
		print("==================================")
	

	print("99- Exit")
	choice = input()
	if (choice == "99"):
		menu()
	
	inventory()


def askill():
	clear()
	global stre, skill, inte, dext
	print("""
              .__=\__                  .__==__,
            jf'      ~~=\,         _=/~'      `\,
        ._jZ'            `\q,   /=~             `\__
       j5(/                 `\./                  V\\,
     .Z))' _____              |             .____, \)/\\
    j5(K=~~     ~~~~\=_,      |      _/=~~~~'    `~~+K\\,
  .Z)\/                `~=L   |  _=/~                 t\ZL
 j5(_/.__/===========\__   ~q |j/   .__============___/\J(N,
4L#XXXL_________________XGm, \P  .mXL_________________JXXXW8L
~~~~~~~~~~~~~~~~~~~~~~~~~YKWmmWmmW@~~~~~~~~~~~~~~~~~~~~~~~~~~
    """)

	print("Available Skillpoints ["+str(skill)+"]")
	print("1- Strength ["+str(stre)+"]")
	print("2- Intelligence ["+str(inte)+"]")
	print("3- Dexterity ["+str(dext)+"]")
	print("99- Exit")
	choice = input()
	if (skill > 0):
		if (choice == "1"):
			stre = stre + 1
			skill = skill - 1
		
		elif (choice == "2"):
			inte = inte + 1
			skill = skill - 1
		
		elif (choice == "3"):
			dext = dext + 1
			skill = skill - 1
		
		elif (choice == "99"):
			menu()
		
	
	else:
		menu()
	
	askill()

def shop():
	clear()
	global hpotion, mpotion, gold
	print("""
                               ____
                  _           |---||            _
                  ||__________|---||___________||
                 /_ _ _ _ _ _ |:._|'_ _ _ _ _ _ _\`.
                /_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\:`.
               /_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\::`.
              /:.___________________________________\:::`-._
          _.-'_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _`::::::`-.._
      _.-' _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ `:::::::::`-._
    ,'_:._________________________________________________`:_.::::-'`
     `.'/ || |:::::`.'/::::::::`.'/::::::::`.'/::::::|.`.'/.|     :|
      ||  || |::::::||::::::::::||::::::::::||:::::::|..||..|     ||
      ||  || |  __  || ::  ___  || ::  __   || ::    |..||||     ||
      ||  || | |::| || :: |:::| || :: |::|  || ::    |.|||:||_____||__
      ||  || | |::| || :: |:::| || :: |::|  || ::    |.|||:||_|_|_||,(
      ||_.|| | |::| || :: |:::| || :: |::|  || ::    |.'||..|    _||,|
   .-'::_.:'.:-.--.-::--.-:.--:-::--.--.--.-::--.--.-:.-::,'.--.'_|| |
    )||_|__||_|__|_||__|_||::|_||__|__|__|_||__|__|_|-'|__|_(,' || '-
    ||||  || |. . . ||. . . . . ||. . . . . ||. . . .|::||''||   ||:'
    ||||.  _|._._._||._._._._._||._._._._._||._._._.|:'||,, ||,,
    '''''           ''-         ''-         ''-         '''  '''
    """)

	price = level * 5
	print("[Gold] >>> "+str(gold))
	print("1- Health Potion ("+str(price)+" gold)")
	print("2- Mana Potion ("+str(price)+" gold)\n")
	print("99- Exit")
	choice = input()
	if (choice == "1"):
		price = level * 5
		if (gold >= price):
			hpotion += 1
			gold -= price
			shop()
		
		else:
			menu()
		
	
	if (choice == "2"):
		price = level * 5
		if (gold >= price):
			mpotion += 1
			gold -= price
			shop()
		
		else:
			menu()

		
	
	elif (choice == "99"):
		menu()
	
	shop()

def leave():
	global name
	print("Goodbye, " + name + "\n")


bhp = 0 # Bonus hp
bphp = 0 # Bonus precantage hp
goldb = 0 # Bonus Gold
# Player Variables
piclass = 0
level = 1 # Level
xp = 0 # Current XP
xpb = 50 # Increases each level, adds to max hp to increase it
xpl = 25 # XP Required till next level
stre = 10 # Strength
inte = 10 # Intelligence
dext = 10 # Dexterity
skill = 0 # Skillpoint points (used to increase Strength, Intelligence, Dexterity)
live = 5
hp = stre * 20 # Current hp
mhp = stre * 20 # Max hp
shp = stre * 20 # hp used to set enemy hp
mana = 100 # Mana
mmana = inte * 10 # Max Mana
						   # Inventory / Shop
mpotion = 0 # Mana Potions
hpotion = 1 # Healing Potions
			   # Resources
gold = 25 # Gold
   # Saving / Loading Strings
x = 0
y = 0

fire = False
ice = False
earth = False
air = False
spirt = False

game()
