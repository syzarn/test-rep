# 'Hello World' program [Importing Array, Math, NumPy, Random & Inflect Module and installing ipython, mypy & black for future usage]
import array
import math
import numpy as np
import random as ran
import inflect
i = inflect.engine()
print("Hello Nunu!")

# Escape sequence [\]
print("Hello \"Guddu\"\nHello \"Gwi\"")
print("My name is Walter Hartwell White. I live at 308 Negra Arroyo Lane, Albuquerque, New Mexico, 87104. This is my confession. If you're watching this tape, I'm probably dead, murdered by my brother-in-law Hank Schrader. Hank has been building a meth empire for over a year now and using me as his chemist. Shortly after my 50th birthday, Hank came to me with a rather, shocking proposition. He asked that I use my chemistry knowledge to cook methamphetamine, which he would then sell using his connections in the drug world. Connections that he made through his career with the DEA. I was... astounded, I... I always thought that Hank was a very moral man and I was... thrown, confused, but I was also particularly vulnerable at the time, something he knew and took advantage of. I was reeling from a cancer diagnosis that was poised to bankrupt my family. Hank took me on a ride along, and showed me just how much money even a small meth operation could make. And I was weak. I didn't want my family to go into financial ruin so I agreed. Every day, I think back at that moment with regret. I quickly realized that I was in way over my head, and Hank had a partner, a man named Gustavo Fring, a businessman. Hank essentially sold me into servitude to this man, and when I tried to quit, Fring threatened my family. I didn't know where to turn. Eventually, Hank and Fring had a falling out. From what I can gather, Hank was always pushing for a greater share of the business, to which Fring flatly refused to give him, and things escalated. Fring was able to arrange, uh I guess I guess you call it a \"hit\" on my brother-in-law, and failed, but Hank was seriously injured, and I wound up paying his medical bills which amounted to a little over $177,000. Upon recovery, Hank was bent on revenge, working with a man named Hector Salamanca, he plotted to kill Fring, and did so. In fact, the bomb that he used was built by me, and he gave me no option in it. I have often contemplated suicide, but I'm a coward. I wanted to go to the police, but I was frightened. Hank had risen in the ranks to become the head of the Albuquerque DEA, and about that time, to keep me in line, he took my children from me. For 3 months he kept them. My wife, who up until that point, had no idea of my criminal activities, was horrified to learn what I had done, why Hank had taken our children. We were scared. I was in Hell, I hated myself for what I had brought upon my family. Recently, I tried once again to quit, to end this nightmare, and in response, he gave me this. I can't take this anymore. I live in fear every day that Hank will kill me, or worse, hurt my family. I... All I could think to do was to make this video in hope that the world will finally see this man, for what he really is.")

'''
YES DAVID BOWIE IS THE EMBODIMENT OF SEX AND MANLYNESS, HE IS A SEX GOD AND I HAVE COME TO A CONCLUSION THAT NO LIVING BEING WOULDN'T HAVE SEXUAL INTEWCOUWSE WITH BOWIE, YES STRAIGHT MEN SECRETLY WANT THIS INCLUDING LESBIANS.
DAVID BOWIE IS THE GOD OF SEX. DAVID BOWIE IS ALL, BOWIE IS EVERYTHING, BOWIE IS LOVE, BOWIE IS LIFE.
'''

''' Docstrings are strings used right after the definition of a function, method, class, or module.
    Otherwise, it's a comment.
    Access doctrings by __doc__ attribute
'''

# Print statements [',', sep (def:[spc]), end (def:\n)]
print("Hey,", 25, 9, sep="~", end="!\n")
print("How are you?")

# Variables
# Variable Declaration Styles

style_snake_case = "All letters of the word are lowercase but delimited by an underscore (used to name function, method)"
styleCamelCase = "First letter of the first word in the identifier is lower case, while the first letter of every subsequent word is uppercase (rarely used in python. used in java to denote function, method, variable, propertie, attribute)"
StylePascalCase = "First letter of every word in the identifier is uppercase (used to name class, interface*, namespace* *->in C#)"
STYLE_SCREAMING_SNAKE_CASE = "All letters of the word are uppercase but delimited by an underscore (used to denote constant)"
STYLEUPPERCASE = "Everything in uppercase (used to denote constant)"
stylelowercase = "Everything in lowercase"
_private = "Starting with an underscore (used to declare private variable)"

print(style_snake_case)
print(styleCamelCase)
print(StylePascalCase)
print(STYLE_SCREAMING_SNAKE_CASE)
print(STYLEUPPERCASE)
print(stylelowercase)
print(_private)

# Invalid Variable Declaration Styles

# 259_BigDipper = "Starting with number"
# station-to-station = "Containing hyphen"
# in_the_flesh? = "Ending with special characters"
# $EXHIBIT = "Starting with special characters"
# the fragile = "Containing spaces"

# Data Types
# Primitive Data Types
string = "mammamia"  # Text Type
print(string, type(string))

integer = 3  # Numeric Type
print(integer, type(integer))

float = 3.14  # Numeric Type
print(float, type(float))

π = math.pi  # Numeric Type [Math Module]
print(π, type(π))

boolean = False  # Boolean Type
print(boolean, type(boolean))

# Non-Primitive Data Types
complex = complex(25, 9)  # Numeric Type
print(complex, type(complex))

lists = ["alef", "bet", "gimel"]  # Sequence Type (Mutable)
print(lists, type(lists))

tuple = ("dalet", "he", "vav")  # Sequence Type (Immutable)
print(tuple, type(tuple))

set = {"zayin", "chet", "tet"}  # Set Type (Mutable)
print(set, type(set))

frozen_set = frozenset({"yod", "kaf", "lamed"})  # Set Type (Immutable)
print(frozen_set, type(frozen_set))

dictionary = {"name": "Antor",  # Mapping Type (Mutable)
              "age": 20,
              "human": False}
print(dictionary, type(dictionary))

range = range(9)  # Sequence Type
print(range, type(range))

array = array.array("I", [3, 6, 9])  # Sequence Type [Array Module]
print(array, array.typecode, type(array))
print("<typecodes:\nb-int~signchar\nB-int~unsignchar\nu-wchar_t~unicode\nh-int~signshort\nH-int~unsignshort\ni-int~signint\nI-int~unsignint\nl-int~signlong\nL-int~unsignlong\nq-int~signlonglong\nQ-int~unsignlonglong\nf-float~float\nd-double~double>")

bytes = b"ninchnails"  # Binary Type
print(bytes, type(bytes))

byte_array = bytearray(6)  # Binary Type
print(byte_array, type(byte_array))

memory_view = memoryview(byte_array)  # Binary Type
print(memory_view, type(memory_view))
print(memory_view[5])  # Access memory view's nth index
# Error in next 2 lines
# print(bytes(memory_view[0:2]))  # Create byte from memory view
# print(list(memory_view[0:3]))  #Create list from memory view

none = None  # None Type
print(none, type(none))

# Arithmetic Operators
w: int = -25
x: int = 24
y: int = 11
z: int = -9
print(x + y)  # Addition
print(x - y)  # Substraction
print(x * y)  # Multiplication
print(x / y)  # Division
print(x % y, x % z, w % y, w % z)  # Modulus (Floored)
print(x ** y)  # Exponentiation
print(x // y)  # Floor Division
print(math.log(x))  # Natural Logarithm
print(math.sqrt(y))  # Square Root
print(math.floor(x / y))  # Floor Function
print(math.ceil(x / y))  # Ceiling Function
print(math.fabs(x / y))  # Absolute Value
print(math.factorial(x - y))  # Factorial
print(math.fmod(x, y), math.fmod(x, z),
      math.fmod(w, y), math.fmod(w, z))  # Modulus (Truncated)
print(math.remainder(x, y), math.remainder(x, z),
      math.remainder(w, y), math.remainder(w, z))  # Remainder

# Number System
print(hex(x))
print(oct(y))
print(bin(z))

# String Formatting
j007: str = "james"
b007: str = "bond"
# % operator
print("my name is %s, %s %s" % (b007, j007, b007))
# str.format()
print("my name is {}, {} {}".format(b007, j007, b007))
print("my name is {1}, {2} {0}".format(b007, b007, j007))
print("my name is {b}, {j} {b}".format(j=j007, b=b007))
# F-String (Literal String Interpolation)
print(f"my name is {b007}, {j007} {b007}")
# Practice String Formatting
order_no = hex(ran.randint(1, 999999))
serial_no: int = ran.randint(1, 99)
customer_name: str = "Anupa"
pizza_name: str = "Pineapple Pizza"
amount: int = 1
size: int = 16
toppings: list = ["mushroom", "chicken", "beef", "octopus"]
crust: str = "thin"
extra_cheese: bool = True
caviar: bool = True
saffron: bool = True
poop_sprinkles: bool = False
price: float = 420.69
order_details: str = f"""
Order No. #{(order_no[2:])}
Serial No. #{serial_no}
Hello, {customer_name},
We've recieved your order of {i.number_to_words(amount)} {size}" {pizza_name} with {toppings} toppings and {crust} crust. We need a bit more info about your pizza.
Do you want extra cheese? {extra_cheese}
Do you want Caviar? {caviar}
Do you want Saffron? {saffron}
Do you want Poop Sprinkles? {poop_sprinkles}
Your bill amount is {price}$ only.
Please pay via Cash/bKash/Card. (We'd also accept your own used panties as currency, if and only if you're a female)
Thank you for staying with us. Never dare to come again!
"""
print(order_details)
