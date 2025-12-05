
def count_words(text):
    return len(text.split()) 

def count_characters(text):
    counting_text = text.lower()
    character_counts = {}

    for characters in counting_text:
        if character_counts.get(characters) == None:
            character_counts[characters] = 1
        else:
            character_counts.update({characters: (character_counts.get(characters) + 1)})

    return character_counts


def sort_character_counts(count_dict):
    count_list = sorted(count_dict.items(), key=lambda item: item[1], reverse=True)

    return count_list
