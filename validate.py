email = input("What's you email? ").strip()

if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")