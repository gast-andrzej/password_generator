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
        op = open("passwords.txt","r")
        for line in op:
            print(line[2:-3:])
        op.close()

def run():
    while True:
        passgenerator()
        print('\nGoodbye :)')

        x = str(input("you want delete folder with passwords? [Y] yes , [N] no "))
        if x.upper() == 'Y':
            b = open("passwords.txt","w")
            b.write("__")
            b.close()
        else:
            pass
        break



if __name__ == "__main__":
    run()

'''
Fragast company creating this code on MIT License
'''
