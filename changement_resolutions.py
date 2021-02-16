resolutions = [(2560,1440),(1920,1080),(1600,900),(1536,864),(1366,768),(1280,720)]
size=(1280,720)
answer=-1
print("Press a number from 0-5 to select a resolution.")
print("Possible choices:")
for x in range(len(resolutions)):
    print(x,resolutions[x],";", sep=' ',end=" ")
print("\n",sep='',end="")
while answer < 0 or answer > 5 or answer!=int(answer):
    answer=int(input("answer here: "))
size=resolutions[answer]
print(size)