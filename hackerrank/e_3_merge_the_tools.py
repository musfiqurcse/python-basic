def merge_the_tools(string, k):
    for i in range(0,len(string), k):
        iter_a = ''
        for l in string[i:i+k]:
            if l not in iter_a:
                iter_a =iter_a +l
        print(iter_a)
    

if __name__ == '__main__':