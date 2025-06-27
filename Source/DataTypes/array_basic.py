def main():
    num = get_integer_input()
    
    if num:
        print_square(num)
        print_square_blocks(num)

def get_integer_input() -> int:
    try:
        num = int(input("Enter number: "))
        return num
    except ValueError:
        print(f"The input value is not an integer.")
        
def print_square(size):
    # For each row 
    for i in range(size):
        # For each column
        for j in range(size):
            print(f"#", end="")
        print() # blank line
        
def print_square_blocks(size):
    for i in range(size):
        print_column(i)
        print() # blank line
        
def print_column(width):
    print(f"#" * width)
        
denominations = [1, 9, 6]
print (f"original order: {denominations}")

denominations.sort()
print (f"increasing order: {denominations}")

denominations.sort(reverse = True)
print (f"descending order: {denominations}")

main()