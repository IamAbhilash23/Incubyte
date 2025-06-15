def stringcalculator(numbers):
    if numbers=="":
        return 0
    elif len(numbers)==1:
        return int(numbers)
    elif numbers[0] == "/":
        result=0
        delim=""
        l=numbers.split("\n")
        for i in range(2,len(l[0])):
            delim=delim+l[0][i]
        n=l[1].split(delim)
        for i in n:
            result+=int(i)
        return result
    else:
        result=0
        delim=","
        if numbers[1]!=",":
            delim="\n"
        n=numbers.split(delim)
        for i in n:
            result+=int(i)
        return result
    