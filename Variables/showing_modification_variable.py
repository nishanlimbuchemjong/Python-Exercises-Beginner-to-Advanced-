"""
Assign the same value to three variables (p, q, r) and show that modifying q does not change the value of p or r.
"""
# assigning same value to multiple variables
p = q = r = 50
print(f"Initial values of p, q, and r:")
print("value of p = ", p)
print("Value of q = ", q)
print("Value of r = ", r)

# changing the value of p variable:
p = 60
print(f"\nAfter changing the value of p = {p}, we get")
print("value of p = ", p)
print("Value of q = ", q)
print("Value of r = ", r)