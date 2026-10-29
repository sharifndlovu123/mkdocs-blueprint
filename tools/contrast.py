def lum(h):
    h=h.lstrip('#'); r,g,b=[int(h[i:i+2],16)/255 for i in (0,2,4)]
    f=lambda c: c/12.92 if c<=.03928 else ((c+.055)/1.055)**2.4
    return .2126*f(r)+.7152*f(g)+.0722*f(b)
def ratio(a,b):
    la,lb=sorted([lum(a),lum(b)],reverse=True); return (la+.05)/(lb+.05)
def mix(fg,bg,a):  # fg over bg at alpha a
    f=[int(fg.lstrip('#')[i:i+2],16) for i in (0,2,4)]; b=[int(bg.lstrip('#')[i:i+2],16) for i in (0,2,4)]
    return '#%02x%02x%02x'%tuple(round(a*x+(1-a)*y) for x,y in zip(f,b))
S={'light':dict(paper='#e6f0f8',ink='#0b2d52',red='#d9480f',muted='#4b6a8a',panel='#d7e6f2'),
   'dark':dict(paper='#0f3d6e',ink='#e8f1fb',red='#ffd166',muted='#9fbad8',panel='#134a80')}
for n,t in S.items():
    print(f"\n== {n} ==")
    # panel actually used at ~70% over paper in cards; table/code use panel directly
    cardbg=mix(t['panel'],t['paper'],.7)
    for label,fg,bg in [('body ink / paper','ink','paper'),('muted / paper','muted','paper'),('link red / paper','red','paper'),
        ('ink / panel (code, th)','ink','panel'),('muted / panel','muted','panel'),('red / panel','red','panel'),
        ('paper on red (bubble)','paper','red')]:
        r=ratio(t[fg],t[bg]); print(f"{label:28s} {r:5.2f}  {'AA ok' if r>=4.5 else ('AA large only' if r>=3 else 'FAIL')}")
    r=ratio(t['red'],cardbg); print(f"{'red / card bg':28s} {r:5.2f}")
    r=ratio(t['muted'],cardbg); print(f"{'muted / card bg':28s} {r:5.2f}")
    # decorative rules vs paper (non-text 3:1)
    for label,a in [('rule2 (45%) vs paper',.45),('rule (20%) vs paper',.2)]:
        c=mix(t['ink'],t['paper'],a); print(f"{label:28s} {ratio(c,t['paper']):5.2f}")
