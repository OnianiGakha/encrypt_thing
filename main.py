import random
import math
generated = False
grid_layout = []
proper_layout = ""
input_layout = []
print("""
generate - Generates a new grille
rotate - Rotates the current grille
encrypt - Encryps a message into the current grille
""")
while True:
    b = input("Input: ")
    i=0
    proper_layout = ""
    used = []
    def generate():
        def ogg(num):
            numx = num%8
            if used == []:
                return True
            numy = math.floor(num/8)
            for p in used:
                px = p%8
                py = math.floor(p/8)
                #print("NUM = " + str(num) + " " + str(numx + 1) + " " + str(numy + 1))

                if (numy == 7-py and numx == 7-px) or (numx == 7 - px and numy == py) or (numy == 7 - py and numx == px) or (numx == py and numy == 7 - px) or (numy == px and numx == 7 - py):
                    return False
                #else:   
                    #print("P = " + str(p) + " " + str(px + 1) + " " + str(py + 1))
            return True
        for i in range(0,64):
            input_layout.append("▨")
            grid_layout.append("▨") 
        for b in range(0,16):
            rand = random.randint(0,63)    
            while True:
                if used.__contains__(rand): 
                    rand = random.randint(0,63)
                else:
                    if ogg(rand) == True:
                        break
                    else:
                        rand = random.randint(0,63)
            input_layout[rand] = "*"
            grid_layout[rand] = "*"
            used.append(rand)


    def encrypt(msg,new):
        msg = list(msg)
        l = 0
        for j in grid_layout:
            if j == "*" or j!="*" and j!="▨":
                if msg != []:
                    if new == True:
                        input_layout[l] = msg[0]
                        msg.remove(msg[0])
                    else:
                        input_layout[l] = msg[0]
                        msg.remove(msg[0])
                else:
                    input_layout[l] = "▨"
            l+=1

    def rotate():
        for i in range(0,64):
            if grid_layout[i] == "*":
                
                grid_layout[i] = "▨"
                ix = i%8
                iy = math.floor(i/8)
                
                newy = ix

                
                newx = 7 - iy
                grid_layout[newy * 8 + newx] = "l"
            
        for k in range(0,64):
            if grid_layout[k] == "l":
                grid_layout[k] = "*"

    if b == "generate":
        input_layout = []
        grid_layout = []
        generate()
        generated = True
    
    if b == "rotate":
        rotate()

    if b == "encrypt" and generated == True:
        msg = input("Encrypt: ")
        encrypt(msg,True)

    proper_layout = ""
    for g in range(0,len(input_layout)):
        i+=1
        if grid_layout[g] == "*":
            if input_layout[g] != "▨":

                if i == 8 :
                    proper_layout += str(input_layout[g]) + "\n"
                    i=0
                else:
                    proper_layout += str(input_layout[g]) + " "
            else:

                if i == 8 :
                    proper_layout += "*" + "\n"
                    i=0
                else:
                    proper_layout += "*" + " "
        else:
            if i == 8 :
                proper_layout += "▨" + "\n"
                i=0
            else:
                proper_layout += "▨" + " "
        
    if b == "help":
        print("""
        generate - Generates a new grille
        rotate - Rotates the current grille
        encrypt - Encryps a message into the current grille
        """)
    else:
        if proper_layout != "":
            print(proper_layout)
        else:
            print("You need to generate a grille first with the 'generate' command")

    #print(input_layout)
    #print(grid_layout)