import random
import string

class passgenerator:
    def __init__(self):
        def func1(lenght):
            c = []
            cb = []
            nums = []
            spec = []
            passwd = []
            schar = r"!@#$%^&*()_+=-]['\"./,"
            for i in schar:
                spec.append(i)
            textier = open("passwords.txt","a")

            try:
                int(lenght)
                for i in string.ascii_lowercase:
                    c.append(i)
                for i in string.ascii_uppercase:
                    cb.append(i)
                for i in string.digits:
                    nums.append(i)
                for i in range(0,int(lenght)):
                    passwd.append(random.choice([c[random.randint(0,len(c)-1)],
                                             cb[random.randint(0,len(cb)-1)],
                                             nums[random.randint(0,len(nums)-1)],
                                             spec[random.randint(0,len(spec))-1]]))
                    passwd[0:len(passwd)] = [''.join(passwd[0:len(passwd)])]
                textier.write(f"{passwd}\n")

            except ValueError:
                print("Only integer !!")

        gg = input('How many password you want? ')
        lenght = input("how many elems you want in your password? ")
        try:
            int(gg)
            int(lenght)
            var = int(lenght)
            for i in range(0,int(gg)):
                func1(var)
        except ValueError:
            print("Please only integer! =)")

passgenerator()

'''
Fragast company creating this one (MIT License)
'''
