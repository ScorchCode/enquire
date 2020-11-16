from enquire import Enquire

enquire = Enquire()

print("DEMO of module enquire.py")
print("Enquire user input safely.")

print("\nEnquire Numbers\n")

print("Default range")
answ = enquire.number("A number between 0 and 9: ")
print(answ, "is okay\n")

print("Random range")
answ = enquire.number("A number between -5 and 5: ", allowed="-5_5")
print(answ, "is okay\n")

print("Arbitrary numbers")
answ = enquire.number("An even number between 2 and 10: ", allowed="2,4,6,8,10")
print(answ, "is okay\n")

print("Default value 5.")
answ = enquire.number("A number between 0 and 9: ", default="5")
print(answ, "is okay\n")


print("\nEnquire Letters\n")

print("Default range a..z, default input X")
answ = enquire.letter("A Letter: ", default="x")
print(answ, "yep, that's a letter\n")

print("Random range")
answ = enquire.letter("A Letter between A and M: ", allowed="a_m")
print(answ, "is okay\n")

print("Arbitrary letters, default input G")
arb = "J, U, G, S"
answ = enquire.letter(f"Choose one of these {arb}: ", allowed=arb, default="g")
print(answ, "is okay\n")

print("\nIf this was a quiz, you would be King!\n")
