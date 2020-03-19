inti =int(input())
named_cases ={}
for _ in range(0,inti):
    i = input().strip()
    if i not in named_cases:
        named_cases[i] = 1
    else:
        named_cases[i]+=1
print(len(named_cases))
#printing dictionary values in space // it will not print the keys of dictionary
#don't use index ( it will become the code slow.)
print(*named_cases.values())
