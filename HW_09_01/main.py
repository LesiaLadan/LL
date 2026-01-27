def popular_words (text, words):
   
    clear_text = text.lower().split(" ") 
   
    count_all = {}
    
    for el in clear_text:
        count_all[el] = count_all.get(el, 0) + 1

    return {word: count_all.get(word, 0) for word in words}

# тайм комплексіті - не знаю, як це вірно виразити через О(), мабуть O(text + words)



#     альтернативні варіанти реалізації:

# -----------------------------------------------------------------------------------------------


# def popular_words (text, words):

#     text = text.lower().split(" ")

    # result = {}

#     for el in words:
#         result[el] = text.count(el)

#     return result

# тайм комплексіті - O(text * words), бо ми проходимо по всіх елементах words і для кожного з них ще прозодимось каунтом по всьому text


# -----------------------------------------------------------------------------------------------


# def popular_words (text, words):

#     text = text.lower().split(" ")

#     result = {}

#     for el in words:
#         counter = 0
#         for i in text:
#             if el == i:
#                 counter += 1
#         result[el] = counter

#     return result

# тайм комплексіті - O(text * words), бо ми проходимо по всіх елементах words і для кожного з них ще прозодимось другим циклос по всьому text   

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
# print(popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']))