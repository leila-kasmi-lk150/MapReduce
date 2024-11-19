from collections import defaultdict, Counter

with open("purchases.txt", "r") as f:
    data = [line.strip().split("\t") for line in f]

sales_store = defaultdict(lambda: {'sales': 0.0, 'count': 0})
for record in data:
    store = record[2] 
    sales = float(record[4]) 
    
    sales_store[store]['sales'] += sales
    sales_store[store]['count'] += 1

print("Sales for each store:")
for store, values in sales_store.items():
    print(f"{store}: {values['count']}: {values['sales']}")

print("Average sales for each store:")
for store, values in sales_store.items():
    avg_sales = values['sales'] / values['count']
    print(f"{store}: {avg_sales}")

product_counter = Counter()
for record in data:
    product = record[3]  
    product_counter[product] += 1

most_requested_product = product_counter.most_common(1)
print("\nMost requested product:")
print(f"{most_requested_product[0][0]} : {most_requested_product[0][1]}")

payment_counter = Counter()

for record in data:
    payment_method = record[5]
    payment_counter[payment_method] += 1

most_used_payment_method = payment_counter.most_common(1)
print("\nMost used payment method:")
print(f"{most_used_payment_method[0][0]} : {most_used_payment_method[0][1]}")
