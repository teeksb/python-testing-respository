#Format: String[start:end:step]
greeting = "Hello, good morning"


print(greeting[0:5])
print(greeting[::-1])
print(greeting[1:6])
print(greeting[:])
print(greeting[0:5:2])

username = "_+ tosinkasaba@gmail.com"
print("Username", username)
print("Username", username.strip("_+"))

username = " tosinkasaba@gmail.com "
print("Username", username.lstrip(""))

username = "+tosinkasaba@gmail.com"
print("+tosinkasaba@gmail.com".strip("+"))

username = "+teekasaba@gmail.com"
print(username.lstrip("2"))


first_name = "John"
last_name = "Doe"
score = 80
base_score= "out of 100"

full_name = first_name + " " + last_name
print("Full Name:",full_name)

print (first_name + " " + last_name + " scored " + str(score) + " " + base_score)


sentence = first_name + " " + last_name + " scored " + str(score) + " " + base_score
print(sentence)


sentence_f = f"{first_name} {last_name} scored {score} {base_score}"
print(sentence_f)


sentence_fa = "{lname} {fname} scored {sc} {bs}".format (
    fname="Tosin", lname = "Kasaba",sc =score, bs=base_score)
print(sentence_fa)


sentence_f = f"{12 * 4} {60} scored {"20"} {base_score}"
print(sentence_f)


