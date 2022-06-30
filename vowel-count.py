def vowel_count(word):
    wordlist = list(word)
    count = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
    letternum = 0
    
    for i in wordlist:
        if wordlist[letternum] == 'a':
            count = {**count, 'a':1}
        if wordlist[letternum] == 'e':
            count = {**count, 'e':1}
        if wordlist[letternum] == 'i':
            count = {**count, 'i':1}
        if wordlist[letternum] == 'o':
            count = {**count, 'o':1}
        if wordlist[letternum] == 'u':
            count = {**count, 'u':1}
        letternum += 1
        
    vowelcount = sum(count.values())
    print(vowelcount)
    # return count
    
word = input('Word: ')
vowel_count(word)
