# Python checks top to bottom and stops at the first True.

# score = 75

# if score >= 90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# else:
#     print("Fail")


# light = "yellow"

light = input("What color is the traffic light?: ").lower()
print(light)

# allowed colors: red, yellow, green , blinking

if light =="red" or light =="yellow" or light =="green" or light == "blinking":
    if light == "green" or light =="blinking":
        print("Go")
    elif light =="yellow": #elif clause
        print("Slow down")
    else: #elif clause
        print("Stop")
else:
    print("Valid colors are red, green, and yellow ONLY!")


# OR

if light in ("red", "yellow", "green", "blinking"):
    if light in ("green", "blinking"):
        print("Go")
    elif light == "yellow":
        print("Slow down")
    else:
        print("Stop")
else:
    print("Valid colors are red, green, yellow, or blinking!")


# OR - Cleaner Code

if light in ("green", "blinking"):
    print("Go")
elif light == "yellow":
    print("Slow down")
elif light == "red":
    print("Stop")
else:
    print("Valid colors are red, yellow, green, or blinking!")


# if light == "green" or light == "blinking":
#     print("GO")
# elif light == "yellow":
#     print ("SLOW DOWN")
# else:
#     print("STOP")

# age = 20

# if age >= 18:
#     print("You are an adult")
# elif age >= 13:
#     print("You are a teenager")
# else:
#     print("You are a child")


# temperature = 15
# humidity = 30
# if temperature > 30 or humidity < 20:
#     print("Warning: Unusual weather condition detected!")
# else:
#     print ("Weather conditions are normal")