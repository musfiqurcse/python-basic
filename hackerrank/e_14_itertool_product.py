from itertools import product

if __name__ ==  "__main__":
    k =  [int(i) for i in input().split()]
    l = [ int(i) for i in input().split()]
    pro = list(product(k,l))
    final = ""
    for j in range(0,len(pro)):
        final +="({0}, {1})".format(pro[j][0],pro[j][1])
        if j+1 < len(pro):
            final+=" "
    print(final)
