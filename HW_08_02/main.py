import string

def is_palindrome(text):
    clean_text = "".join(c.lower() for c in text if c not in string.punctuation and c != " ")
    # print(clean_text)
    # reverse_text = clean_text[::-1]
    # # print(reverse_text)
    # if clean_text == reverse_text:
    #     return (True)
    # else:
    #     return (False)
    a = 0
    z = len(clean_text) - 1
    
    while a < z:
        if clean_text[a] != clean_text[z]:
            return False
        a += 1
        z -= 1
    return True

     
assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1' 
assert is_palindrome('0P') == False, 'Test2' 
assert is_palindrome('a.') == True, 'Test3' 
assert is_palindrome('aurora') == False, 'Test4' 
assert is_palindrome("Madam, I'm Adam") == True, 'Test5'
assert is_palindrome("No 'x' in Nixon") == True, 'Test6'
assert is_palindrome(" ") == True, 'Test7'
assert is_palindrome("Able was I, ere I saw Elba") == True, 'Test8'
assert is_palindrome("Was it a car or a cat I saw?") == True, 'Test9'

print("ОК")
