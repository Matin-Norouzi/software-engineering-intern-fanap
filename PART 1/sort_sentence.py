# This function sorts the words in a sentence alphabetically
def sort_words(sentence):
    words = sentence.split()
    words.sort()
    return " ".join(words)
print(sort_words("hello world this is a test"))  # خروجی: a hello is test this world