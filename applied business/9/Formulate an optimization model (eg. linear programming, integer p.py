from scipy.optimize import linprog

profit = [-40, -30]

A = [
    [2, 1],
    [1, 2]
]

b = [40, 50]

result = linprog(
    profit,
    A_ub=A,
    b_ub=b,
    bounds=[(0, None), (0, None)],
    method="highs"
)

if result.success:
    product_A = result.x[0]
    product_B = result.x[1]
    maximum_profit = -result.fun

    print("Optimal Production Plan")
    print("-----------------------")
    print("Product A:", round(product_A, 2), "units")
    print("Product B:", round(product_B, 2), "units")
    print("Maximum Profit: ₹", round(maximum_profit, 2))
else:
    print("No optimal solution found.")