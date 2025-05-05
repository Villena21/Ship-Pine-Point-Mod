label start:
    stop music

#Act A
    play music ("shadow - warmth.mp3") fadein 0.5
    scene bg black

    show a01 at top
    $ renpy.pause ()   # will wait untill player click
    show a02 at top
    $ renpy.pause ()   # will wait untill player click
    hide a01
    show a03 at top
    hide a02
    text "You're no stranger to the feeling of being watched."
    hide a03
    show a04 at top
    text "The people of Pine Point stare at you all the time, whispering things and talking behind your back."
    hide a04
    show a05 at top
    text "\"There goes that kid who sleeps in the woods again.\""
    text "\"What a freak.\""
    text "They always look so offended, like you're about to drown their dog or smash their car windows with a baseball bat or something."
    hide a05
    show a06 at top
    text "To be fair, you DID do the latter to Roark Romano's brand new Civic last summer, but it was in the name of justice."
    hide a06
    show a07 at top
    text "Yeah."
    hide a07
    show a08 at top
    text "{i}Justice."
    hide a08
    show a12 at top
    text "Despite being used to the judgemental eye of the town, you admit the past few days have felt..."
    hide a12
    show a14 at top
    text "{color=#f00}...different."
    hide a14
    show a13 at top
    text "It's the kind of {i}different{/i} that makes the hair on the back of your neck stand up, the kind that makes you think someone is standing behind you..."
    hide a13
    show a15:
        pos (0.5, 0.025) anchor (0.5, 0)
    text "...but when you turn around there's nothing except the summer breeze..."
    hide a15
    show a16:
        pos (0.5, 0.025) anchor (0.5, 0)
    text "That's why you haven't gotten a single hour of sleep in the past few days, despite curbing your insomnia ages ago."
    hide a16
    show a17:
        pos (0.5, 0.025) anchor (0.5, 0)
    text "It's this goddamn town."
    text "It's driving you crazy."
    hide a17
    show a18:
        pos (0.5, 0.025) anchor (0.5, 0)
    with pixellate
    pause 1.5
    hide a18
    with fade
#Act B
    stop music
    play music ("nurture nurture - dinner with luis.mp3") fadein 0.5
    show bkitchen:
        pos (0.5, 0.025) anchor (0.5, 0)
    with moveinright

    show niljob yawn:
        pos (0.2, 1.0) anchor (0.5, 1.0)
    with longer_easein
    n "{i}Yawn..."

    show dimitrijob talk at right
    with moveinright
    d "Whooooah, did you carry your groceries with those eye bags?"
    show dimitrijob talkclose at right

    show niljob talk:
        pos (0.2, 1.0) anchor (0.5, 1.0)
    n "I'm going to kill you."
    show niljob talkclose:
        pos (0.2, 1.0) anchor (0.5, 1.0)

    show dimitrijob talk at right
    d "Not if I kill you first."
    d "I know where they keep the industrial strength bleach."
    show dimitrijob talkclose at right

    show niljob smug:
        pos (0.2, 1.0) anchor (0.5, 1.0)
    n "I'll lock you in the meat freezer."
    show niljob smugclose:
        pos (0.2, 1.0) anchor (0.5, 1.0)

    show dimitrijob talk at right
    d "Joke's on you, the freezer lock's broken."
    d "I jammed it on my first day and they never fixed it."
    show dimitrijob talkclose at right

    show niljob talk:
        pos (0.2, 1.0) anchor (0.5, 1.0)
    n "Dammit."
    show niljob talkclose:
        pos (0.2, 1.0) anchor (0.5, 1.0)

    show dimitrijob talk at right
    d "10AM's too early for murder anyway."
    show dimitrijob talkclose at right 

    show romeo
    with moveinright
    r "But not too early for prep work!"
    r "Dimitri, work bitch, teach Nil the sauce station today, will ya?"
    hide romeo
    with moveoutright

    show dimitrijob talk at right
    d "Sure thing, boss."
    d "Okay, Marco (POLO) also says you make the thin crust pizzas too thick and the thick crust ones too thin, so I gotta run you through everything again on top of teaching you the sauce station."
    show dimitrijob talk at right:
        xzoom -1.0
    d "Oh, and they're adding some gimmicky summertime promo so we gotta learn how to make that monstrosity too."

    show niljob yawn:
        pos (0.2, 1.0) anchor (0.5, 1.0)
    n "{i}Yawn..."
    show niljob talkclose
    show dimitrijob talkclose at dim_tint:
        xzoom -1.0
        xpos 1.0
    show bkitchen at dim_tint:
        pos (0.5, 0.025) anchor (0.5, 0)
    text "It'd be a miracle if you survived today's shift."
    text "Normally, you wouldn't give a rat's ass about a minimum wage job and would much rather play hooky, but this time you get to work with Dimitri."
    text "You don't want to disappoint your best friend."
    text "He did help land you this job, after all."
    text " Also you're gay as fuck"
    hide bkitchen
    hide dimitrijob
    hide niljob
    show bkitchen:
        pos (0.5, 0.025) anchor (0.5, 0)        
    show niljob talkclose:
        pos (0.2, 1.0) anchor (0.5, 1.0)
    show dimitrijob talk at right:
        xzoom 1.0
    d "Snoozin' on your second day?"
    d "{i}Tsk, tsk."
    d "Did you stay up watching the rerun of {i}Snailman and Slime Frog{/i} too?"
    show dimitrijob talkclose at right
    
    show niljob talk:
        pos (0.2, 1.0) anchor (0.5, 1.0)

    menu:
        "Dude, what are you, six?":
            jump one
        "I haven't seen {i}Snailman and Slime Frog{/i} since I was a kid.":
            jump two
        "Shit like that is never good as you remember.":
            jump three
        "No I was stalking you":
            jump meme_shit

    label meme_shit:
        hide dimitrijob talkclose
        show dimitrijob sincere
    d   "Dude WTF"
        hide niljob talk
        show NilJob Sincere
    n   "Yeah man I like you"
    d   "Dude"
        hide dimitrijob sincere
        show DimitriJob Laugh
    d   "I like you too"
        hide NilJob Sincere
        show NilJob Paranoid
    n   "ª"

    label one:
        show niljob talkclose:
            pos (0.2, 1.0) anchor (0.5, 1.0)        
        show dimitrijob talk at right
        d "Haha, maybe."
        n "I showed it to my siblings and I swear to God I never saw them blink, their eyes were so glued to the screen."
        d "Reminds me of when we watched Snailman for the first time."
        show dimitrijob talkclose
        jump four

    label two:
        show niljob talkclose:
            pos (0.2, 1.0) anchor (0.5, 1.0)
        show dimitrijob talk at right
        d "Me neither. I heard some kid in Toronto got so upset about Snailman's voice actor getting replaced that they set their TV on fire."
        d "Burned their house down and almost killed their entire family."
        show dimitrijob talkclose
        show niljob talk
        n "Damn, some people can't accept change."
        show niljob smug
        n "I'd get it if they did it for the shitty writing though."
        show niljob smugclose
        jump next

    label three:
        show niljob talkclose:
            pos (0.2, 1.0) anchor (0.5, 1.0)
        show dimitrijob talk at right
        d "You know what they say. Nostalgia's a hell of a drug, and I'm jonesing."
        d "They played the episode where Snailman was dying cuz he couldn't make enough slime, so Slime Frog had to give him a slime transplant."
        show dimitrijob talkclose at right
        jump four

    label four:
        show niljob talk:
            pos (0.2, 1.0) anchor (0.5, 1.0)
        n "How could I forget the greatest television line ever written..."
        show niljob smug:
            pos (0.2, 1.0) anchor (0.5, 1.0)
        n "\"It's slime time.\""
        show niljob smugclose:
            pos (0.2, 1.0) anchor (0.5, 1.0)

        show dimitrijob talk at right
        d "\"He's not just a Slime Frog, he's also-\""
        show dimitrijob talkclose at right
        
        show niljob smug:
            pos (0.2, 1.0) anchor (0.5, 1.0)
        n "...\"my Slime Friend.\""
        show niljob smugclose:
            pos (0.2, 1.0) anchor (0.5, 1.0)
        jump next

    label next:
        show dimitrijob talk at right
        d "Shitty writing or not, that shit had us kids in a fuckin' chokehold."
        show dimitrijob talk at right
        d "Remember when we dressed up as them for Halloween? My mom still has the photos."
        show dimitrijob talkclose at right

        show niljob talk:
            pos (0.2, 1.0) anchor (0.5, 1.0)
        n "I wish I could forget."
        show niljob talkclose:
            pos (0.2, 1.0) anchor (0.5, 1.0)

        show dimitrijob talk at right
        d "Your head was so big we had to cut the costume so you could fit through the hole."
        show dimitrijob talkclose at right
        d "Hm..."
        pause 0.5
        show dimitrijob talk at right
        d "Seems like things haven't really changed."
        show dimitrijob talkclose at right

        show niljob smug:
            pos (0.2, 1.0) anchor (0.5, 1.0)
        n "Hey, you know what they say about big heads."
        
        show romeo
        with moveinleft
        show niljob talkclose
        r "I'd love to pay you two to reminisce, but I pay you to make pizzas, okay?"

        show dimitrijob talk at right
        d "What were you like as a kid, Marco?"
        show dimitrijob talkclose at right

        r "Oh, got into all sorts of trouble. Stay in school, kids, or else you'll end up like me."

        show dimitrijob talk at right
        d "What, bald and divorced?"
        show dimitrijob talkclose

        r "{i}Hah!{/i}"
        pause 0.3
        r "Shuddup, kid."
        show dimitrijob laugh
        d "Haha!"
        
        hide dimitrijob
        hide niljob
        hide romeo
        hide bkitchen
        with dissolve

        show b01:
            pos (0.5, 0.025) anchor (0.5, 0)
        with dissolve
        text "Everyone in town loves Dimitri, and Dimitri loves them right back."
        pause 0.8
        text "It's weird."
        text "Dimitri even gets along with authority figures, which is something you could never achieve in an entire lifetime."
        text "But you guess that's why you didn't mind his company — he never cared if you slept in the woods or had anger issues or whatever."
        text "He just treats you like everyone else, instead of like some rabid stray animal."
        text "Too bad he's not going to be here forever."

        hide b01
        with fade
        
        show b02:
            pos (0.5, 0.025) anchor (0.5, 0)
        show dimitrijob talk at right
        with dissolve
        d "Not bad for your second day."
        show dimitrijob talkclose at right

        show niljob talk:
            pos (0.2, 1.0) anchor (0.5, 1.0)
        with dissolve
        n "...You're being way too nice."
        show niljob talkclose:
            pos (0.2, 1.0) anchor (0.5, 1.0)
        
        show dimitrijob talk at right
        d "No, seriously. When I first started, mine looked worse and I wasn't even stoned."
        d "Marco can probably teach you how to do the dough toss thing when you're more accustomed."
        d "He's been in the biz for like, 40 years."
        show dimitrijob talkclose at right
        
  
        show niljob concern
        n "Holy shit. 40 years?"
        hide b02
        hide niljob
        hide dimitrijob
        with dissolve

        show b03:
            pos (0.5, 0.025) anchor (0.5, 0)
        with dissolve
        text "You look around the ugly, fluorescent-lit kitchen. No windows, no A/C, over 12 hours a day, for 40 years."
        text "Doing the same thing, over and over for over half your life... then having kids, and making them do the same thing over and over in the same small town you grew up in..."
        text "You can't stomach it."
        hide b03
        with dissolve

        show bkitchen:
            pos (0.5, 0.025) anchor (0.5, 0)
        show dimitrijob talkclose at right:
            xzoom -1.0
        show niljob sincere:
            pos (0.2, 1.0) anchor (0.5, 1.0)
        with dissolve
        n "Hey, can I come with you?"
        show niljob sincereclose

        show dimitrijob talk at right:
            xzoom 1.0
        d "To the storage room?"
        show dimitrijob talkclose at right

        show niljob talk:
            pos (0.2, 1.0) anchor (0.5, 1.0)
        n "No, stupid. To uni."
        show niljob talkclose:
            pos (0.2, 1.0) anchor (0.5, 1.0)

        show dimitrijob talk at right
        d "To do what?"
        show dimitrijob talkclose at right

        show niljob talk:
            pos (0.2, 1.0) anchor (0.5, 1.0)
        n "I dunno. Hang out?"
        show niljob talkclose:
            pos (0.2, 1.0) anchor (0.5, 1.0)

        show dimitrijob talk at right
        d "Hang out?"
        d "Yeah, I don't know if it's that easy, haha."
        show dimitrijob talkclose
    
        show niljob talk:
            pos (0.2, 1.0) anchor (0.5, 1.0)
        n "Seemed easy for you."
        show niljob talkclose:
            pos (0.2, 1.0) anchor (0.5, 1.0)

        show dimitrijob sincere
        d "What's that supposed to mean?"

        show niljob talk:
            pos (0.2, 1.0) anchor (0.5, 1.0)
        n "Nevermind. Pretend I never said anything."
        show niljob talkclose:
            pos (0.2, 1.0) anchor (0.5, 1.0)

        d "Dude... I spent so many nights studying til my brain turned to static, plus I worked two jobs."
        d "You don't think I busted my ass off to get into university?"

        show niljob sincere:
            pos (0.2, 1.0) anchor (0.5, 1.0)
        n "No, you're the hardest working person I know. I didn't mean it like that. Sorry."
        show niljob sincereclose:
            pos (0.2, 1.0) anchor (0.5, 1.0)

        d "It was the hardest I've ever worked for anything in my life."
        d "It just kinda rubs me the wrong way when people assume things about me, y'know?"
        show dimitrijob sincereclose
        pause 0.8
        show dimitrijob talk at right
        d "But it's cool, I'm sure you didn't mean any harm. Wanna drop it?"
        
        show niljob sincere:
            pos (0.2, 1.0) anchor (0.5, 1.0)
        n "Yeah, let's drop it."

        show dimitrijob talkclose at right
        show niljob sincereclose:
            pos (0.2, 1.0) anchor (0.5, 1.0)
        n "..."
        d "..."

        show niljob sincere:
            pos (0.2, 1.0) anchor (0.5, 1.0)
        n "So... what should we do with the band?"
        show niljob sincereclose

        show dimitrijob talk at right
        d "I mean, you'll still have Momo and Journey, right?"
        d "I know a couple guys who can fill in as guitarist if you still wanna continue band stuff."
        d "Either that, or you're gonna have to finally pick up a guitar."
        d "It shouldn't be too hard to replace me, though."
        hide dimitrijob
        hide niljob
        
        show b04:
            pos (0.5, 0.025) anchor (0.5, 0)            
        text "The fluorescent lights are starting to get to you for some reason."

        show dimitrijob talkclose at right
        show niljob sincereclose:
            pos (0.2, 1.0) anchor (0.5, 1.0)

        show dimitrijob talkclose at right
        show niljob sincere:
            pos (0.2, 1.0) anchor (0.5, 1.0)
        with dissolve
        n "You should stay in Pine Point. We could go fishing at Lost Lake every day."
        show niljob sincereclose

        show dimitrijob laugh at right
        d "Man, I wish! That would be the fuckin' dream."
        show dimitrijob talk at right
        d "That's definitely one of the things I'll miss about Pine Point- the fishing here's too good."
        d "I don't even know if they have lakes where I'm going."
        show dimitrijob talkclose

        show niljob talk
        n "No lakes?"
        pause 0.5
        n "Fuck that."
        show niljob talkclose

        show dimitrijob laugh at right
        d "Y'know, sometimes I wish I was more like you. No thoughts in my brain except for fishing."

        show niljob smug:
            pos (0.2, 1.0) anchor (0.5, 1.0)
        n "You calling me dumb?"
        show niljob smugclose

        show dimitrijob talk at right
        d "Yes. But I'm also kinda jealous."
        d "You're like a wild animal, you just do whatever the fuck you want and you don't give a shit about what people think."
        d "I respect the hell out of that."
        d "I could never live the way you live."
        d "You're more like a coyote and I'm more of just a... sheepdog."
        show dimitrijob talkclose

        show niljob talk:
            pos (0.2, 1.0) anchor (0.5, 1.0)
        n "People love sheepdogs though."
        show niljob talkclose
        pause (0.5)
        show niljob sincere
        n "I've never heard anyone say their favorite animal was a coyote."
        show niljob talkclose

        show dimitrijob talk at right
        d "Eh, to each their own. I think coyotes are pretty neat."
        show dimitrijob talkclose

        show niljob smug:
            pos (0.2, 1.0) anchor (0.5, 1.0)
        n "You're fuckin' weird."
        show niljob smugclose

        show dimitrijob talk at right
        d "But yeah, trust me, I'd choose to stay in Pine Point if I could."
        show dimitrijob talkclose at right
        
        show niljob talkclose:
            pos (0.2, 1.0) anchor (0.5, 1.0)
        hide niljob
        hide dimitrijob
        hide bkitchen
        hide b04
        with pixellate
        
        show b05:
            pos (0.5, 0.025) anchor (0.5, 0)
        with pixellate
        
        stop music fadeout 0.5

        play audio ("static.mp3") volume 10 loop channel 1
        text "Now the fluorescent lights are {i}really{/i} starting to get to you."
        hide b05

        show b06:
            pos (0.5, 0.025) anchor (0.5, 0)
        with dissolve

        text "There's the sleep deprivation finally catching up. But this is not the right time. You can't afford to lose this job."
        text "You feel your heart thumping slowly and heavily, and your vision starts to blur. Your body craves sleep, and you want to pass out right there, but there's something..."

        show b07:
            pos (0.5, 0.025) anchor (0.5, 0)
        text "{sc}...there!!{/sc}" with hpunch
        hide b06
        stop sound channel 1
        show b08:
            pos (0.5, 0.025) anchor (0.5, 0)
        hide b07
        d "{sc}!!!"
        hide b08


        play audio "splat freesound.mp3" volume 2
        pause 5.0
        hide b08a
        stop sound channel 1

        show b09:
            pos (0.5, 0.025) anchor (0.5, 0)
        n "..."

        show b10:
            pos (0.5, 0.025) anchor (0.5, 0)
        $ renpy.pause ()   # will wait untill player click
        hide b09
        show b11:
            pos (0.5, 0.025) anchor (0.5, 0)
        hide b10
        d "...It really wasn't that bad. I woulda eaten it."
        hide b11
        with dissolve
        play music ("nurture nurture - dinner with luis.mp3") fadein 0.5
        show bkitchen:
            pos (0.5, 0.025) anchor (0.5, 0)
        show dimitrijob sincere2 at right
        with dissolve
        d "You've been looking really tired lately, you okay?"
        show dimitrijob sincereclose2

        show niljob sincere:
            pos (0.2, 1.0) anchor (0.5, 1.0)
        n "Sorry. I'm fine."
        show niljob sincereclose

        show dimitrijob talk2
        d "No you're not. You look like Mrs. Samanski after her divorce."
        d "I know you're a coffee hater, but Marco always keeps a pot warm for employees if you want some."
        show dimitrijob talkclose2
    
        menu:
            "...You know what, fine. I'll bite.":
                jump ending_c
            "Yeah, coffee's nasty. I'll take my 15.":
                jump ending_d
            "Nah.":
                jump ending_e
#Ending_C
        label ending_c:
            show niljob talkclose
            show dimitrijob talk2 at right
            d "Dope. Coffee's over there."
            d "There's usually sugar and creamers too."
            
            hide dimitrijob
            hide niljob
            hide bkitchen
            with dissolve

            show c01:
                pos (0.5, 0.025) anchor (0.5, 0)
            text "Dimitri points you over to the front where they keep the coffee pot. You walk over and the bitter smell makes your nose scrunch in disgust."
            text "You're more of a soda drinker yourself."


            text "Still, you have to survive the day somehow, and you pour yourself a cup."
            hide c01
            with dissolve

            play audio "pour sfx - freesound.mp3" volume 20
            pause 5.0
            stop audio    
 
            show c02:
                pos (0.5, 0.025) anchor (0.5, 0)
            with dissolve


            text "You find the sugar and creamers stashed behind the coffee pot, and add one of each to the steaming black liquid."
            text "You take a sip."
            text "{i}EUGH.{/i}" with vpunch
            text "How do people drink this shit?"
            text "Maybe it needs more sugar..."
            
            show c03:
                pos (0.5, 0.025) anchor (0.5, 0)
            hide c02
            
            text "Perfect."
            text "You're not proud of your childlike palate, but the coffee is finally drinkable."
            show c04:
                pos (0.5, 0.025) anchor (0.5, 0)
            hide c03                      
            text "You guzzle down your cup, not flinching even one bit. It's much better than before."
            text "Now you're wide awake and ready to take on the rest of the day."

            stop music
            pause 1.5
            play music ("I am worse than a drug.wav") fadein 0.5

            show c06:
                pos (0.5, 0.025) anchor (0.5, 0)
            hide c04
            text "{sc}{size=-5}Except you feel as if your third eye opened and your heart is now about to beat out{para}of your chest and you wanna throw up and oh god if you don't rip your fucking heart{para}out right now you'll explode oh fuck is there someone standing behind you are you{para}gonna die-"

            show dimitrijob talk at left:
                xzoom -1.0
            with moveinleft
            d "You good?"
            show dimitrijob talkclose at left:
                xzoom -1.0

            show niljob paranoid at right:
                xzoom -1.0
            n "{sc}Yeah, I'm fine."
            show niljob talk
            n "You don't have to check in on me every second, y'know."
            show niljob talkclose

            show dimitrijob talk at left:
                xzoom -1.0
            d "Sorry, oldest sibling habits."
            d "How's the coffee? Nasty?"
            show dimitrijob talkclose

            show niljob sick at right:
                xzoom -1.0
            n "...{i}*hurk*" with hpunch

            show dimitrijob talk
            d "Haha. Bathroom's to your left."
            show dimitrijob talkclose
            show niljob sick
            n "Thanks."
            hide niljob
            with moveoutleft

            show dimitrijob talk at left:
                xzoom 1.0
            d "You'll learn to like it someday!"
            hide dimitrijob
            hide bkitchen
            
            stop music fadeout 1.0
            show c07:
                pos (0.5, 0.025) anchor (0.5, 0)
            hide c06

            n "Ughhh..."
            play audio "static.mp3" volume 5 loop channel 1
            show c08:
                pos (0.5, 0.025) anchor (0.5, 0)
            text "If there's anything you hate the most, it's throwing up."
            
            show c10:
                pos (0.5, 0.025) anchor (0.5, 0)
            text "You've had a rough couple of days, and this isn't helping with that sense of dread you've been feeling."
            text "The bathroom tiles are cool against your skin, and maybe if you just shut your eyes for a while,  you'll return to normal..."
            hide c08
            hide c10
            show c11:
                pos (0.5, 0.025) anchor (0.5, 0)
            with dissolve
            $ renpy.pause ()   # will wait untill player click
            show c12:
                pos (0.5, 0.025) anchor (0.5, 0)
            $ renpy.pause ()   # will wait untill player click
            stop sound channel 1

            play audio "tv.mp3"
            show c13:
                pos (0.5, 0.025) anchor (0.5, 0)
            $ renpy.pause ()   # will wait untill player click
            stop sound channel 1
            "Ending (1/3): Coffee"

            #ENDING GRAPHIC
            return
#Ending_D
        label ending_d:
            show niljob talkclose
            show dimitrijob talk2
            d "That's a good idea. Fresh air should be good for ya."
            hide dimitrijob
            hide niljob
            hide bkitchen
            with fade

            stop music fadeout 0.5
            play music ("nobodysthereforme - flowers in bloom.mp3") fadein 0.5

            show dautoshop:
                pos (0.5, 0.025) anchor (0.5, 0)
            with moveinright
            text "You step outside and take a stroll around the block."
            text "Somehow the automotive repair shop around the corner is still in business, even though it looks like it should have been demolished years ago."
            text "This small-ass town has nothing and is nothing, but hey- at least today the weather was nice."
            
            hide dautoshop
            with moveoutleft

            show dcornerstore:
                pos (0.5, 0.025) anchor (0.5, 0)
            with moveinright


            text "You decide to continue up the street to hit up Junkie's convenience for a soda."
            pause 1.5

            stop music
            play music ("iriesunset-miracle-153-bpm-emaj-02-mp3.mp3") fadein 0.5 volume 0.6

            show journey talk at bounce:
                xalign 1.05
            show momo talk at bounce:
                xalign 1.9
            with moveinright
            
            text "Oh god, Momo and Journey are here."
            text "Fuuuuck. Is it too late to turn back?"
            
            
            show momo talk at bounce2:
                xalign 1.9
            m "NIIIIIIIL! Nil!!"
            m "Did you catch last night's episode of {i}Snailman and Slime Frog{/i}? They're doing reruns!!"
            show momo talkclose at bounce2:
                xalign 1.9

            show nil talk:
                pos (0.2, 1.0) anchor (0.5, 1.0)
            with moveinleft
            n "Yeah, I heard."
            n "I'm just here to grab a soda so could you fuck off, please?"
            show nil talkclose

            show momo talk at bounce3:
                xalign 1.9
            m "It's wild; when you rewatch these shows as an adult, you catch all the dark shit they threw in, all the stuff that flew over our heads as kids."
            m "Like, did you know the Slippery Seven were actually based off of the seven deadly sins?"
            
            show nil talk
            n "Yeah, you can't convince me to rewatch that shit. It's never gonna hit the same as when we were younger."
            show nil talkclose

            show momo talkclose at bounce:
                xalign 1.9
            show journey talk at bounce2:
                xalign 1.05
            j "Hi, Nil!"

            show nil talk
            n "...Hi."
            show nil talkclose
            pause 1.0
            show nil talk
            n "What are you guys even doing here?"
            show nil talkclose
            
            show journey talk at bounce3:
                xalign 1.05
            j "Freestylin'!"

            show nil talk
            n "...Okay."
            show nil talkclose

            show journey talk at bounce:
                xalign 1.05
            show momo talk at bounce2:
                xalign 1.9
            m "Dimitri told us you were working with him now. How's it feel to be part of the dead-end job club?"
            show momo talkclose

            show nil talk
            n "Feels great."
            n "Can I go now?"
            show nil talkclose

            show momo surprise at bounce4:
                xalign 1.0
            m "{i}WAIT!" with hpunch
            m "I JUST REALIZED SOMETHING...!"
            m "You look like shit!"
            show momo talkclose at bounce2:
                xalign 1.9

            show nil talk
            n "Thanks."
            show nil talkclose
            
            show momo talk at bounce2:
                xalign 1.9
            m "Yeah, I know that look. That's the insomnia look."
            m "You been out canoodling? Getting all up in kerfuffles in the AM?"
            show momo talkclose

            show nil talk
            n "Nah, just thinking about..."
            pause 0.5
            n "What happens next."
            show nil talkclose

            show momo talk at bounce2:
                xalign 1.9
            m "What, like, after dying?"

            show nil talk
            n "You could say that."
            show nil talkclose

            show momo talk at bounce3:
                xalign 1.9
            m "It's good that you're here, then."
            show momo talk at bounce2:
                xalign 0.3
            with moveoutright
            m "Gimme yer hand."
            m "Pop two of these an hour before bed and you'll be out like a light."
            show momo talkclose at bounce:
                xalign 1.9
            with moveoutleft

            show nil talk
            n "Something tells me I shouldn't trust these."
            show nil talkclose
            pause 0.2
            show nil talk
            n "Or you."
            n "This better not be fuckin' acid."
            show nil talkclose

            show momo talk at bounce2:
                xalign 1.9
            m "It's just melatonin. You're not the only one who's losing sleep freaking out about the future."
            m "Not saying that I freak out about the future, it's just I'm sure someone out there is."
            m "That's why I carry melatonin. So I can sell it to the people who {i}are{/i} freaking out."
            pause 0.3
            show momo talk at bounce3:
                xalign 1.9
            m "For you, it's free of charge, {i}but{/i}! Only if you're on time for band practice on Friday."
            show momo talk at bounce2:
                xalign 1.9
            m "Otherwise it's gonna run ya your firstborn and a pack of Cheetos."
            show momo talkclose at bounce:
                xalign 1.9
            
            show nil talk
            n "You're barely on time yourself..."
            show nil talkclose

            show momo talk at bounce3:
                xalign 1.9
            m "I'm the bassist, I can do whatever I want!"
            show momo talkclose at bounce:
                xalign 1.9
            
            show nil talk
            n "Okay, okay, whatever. My 15's almost up. I'll see ya Friday."
            show nil talkclose

            show momo talkclose at bounce:
                xalign 1.9
            show journey talk at bounce3:
                xalign 1.05
            j "Bye, Nil!"

            hide dcornerstore
            hide momo talk
            hide journey talk
            hide nil
            with dissolve

            stop music fadeout 0.5

            play audio "cricketsandfrogs.mp3" fadein 0.5 volume 5 loop channel 1

            show d01:
                pos (0.5, 0.025) anchor (0.5, 0)
            with Fade(0, 1.0, 2.0)
            text "Ugh, what a day."
            
            show d02:
                pos (0.5, 0.025) anchor (0.5, 0)            
            hide d01
            text "There's a reason why Momo and Journey are Dimitri's friends and not {i}yours{/i}."

            show d03:
                pos (0.5, 0.025) anchor (0.5, 0)
            text "Wait, dammit. You never got your soda."
            show d04:
                pos (0.5, 0.025) anchor (0.5, 0)
            hide d03
            text "But at least Momo hooked you up with some melatonin, which couuuuld be good for you."
            hide d02

            text "You take the pills out of your pocket and stare at them for a while."

            show d05:
                pos (0.5, 0.025) anchor (0.5, 0)
            hide d04
            text "Sleeping alone in the woods is how you cured your insomnia in the first place."
            text "You discovered this when you got locked out of the house one day and decided to spend the night at Lost Lake."
            text "You had the best sleep of your life, and now, the woods are your haven."
            
            show d06:
                pos (0.5, 0.025) anchor (0.5, 0)
            hide d05
            text "On most nights, the harmony of the frogs croaking and rustle of the breeze lull you to sleep - but again, your survival instincts have been forcing you to be on guard for the past couple of days."
            show d07:
                pos (0.5, 0.025) anchor (0.5, 0)
            hide d06
            text "...You imagine another restless night and lugging your sleep-deprived body to work again the next day and..."
            pause 0.8
            text "Yeah, no. You gotta take the melatonin, or else you're gonna be deliriously chucking shittily-made pizzas at Dimitri's head again."

            show d08:
                pos (0.5, 0.025) anchor (0.5, 0)
            hide d07
            text "You pop the pills and wait for the wave of sleep to wash over you."

            pause 1.5

            show d09:
                pos (0.5, 0.025) anchor (0.5, 0)
            text "Finally."
            hide d08
            pause 1.0

            show d10:
                pos (0.5, 0.025) anchor (0.5, 0)
            hide d09
            with None
            pause 1.0
            
            stop sound channel 1 fadeout 2.0
            text "..."
            show d11:    
                pos (0.5, 0.025) anchor (0.5, 0)
            with Fade (2.0, 0.5, 1.0)

            hide d10
            with None
            $ renpy.pause ()   # will wait untill player click

            play music ("grayskies-take-a-walk-unmastered-prod-mp3.mp3") volume 2.0
            show d12:
                pos (0.5, 0.025) anchor (0.5, 0)
            text "{sc}{color=#f00}That was NOT melatonin." with vpunch
            pause 0.3
            hide d11

            show d13:
                pos (0.5, 0.025) anchor (0.5, 0)
            hide d12
            text "{sc}Momoooo you bitch."

            show d13a:
                pos (0.5, 0.025) anchor (0.5, 0)
            hide d13
            $ renpy.pause ()   # will wait untill player click

            show d13b:
                pos (0.5, 0.025) anchor (0.5, 0)
            hide d13a

            show d13c:
                pos (0.5, 0.025) anchor (0.5, 0)

            hide d13b
            $ renpy.pause ()   # will wait untill player click    

            show d14:
                pos (0.5, 0.025) anchor (0.5, 0)
            hide d13c
            $ renpy.pause ()   # will wait untill player click    

            show d15:
                pos (0.5, 0.025) anchor (0.5, 0)
            hide d14
            $ renpy.pause ()   # will wait untill player click

            show d16:
                pos (0.5, 0.025) anchor (0.5, 0)
            hide d15
            $ renpy.pause ()   # will wait untill player click

            show d17:
                pos (0.5, 0.025) anchor (0.5, 0)
            with dissolve
            $ renpy.pause ()   # will wait untill player click
            hide d16

            show d18:
                pos (0.5, 0.025) anchor (0.5, 0)
            hide d17
            text "Is that..."
            
            show d19:
                pos (0.5, 0.025) anchor (0.5, 0)
            pause 1.2
            hide d18
            text "...Snailman and Slime Frog?"
            hide d19
            with dissolve
            show d20:
                pos (0.5, 0.025) anchor (0.5, 0)
            with dissolve
            
            text "They look... different."

            d "Nil!"
            show d21:
                pos (0.5, 0.025) anchor (0.5, 0)
            with dissolve
            hide d20
            pause 1.5

            show d22:
                pos (0.5, 0.025) anchor (0.5, 0)
            hide d21
            n "Dimitri?"
            
            show d23:
                pos (0.5, 0.025) anchor (0.5, 0)
            hide d22
            d "Good luck."

            show d24:
                pos (0.5, 0.025) anchor (0.5, 0)
            $ renpy.pause ()   # will wait untill player click
            hide d23
            
            show d25:
                pos (0.5, 0.025) anchor (0.5, 0)
            hide d24
            n "Wait!"

            show d26:
                pos (0.5, 0.025) anchor (0.5, 0)
            with dissolve
            hide d25
            n "Do you have..."
            
            show d27:
                pos (0.5, 0.025) anchor (0.5, 0)
            hide d26
            n "...a pair of scissors?"
            
            show d28:
                pos (0.5, 0.025) anchor (0.5, 0)
            hide d27
            n "{size=-5}This costume's..."
            
            show d29:
                pos (0.5, 0.025) anchor (0.5, 0)
            hide d28
            n "{size=-10}...too small..."

            show d30:
                pos (0.5, 0.025) anchor (0.5, 0)
            hide d29
            $ renpy.pause ()   # will wait untill player click

            show d31:
                pos (0.5, 0.025) anchor (0.5, 0)
            hide d30
            $ renpy.pause ()   # will wait untill player click

            show d32:
                pos (0.5, 0.025) anchor (0.5, 0)
            with dissolve
            hide d31
            $ renpy.pause ()   # will wait untill player click

            show d33:
                pos (0.5, 0.025) anchor (0.5, 0)
            hide d32
            $ renpy.pause ()   # will wait untill player click

            play sound "fire.mp3" fadein 0.5 loop channel 1 volume 1.5
            show d34:
                pos (0.5, 0.025) anchor (0.5, 0)
            hide d33
            $ renpy.pause ()   # will wait untill player click

            show d35:
                pos (0.5, 0.025) anchor (0.5, 0)
            hide d34
            $ renpy.pause ()   # will wait untill player click
            
            show d36:
                pos (0.5, 0.025) anchor (0.5, 0)
            hide d35
            $ renpy.pause ()   # will wait untill player click
            
            show d37:
                pos (0.5, 0.025) anchor (0.5, 0)
            hide d36
            $ renpy.pause ()   # will wait untill player click    
            stop sound channel 1

            play audio "static.mp3" volume 5 loop channel 1
            show d38:
                pos (0.5, 0.025) anchor (0.5, 0)
            with pixellate
            hide d37
            pause 2.0
            stop sound channel 1
            stop music
            play audio "tv.mp3"
            show d39:
                pos (0.5, 0.025) anchor (0.5, 0)
            hide d38
            $ renpy.pause ()   # will wait untill player click

            "Ending (2/3): It wasn't melatonin"

            stop sound channel 1
            return
#Ending_E
        label ending_e:
            #Ending_E
            show niljob talkclose:
                pos (0.2, 1.0) anchor (0.5, 1.0)
            show dimitrijob talk2 at right
            d "Okay, well, how about you stay over at my place tonight? It's about time you tried sleeping in a normal bed again."
            d "We can play pong. Or I can show you some shit I wrote for the band. C'mon, you haven't been over in forever."
            hide bkittchen
            hide dimitrijob
            hide niljob
            with None

            show bkitchen at dim_tint:
                pos (0.5, 0.025) anchor (0.5, 0)
            show dimitrijob talkclose2 at dim_tint:
                xalign 1.0 yalign 1.0
            show niljob talkclose:
                pos (0.2, 1.0) anchor (0.5, 1.0)

            text "You do kind of miss hanging out in Dimitri's room."
            text "You didn't like interacting with his family so you'd always climb up and get in through his window on the second floor."
            text "He hated it."

            hide dimitrijob
            hide niljob
            hide bkitchen

            show bkitchen:
                pos (0.5, 0.025) anchor (0.5, 0)
            show dimitrijob talkclose2 at right
            show niljob talk:
                pos (0.2, 1.0) anchor (0.5, 1.0)
            n "Fine, I'll stay over."
            show niljob talkclose


            show dimitrijob talk2 at right
            d "Right on."
            show dimitrijob talkclose2

            hide niljob
            hide dimitrijob
            hide bkitchen
            with dissolve
        
            stop music fadeout 0.5

            play music "Rot By Neverforever 110bpm.mp3"
            pause 1.5

            show e01:
                pos (0.5, 0.025) anchor (0.5, 0)
            with dissolve

            n "Ugh, that sucked."
            show e03:
                pos (0.5, 0.025) anchor (0.5, 0)
            hide e01
            n "I can't believe we ate the wall pizza too."

            d "I can't stand the sight of wasting food! I hate when my siblings do it."

            show e04:
                pos (0.5, 0.025) anchor (0.5, 0)
            hide e03

            show nil talk:
                pos (0.82, 1.0) anchor (0.5, 1.0)
                xzoom -1.0
            n "There were DEAD FLIES on the wall, dude. Stuck there with thousand-year-old grease."
            show nil talkclose

            show dimitri talk:
                xzoom -1.0
                pos (0.2, 1.0) anchor (0.5, 1.0)
            d "You practically live in the woods; I'm sure you've eaten worse."
            show dimitri talkclose

            show nil talk
            n "You're right."
            show nil talkclose
            pause 0.2
            show nil talk
            n "I've had Momo's food."
            n "I swear the only things she knows how to make are pregnancy cravings."
            show nil talkclose

            show dimitri talk
            d "You're not wrong on that front."
            d "Here, listen to this song I wrote about Juno."
            d "I'm gonna pitch it to the band this Friday. Tell me if it sucks ass."
            show dimitri talkclose

            hide dimitri
            hide nil
            with None
            hide e04

            show e06:            
                pos (0.5, 0.025) anchor (0.5, 0)
            text "Dimitri's room is where you fell in love with music."
            text "The days spent listening to whiny vocalists and shitty distorted guitar while doing homework. It was a miracle you even got any assignments done."
            text "Eventually, you and a couple of Dimitri's other friends formed a crappy little garage band called 'My Life is a Shitshow and I Can't Wipe Away the Stains', and now you're playing at some guy's basement in a couple of weeks."
            text "They all roped you into doing vocals because you were good at yelling or whatever, which is apparently good for punk."
            
            show e07:
                pos (0.5, 0.025) anchor (0.5, 0)
            hide e06
            text "You were reluctant at first, claiming that you were only there for the free sodas, but now this shitty little garage band is the only time you ever feel like you're wanted."
            pause 2.0
            text "If only summer didn't end. Then things could remain exactly how they are, and how they used to be."

            show e08:
                pos (0.5, 0.025) anchor (0.5, 0)
            hide e07
            text "Thankfully, Dimitri's room hasn't changed one bit."
            
            hide e08

            show e10:
                pos (0.5, 0.025) anchor (0.5, 0)
            text "You look around the room and your eyes land on Dimitri's {i}Snailman and Slime Frog{/i} poster."
            text "That nerd."
            text "That poster is probably at least 11 years old."
            text "Dimitri was the one who introduced you to the show, and you remember following him home every day after school to watch the new episode."
            hide e10
            
            show e11:
                pos (0.5, 0.025) anchor (0.5, 0)
            
            text "There's the lighter you gave him in tenth grade."
            
            show e12:
                pos (0.5, 0.025), anchor (0.5, 0)
            text "The stop sign you toppled over when Dimitri let you take Juno for a spin."
            pause 0.2
            text "Never again."
            hide e11

            show e13:
                pos (0.5, 0.025) anchor (0.5, 0)
            hide e12
            text "He even kept the cool stick you found in the woods."
            pause 0.5
            text "Why did he tape it up like that..."
            
            show e14:
                pos (0.5, 0.025) anchor (0.5, 0)
            hide e13
            text "Oh."
            pause 0.2
            show e15:
                pos (0.5, 0.025) anchor (0.5, 0)
            hide e14
            text "Man, your head WAS big."

            show e04:
                pos (0.5, 0.025), anchor (0.5, 0)
            hide e15

            show nil talk:
                pos (0.82, 1.0) anchor (0.5, 1.0)
                xzoom -1.0
            n "When are you leaving?"
            show nil talkclose

            show dimitri talk:
                xzoom -1.0
                pos (0.2, 1.0) anchor (0.5, 1.0)
            d "For uni? The 27th."
            show dimitri talkclose

            show nil sad
            n "I see."
            show nil sadclose

            show dimitri talk            
            d "Dude, don't worry 'bout that right now. We still have plenty of summer left."
            show dimitri talkclose

            n "..."

            show dimitri talk
            d "Tell you what. I don't know what the future's gonna look like, but let's make this the best summer of our lives."
            hide nil
            hide dimitri
            hide e04
            with dissolve

            show e16:
                pos (0.5, 0.025), anchor (0.5, 0)
            with dissolve
            d "You wanna go fishing at Lost Lake?"
            d "I'll grab my finest tackle."
            
            show e17:
                pos (0.5, 0.025) anchor (0.5, 0)
            hide e16
            d "Wanna grab 2AM slushies?"
            d "I'll meet you at the Junkie's parking lot 5, even 10 minutes early."
            show e18:
                pos (0.5, 0.025) anchor (0.5, 0)
            hide e17
            d "Wanna get high and play Pong at my house?"
            d "I'll be here. Just call me."
            
            show e19:
                pos (0.5, 0.025) anchor (0.5, 0)
            hide e18
            
            d "But for now- please, just shut the fuck up and get some sleep."

            show e20:
                pos (0.5, 0.025) anchor (0.5, 0)
            hide e19
            
            n "Okay, okay, jeez."

            show e21:
                pos (0.5, 0.025), anchor (0.5, 0)
            hide e20
            text "Your last summer together, before everything changes."
            text "You take in the droning sound of Dimitri's guitar playing, this precious snapshot that you know will be no more in a couple months' time."
            show e22:
                pos (0.5, 0.025), anchor (0.5, 0)
            hide e21
            text "However, at this exact moment, things are exactly how they used to be."
            show e23:
                pos (0.5, 0.025), anchor (0.5, 0)
            hide e22
            text "And for the first time in about a week, the sense of dread that's been following you around is not there."
            text "Slowly, you finally drift to sleep."
            show e24:
                pos (0.5, 0.025), anchor (0.5, 0)
            hide e23
            with None
            
            "Ending (3/3): Good night"
            
            hide e24
            with fade

        label finalcredits:
            scene black
            show screen creditscreen
            pause 100 # or however long it takes to scroll through in a reasonable speed
            hide screen creditscreen
            stop music
            return