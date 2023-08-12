COLOR_CODES = {"absolute zero": "#0048ba",
               "acid green": "#b0bf11",
               "aliceblue": "#f0f8ff",
               "amber": "#ffbf00",
               "amethyst": "#9966cc",
               "antiquewhite": "#faebd7",
               "aqua": "#00ffff",
               "apricot": "#fbceb1",
               "army green": "#4b5320",
               "azure1": "#f0ffff",
               "azure2": "#e0eeee",
                }
def get_colour(colour_name):
    return COLOR_CODES.get(colour_name.lower(), "Unknown color")


print("Available colours: ")
for colour_name in COLOR_CODES:
    print(colour_name)

while True:
     user_input = input("Please enter you want to colour name: ").lower()
     if user_input == " ":
          break

     colour_code  = get_colour(user_input)
     print(f"The colour code for {user_input.capitalize()} is {colour_code}")
