# Get words count 
def get_num_words(string):
    word_count = len(string.split())   
    return word_count

def characters_count(strings):
    character_list = {}
    strings = strings.lower()
    for string in strings:
        if string not in character_list:
            character_list[string] = 1
        else:
            character_list[string] = character_list[string] + 1
    return character_list

def dico(character_count):
    new_dict = []
    for key, value in character_count.items():
        if key.isalpha():
            new_dict.append({"char": key, "num": value})
    
    def sort_on(dict):
        return dict["num"]
    new_dict.sort(reverse=True, key=sort_on)
    return new_dict
