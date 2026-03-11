products = {
    "bread": 2.20,
    "milk": 1.50,
    "eggs": 3.40
}

def total_sum(products):
    total = 0
    for key,value in products.items():
        total += value
    return total

def most_expensive(products):
    return max(products.items(), key=lambda x: x[1])
print(total_sum(products))
print(most_expensive(products))
