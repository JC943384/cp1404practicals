COLOUR_CODES = {"absolute zero": "#0048ba",
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
    return COLOUR_CODES.get(colour_name.lower(), "Unknown colour")


while True:
    # Prompt user to enter a color name
    input_colour = input("Enter a color name (or blank to stop): ").strip()

    # Check if user wants to stop the loop
    if input_colour == "":
        break

    # Look up the color code and display the result
    colour_code = get_colour(input_colour)
    print(f"The hexadecimal color code for {input_colour} is {colour_code}")




