n = input()
string = input()
anton, danik = string.count("A"), string.count("D")
if anton == danik:
    print("Friendship")
elif anton > danik:
    print("Anton")
else:
    print("Danik")