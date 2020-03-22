def minion_game(string):
    # your code goes here
    len_str = len(string)
    kevin = 0
    stuart = 0
    vowels = ['A','E','I','O','U']
    for i in range(0,len(string)):
        if string[i] in vowels:
            kevin +=len_str
        else:
            stuart +=len_str
        len_str -=1
    if kevin == stuart:
        print('Draw')
    else:
        print( 'Kevin {0}'.format(kevin) if kevin >  stuart else 'Stuart {0}'.format(stuart))

