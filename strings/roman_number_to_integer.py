def convert(s):
    roman = {"M": 1000, "D": 500, "C":100, "L": 50, "X":10, "V":5, "I":1}
    i = 0
    n = len(s)
    value = 0
    while i < n:
        if (i+1) < n:
            value1 = roman[s[i]]
            value2 = roman[s[i+1]]
            if value1 >= value2:
                value += value1
                i = i +1
            else:
                value -= value1
                i = i + 1
        else:
            value += roman[s[i]]
            i +=1

    print(value)
            
            
        


s = "V"
convert(s)
