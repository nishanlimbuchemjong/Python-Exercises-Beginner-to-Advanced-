"""
Write a program to compute the compound interest using mathematical operators.
"""
def calculate_simple_interest(p, t, r):
    return (p * t * r) / 100

principle = 145000  # rs 
rate = 5    # percentage
time = 2    # year

result = calculate_simple_interest(principle, rate, time)

print(f"Priciple: Rs. {principle}\nRate = {rate}%\nTime = {time} years")
print(f"\nSimple Interest = Rs. {result}/-")