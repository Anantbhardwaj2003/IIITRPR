# Write down a function that takes a number as input and returns as the sum of index of the digits in the number.
# For example, if the input is 1234, the output should be 0+1+2+3=6.
# If the input is 5678, the output should be 0+1+2+3=6. If the input is 0, the output should be 0.
# If the input is 1, the output should be 0. If the input is 2, the output should be 0. If the input is 3, the output should be 0.
# If the input is 4, the output should be 0. If the input is 5, the output should be 0. If the input is 6, the output should be 0.
# If the input is 7, the output should be 0. If the input is 8, the output should be 0. If the input is 9, the output should be 0.
def sum_of_index(num):
    # Convert the number to a string to iterate over its digits
    num_str = str(num)
    
    # Initialize the sum of indices
    index_sum = 0
    
    # Iterate over the digits and their indices
    for index, digit in enumerate(num_str):
        # Add the index to the sum
        index_sum += index
    
    return index_sum

sum_of_index(1234)  # Output: 6
print(sum_of_index(5678))  # Output: 6

# Write down a function that checks whether  a given year is a leap year or not.
# A year is a leap year if it is divisible by 4, but not divisible by 100, unless it is also divisible by 400.
# For example, 2000 is a leap year, but 1900 is not. 2004 is a leap year, but 2001 is not.
def is_leap_year(year):
    # Check if the year is divisible by 4 and not divisible by 100, or if it is divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

is_leap_year(2000)  # Output: True
print(is_leap_year(1900))  # Output: False

# Write down a function that takes a string as input and encrypts it using a method named "Caesar Cipher".
# The Caesar Cipher is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.
# So take a shift of 3 for example, A would be replaced by D, B would become E, and so on.
def caesar_cipher(text, shift):
    encrypted_text = ""
    
    # check if the encrypted text contains any numbers or special characters
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            # Shift the character and wrap around the alphabet
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            encrypted_text += char  # Keep non-letter characters unchanged
    return encrypted_text

c1=caesar_cipher("Hello, World!", 3)  # Output: "Khoor, Zruog!"
print(c1)

# Write a function that decrypts a string that was encrypted using the Caesar Cipher method.
# The decryption process is based according to the same shift without defining the shift value.
# Use the value -1 in the function to decrypt the string.
# The function should return the decrypted string.
# Not taking the argument of the shift value, but take as -1 for decryption for all texts.
# The function should return the decrypted string.
def caesar_cipher_decrypt(encrypted_text):
    decrypted_text = ""
    
    # Decrypt the text using a shift of -1
    for char in encrypted_text:
        if char.isalpha():  # Check if the character is a letter
            # Shift the character and wrap around the alphabet
            if char.islower():
                decrypted_text += chr((ord(char) - ord('a') - 3) % 26 + ord('a'))
            else:
                decrypted_text += chr((ord(char) - ord('A') - 3) % 26 + ord('A'))
        else:
            decrypted_text += char  # Keep non-letter characters unchanged
    return decrypted_text

c2=caesar_cipher_decrypt(c1)  # Output: "Hello, World!"
print(c2)

# Write a function that takes a string and prints its corresponding indexes in the alphabet.
# For example, if the input is "abc", the output should be "0 1 2".
def alphabet_indexes(text):
    indexes = []
    
    # print the indexes of each character in the aplhabet also print the corresponding character for example a=0, b=1, c=2
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            index = ord(char.lower()) - ord('a')  # Calculate the index in the alphabet
            indexes.append(f"{char}={index}")
        else:
            indexes.append(f"{char}=-1")  # Non-letter characters get -1 as index
    return " ".join(indexes)

c3=alphabet_indexes("efg")  # Output: "e=4 f=5 g=6"
print(c3)

# add binary strings a and b and return their sum as a binary string
class Solution:
    def addBinary(self,a,b):
        # convert the binary strings to integers, add them, and convert the result back to a binary string
        return bin(int(a, 2) + int(b, 2))[2:]
s = Solution()
c4=s.addBinary("1010", "1011")  # Output: "100"
print(c4)
            
# Write a function that takes array as an input of digits and then increments the arrays digits by 1 such as [1,2,3] then 123+1=124 and returns output as [1,2,4]
def increment_array(digits):
    # convert the array of digits and split them into a number
    num = int("".join(map(str, digits))) + 1
    # convert the number back to an array of digits
    return [int(digit) for digit in str(num)]
c5=increment_array([1,2,3])  # Output: [1,2,4]
print(c5)

# Write a function that given string is valid number or not
# A valid number can be an integer or a decimal number, and it can also be in scientific notation.
# For example, "123", "123.45", "1e10", and "-1.5" are valid numbers, while "12a", "1.2.3", and "1e" are not.
import re
def is_valid_number(s):
    # Regular expression pattern for a valid number
    pattern = r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$'
    
    # Check if the string matches the pattern
    return bool(re.match(pattern, s))
c6=is_valid_number("abc")  # Output: True
print(c6)

# Write a function that takes a string as input and returns the last word in the string such as "Anant bhardwaj" with their length 8 and last word is bhardwaj and write as the last word is "last-word" with length corresponding size.
# The last word is "last-word" with length corresponding size.
# For example, if the input is "Hello World", the output should be "The last word is "World" with length 5".    
# If the input is "Anant bhardwaj", the output should be "The last word is "bhardwaj" with length 8".
# If the input is "Anant", the output should be "The last word is "Anant" with length 5".   

def last_word_info(s):
    # Split the string into words
    words = s.split()
    
    # Get the last word
    last_word = words[-1] if words else ""
    
    # Get the length of the last word
    length = len(last_word)
    
    return f'The last word is "{last_word}" with length {length}'
c7=last_word_info("Fly in the moon")  # Output: "The last word is "bhardwaj" with length 8"
print(c7)

# write a function that takes a pow(x,n) and returns the value of x raised to the power n.
# The function should take two arguments, x and n, and return the value of x raised to the power n.
def power(x, n):
    # Calculate x raised to the power n
    return x ** n
    
# Write a function in which we have list of strings and we have to check the anagrams in the list and returns the following anagrams in the list.
# For example, if the input is ["eat","tea","tan","ate","nat","bat"], the output should be [["tan"],["bat"],["eat"]].
# If the input is ["a"], the output should be [["a"]].
# If the input is ["eat","tea","tan","ate","nat","bat"], the output should be [["tan"],["bat"],["eat"]].
def find_anagrams(words):
    # Create a dictionary to store anagrams
    anagrams = {}
    
    # Iterate over the words
    for word in words:
        # Sort the word and use it as a key
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]
    
    # Filter out groups with only one word
    return [group for group in anagrams.values() if len(group) > 1]
c8=find_anagrams(["eat","tea","tan","ate","nat","bat"])  # Output: [["eat", "tea", "ate"], ["tan", "nat"]]
print(c8)

# Write a function that list of numbers and have a target value and return the indices of the two numbers such that they add up to the target value.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


def two_sum(nums, target):
    # Create a dictionary to store the indices of the numbers
    num_indices = {}
    
    # Iterate over the list of numbers
    for i, num in enumerate(nums):
        # Calculate the complement
        complement = target - num
        
        # Check if the complement is in the dictionary
        if complement in num_indices:
            return [num_indices[complement], i]
        
        # Store the index of the current number
        num_indices[num] = i
    
    return []
c9=two_sum([2,7,11,15], 9)  # Output: [0, 1]
print(c9)

# Write a function that takes two lists l1 and l1 and and add these two lists and return the answer of this list in the form of list.
# for example, if the input is[2,4,3] and [5,6,4], the output should be [7,0,8].
# If the input is [0] and [0], the output should be [0].

def add_two_numbers(l1, l2):
   # intialize the result list
    result = []
    
    # Initialize carry
    carry = 0
    
    # Iterate over the lists in reverse order not using length function
    # to avoid using length function
    # and to handle the case where the lists are of different lengths
    i = 0
    while i < len(l1) or i < len(l2) or carry:
        # Get the digits from both lists, defaulting to 0 if the list is shorter
        digit1 = l1[i] if i < len(l1) else 0
        digit2 = l2[i] if i < len(l2) else 0
        
        # Calculate the sum and carry
        total = digit1 + digit2 + carry
        carry = total // 10
        result.append(total % 10)
        
        i += 1
    # Reverse the result list to get the correct order
    result.reverse()
    return result

# Write a function to check whether n is happy number or not.
# A happy number is a number which eventually reaches 1 when replaced by the sum of the square of each digit.

def is_happy(n):
    # Initialize a set to keep track of seen numbers
    seen = set()
    
    while n != 1 and n not in seen:
        seen.add(n)
        # Calculate the sum of the squares of the digits
        n = sum(int(digit) ** 2 for digit in str(n))
    
    return n == 1

# Write a function to check the the two strings are isomorphic or not.
# Two strings are isomorphic if the characters in one string can be replaced to get the other string.

def is_isomorphic(s, t):
    # Create dictionaries to store the mapping of characters
    s_to_t = {}
    t_to_s = {}
    
    # Iterate over the characters in both strings
    for char_s, char_t in zip(s, t):
        # Check if the mapping exists and is consistent
        if (char_s in s_to_t and s_to_t[char_s] != char_t) or (char_t in t_to_s and t_to_s[char_t] != char_s):
            return False
        
        # Create the mapping
        s_to_t[char_s] = char_t
        t_to_s[char_t] = char_s
    
    return True

# write a function in which string contains valid expression and evaluate the expression and return the result without using eval function.
def evaluate_expression(expression):
    # Initialize a stack to store numbers and operators
    stack = []
    
    # Initialize a variable to store the current number
    current_number = 0
    
    # Initialize a variable to store the last operator
    last_operator = '+'
    
    # Iterate over the characters in the expression
    for char in expression:
        if char.isdigit():
            current_number = current_number * 10 + int(char)
        elif char in "+-*/":
            if last_operator == '+':
                stack.append(current_number)
            elif last_operator == '-':
                stack.append(-current_number)
            elif last_operator == '*':
                stack[-1] *= current_number
            elif last_operator == '/':
                stack[-1] = int(stack[-1] / current_number)  # Use int() to truncate towards zero
            
            current_number = 0
            last_operator = char
    
    # Handle the last number
    if last_operator == '+':
        stack.append(current_number)
    elif last_operator == '-':
        stack.append(-current_number)
    elif last_operator == '*':
        stack[-1] *= current_number
    elif last_operator == '/':
        stack[-1] = int(stack[-1] / current_number)  # Use int() to truncate towards zero
    
    return sum(stack)

# Write a function to find the square root of a number without using the pow function.
def square_root(n):
    # Use binary search to find the square root
    if n < 0:
        return None  # Square root of negative number is not defined
    
    left, right = 0, n
    
    while left <= right:
        mid = (left + right) // 2
        square = mid * mid
        
        if square == n:
            return mid
        elif square < n:
            left = mid + 1
        else:
            right = mid - 1
    
    return right  # The integer part of the square root

c10=square_root(17)  # Output: 4
print(c10)



    
    


    


    


    
    


    