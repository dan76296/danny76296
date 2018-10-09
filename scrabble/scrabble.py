def calculate_scores(word):
    word_score = 0
    for x in word:
        word_score += scores[x]
    return word_score

def dict_lookup():
    word_list = 'wwflist.txt'
    words_from_list = open(word_list, 'r')
    dictionary = words_from_list.read()
    words_from_list.close()
    dictionary = dictionary.split('\n')
    return dictionary

dict_lookup()

def anagrammer():
    for item in dict_lookup():

my_letters = input(Enter your Letters...>)

possiblities = False
while possiblities == False:
    try
        possible_spots = input()
        if possible_spots = '':
            possiblities = True

scores = {'a':1, 'b':4,'?': 0, 'c':4, 'd': 2,'e': 1, 'f': 4, 'g': 3, 'h': 3,'i': 1,'j':10, 'k':5, 'l':2,'m':4,'n':2,'o':1,'p':4,'q':10,'r':1,'s':1,'t':1,'u':2,'v':5,'w':4,'x':8,'y':3,'z':10}

for possible_spot in possible_spots:

'''

def rack_check(f_rack):
    """Check the letters in the rack against the SOWPOD dictionary and
    append valid words to a list."""
    valid_list = []
    for item in word_master:
        letter_bank = list(f_rack)
        for letter in item:
            if letter in letter_bank:
                valid = True
                letter_bank.remove(letter)
            else:
                valid = False
                break
        if valid == True:
            valid_list.append(item)
    return valid_list

def dict_maker():
    """Create a dictionary of the words with their scores."""
    valid_dict = {}
    f_list = rack_check(list((raw_input("Letters: ")).lower()))
    for i in f_list:
        valid_dict[i] = calc_score(i)
    return valid_dict

def list_print():
    """Print a list of the words in descending order of value."""
    dict = dict_maker()
    sort_dict = sorted(dict.items(), key=lambda k: k[1], reverse=True)
    for x in sort_dict:
        print x[0], "-", x[1]

list_print()
'''