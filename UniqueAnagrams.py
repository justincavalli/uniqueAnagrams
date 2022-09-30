import ListHash
import re

testfile = open('file.txt', 'r')
HashTable = ListHash.ListHash()

while True:
    line = testfile.readline()

    # stop looping if the end of the file is reached
    if not line:
        break
    
    # split on every non alphanumeric character
    words = re.split('[^a-zA-Z0-9]', line)
    print(words)
    # put every word into the hastable
    for word in words:
        
        # sort the word by its characters
        sort = ''.join(sorted(word))
        # value does not matter in this instance
        item = sort, 0
        HashTable.insert(item)
    
print('There are ', HashTable.size(), ' unique anagrams in file.txt')