import string

letters = string.ascii_letters

user_input = input("Enter letter range (e.g. a-f):\n")

start, end = user_input.split("-")

start_idx = letters.index(start)
end_idx = letters.index(end)

result = letters[start_idx:end_idx + 1]

print(result)