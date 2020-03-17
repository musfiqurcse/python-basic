import textwrap

def wrap(string, max_width):
    final_array = ''
    # range will loop till the length of string and the steps will be 4 (e.g. if max_width =4 then steps are i=0,4,8,12..>=len_of_string)
    for i in range(0,len(string),max_width):
        final_array = final_array+string[i:i+max_width]
        if i+max_width <len(string):
            final_array = final_array + '\n'
    return final_array

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
