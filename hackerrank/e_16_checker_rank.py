if __name__ == "__main__":
    test = int(input())
    for i in range(0,test):
        get = int(input())
        numbers = [int(i) for i in input().split()]
        res = get
        ot = "Yes"
        i = 0
        while i < res -1 and numbers[i]>=numbers[i+1]:
            i+=1
        while i < res - 1 and numbers[i]<=numbers[i+1]:
            i+=1
        print("Yes" if i ==res -1 else "No")
