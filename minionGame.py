def minion_game(string):
    #first we declare 2 variables that beave as counters for kevin and stuart
    stuart_counter = 0
    kevin_counter = 0
    
    # Now we need to loop over the string to identify if the value at each index is vowel(for kevin) or consonant(for stuart)
    for index in range(len(string)): # for BANANA  length = 6, looping occurs from 0 to 5
        # if value in the current index is a vowel, counter adds points for kevin
        if string[index] in {'A','E','I','O','U'}:
            kevin_counter += len(string) - index
        else:
            stuart_counter += len(string)-index
    # Now deciding the winner based on values of counter
    if kevin_counter == stuart_counter:
        print("Draw")
    elif kevin_counter > stuart_counter:
        print("Kevin", kevin_counter)
    else:
        print("Stuart", stuart_counter)
    
if __name__ == '__main__':
    s = input()
    minion_game(s)
