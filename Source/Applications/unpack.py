def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

print("1-integer-values:", total(100, 50, 25), "Knuts")

coinsList = [100, 50, 25]
print("2-list-values:", total(coinsList[0], coinsList[1], coinsList[2]), "Knuts")

# unpack list into individual numbers.
print("3-unpack-list:", total(*coinsList), "Knuts")

# named parameters
print("4-named-parameters:", total(knuts=25, sickles=50, galleons=100), "Knuts")

coinsDict = {"galleons": 100, "sickles": 50, "knuts": 25}
print("5-dictionary-values:", total(coinsDict["galleons"], coinsDict["sickles"], coinsDict["knuts"]), "Knuts")

# unpack dictionary, key and value
print("6-unpack-dictionary:", total(**coinsDict), "Knuts")


def print_arguments(*positional_args, **keyword_args):
    if positional_args:
        print("Positional:", positional_args)
    if keyword_args:
        print("Named:", keyword_args)
    
print_arguments(100, 50, 25)
print_arguments(coinsList)
print_arguments(coinsDict)
print_arguments(knuts=25, sickles=50, galleons=100)
