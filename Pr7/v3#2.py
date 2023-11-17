s='меня зовут андрей'
ws=s.split()
r=''.join([''.join(sorted(w)) for w in ws])
print(r)
