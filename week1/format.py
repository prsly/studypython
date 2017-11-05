# first
template = "%s - главное достоинство программиста. (%s)"
template % ("Лень", "Larry Wall")

# second
"{} не лгут, но {} пользуются формулами. ({})".format(
    "Цифры", "лжецы", "Robert A. Heinlein"
)

# third
"{num} Кб должно хватить для любых задач. ({author})".format(
    num=640, author="Bill Gates"
)

# fourth
subject = "оптимизация"
author1 = "Donald Knuth"

f"Преждевременная {subject} - корень всех зол. ({author1})"

# modifications
num1 = 8
f"Binary: {num1:#b}"

num2 = 2 / 3
print(num2)
print(f"{num2:.3f}")

# input
name = input("Введите ваше имя: ")

# bytes
example_bytes = b"Hello"

# encode / decode utf-8
example_string = "Привет"
encoded_string = example_string.encode(encoding="utf-8")
decoded_string = encoded_string.decode()
