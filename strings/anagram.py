#an anagram is having same characters in both string , the format can vary
#prasilla and pillasra both are angrams

def checkAnagram(str1, str2):
    if len(str1) != len(str2):
        return False
    
    for element in str1:
        count1 = str1.count(element)
        print('count1 {0}'.format(count1))
        count2 = str2.count(element)
        print('count2 {0}'.format(count2))
        if count1 != count2:
            return False

    return True


s1 = "ALLERGY"
s2 = "allergic"
v = checkAnagram(s1,s2)
if v:
    print('yes')
else:
    print('no')
            
        
