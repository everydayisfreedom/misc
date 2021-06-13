import tokenize
#count occurences

##Observer perspective
Obs1 = "The day that orientation started he was excited for many things.\
		New friends, new girls, and the interesting events and games that were planned.\
		He was surely determined to meet as many people as possible with full confidence \
		and takimg part in every event from the ice breaking games to the mountain hiking.\
		He was happy, and couldn't wait to start the first day of this new phase in his life,\
		and eagerly looked forward to the rest of it."

Obs2 = "She didn't have much expectations for university. Her high school experience was the worse,\
		so going to another educational institution was not the thing that she was most excited about.\
		She already knew how campus looked like, as she already came her before on open doors day.\
		But mostly, she was scared of people, as they were not always friendly to her.\
		However the first five minutes, being in the gymnasium to register officially, resulted in her talking to three very friendly and kind people.\
		It made her a bit more comfortable about being there. Although the people registering her were not being very nice, she was not expecting them to be.\
		What followed during that day was surprisingly positive, as she met people that she thought would never even think about talking to her.\
		Even though her mentor seemed like a very messy and unorganized girl, the other mentees seemed like people who were willing to help each other\
		if she revealed herself to be useless. The end of the day was kind of sad. She did not know how she was supposed to get used to campus life,\
		but sleeping helped her het through the next morning."

Obs3 = "She came with her parents and siblings. You could tell that she was excited and looking forward to the journey ahead,\
		in that place that she thought was amazing. Happy, excited, and overly energetic, she took care of all the paperwork needed\
		so that she could check in her room. Situations that would normally intimidate her did  not seem to bother her at all that day.\
		Although she knows it’s not justified, she already felt like a new and better person. Surrounded by lots of similarly excited\
		and happy strangers, waiting for long hours, she can now head to her room. She joined her family in the car and they all went together.\
		Everyone was excited. Even her brother who wished he could have stayed home playing video games was curious. They all enter the room, everyone is satisfied. \
		Then it’s time to move the suitcases and boxes; a tiring task that no one complained about. She waves bye to her family. She’s now left alone to rest\
		and reflect on her busy day and and prospect for the future that seemed to hold for her endless possibilities."

Obs4 = "He had a depression after seeing his family leave as he was feeling abondonned by his own,\
		his heart was full of fear and now he has to learn smth that wasn’t meant for him: independence,\
		as he enters his room, he was looking for someone to talk to but he didn’t know anybody in the campus,\
		a huge fear and loniless can be seen in his eyes as he rush to sleep and wish it was all just a dream\
		that he will wake up from. Ayoub didn’t know how to take care of himself, the 17 years old boy rely all his life\
		on his family and now that the reality hits, he didnnt know what to do, he felt an infinite unhapiness inside his heart."

Obs = [Obs1, Obs2, Obs3, Obs4]

#Field perspectied
Fie1 = "I remember waking up at 5 o’clock in the morning to go to Ifrane. My parents couldn’t come with me, so a family friend took me.\
		I remember being scared, stressed, anxious. When I first arrived on campus, it seemed huge to me. we parked the car in parking lot\
		and took the van to go to the gymnasium to get my ID, room keys and all. It was all very overwhelming.I remember getting to my room,\
		the family friend who dropped me off left, and I was alone. I didn’t know what to do, my roommate wasn’t there yet so I choose my bed,\
		my closet and started to unpack. I was anxious about meeting my roommate as well, but then I did, she was nice but I knew we would not be friends.\
		I remember finishing unpacking, then going to dinner alone. I didn’t know anyone and I felt lost. I remember going to the “treasure hunt” they had\
		that night and meeting a couple of people. Honestly, that whole day was kind of a blur, I just remember the anxiety I was feeling that day and how\
		scared I was of being  left alone in an unknown environment."

Fie2 = "I can still hear mom’s voice shouting from across the house. I opened my eyes and a realization hit me faster than I gained my full consciousness.\
		It was officially my last day living at home. I could barely reach out for my phone when my dad popped his head from behind the door telling me hurry up\
		and that we were going to be late. I looked at the clock ticking above my head, it read 5 am. I jumped from my bed, got ready in twenty-five minutes or so\
		and finished packing the last items scattered here and there. My aunt was home too to help in the moving out process. We packed the car to the brim and hit the road.\
		An awkward silence reined the vehicle with occasional small words and warnings thrown from mom to dad at the driver seat. We arrived to Ifrane at 7 am or so, my aunt\
		wanted to take pictures of me in the park in front of la “Paix” to send to other family members. I abided, sporting a shy grin and occasional hair flips.\
		We had breakfast in “L’adresse”, while dad complaining how overpriced everything in Ifrane is, I glanced at the folks at the neighboring tables. they seemed young and nervous;\
		it doesn’t take much investigation to realize that it’s their first day in college. They had that nervous freshman aura. These people might be friends, classmates or even future lovers.\
		I watched the curly headed tall guy lean his head on the table to catch up on his lost night sleep. My lurking session was interrupted with my dad asking the waiter for the check,\
		and in less than 5 mins we found ourselves inside the university. We were directed towards the gymnasium, and the first thing we noticed was the dying grass. How come the “best” university\
		in Morocco keeps its dull grass on display? We went through the what seemed to be thousands of cubicles until I reached the one that read “cash wallet issuance”.\
		I could not conceal my excitement when I held in my freshly manicured hands the white card with a green strip. I did not specifically admire the picture I was seeing with the ungroomed eyebrows\
		and messy hair, but none of that mattered at the time. “I am going to have my own wallet filled with cards”, I repeated to my parents while my body jumped with excitement.\
		By the time I was going to have a  feedback from my small audience, I squinted my eyes at the guy in front of me, forcefully trying to recall the Facebook pictures I had saved in my phone\
		and compare it with the figure in front of. However, before I could make a final judgement, I saw him walking towards me, thoroughly trying to read my parents body language to make a proper\
		decision to whether go for a hug or a high five. I have seen his discomfort and happily welcomed him in my arms. Suddenly about a third of my anxiety banished, and I could not believe that\
		my favorite Facebook friend was right there with me. And before being able to catch up, my mom interrupted our talk and asked for my room key so that she could set everything up for me.\
		I handed it to her and headed towards building 17 to attend to the president’s speech with my aunt. I cannot remember much of all the talks and names but I still vividly remember the picture\
		of the girl sitting on a guy’s lap with her thong showing steering attention from the huge line reading «No PDA is allowed”. I skimmed through the faces of the audience, parents were in shock\
		and disbelief and the students were cracking up so much. An avalanche of hysterical laughs filled the theater. Soon after, I headed to building 39 where my new home was. It was a huge building\
		with white walls and hospital style lamps. It looked scary and daunting. I could not comprehend the fact that I will not be tucked to bed by mom that night, and I will not wake up to the sound\
		of her tea pouring. A strangling sensation debilitated my movement for a few minutes before I resumed the stairs down to the door with my name’s tag. My aunts faced welcomed me with a worrisome look,\
		“the room is horrible” she shouted. And before I could examine me soon to be new home, my mom resumed “the floor is all stained, the flush is not working, and the windows are creaky”.\
		I did not mutter a word, I just sat and looked at them as if I tried to absorb their presence as much as I could so that I feed on it for the following weeks. Two hours fast forward,\
		my mom pushed my backpack and placed herself as close to me as possible while running her rigid hands through my hairlocks. “We have to leave, take care of yourself and do not forget to eat\
		the meals in the fridge before they go bad, and call me before you go to bed”. Without realizing it, I felt my tears race through my cheeks, and shortly after, my mom joined the marathon.\
		We hugged so tight, but it did not seem to be enough. And in less than five minutes, I found myself alone with the creaking window I was warned about earlier. Before I let myself succumb to my loneliness,\
		I dragged myself out of bed to the desk in front of me. I slapped on a full face of makeup, put on my choker and headed to the main part of campus.\
		I awkwardly sat on the bench facing the fountain, waiting for my Facebook friend to show up. Unsurprisingly, I saw clicks already formed and people swaddled together tightly.\
		There were the musicians, the guitar people and the singers next to the cafeteria, there was also edgy teens sharing cigarettes and a few laughs overshadowed by despair.\
		My fear of not belonging rose to the surface again and already foresaw my social anxiety ruining my chances of having a social life in this new place.\
		Suddenly, my train of thought was interrupted by the humming of three guys walking towards me led by my Facebook friend. I greeted them shyly and we all walked together to the cafeteria.\
		I sensed my anxiety gradually easing and felt my voice regained its steadiness again. We talked about our travels, families, studies, favorite shows and not for a second the conversation felt dull.\
		Four hours passed as a breeze, and I was left alone with this skinny, brown haired guy. I never had any experience with guys before, whether friends or potential lovers before, naturally,\
		my flight reflex ordered me to call it a night. The guy gently offered to walk me back to my building, and I obliged. Little did I know he was going to shortly be my boyfriend of two years."

Fie3 = "I woke early and dressed up for the day i was excited and also scared nervous mostly i didnt know what to do first so i just went with the flow i packed a bag with aui logo\
		in it and put a notebook  and a pen inside it i then went to pick up my books from the bookstore. Because the line was long i went to my 9 am class late i felt embarassed cuz\
		everyone was looking at me. the first activity was introducing ourselves to our classmates since im a shy person i felt more anxious and nervous.\
		in all my classes we did the same thing:brief introduction of ourselves. after i finished all my classes at 12 i decided to go grab launch and discover the acadamic area\
		after doing so , i went back to my room and slept."

Fie4 = "First day at college, my dad had driven me to the dormitory we dropped my luggage there and wen to have lunch. We said goodbye after he dropped me bak to my room.\
		It weird to be away from home for the first time. I set homy things and my clothe in the closet. I decided to take nap. After I woke up, I dressed up and took the\
		schools bus to go to campus since my room was in the annex residence. It was pretty quiet around campus, walked around for a bit then headed to the restaurant and had\
		my first meal there. After, I took a coffee and went back to the bus shelter. My first day was pretty lonely as I remember it,  I didn’t know anyone Andy roommate hadn’t arrived yet."


Fie = [Fie1, Fie2, Fie3, Fie4]

def countPercentage(string, flag):
	string.replace(",", "").replace(".", "").replace("\"","").replace(":", "").replace(";","")
	tokens = string.split(" ")
	length = len(tokens)

	if flag == 1:
		reference = {"I", "Me", "me", "Myself", "myself", "My", "my", "we"}
	else:
		reference = {"he", "He", "She", "she", "They", "they", "His", "his", "Her", "her"}

	cnt = 0
	for l in range(0,length):
		if tokens[l] in reference:
			cnt +=1

	Percentage = cnt/length * 100
	print("-Number of tokens :", length, "\n-Number of occurrences of ", reference, " : ", cnt, "\nPercentage (Number of occurrences/Number of tokens * 100) :", Percentage, "%")




def showPerc(type, string, flag):
	for i in range(0,len(string)):
		print("\n")
		print(type, i+1,":")
		countPercentage(str(string[i]), flag)

showPerc("Observer perspective", Obs, 0)
print("\n\n")
showPerc("Field perspective", Fie, 1)