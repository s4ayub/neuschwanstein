# word in list of words 

_end = "end"

def make_trie(*words):
    root = dict()
    
    for word in words:
        current_dict = root
        for letter in word:
            if current_dict.get(letter):
                current_dict = current_dict[letter]
            else:
                current_dict[letter] = {}
                current_dict = current_dict[letter]
    return root

def search(trie, word):
    curr_hash = trie
    
    for letter in word:
        if curr_hash.get(letter):
            curr_hash = curr_hash[letter]
        else:
            return False
    
    return True

a = make_trie('foo', 'foor', "nyeah", 'floor')
print(search(a, "nyeas"))

print(a)

