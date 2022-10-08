# todo 1. Напишіть програму, яка прочитає два рядки тексту з клавіатури і виведе на екран літери, які є одночасно і в першому, і в другому рядку. Наприклад, для рядків «Hello» та «World» на екрані мають бути літери «l» та «o».
# user_string_1 = list(input("Enter first word "))
# user_string_2 = list(input("Enter second word "))
user_string_1 = list("Hello")
user_string_2 = list("World")
print(set(user_string_1) & set(user_string_2))
# todo 2. Напишіть програму, яка згенерує два списки. Один із числами кратними 3, інший із числами кратними 5.


def gener(num, lim):
    list_ = [i for i in range(1,lim + 1) if not i % num]
    return list_


# todo 3. Створіть список із числами, які є в обох списках. Напишіть функцію, яка поверне максимальне число зі списку чисел.
limit = 1000
print(max(set(gener(3, limit)) & set(gener(5, limit))))

# todo 4. Реалізуйте функцію, параметрами якої є два числа та рядок. Повертає вона конкатенацію рядка із сумою чисел.
def combine(num1, num2, str_):
    return str_ + str(num1 + num2)


print(combine(5, 7, "Sum = "))


# todo 5. Реалізуйте функцію, яка малює на екрані прямокутник із зірочок «*». Її параметрами будуть цілі числа, які описують довжину та ширину такого прямокутника.
def char_rectangle(hight, wight, ch):
    print(ch * wight + '\n' + (ch + ((wight - 2) * " ") + ch + '\n') * (hight - 2) + ch * wight)


char_rectangle(10, 10, "*")


# todo 6. Напишіть функцію, яка реалізує лінійний пошук елемента у списку цілих чисел. Якщо такий елемент у списку є, то поверніть індекс, якщо ні, то поверніть число «-1».
def find_index(list_, num):
    for idx, i in enumerate(list_):
        if num == i:
            return idx
    else:
        return -1


print(find_index(range(100),51))
print(find_index(range(100),101))


# todo 7. Напишіть функцію, яка поверне кількість слів у текстовому рядку.
def how_meny_words(text):
    return len(text.split())


print(how_meny_words("Напишіть функцію, яка поверне кількість слів у текстовому рядку"))