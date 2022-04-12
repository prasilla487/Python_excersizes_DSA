#check the given captial letter pattern is found in camelCase pattern

def camelCase(ar, pattern):
    for word in ar:
        i = 0
        j = 0
        flag = 0
        while i < len(word) and j < len(pattern):
            if word[i].isupper() and word[i] == pattern[j]:
                j +=1
            elif word[i].isupper() and word[i] != pattern[j]:
                flag = 1
                break
            
            i+=1
        if not flag:
            return word

    return 'No match found'

ar = ['WelcomeGeek', 'WelcomeToGeeksForGeeks', 'GeeksForGeeks']
p = 'WTF'
print(camelCase(ar, p))
        
        
