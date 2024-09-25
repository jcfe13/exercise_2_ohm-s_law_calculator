# 1. Ask the user what they want to calculate in Ohm's Law
print("Welcome to simple Ohm's Law Calculator:")
print("1. Voltage(V)\n2. Current(I)\n3. Resistance(R)")
missing_value = input("\nSelect the number that you want to calculate: ")
# 2. If the user input '1', it will ask to input values to solve voltage (V = I * R)
if missing_value == "1":
    current = float(input("\nInput your Current: "))
    resistance = float(input("Input your Resistance: "))
    voltage = current * resistance
    print(f"The value of voltage is: {round(voltage, 2)} Volt/s")
# 3. If the user selects '2', proceed to calculate current (I = V / R)
elif missing_value == "2":
    voltage = float(input("\nInput your Voltage: "))
    resistance = float(input("Input your Resistance: "))
# 4. If the user selects '3', proceed to calculate resistance (R = V / I)
# 5. If the user enters anything other than '1', '2', or '3', display an error
