print("Verification palindrome")
while True:
    
    pal = str(input("Saisissez un mot:  ")).lower().replace(" ", "")

    lap = ""
    for car in pal:
        lap = car + lap
        
    if lap == pal:
        print("Votre mot est un palindrome")
        break
    else:
        print("Votre mot n'est pas un palindrome")
