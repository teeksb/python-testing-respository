users = [
    {"user_id": 1, "device": "Mobile", "step": "Signup"},
    {"user_id": 1, "device": "Mobile", "step": "Verify Email"},
    {"user_id": 1, "device": "Mobile", "step": "Complete Profile"},
    {"user_id": 1, "device": "Mobile", "step": "Activated"},

    {"user_id": 2, "device": "Desktop", "step": "Signup"},
    {"user_id": 2, "device": "Desktop", "step": "Verify Email"},

    {"user_id": 3, "device": "Mobile", "step": "Signup"},
    {"user_id": 3, "device": "Mobile", "step": "Verify Email"},
    {"user_id": 3, "device": "Mobile", "step": "Complete Profile"},

    {"user_id": 4, "device": "Desktop", "step": "Signup"},

    {"user_id": 5, "device": "Mobile", "step": "Signup"},
    {"user_id": 5, "device": "Mobile", "step": "Verify Email"},
    {"user_id": 5, "device": "Mobile", "step": "Complete Profile"},
    {"user_id": 5, "device": "Mobile", "step": "Activated"},
]


#Filter - Find all users who reached Activated
def get_activated_users():
    activated_users = set()
    for u in users:
        if u["step"] == "Activated":
            activated_users.add(u["user_id"])
    return activated_users

print(f"1.) {get_activated_users()}")

print ("================================================")

# Transform - Get unique user IDs who signed up.
def get_signup_users ():
    signup_users = set()
    for u in users:
            if u["step"] == "Signup":
                signup_users.add(u["user_id"])
    return signup_users

print(f"2.) {get_signup_users()}")
print ("================================================")

# Aggregate: Calculate overall activation rate.
def get_activation_rate():
     activated = get_activated_users()
     signed_up = get_signup_users()
     return len(activated) /len(signed_up)

print("Length of activavted users is:", len(get_activated_users()))
print("Length of signed up users is:", len(get_signup_users()))
print(f"3.) Activavtion rate is :{get_activation_rate()}")

print ("================================================")

# Group by : Compare activation by device.
def activation_by_device():
    device_stats = {}
    for u in users:
    
        device = u["device"]

        if device not in device_stats:
            device_stats[device] = {
            "signup": set(),
            "activated": set()
            }

        if u["step"] == "Signup":
                device_stats[device]["signup"].add(u["user_id"])

        if u["step"] == "Activated":
                device_stats[device]["activated"].add(u["user_id"])

    return device_stats

print(f"4a) {activation_by_device()}")


   
def activation_rate_by_device():
    stats = activation_by_device()
    results = {}

    for device in stats:
        signup_count = len(stats[device]["signup"])
        activated_count = len(stats[device]["activated"])


        rate = activated_count / signup_count if signup_count > 0 else 0

        results[device] = {
             "signup" : signup_count,
             "activated" : activated_count,
             "activation_rate" : rate
        }

    return results

print(f"4b.) {activation_rate_by_device()}")

print ("================================================")

# FIND THE PROBLEM (MIN/MAX thinking)

def worse_activation_rate():
     device_stats = activation_by_device()
     worst_device = None
     worst_rate = 1
     for device in device_stats:
          signup_count = len(device_stats[device]["signup"])
          activated_count = len(device_stats[device]["activated"])

          rate = activated_count / signup_count if signup_count  > 0 else 0

          print(device, "activation rate:", rate)

          if rate < worst_rate:
               worst_rate = rate
               worst_device = device
     return worst_device, worst_rate    

print("Worst device:", worse_activation_rate())
 

 # Insight Summary :  Desktop users have lower activation , i'd investigate desktop UX.
     


     