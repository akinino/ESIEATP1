class Syracuse_POO : 
    def syracuse(n):
        with open("outputSyracuse.txt","w") as fichier_txt:
            fichier_txt.write("la valeur de y est %d \n" %n)
            rs = []
            while n != 1:
                fichier_txt.write("%d "%n)
                if (n%2==1) :
                    n = n*3+1
                else:
                    n = n // 2

y = int(input("Donnez la valeur de y = "))
Syracuse_POO.syracuse(y)
