type = 'a'

def check_var(variable):
    match variable:
        case 'a' | 'b' as value:
            print("value is:", value)
        case 'c' as value:
            print("value is:", value)
        case value:
            print("value is:", value)
            
check_var(type)

my_tuple = (1, 3, 4, 5)

match my_tuple:
    case (1, 3, 5, 7):
        print('Sequence 1')
    case (1, 2, 3, 4):
        print('Sequence 2')
    case (1, (2| 3), 4, 5):
        print('Sequence 3')
        
        
name = input("Enter your name: ").strip().title()

match name:
    case "Harry" | "Hareather":
        print("Hareather")
    case "Daniel":
        print("Danel")
    case _:
        print("Who?")
        
