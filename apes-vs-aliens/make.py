import re,csv
s=open('/workspace/games/cat-runner-licence/index.html').read()
def R(a,b,cnt=1):
    global s
    assert a in s,a[:50]; s=s.replace(a,b) if cnt==0 else s.replace(a,b,cnt)
rows=list(csv.DictReader(open('/workspace/venture/game/reverso-assets/manifest.csv')))
apes=[r['image_file'] for r in rows if r['type']=='ape']; apes.insert(0,apes.pop(apes.index('reversoz-6809.png')))
aliens=[r['image_file'] for r in rows if r['type']=='alien']
s=re.sub(r'<title>[^<]*</title>','<title>Apes vs Aliens – Whisker Parade (PRIVATE TEST)</title>',s)
s=re.sub(r'<script type="application/ld\+json">.*?</script>','',s,flags=re.S)
R("SAVEK='whiskerParade.save.v2',SAVEK1='whiskerParade.save.v1'","SAVEK='apesVsAliens.save.v1',SAVEK1='apesVsAliens.save.v0'")
R("function cat(x,y,s,c,ph,i){","function cat_old(x,y,s,c,ph,i){")
R("function mouse(x,y,s,ph){","function mouse_old(x,y,s,ph){")
R("function drawDog(z){","function drawDog_old(z){")
R("function drawDuchess(z){","function drawDuchess_old(z){")
R("text(o.n+' mice'","text(o.n+' aliens'")
R("function bossName(){return curL&&curL.den===3?'DUCHESS FLUFFINGTON':'RACCOON BOSS'}","function bossName(){return 'LAO MEGA'}")
R("FUR[c.i%FUR.length],anim*12+c.i)","FUR[c.i%FUR.length],anim*12+c.i,c.i)")
for a,b in [('RACCOON BOSS','LAO MEGA'),('Raccoon Boss','LAO Mega'),('raccoon boss','LAO Mega boss'),('Raccoon Den','Alien Base'),('raccoon','alien boss'),('DUCHESS FLUFFINGTON','LAO MEGA'),('Duchess Castle','Mothership'),('Duchess','LAO Mega'),('BIG CAT','BIG APE')]: s=s.replace(a,b)
s=s.replace('drawLAO Mega','drawDuchess');s=s.replace('kittens','apes').replace('Kittens','Apes').replace('Whisker Parade','Apes vs Aliens')
new=r"""
const HD='heads/',APES=%s,ALIENS=%s,IMG={};
function himg(f){let m=IMG[f];if(!m){m=new Image();m.src=HD+f;IMG[f]=m}return m}
// simple runner: legs+arms swing with ph, head = NFT portrait disc
function runner(x,y,s,ph,head,body,dark,hs){const sw=Math.sin(ph),b=Math.abs(Math.cos(ph))*1.5*s;
 ctx.lineCap='round';ctx.strokeStyle=dark;ctx.lineWidth=2.6*s;
 for(const k of[1,-1]){ctx.beginPath();ctx.moveTo(x+k*1.5*s,y-7*s-b);ctx.lineTo(x+k*1.5*s+sw*k*3.5*s,y-3.5*s-b+Math.max(0,sw*k)*1.5*s);ctx.lineTo(x+k*1.5*s+sw*k*2.5*s,y);ctx.stroke()}// legs
 ctx.fillStyle=body;rr(x-4*s,y-15*s-b,8*s,9*s,3*s);ctx.fill();ctx.lineWidth=1*s;ctx.stroke();// torso (squash)
 ctx.lineWidth=2*s;for(const k of[1,-1]){ctx.beginPath();ctx.moveTo(x+k*4*s,y-13.5*s-b);ctx.lineTo(x+k*5.5*s-sw*k*3*s,y-9*s-b);ctx.stroke()}// arms
 const r=(hs||7)*s,hy=y-15*s-b-r*.8,m=himg(head);
 if(m.complete&&m.naturalWidth){ctx.drawImage(m,x-r,hy-r,2*r,2*r)}else{ctx.fillStyle=body;ctx.beginPath();ctx.arc(x,hy,r,0,7);ctx.fill()}
 ctx.lineWidth=1*s;ctx.beginPath();ctx.arc(x,hy,r,0,7);ctx.stroke()}
const ABODY=['#7a4a2a','#3b5998','#2e8b57','#8e44ad','#c0392b'];
function cat(x,y,s,c,ph,i){i=i|0;runner(x,y,s,ph,APES[i%%APES.length],ABODY[i%%5],'#2a1a10',i===0?8:7)}
let _mi=0;function mouse(x,y,s,ph){const i=Math.floor(Math.abs(ph))%%ALIENS.length;runner(x,y,s*1.1,ph,ALIENS[(i*7)%%ALIENS.length],'#4caf50','#1b3d1b',6.5)}
function bossFig(x,y,w,fl){ctx.save();const s=w/28;if(fl)ctx.translate(Math.sin(anim*80)*3,0);runner(x,y,s,anim*9,'boss-lao-mega-1.png',fl?'#c0392b':'#222','#000',8.5);ctx.restore()}
function drawDog(z){drawDog_old(z)}
function drawDuchess(z){drawDuchess_old(z)}
"""%(apes,aliens)
s=s.replace("function button(",new+"function button(",1)
for nm in ['drawDog_old','drawDuchess_old']:
    a=s.index('function '+nm+'(');b=s.index('\nfunction',a+5);f=s[a:b]
    p0=f.index('const p=proj(0,z),w=RW*');p1=f.index('const bw=Math.max(80,w*.9)')
    seg=f[p0:p1];hdr=seg[:seg.index(';')+1]
    f=f[:p0]+hdr+"bossFig(x,y,w,dogFlash>0);"+f[p1:]
    s=s[:a]+f+s[b:]
exec(open('patch2.py').read())
# test hook
i=s.rindex('</script>')
s=s[:i]+"window.__av={startLevel,get st(){return st},set st(v){st=v},LEVELS,get dist(){return dist},get count(){return count},setTx(v){tx=v},step(dt){update(dt)},get bossHp(){return bossHp},get ph(){return bossPh},get warn(){return dogWarn},auto(){const n=objs.find(o=>o.t==='g'&&!o.used);if(n){const a=applyOp(n.ops[0],count),b=applyOp(n.ops[1],count);tx=a>=b?-.5:.5}}};\n"+s[i:]
open('index.html','w').write(s)
