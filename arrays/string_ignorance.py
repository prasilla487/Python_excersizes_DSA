#ignore the letter already seen and print first space ignore second space
#a = "it is a long day dear" op: it sa longdy ear"

def ignorance(ar):
    seen = []
    new = ""
    for let in ar:
        let = let.lower()
        if let in seen:
            seen.remove(let)
            continue
        else:
            new += let
            seen.append(let)
    return new

#a = "It is a long day Dear."
a = 'Geeks for geeks'
print(ignorance(a))
