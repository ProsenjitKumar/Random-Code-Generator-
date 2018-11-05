import string, random
import sys

def random_code():
    x = "f739d638-dfa1-402a-a143-16dfb9a380ec"
    y = "93bbdfc7-cb10-423e-91c9-7b6aab474dd5"
    b = "402a"
    lol = sys.stdout.write(x)
    return lol

random_code()
#
# for item in range(1,100):
#     print item

# print("fhshih", end='-')
# print("Hi","Poftut",sep='')
#
# ch = ['a','b']
#
# strng = ""
# for i in range(97,123):
#     strng = strng + chr(i)
# print(strng)
# print(string.ascii_uppercase)
# print(string.ascii_letters)
#
# x = "93bbdfc7-cb10-423e-91c9-7b6aab474dd"
# value = random.choices(x, k=10)
# p = value.index(0)
# print(p)

def id_8(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def id_4_1(size=4, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def id_4_2(size=4, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def id_4_3(size=4, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def id_12(size=12, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
print("\n")
a = "-"
a_8 = id_8()
b_4 = id_4_1()
print(a_8+a+b_4)













