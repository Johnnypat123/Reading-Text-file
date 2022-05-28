# Read text from a file, and count the occurrence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    filepath = open("./story.txt", "r")
    result = filepath.read()
    return result
    filepath.close()


def count_words():
    text = read_file_content("./story.txt")
    split_text = text.split()
    count = {}
    for x in split_text:
        if x in count:
            count[x] += 1
        else:
            count[x] = 1
    return count


print(count_words())
