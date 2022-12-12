"""
hex_colours
Estimate: 10 minutes
Actual:   8 minutes
"""

color = {"Amber": "#ffbf00", "Amethyst": "#9966cc", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb",
         "AntiqueWhite2": "#eedfcc",
         "AntiqueWhite3": "#cdc0b0"}
print(color)

color_code = input("Enter a color name: ").upper()

while color_code != " ":
    if color_code in color:
        print(color[color_code])

    else:
        print("invalid color code")

    color_code = input("Enter a color name: ").upper()