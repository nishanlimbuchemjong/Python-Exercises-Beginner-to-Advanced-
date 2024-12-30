"""
Write a program that simulates a simple traffic light system. Based on the input color ("red", "yellow", "green"), display the appropriate action (e.g., "Stop", "Caution", "Go")
"""
traffic_light = input("Enter color (Red or Yellow or Green): ").strip().lower()
print(traffic_light)

if traffic_light == 'red':
    print("Stop")
elif traffic_light == 'yellow':
    print("Caution")
elif traffic_light == 'green':
    print("Go")
else:
    print("Choose among three colors (Red or Green or Yellow)")
