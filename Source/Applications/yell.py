def main():
    yell("This", "Is", "CAT", "meou", "Meou")


def yell(*words):
    # map feature or function
    uppercased = map(str.upper, words)
    print("Map function:", *uppercased)
    
    # Lambda map
    uppercased = map(lambda word: word.upper(), words)
    print("Lambda Map function:", *uppercased)
    
    # list comprehensions
    uppercased = [word.upper() for word in words]
    print("List comprehensions:", *uppercased)
    
    # Generator expressions
    uppercased = (word.upper() for word in words)  # Generator expression
    print("Generator expressions:", *uppercased)

if __name__ == "__main__":
    main()