import random

def main():
    ## hello world
    print("hello world")
    challege1()
    challenge2()
    
def challege1():
    ##Challenge 1 -affirmation
    nameInput = input("Enter your name please: ")
    affirmations = ["you are doing a good job", "you are loved", "you are not an imposter", "you belong", "you are a hardworker", "you deserve to be happy"]
    randomNum = random.randint(0,5)
    print(nameInput + ", "+affirmations[randomNum])

def challenge2():
    ##Challenge 2 - Don Quixote
    with open('Level1Challenges/Challenge2.txt', encoding='utf8') as f:
        data = f.read()
    length = len(data)
    challege_2_count_part_1 = 0
    check1 = "Don Quixote"
    count1 = data.count(check1)
    count2 = data.count("DON QUIXOTE")
    stringUpperCase = data.upper()
    count3 = stringUpperCase.count("DON QUIXOTE")
    str1 = str(count1)
    str2 = str(count2)
    str3 = str(count3)
    sum = count1 + count2 + count3
    sumStr = str(sum)

    print("Count 1 = " + str1 +"\n"+ 
          "Count 2 = " + str2 +"\n"+
            "Count 3 = " + str3 +"\n" +
            "Sum of counts is " + sumStr)
    
def challege3():
    
main()