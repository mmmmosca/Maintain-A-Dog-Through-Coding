import sys
# commands: woof, bark, argh, rrrr, yawn, barf, howl, ruff, umph
file = open(sys.argv[1],"r")
cookies = 1
stack = []

for line in file:
    if "woof" in line:
        cookies += 1
    if line.startswith("bark"):
        reverse_number=str(line.replace("bark","").strip())[::-1]
        stack.insert(0,int(reverse_number))
        cookies-=1
    if "argh" in line:
        stack.reverse()
        cookies-=1
    if "rrrr" in line:
        print(chr(stack[0]),end='')
        cookies-=1
    if "ruff" in line:
        print(stack[0],end='')
        cookies-=1
    if "yawn" in line:
        stack.pop(0)
        cookies-=1
    if "barf" in line:
        stack.insert(0,int(input()))
    if "howl" in line:
        stack.insert(0,stack[0])
    if cookies <= 0:
        print("the dog won't answer you, no cookies, no program")
        break
    if "umph" in line:
        if len(stack) > 0:
            print("Your dog's exausted! Too much informations to remeber")
        else:
            break   