# This is a simple Pokemon Madlib.
# Ash's Pikachu MadLib
# From the book, coded by Dev Sodagar.

print("Welcome to this little MadLib. The MadLib itself has been")
print("taken from the Pokemon MadLib book. It's coded by Dev.\n")


def article(item):
    # Determine if indefinite article should be a or an
    vowel = {"a", "e", "i", "o", "u"}
    if item[0].lower() in vowel:
        var = "an"
    else:
        var = "a"
    return var


adjective_one = input("Please type an adjective: ")
# adjective_two = input("Please type an adjective:")
# adjective_three = input("Please type an adjective:")
# adjective_four = input("Please type an adjective:")
noun_one = input("Please type a noun: ")
plural_noun_one = input("Please type a plural noun: ")
# plural_noun_two = input("Please type a plural noun: ")
colour_one = input("Please type a colour: ")
number_one = input("Please type a number: ")
body_part_one = input("Please type a body part (yes that one if you must): ")
silly_word_one = input("Please type a silly word (sigh, go on then...): ")
person_one = input("Please type a person's name: ")
verb_one = input("Please type a verb: ")
# verb_two = input("Please type a verb: ")

print("I'm sure you've heard of Pikachu, Ash's " + adjective_one + " Pokemon. Like most Pikachu, it has a plump,\n"
      + adjective_one + " body with a red " + noun_one + " on each cheek. It has " + colour_one +
      " tips on it's ears and " + number_one + " stripes on\nits " + body_part_one +
      ". Ash's Pikachu may have evolved from " + article(adjective_one) + " " + adjective_one +
      " Pichu, and could evolve (if it wanted) into a Raichu,\nwhich is quite like " + article(adjective_one) + " "
      + silly_word_one + ". But Ash's Pikachu likes itself just as it is. Professor " + person_one +
      " gave Pikachu to Ash when he was ten,\nand they've been best " + plural_noun_one +
      " ever since. Even though Pikachu is very cute, it can also " + verb_one +
      " really well.\nUsing the power of electricity, Pikachu can do all sorts of " + plural_noun_one +
      "to defeat other Pokemon in battle.\nSome of its " + adjective_one +
      "moves include Thunder Shock, Iron Tail, and " + verb_one + "!\nSo, Rockruff, Bounsweet or " + person_one +
      ": You'd better watch out. Pikachu is here! Pika-pika!")
