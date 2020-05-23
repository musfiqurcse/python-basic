if __name__ == "__main__":
    tcase = int(input())
    pcase = [ int(i) for  i in input().split(' ')]
    leng = len(pcase) + 1
    items = [0]*leng
    for i in pcase:
        items[i-1] +=1
    for i in items:
        print(i)