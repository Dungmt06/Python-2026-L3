def remove_dollar_sign(s):
    return s.replace("$", "")

text = input("Enter a string: ")
result = remove_dollar_sign(text)

print(f"Result: {result}")