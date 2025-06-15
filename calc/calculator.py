def stringcalculator(numbers):
    if numbers=="":
        return 0
    elif len(numbers)==1:
        return int(numbers)
    else:
        result=0
        delim=","
        if numbers[1]!=",":
            delim="\n"
        n=numbers.split(delim)
        for i in n:
            result+=int(i)
        return result
    