

SECURE = (("i" , "1") , ("and" , "&") , ("s" , "$") , ("o" , "0"))

def secure(password):
    for a,b in SECURE:
        password = password.replace(a,b)
    return password 

if __name__ == "__main__":
    user_password = input("Enter a password: \n")   
    secured_password = secure(user_password)
    print(f"your secure password is:{secured_password}")
    