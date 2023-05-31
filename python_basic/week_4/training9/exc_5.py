from collections import defaultdict
# pozwala uniknac warunkow logicznych i skrocic kod
bill_items = [
    ['Tom', 'Calamari', 6.00],
    ['Tom', 'American Hot', 11.50],
    ['Tom', 'Chocolate Fudge Cake', 4.45],
    ['Clare', 'Bruschetta Originale', 5.35],
    ['Clare', 'Fiorentina', 10.65],
    ['Clare', 'Tiramisu', 4.90],
    ['Rich', 'Bruschetta Originale', 5.35],
    ['Rich', 'La Reine', 10.65],
    ['Rich', 'Honeycomb Cream Slice', 4.90],
    ['Rosie', 'Garlic Bread', 4.35],
    ['Rosie', 'Veneziana', 9.40],
    ['Rosie', 'Tiramisu', 4.90],
]
bill = defaultdict(lambda: {"dish": [], "price": 0.00})
for name, dish, price in bill_items:
    bill[name]["dish"].append(dish)
    bill[name]["price"] += price

for name, details in bill.items():
    print(f"{name}:")
    print(f" Dishes: {', '.join(details['dish'])}")
    print(f" Prices: {details['price']}")

# lambda = w zeszycie mam