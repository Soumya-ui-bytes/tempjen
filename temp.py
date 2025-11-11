# Temperature Classification Program

# Accept temperatures from user input
temperatures = input("Enter temperatures separated by space: ")
temperatures = [float(temp) for temp in temperatures.split()]

# Classify temperatures
for temp in temperatures:
    if temp < 15:
        classification = "Cold"
    elif 15 <= temp <= 30:
        classification = "Normal"
    else:
        classification = "Hot"

    print(f"Temperature: {temp}°C - {classification}")