def first_word(text):
    """ Пошук першого слова """
    simbol = 0
    
    while simbol < len(text) and not text[simbol].isalpha():
        simbol += 1
    word = ""
    
    while simbol < len(text) and (text[simbol].isalpha() or text[simbol] in "'-"):
        word += text[simbol]
        simbol += 1
    
    return word
 
assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
assert first_word("step-mother - is kind") == "step-mother", 'Test7'

print('OK')