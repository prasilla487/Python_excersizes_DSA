classes = (
('V', 1),
('VI', 1),
('V', 2),
('VI', 2),
('VI', 3),
('VII', 1),
)

from collections import defaultdict
l = classes
d = defaultdict(list)
for c, r in l:
    d[c].append(r)

print(d)

def count():
    for clas, roll in d.items():
        d[clas] = (len(roll))
    print(d)

count()

