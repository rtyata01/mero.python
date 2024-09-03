list_numbers = []
for x in range(10):
    list_numbers.append(x)
    
print('count:', len(list_numbers))
print(list_numbers)

list_numbers_alternative = [x for x in range(10)]
print('count:', len(list_numbers_alternative))
print(list_numbers_alternative)

list_odd_numbers = [x for x in range(10) if not x % 2 == 0]
print(list_odd_numbers)

list_even_numbers = [x for x in range(10) if x % 2 == 0]
print(list_even_numbers)


list_words = ['HELLO', 'HaPPy', 'sad' , 'Smile']
lowercase_words = [word.lower() for word in list_words]
print(lowercase_words)

prefix_words = [word for word in lowercase_words if word.startswith('h')]
print(prefix_words)
