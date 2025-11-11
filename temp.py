import sys

# Temperature Classification Program

# Accept temperatures from command-line arguments
if len(sys.argv) < 2:
    print("Please provide temperatures as command-line arguments.")
    sys.exit(1)

temperatures = [float(temp) for temp in sys.argv[1:]]

# Classify temperatures
for temp in temperatures:
    if temp < 15:
        classification = "Cold"
    elif 15 <= temp <= 30:
        classification = "Normal"
    else:
        classification = "Hot"

    print(f"Temperature: {temp}°C - {classification}")