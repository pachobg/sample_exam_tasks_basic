country = input()
tool = input()

evaluation = 0

difficulty = 0
performance = 0

if country == "Russia":
    if tool == "ribbon":
        difficulty = 9.100
        performance = 9.400
        evaluation = difficulty + performance
    elif tool == "hoop":
        difficulty = 9.300
        performance = 9.800
        evaluation = difficulty + performance
    elif tool == "rope":
        difficulty = 9.600
        performance = 9.000
        evaluation = difficulty + performance
elif country == "Bulgaria":
    if tool == "ribbon":
        difficulty = 9.600
        performance = 9.400
        evaluation = difficulty + performance
    elif tool == "hoop":
        difficulty = 9.550
        performance = 9.750
        evaluation = difficulty + performance
    elif tool == "rope":
        difficulty = 9.500
        performance = 9.400
        evaluation = difficulty + performance
elif country == "Italy":
    if tool == "ribbon":
        difficulty = 9.200
        performance = 9.500
        evaluation = difficulty + performance
    elif tool == "hoop":
        difficulty = 9.450
        performance = 9.350
        evaluation = difficulty + performance
    elif tool == "rope":
        difficulty = 9.700
        performance = 9.150
        evaluation = difficulty + performance

points_to_20 = 20 - evaluation
percent_to_20 = (points_to_20 / 20) * 100

print(f"The team of {country} get {evaluation:.3f} on {tool}.")
print(f"{percent_to_20:.2f}%")
