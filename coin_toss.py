# FILE NAME - coin_toss.py

# NAME: Nick Twardeski
# DATE: 3/13/26
# BRIEF DESCRIPTION:  Coin Toss Lab CH4



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########

# Don't forget to import random!!!!!
import random

def main():
    coin_toss()

def coin_toss():
    
    randomnum = random.randint(1, 100)

    print ('===== Coin Flipper =====')

    if randomnum >= 51:
        print('Tails')
    
    else:
        print('Heads')





main()


########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################
'''
===== Coin Flipper =====
Heads
'''



'''
===== Coin Flipper =====
Tails
'''


########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What was the hardest part of completing this lab? 



Finding out I had to use >= instead of =>



'''
