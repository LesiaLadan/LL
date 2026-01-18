
import string

raw_str = input("Enter a string to create a hashtag: ")

raw_str = "".join(c for c in raw_str if c not in string.punctuation)

words = raw_str.split()

words = [word.capitalize() for word in words]

hashtag = "#" + "".join(words)
if len(hashtag) == 1:
    hashtag = "Error! No words to form a hashtag."
hashtag = hashtag[:140]

print(hashtag)
