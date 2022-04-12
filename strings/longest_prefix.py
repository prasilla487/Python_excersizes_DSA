#find the longest prefix among all the given strings
#"geeksgeeks" "geek" "geed" "geer" op: gee

def long_prefix(a):
    n = len(a)
    result = 0
    min_length = min([ len(s) for s in a])
    prefix_word = ""
    for i in range(min_length, -1,-1):
        flag = 1
        prefix = a[0][:i]
        for j in a:
            if j[:i] != prefix:
                flag = 0
                break
        if flag and result < max(result, len(prefix)):
            result = max(result, len(prefix))
            prefix_word = prefix

    return result, prefix_word




s = ["apple", "apart", "appendix"]
print(long_prefix(s))
        
        
        
        

