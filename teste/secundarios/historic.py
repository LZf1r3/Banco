def historic():
    with open("teste/textos/withdraw.txt","r") as usos:
            for linha in usos.readlines():
                print(linha)

if __name__ == "__main__":
     historic()