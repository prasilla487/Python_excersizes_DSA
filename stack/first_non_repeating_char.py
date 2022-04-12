#find the first-non-repeating character in stream

max_char = 256

def find(s):
    inDll = [] * 256
    repeated = [False] * 256

    for x in s:
        print('reading {0} from stream'.format(x))
        if not repeated[ord(x)]:

            if x not in inDll:
                inDll.append(x)
            else:
                inDll.remove(x)
                repeated[ord(x)] = True

    if len(inDll) != 0:
        print("first non-repeating character is {}".format(inDll[0]))



find('geeksforgeeks')
    
