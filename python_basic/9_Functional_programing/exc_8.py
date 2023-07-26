orders = [
    ["34587", "Learning Python, Mark Lutz", 4, 40.95],
    ["98762", "Programming Python, Mark Lutz", 5, 56.80],
    ["77226", "Head First Python, Paul Barry", 3, 32.95],
    ["88112", "Einführung in Python3, Bernd Klein", 3, 24.99]
]


def calculate_invoice(order):
    order_id, product, quantity, price = order
    total = quantity * price
    if total < 100:
        total += 10
    return (order_id, round(total, 2))


invoice = list(map(calculate_invoice, orders))

print(invoice)
