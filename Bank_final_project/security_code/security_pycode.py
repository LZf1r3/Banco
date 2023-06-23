if __name__ == "__main__":
    print("!!Get the hell out of here!!")
    exit()
else:
    import random 
    security_code_soft = random.randrange(0,10000000000001)
    security_code = security_code_soft
    with open("Bank_final_project/security_code/security_code.txt","a") as security:
        security.write(f"{security_code}\n")

