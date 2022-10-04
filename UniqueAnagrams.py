import ListHash
import re

def test(filename):

    testfile = open(filename, 'r')
    # testfile = open('file.txt', 'r')
    HashTable = ListHash.ListHash()

    while True:
        #line = testfile.readline()
        line = testfile.readline()

        # stop looping if the end of the file is reached
        if not line:
            break
        
        # split on every non alphanumeric character
        words = re.split('[^a-zA-Z0-9]', line)
        # put every word into the hastable
        for word in words:
            
            # sort the word by its characters
            sort = ''.join(sorted(word))
            
            # takes care of the empty string case caused by \n
            if (len(sort) > 0):
                # value does not matter in this instance
                item = sort, 0
                HashTable.insert(item)
        
    print('There are ', HashTable.size(), ' unique anagrams in ', filename)
    print('The size of the HashTable is ', len(HashTable._HashTable), '\n')

test("pride-and-prejudice.txt")
test("file.txt")
test("randomtext.txt")