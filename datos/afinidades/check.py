import sys,collections,re
ROSTER=[l.strip().split('|') for l in open('/home/claude/sociopolitica/datos/afinidades/raw/2623.txt') if not l.startswith('#')]
NAMES=[r[0] for r in ROSTER]
def load(f):
    lines=open(f).read().splitlines(); h=lines[0]
    m=re.search(r'default=(\w)',h); d=m.group(1) if m else None
    votes={n:d for n in NAMES} if d else {}
    bad=[]
    for l in lines[1:]:
        if not l.strip(): continue
        p=l.split('|'); n,v=p[0].strip(),p[-1].strip()
        if n not in NAMES: bad.append(n)
        votes[n]=v
    return h,votes,bad
if __name__=='__main__':
    for f in sys.argv[1:]:
        h,v,bad=load(f); c=collections.Counter(v.values())
        exp=dict(re.findall(r'\b(A|N|AB|AU)(\d+)',h.split('·')[-1]))
        ok = c.get('A',0)==int(exp.get('A',-1)) and c.get('N',0)==int(exp.get('N',-1)) and c.get('B',0)==int(exp.get('AB',0)) and c.get('X',0)==int(exp.get('AU',0))
        print(f,len(v),dict(c),exp,'OK' if ok and len(v)==72 and not bad else 'MISMATCH',bad)
