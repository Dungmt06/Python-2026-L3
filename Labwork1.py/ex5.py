colors = ["Blue", "Green", "Red", "Yellow", "Orange"]
favorite_color = input("What is your favorite colors? ").strip()
if favorite_color in colors:
    index = colors.index(favorite_color)
    print(f"Your color is at index {index} in the list")
else:
    print("Sorry, I could not find your color")