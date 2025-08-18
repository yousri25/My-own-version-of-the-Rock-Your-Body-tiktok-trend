from time import sleep
import subprocess

AUDIO = "song"  

lyrics = [
"I wanna rock right now",
"I wanna, I wanna rock right now",
"I wanna, I wanna rock right now",
"Now, now, rock right now",
"I wanna, I wanna rock right now",
"I wanna, I wanna rock right now",
"I wanna, I wanna rock right now",
"I wanna da—, I wanna dance in the lights",
"I wanna ro—, I wanna rock yo' body",
"I wanna go, I wanna go for a ride",
"Hop in the music and rock yo' body right",
"Rock that body, come on, come on, rock that body (rock yo' body)",
"Rock that body, come on, come on, rock that body",
"Rock that body, come on, come on, rock that body (rock yo' body)",
"Rock that body, come on, come on, rock that body",
"Let me see your body rock",
"Shakin' it from the bottom and top",
"Freak to what the DJ drop",
"We be the ones to make it hot (to make it hot)",
"Electric shock, energy like a billion watts",
"Space be boomin', the speakers pop",
"Galactic Comb and Mr. Spock",
"We bumpin' in your parkin' lot",
"When you comin' up in the spot",
"Don't bring nothin' we call P. Dot",
"'Cause we burnin' around the clock",
"Hit the lights and then turn them off",
"If you bring that, don't make you stop",
"Like the jungle, we run the block",
"No one rollin' the way we rock, way we rock",
"I wanna, I wanna rock right now",
"I wanna, I wanna rock right now",
"I wanna, I wanna rock right now",
"I wanna da—, I wanna dance in the lights",
"I wanna ro—, I wanna rock yo' body",
"I wanna go, I wanna go for a ride",
"Hop in the music and rock yo' body right",
"Rock that body, come on, come on, rock that body (rock that body)",
"Rock that body, come on, come on, rock that body",
"Rock that body, come on, come on, rock that body (rock yo' body)",
"Rock that body, come on, come on, rock that body",
"Super fly ladies, all of my super fly ladies",
"All of my super fly ladies",
"All of my super fl—, super fly ladies",
"Yeah, you could be big-boned long as you feel like you on",
"You could be the model type, skinny with no appetite",
"Short, stacked, black, or white",
"Long as you do what you like",
"Body outta sight",
"Body, body outta sight (yeah)",
"She does the two-step and the tongue drop",
"She does the cabbage patch and the bus stop",
"She like electro, she love hip-hop",
"She like the reggae, she feel punk rock",
"She love samba and the mambo",
"She like to breakdance and calypso",
"Get a lil' crazy, get a lil' stupid",
"Get a lil' crazy, crazy, crazy",
"I wanna da—, I wanna dance in the lights (I wanna dance in the lights)",
"I wanna ro—, I wanna rock yo' body (rock your body)",
"I wanna go, I wanna go for a ride (I wanna go for a ride)",
"Hop in the music and rock yo' body right",
"Rock yo' body right",
"Rock yo' body right",
"Come on, yeah",
"Rock that body, come on, come on, rock that body (come on, yeah)",
"Rock that body, come on, come on, rock that body",
"Go, oh-oh-oh-oh-oh-oh",
"Let go, oh-oh-oh-oh-oh-oh",
"Let go, oh-oh-oh-oh-oh-oh",
"Let go, oh-oh-oh-oh-oh-oh",
"I wanna, I wanna rock right now",
"I wanna, I wanna rock",
"I wanna, I wanna rock",
"Let go, oh-oh-oh-oh-oh-oh",
"I wanna, I wanna rock",
"I wanna, I wanna rock",
"Let go, oh-oh-oh-oh-oh-oh",
"Let go, oh-oh-oh-oh-oh-oh",
"I wanna, I wanna rock right now",
"I wanna, I wanna rock right now",
"I wanna, I wanna rock right now",
"Now, now, rock right now",
"I wanna, I wanna rock right now",
"I wanna, I wanna rock right now",
"I wanna, I wanna rock right now"
]
delays = [
    # First 4 lines (1.5x original)
    1.35, 1.275, 0.975, 1.2,
    
    # Gradually transition to 2x (lines 5-10)
    1.6, 1.6, 2.8, 1.8, 1.8, 2.0,
    
    # Full 2x slower from line 11 onward
    2.4, 1.8, 1.8, 1.8, 2.4, 1.8, 1.6, 2.4, 2.6, 1.6,
    1.4, 2.4, 2.2, 1.8, 2.2, 2.2, 1.6, 1.6, 1.2, 3.2,
    1.6, 1.6, 1.6, 1.6, 1.8, 1.8, 2.0, 2.2, 1.8, 1.6,
    1.6, 2.8, 2.0, 1.6, 1.6, 2.8, 2.0, 2.0, 2.0, 2.0,
    1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 2.4, 1.6,
    1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 1.6, 2.0,
    2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0,
    2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0,
    2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0,
    2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0,
    2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0,
    2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0
]
player = subprocess.Popen(["mpv", AUDIO])

i=0
sleep(17)
for i in range(len(lyrics)): 
    print(lyrics[i]) 
    sleep(delays[i])
player.wait()
print("hope you like it :)")
