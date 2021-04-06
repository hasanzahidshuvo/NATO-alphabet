import pandas

# Reading csv data
data = pandas.read_csv('NATO-alphabet/nato_phonetic_alphabet.csv')

# Creating dictionary from csv
data_dict = {row.letter:row.code for (index, row) in data.iterrows()}

# Taking input
word = input("Enter a Word: ").upper()

# Creating a list output
output_list = [data_dict[letter]for letter in word]

# Creating a String output
output_string = ' '.join(output_list)

print(output_string)
