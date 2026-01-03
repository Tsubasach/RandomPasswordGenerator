import random
import string
def randompassword():
    randNUM=(random.choice(range(10,20)))
    j=0
    strin=""
    while j<randNUM:
        strin+=random.choice((string.ascii_letters + string.punctuation + string.digits))
        j+=1
    return strin

def main():
    print(randompassword())
    print("Password Length is:",len(randompassword()))

if __name__ == "__main__":
    main()