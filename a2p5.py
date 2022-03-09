#problem 5
def count(string):
    vowels=0
    consonents=0
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    for i in string:
        if i in vowels:
            vowels+=1
        else:
            consonents+=1
    return vowels


count("apple")
