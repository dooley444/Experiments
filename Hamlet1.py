from sys import exit


print("""Hello, Hamlet. I've been expecting you.  """)
reaction0 = input("Ask who this is. " )
print(f"""{reaction0}? I am your father's ghost, speaking from the beyond.\n""")

reaction1 = input("Do you believe your father's ghost? Write 'Yes' or 'No'")

if reaction1 == "No":
    print("No??? Hamlet, dost thou not remember the voice of thy father? \n Away with you!")
    exit(0)


if reaction1 == 'Yes':
    print("""I am pleased with this answer. \n
    You are a straight-thinking Prince, not given to fear or suspicion, but action!\n
    Now, noble Hamlet, list: I was murdered by your uncle, who now wears my crown!""")

reaction2 = input("""Type 'a' if you believe this Ghost and want to ask him what to do next..\n
Type 'b' if you want to leave the Ghost, go find your friend Horatio, and talk things over with him.\n
Type 'c' if you are starting to get scared of the Ghost and decide to draw your sword.""")

if reaction2 == 'a':
    print("Brave Hamlet! Avenge my foul and most unnatural murder. Go and find the usurper, Claudius my brother, and kill him whilst he sleeps.")

kill = input("Will you do so? Type 'Yes' or 'No'")
if kill == 'Yes':
    print("Aha, I have won you for Satan! I am not the Ghost of your father, but a demon sent from hell! \nThou art bound for damnation!!! AHAHAHAHAHA")
    print("You have lost the game. Goodbye.")
    exit(0)

if kill == 'No':
    print("Ah, please? Pretty please?")
    temptation = input("Will you reconsider? Type 'Yes' to agree to kill Cladius, or 'No' to firmly reject the Ghost's plea.")

if temptation == 'Yes':
        print("Aha, I have won you for Satan! I am not the Ghost of your father, but a demon sent from hell! Thou art bound for damnation!!! AHAHAHAHAHA")
        print("You have lost the game. Goodbye.")
        exit(0)

else: print("Horatio comes along and spots you. 'My Lord' he cries.\n'You have been speaking to thin air!\n Come with me. We shall restore you to health'.\n You leave with Horatio, saved from the demon that was claiming to be the Ghost of your father.\n""")
exit(0)

if reaction2 == 'b':
    print("""That was the right choice. Horatio is a good friend of yours. \n He tells you the truth: That the 'Ghost is actually a demon.
          \nYou have been saved from hell!""")
    exit(0)

if reaction2 == 'c':
    print("""What, dost thou draw thy sword, Hamlet?
          \nThou art a villain to treat thy father's spirit so! Then no more with thee. I'll away!""")
    exit(0)
