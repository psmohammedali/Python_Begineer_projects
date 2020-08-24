from time import sleep
import random

print("------------- Welcome to Ali's Dice Roll Simulator------------")
print()
sleep(1.0)
s = input("Press Y to roll (or) Press N to end: " )

s = s[0].lower()

while s == "y":
    temp = random.randint(1,7)
    if temp == 1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")

    elif temp == 2:
        print("[-----]")
        print("[ 0   ]")
        print("[     ]")
        print("[   0 ]")
        print("[-----]")

    elif temp == 3:
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[  0  ]")
        print("[-----]")

    elif temp ==4:
        print("[-----]")
        print("[ 0 0 ]")
        print("[     ]")
        print("[ 0 0 ]")
        print("[-----]")
    elif temp ==5:
        print("[-----]")
        print("[ 0 0 ]")
        print("[  0  ]")
        print("[ 0 0 ]")
        print("[-----]")

    elif temp ==6:
        print("[-----]")
        print("[0 0 0]")
        print("[     ]")
        print("[0 0 0]")
        print("[-----]")

    s = input("Press Y to roll (or) Press N to end: " )
else:
    print("You have entered N or any other key, So exited from the Roll dice Simulator")
    sleep(1)
    print("Thank you using Roll Dice Simulator")







