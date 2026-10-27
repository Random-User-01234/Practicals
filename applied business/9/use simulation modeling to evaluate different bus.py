import random

random.seed(10)

customer_demand = [random.randint(50, 100) for i in range(5)]

prices = [100, 120, 150]

cost = 60

print("Customer Demand:", customer_demand)

for price in prices:
    total_revenue = 0
    total_profit = 0
    total_sales = 0

    for demand in customer_demand:
        if price == 100:
            sales = demand
        elif price == 120:
            sales = int(demand * 0.8)
        else:
            sales = int(demand * 0.6)

        revenue = sales * price
        profit = sales * (price - cost)

        total_sales += sales
        total_revenue += revenue
        total_profit += profit

    print("\nProduct Price: Rs.", price)
    print("Total Sales:", total_sales)
    print("Total Revenue: Rs.", total_revenue)
    print("Total Profit: Rs.", total_profit)