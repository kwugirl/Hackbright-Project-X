import os
import string
import shutil

alphabet = list(string.lowercase)

# makes a bunch of folders, each named for a letter in the alphabet
for letter in alphabet:
	os.mkdir(letter)

word_list = os.listdir("original_files/files/")

# gets file at position 0 in word_list, grabs first letter of that file, copies file to a directory named that first letter. This was test code for proof of concept.
#print word_list[0]
#print (word_list[0])[0]
#shutil.copy("original_files/files/" + word_list[0], (word_list[0])[0])

for i in range(len(word_list)):
	shutil.copy("original_files/files/" + word_list[i], (word_list[i])[0])

# deletes original text files, we're doing copy + delete since shutil.move requires that the directories don't already exist
shutil.rmtree("original_files/files/")