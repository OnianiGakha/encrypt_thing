import random
import math
generated = False
grid_layout = []
proper_layout = ""
while True:
    b = input()
    i=0
    proper_layout = ""
    used = []
    def generate():
        def ogg(num):
            numx = num%8
            if used == []:
                return True #7 0   0 7
            numy = math.floor(num/8)
            for p in used:
                px = p%8
                py = math.floor(p/8)
                print("NUM = " + str(num) + " " + str(numx + 1) + " " + str(numy + 1))

                if (numy == 7-py and numx == 7-px) or (numx == 7 - px and numy == py) or (numy == 7 - py and numx == px) or (numx == py and numy == 7 - px) or (numy == px and numx == 7 - py):
                    return False
                else:
                    print("P = " + str(p) + " " + str(px + 1) + " " + str(py + 1)) # 2 7    0 2
            return True
        for i in range(0,64):
            grid_layout.append("#") #1 6    6 1
        for b in range(0,16):
            rand = random.randint(0,63)    
            while True:
                if used.__contains__(rand): #6 0    7 6  
                    rand = random.randint(0,63)
                else:
                    if ogg(rand) == True:
                        break
                    else:
                        rand = random.randint(0,63)
            grid_layout[rand] = "!"
            used.append(rand)


    def encrypt(msg,new):
        msg = list(msg)
        l = 0
        for j in grid_layout:
            if j == "!" or j!="!" and j!="#":
                if msg != []:
                    if new == True:
                        grid_layout[l] = msg[0]
                        msg.remove(msg[0])
                    else:
                        grid_layout[l] = msg[0]
                        msg.remove(msg[0])
                else:
                    grid_layout[l] = "#"
            l+=1

    if b == "generate":
        generate()
        generated = True
        msg = input("encrypt: ")
        encrypt(msg,False) #1 7    8 2
    
    if b == "rotate" and generated == True:
        pass

    if b == "encrypt" and generated == True:
        msg = input("encrypt: ")
        encrypt(msg,True)

    proper_layout = ""
    for g in grid_layout:
        i+=1
        if i == 8:
            proper_layout += str(g) + "\n"
            i=0
        else:
            proper_layout += str(g) + " "
        
        

    print(proper_layout)
    print(grid_layout)