#Exercise 3: I Came, I 'Saur, I Conquered
# If T-Rex is angry, hungry, and bored he will eat the Triceratops.
# Otherwise if T-Rex is tired and hungry, he will eat the Iguanadon.
# Otherwise if T-Rex is hungry and bored, he will eat the Stegasaurus.
# Otherwise if T-Rex is tired, he goes to sleep.
# Otherwise if T-Rex is angry and bored, he will fight with the Velociraptor.
# Otherwise if T-Rex is angry or bored, he roars.
# Otherwise T-Rex gives a toothy smile.

angry = False
bored = True   #change this for every statement
hungry = False
tired = False

if angry and hungry and bored:
    print('he will eat the Triceratops.')
elif tired and hungry:
    print('he will eat the Iguanadon.')
elif hungry and bored:
    print('he will eat the Stegasaurus.')
elif tired:
    print('he goes to sleep.')
elif angry and bored:
    print('he will fight with the Velociraptor.')
elif angry or bored:
    print('he roars.')
else:
    print('T-Rex gives a toothy smile.')    