import pandas
data = pandas.read_csv('nato_phonetic_alphabet.csv')
alpha_dict = {row.letter: row.code for (index, row) in data.iterrows()}
is_on = True
while is_on:
    user_word = input("Enter a word: ").upper()
    try:
        list_converted = [alpha_dict[letter] for letter in user_word]
    except KeyError:
        print('Sorry, only letters ca be converted.')
    else:
        print(list_converted)

