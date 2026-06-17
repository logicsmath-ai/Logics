from pathlib import Path

W, H = 595, 842

def text(x, y, s, size=13, color="#222", weight="400", cls="hand"):
    return f'<text x="{x}" y="{y}" class="{cls}" font-size="{size}" font-weight="{weight}" fill="{color}">{s}</text>'

def rect(x, y, w, h, fill, stroke=None, r=7, dash=False):
    stroke = stroke or fill
    dash_attr = ' stroke-dasharray="5 4"' if dash else ''
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="1.5"{dash_attr}/>'

def line(x1, y1, x2, y2, color="#444", width=1.5, dash=False):
    dash_attr = ' stroke-dasharray="5 4"' if dash else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}" stroke-linecap="round"{dash_attr}/>'

def arrow(x1, y1, x2, y2, color="#444"):
    return line(x1, y1, x2, y2, color, 1.7) + f'<polygon points="{x2},{y2} {x2-7},{y2-4} {x2-7},{y2+4}" fill="{color}"/>'

pink="#eb2065"; blue="#1f69dc"; red="#dc323c"; green="#269650"; purple="#8246be"
lblue="#c6e1ff"; lpink="#ffcdda"; lgreen="#d2f2d2"; lpurple="#e1d2ff"; yellow="#ffee80"
parts=[]
parts.append(f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<style>
  .hand {{ font-family: "Comic Sans MS", "Trebuchet MS", "DejaVu Sans", sans-serif; font-variant-ligatures:none; }}
  .print {{ font-family: "DejaVu Sans", Arial, sans-serif; }}
  text {{ dominant-baseline: alphabetic; }}
</style>
<rect width="100%" height="100%" fill="white"/>
''')
parts += [line(297,50,297,803,"#e5e5e5",1), line(0,50,W,50,"#eeeeee",1), line(0,803,W,803,"#f2f2f2",1)]
parts += [text(20,39,"mock CSAT math / annotated",11,"#222","700","print"), text(290,825,"09",11,"#222","400","print")]

# Q30
parts += [text(42,100,"30",24,pink,"700"), text(75,97,"A²=B,  ab=0,  a+b≤0",12,"#333")]
parts += [rect(76,116,60,22,lblue), text(84,132,"ab=0",13,"#222","700"), rect(146,116,86,22,lpink), text(154,132,"a+b≤0",13,"#222","700"), rect(78,168,178,24,lgreen), text(88,185,"sum=-1, product=-8",13,"#222","700")]
parts += [arrow(122,140,68,220,blue), arrow(189,140,128,242,red)]
y=225
for s,c,w in [("A²=B",blue,"700"),("a₁₂≠0,  a₁₁+a₂₂=0",red,"400"),("a₁₁=0  →  A=[0 a₁₂; a₂₁ 0]","#222","400")]:
    parts.append(text(42,y,s,14,c,w)); y+=22
parts += [rect(42,y-5,188,25,lblue), text(50,y+12,"a₁₂² a₂₁² = -8",13,blue,"700")]; y+=31
parts += [rect(42,y-5,170,25,lpink), text(50,y+12,"a₁₂ + a₂₁ = 3",13,red,"700")]; y+=31
parts += [text(42,y,"a₁₂³+a₂₁³",14,purple,"700")]; y+=22
parts += [text(42,y,"=3³-3(-2)·3 = 45",14,"#222")]; y+=27
parts += [rect(42,y-8,80,28,yellow,"#d7bd35"), text(64,y+12,"45",16,"#111","700")]

# Q32
parts += [text(315,100,"32",24,pink,"700"), text(348,97,"|x-k|≤5,  x²-x-12&gt;0",12,"#333")]
parts += [rect(348,114,143,22,lblue), text(356,130,"k-5≤x≤k+5",13,"#222","700"), rect(348,144,120,22,lpink), text(356,160,"x&lt;-3 or x&gt;4",13,"#222","700")]
parts += [arrow(420,138,330,220,blue), arrow(410,166,450,220,red)]
y=220
parts += [text(318,y,"(i) k≤-1 : count &gt; 7  ✕",13,red)]; y+=26
parts += [line(333,y,558,y,"#555",2), text(350,y-6,"-3",10,"#333"), text(470,y-6,"k+5",10,blue), rect(398,y-14,72,14,"#ffd2dc",red,0)]; y+=45
parts += [text(318,y,"(ii) -1&lt;k&lt;2",13,purple,"700")]; y+=22
parts += [text(318,y,"k=0: {-5,-4} → -4  ✕",12,"#555")]; y+=20
parts += [rect(390,y-15,64,16,"#ffd2dc",red,0), text(318,y,"k=1: {-4,5,6} → 7  ○",12,green,"700")]; y+=30
parts += [text(318,y,"(iii) k≥2 : count &gt; 7  ✕",13,red)]; y+=42
parts += [rect(326,y-12,82,28,yellow,"#d7bd35"), text(344,y+8,"k=1",15,"#111","700"), text(430,y+8,"answer ④",13,green,"700")]

# Q31
parts += [text(42,452,"31",24,pink,"700"), text(75,449,"x²+3x-10&lt;0,  ax≥a²",12,"#333")]
parts += [rect(75,467,82,22,lblue), text(86,483,"-5&lt;x&lt;2",13,"#222","700"), rect(168,467,92,22,lpink), text(177,483,"4 integers",13,"#222","700")]
y=525
for s,c,w in [("x=-4,-3,-2,-1,0,1  (6)",blue,"400"),("a=0 → 6  ✕",red,"400"),("a&gt;0 → x≥a : 0 or 1  ✕",red,"400"),("a&lt;0 → x≤a",purple,"700")]:
    parts.append(text(42,y,s,13,c,w)); y+=23
parts += [rect(42,y-16,190,26,lpink), text(52,y+2,"need -4,-3,-2,-1",13,"#222","700")]; y+=34
parts += [text(42,y,"⌊a⌋=-1  →  -1≤a&lt;0",13,"#222")]; y+=30
parts += [rect(42,y-14,126,28,yellow,"#d7bd35"), text(54,y+7,"a=-1  (②)",15,"#111","700")]

# Q33
parts += [text(315,452,"33",24,pink,"700"), text(348,449,"a&lt;0,  (x-a)²&lt;a²,  x²+ax&lt;(a+1)x",10,"#333")]
parts += [rect(348,467,82,22,lblue), text(358,483,"2a&lt;x&lt;0",13,"#222","700"), rect(440,467,70,22,lpink), text(449,483,"a&lt;x&lt;1",13,"#222","700")]
y=525
for s,c,w in [("(x-a)²&lt;a²",blue,"400"),("x(x-2a)&lt;0 → 2a&lt;x&lt;0",blue,"400"),("x²+ax&lt;(a+1)x",purple,"400"),("(x-1)(x-a)&lt;0 → a&lt;x&lt;1",purple,"400")]:
    parts.append(text(318,y,s,13,c,w)); y+=23
ny=y+22
parts += [line(328,ny,563,ny,"#444",2), text(357,ny+20,"2a",10,blue), text(410,ny+20,"a",10,purple), text(463,ny+20,"0",10,red), text(523,ny+20,"1",10,green), rect(410,ny-18,53,13,lblue,blue,0)]
y=ny+55
parts += [text(318,y,"common:  a&lt;x&lt;0",14,green,"700")]; y+=25
parts += [text(318,y,"b=a,  b+1=0",13,"#222")]; y+=23
parts += [text(318,y,"a=-1, b=-1",13,"#222")]; y+=31
parts += [rect(318,y-14,126,28,yellow,"#d7bd35"), text(328,y+7,"a+b=-2  (⑤)",15,"#111","700")]

parts.append('</svg>')
Path('assets').mkdir(exist_ok=True)
Path('assets/handwritten_solutions_30_33.svg').write_text('\n'.join(parts), encoding='utf-8')
