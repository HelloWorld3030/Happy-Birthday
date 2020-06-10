name = input("Enter your name: ")
year = int(input("Enter your year of birth: "))
age = 2020 - year
print("Happy birthday, ",name,"!", sep = '')
print("Happy ",age,"!", sep = '')
a = len(name) - 4 
if a>0:
    print(" __  __")
    print("|  \/  |")
    print("|",name,"|", sep='')
    print(" \    /")
    print("  \  /")
    print("   \/")
else :
    print(" __  __")
    print("|  \/  |")
    print("|",name,"|")
    print(" \    /")
    print("  \  /")
    print("   \/")
