def string():
    vowels = 0
    str1 = input(str("Enter a string: "))
    r = "AEIOU"
    old = str1.upper()
    new = " "
    for e in old:
        if e not in r:
            new = new + e
        else:
            new = new + "*"
    print("Old String: ", old)
    print("New String: ", new)
    for i in str1:
        if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
            vowels = vowels + 1
    print("Number of vowel characters: ", vowels)
string()
