# 比較兩句哪個字一樣，只算英文小寫，空格則跳一行，注意算字的重複次數和排序順序
# 例如: aau 和 iau 會印出 au ， ayau 和 taauyr 會印出 aau
# v1
while True:
    try:
        a = list(input().strip())
        b = list(input().strip())
        temp = []
        if len(a) != 0 and len(b) != 0:
            a.sort()
            b.sort()
            for i in range(97, 123):  # a~z的ascii
                if chr(i).isalpha():
                    Acount = a.count(chr(i))
                    Bcount = b.count(chr(i))
                    if Acount > Bcount and Acount != 0 and Bcount != 0:
                        for j in range(Bcount):
                            temp.append(chr(i))
                    elif Acount <= Bcount and Acount != 0 and Bcount != 0:
                        for j in range(Acount):
                            temp.append(chr(i))
            if len(temp) != 0:
                temp.sort()
                for i in range(len(temp) - 1):
                    print(temp[i], end="")
                print(temp[-1])
            else:
                print()
        else:
            print()
    except EOFError:
        break

# v2
while 1:
    try:
        a = input()
        b = input()
        countA, countB = [0] * 26, [0] * 26
        for i in range(len(a)):
            countA[ord(a[i]) - 97] += 1
        for i in range(len(b)):
            countB[ord(b[i]) - 97] += 1
        for i in range(26):
            if countA[i] <= countB[i]:
                print(chr(i + 97) * countA[i], end="")
            else:
                print(chr(i + 97) * countB[i], end="")
        print()
    except EOFError:
        break
