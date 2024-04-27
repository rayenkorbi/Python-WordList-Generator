#made by rayen

from itertools import product
import string

minLen = int(input("Enter the minimum Length of the Password you want to crack: "))
maxLen = int(input("Enter the maximum Length of the Password you want to crack: "))

counter = 0

#remove what you don't need in your wordlist 
character = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

file = open("wordlist.txt" , "w")

for i in range(minLen , maxLen+1):
    for j in product(character , repeat = i):
        word = "".join(j)
        file.write(word)
        file.write('\n')
        counter = counter + 1
        
print("Wordlist of {} passwords created".format(counter))
        