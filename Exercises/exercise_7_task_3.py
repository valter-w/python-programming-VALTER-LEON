import random

def get_random_key(dictionary):
    keys = list(dictionary.keys())
    print(f"{keys = }")
    random_index = random.randint(0, len(keys) - 1)
    print(f"{random_index = }")
    random_key = keys[random_index]
    print(f"{random_key = }")
    return dictionary[random_key]

def get_random_set_item(set):
    return random.sample(set, 1)[0]

swedish_colors = {
    "black": "svart",
    "grey": "grå",
    "white": "vit",
    "red": "röd",
    "orange": "orange",
    "yellow": "gul",
    "green": "grön",
    "blue": "blå",
    "purple": "lila",
    "pink": "rosa",
    "brown": "brun",
}

answered_colors = 0
correct_answers = 0

# this list keeps track of 
colors_to_guess = list(swedish_colors.keys())

#print(colors_to_guess)

#print(list(swedish_colors.keys()))
#random_key = get_random_key(swedish_colors)
#print(f"{random_key = }")

print("Enter an empty value at any time to exit stop playing.")

# keeps track of last color to translate to avoid repetition
# when all colors in the dictionary have been guessed.
last_color = None

while True:
    # if user has translated all colors in swedish_colors, start over
    if len(colors_to_guess) == 0:
        colors_to_guess = list(swedish_colors.keys())

    random_color = random.choice(colors_to_guess)

    # make sure user is not asked to translate the same color as last one
    while random_color == last_color:
        random_color = random.choice(colors_to_guess)

    last_color = random_color
    colors_to_guess.remove(random_color)

    entered_color = input(f"Type the Swedish word for {random_color}: ")
    entered_color = entered_color.strip()
    entered_color = entered_color.lower()

    if len(entered_color) == 0 or entered_color == "quit":
        break
    else:
        answer = swedish_colors[random_color]
        answered_colors += 1
        if entered_color == answer:
            print("Correct!")
            correct_answers += 1
        else:
            msg = "Wrong answer. The Swedish word for "
            msg += f'{random_color} is "{answer}".'
            print(msg)

    #print(f"{random_color = }")
    #print(f"{colors_to_guess = }")
if answered_colors > 0:
    msg = f"You got {correct_answers} out of {answered_colors} correct answers. "
    msg += f"That is {correct_answers / answered_colors:.0%}."
    print(msg)
    print("Thank you for playing!")
else:
    print("Exiting game.")