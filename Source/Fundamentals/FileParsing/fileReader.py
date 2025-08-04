import os

# Get the script's directory
script_dir = os.path.dirname(__file__)  

# Construct the full path to names.txt
file_path = os.path.join(script_dir, "names.txt")

names = []
with open(file_path, "r") as file:
    for line in file:  # sorted(file), can also read in sorted order.
        print(f"{line.strip()}")
        names.append(line.rstrip())

print()
for name in sorted(names, reverse = True):
    print(f"{name}")