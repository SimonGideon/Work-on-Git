from gtts import gTTS
import os
from playsound import playsound
import random
import shutil
name = "Unix Stories"
path = os.getcwd()
shutil.rmtree(name, ignore_errors=True)
print("-----> This Process may take a while stay connected. Gathering info.....")

os.mkdir(path + f'/{name}')
noun=[
"Title: At the Whitemare. It was unclear whether I was supposed to continue my work. The guests sometimes left used dishes out on tables, and sometimes did the chore themselves, chatting with one another. Few things more grounding than housework, one said. The first night of the blizzard, the storm of the decade the radio broadcasts and cable news networks called it, some staff sneaked to the least used balcony to smoke a joint. We huddled in a shaft some of the others had dug out, up to our necks in smoke and steam. In the evenings, a few of the guests watched films in the home theatre, at intervals turning their attention away to discuss anecdotes of the actors’ lives and the social or political relevance of the themes. Others gathered in the den, shuffling between the wet bar and the lounging furniture. I would do a sweep, one or two a night, and the guests’ countenance spoke of an uncertainty apparently not unlike mine. Don’t bother yourself, one said, clearly betraying sincerity as he did so. Anyway, there was no real inlet in the various social scenes for me or any of the staff to meaningfully join.  I had come to Stowe, to Whitemare because I needed a job. I’d come to Vermont because, in my mind, it was the closest I could get to being somewhere while being nowhere, in a way. The catalyst for my decision to come to this place was a story, an overhearing that I, in time, integrated into my own set of possible choices. It happens more often than we’d perhaps like to think, more or less enacting the stories we pick up on our move through the world.    The Whitemare Mountain Lodge was a luxury accommodation less than a mile from the slopes, a fabulously expensive architecture of minimalist rustic design. I had the feeling that the new-old place would survive the worst catastrophes, for decades to come, in fact. If catastrophe struck - flood, wind, landslide - the Whitemare would stand. We were one of the very few around that didn’t end up requiring generators to keep the lights on. On the fourth night, Dale died. He was found wilted over one of the beds, where he’d been making various phone calls. The staff knew he’d been dealing with late-stage congestive heart failure. A veteran staff, a woman around his age, sixty-ish, suspected his fate before we found him. She’d been the one to remind him to keep up with his medicines. He’s the only one here who knows how the generators work? A panicked guest asked.",
" Title: my fellow passerine by Jay Wayne.   When Bast hears the low groan from the bedroom, he quietly begins making tea. The motions are familiar, as soothing as the brew itself. He takes a handful of dried ironwort stalks down from the cupboard, the flower buds crinkling as he counts out six and returns the rest to the bundle.  It’s about midnight when Bast looks over at Corvin and sees him swaying on his barstool. He grins and claps him on the shoulder. “Looks like you’ve had plenty,” he says. “Thought you were switchin’ to non-alcoholic stuff?”",
" The Problem Is” by Dena Linn It was day four hundred and fifty-eight for Paul. He weighed in at fifty-eight kilos, down from a strapping ninety-three. He was also fifty-eight years and counting. His doctor prognosed it and Paul felt old, sick, and wasted, his body no longer his own, and tomorrow would be 1999, another absolutely nothing new year.   It was years now, he’d asked Matt what Silence equals Death meant. He’d be the first to admit to being a simple guy, the one whose IQ matched his shoe size - a running joke back at the warehouse. Matt smiled broad and explained that it meant if you don’t talk, more would die. But that was before. Now, it was just a problem without solution, Paul was dying, and he was alone. ",
]
verb=[
"Thank you for taking time to listen to Unix Stories. We dont own the copyrights of these stories",
"Your interest in reading our stories is highly appreciated. Feel much more encouraged",
" This story is valued by most western communities and proofs have shown its truth and audacity to people"
]
noun_1 = random.choice(noun)
verb_1 = random.choice(verb)
combine = noun_1 + " ", verb_1
def convertTuple(tup):
    st = ''.join(map(str, tup))
    return st
# Driver code
tuple = (combine)
str = convertTuple(tuple)

audio = 'speech.mp3'
language = 'en'
sp = gTTS(text=str, lang= language, slow=False)
sp.save(audio)
shutil.move("speech.mp3", path + f'/{name}')
playsound(audio)