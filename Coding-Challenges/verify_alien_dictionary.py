from typing import List

# PostMortem:
    # So, manual iterators, were probably not the best idea here,
    # but it felt like this comparison was so involved, that the only way to
    # avoid a crazy run-time, was to 'tweak all the knobs'.
    # A naive solution might have looked like using a for loop,
    # and adding or subtracting to variables pointing to i,
    # which would make the handling the iterators easier.
    # Note to self, tries might have been good here, prefix tries specifically,
    # as they seem similar to Huffman encoding for a group of words (the message))
    # So, one of the working online solutions is to use a Hashtable.
def isAlienSorted(words: List[str], order: str) -> bool:
# So, given a set of words, and an alphabet,
# We want to say, for words[i][j], and words[i][j + 1]
# are they in the same order, in `order`, as they are in word[i].
    # If they aren't, we can return False.
    # If they are, we want to swap words[i][j], with words[i][j + 1],
    # and words[i][j + 2], with words[i][j]
# If we get through word[i], and find that everything is alphabetically ordered,
# we can move on to word[i + 1], and continue the process
    # Noting that this may be an entry point to recursion
    # which might make our solution more performant.
# What's tricky here is that, we can also compare words[i][j],
# with words[i][j + 1], in the same pairwise manner, and get to the same result,
# however handling the indexing here may get tricky, if one of the words 
    # Noting that we have to handle some index bounds properly here.
# Also note that if words end early, in a word to word comparison method,
# the word that's longer is greater, and should be last.
# Tries would be nice to know right now.
    ordered = False
    order.split(" ")
    
    i = 1
    j = 1
    k = j + 1 # this is going to be the first iterator variable to throw an index out of bounds error, 
                # because it's looking ahead by two steps.
                    # We need to form some connection between the variable k, and the word it's attached to.
                        # This seems to require us to capture a word[i], and then capture word[i].len(),
                        # so we can make the value of k dependent upon the len
    cur_word_len = len(words[i])
    # cur_word_len = len(words[i]), to trap this variable in our loop and maintain access to it
    greater = lambda i, j, k, cur_word_len: cur_word_len > i and cur_word_len > j and cur_word_len > k
    while not ordered or greater(i, j, k, cur_word_len):
        
         # this is going to be the first iterator variable to throw an index out of bounds error, 
                # because it's looking ahead by two steps.
                    # We need to form some connection between the variable k, and the word it's attached to.
                        # This seems to require us to capture a word[i], and then capture word[i].len(),
                        # so we can make the value of k dependent upon the len
        # cur_word_len = len(words[i]), to trap this variable in our loop and maintain access to it
        # We want to say, for words[i][j], and words[i][j + 1]
        fst_word_char = words[i - 1][j - 1] # capture our first word character
        try: 
            snd_word_char = words[i - 1 ][k - 1] # !!!!!!! This is the bug- k is out of bounds.
        except IndexError as ie: 
            print(ie) # capture our second word character
        # The next step is to compare the location of these chars in the `order` list.
        fst_char_ind = order.index(fst_word_char) # Capture the index of the corresponding word_char element in order.
        snd_char_ind = order.index(snd_word_char)
        # j += 1 
        # k = j + 1
        # print(fst_word_char, snd_word_char)
        # print("words[i - 1][j - 1]: ", words[i - 1][j - 1], "words[i - 1 ][k - 1]: ", words[i - 1 ][k - 1])
        if fst_char_ind < snd_char_ind: # if the index of the first_char is less than the second, we do our swap
            j += 1
            k = j + 1
            # words[i][j] =>
                # this means:
                    # i = 0
                    # j = 1
                    # k = 2
            # If they are, we want to swap words[i][j], with words[i][j + 1],
            # and words[i][j + 2], with words[i][j]
            pass
        elif fst_char_ind > snd_char_ind:
            return False # If they aren't, we can return False.
        
        # are they in the same order, in `order`, as they are in word[i].   
        # If they aren't, we can return False.
        # If they are, we want to swap words[i][j], with words[i][j + 1],
        # and words[i][j + 2], with words[i][j]


    
words = ["word","world","row"]
order = "worldabcefghijkmnpqstuvxyz"
print(isAlienSorted(words, order))