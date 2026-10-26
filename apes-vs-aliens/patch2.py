# --- v2 additions (26 Oct 16:55) ---
s=re.sub(r'<title>[^<]*</title>','<title>Apes vs Aliens</title><meta name="robots" content="noindex,nofollow">',s)
s=re.sub(r'<meta name="description"[^>]*>','',s)
R("function lidUp(){return ","function lidUp(){return false&&")
R("function napUp(){return ","function napUp(){return false&&")
R("let dogWarn=0,","let bossPh=1,throwT=1.5,dogWarn=0,")
R(" const bossZ=dogZ-dist;\n"," const bossZ=dogZ-dist;\n if(!surv&&bossHp>0&&dogSet&&bossZ<44){const f=bossHp/bossMax;bossPh=f>.66?1:f>.25?2:3;if(bossPh===1){if(dogWarn<=0)dogCD=Math.max(dogCD,.6);throwT-=dt;if(throwT<=0){throwT=2.4;const z=dogZ-1.5;if(z-dist>5){const n=3+lvl*2;objs.push(Object.assign({z,used:false,max:1+lvl*.4},M(n,1+lvl*.4)));pops.push({txt:'ALIENS INCOMING!',x:0,z:Math.min(bossZ,18),t:1,c:'#39ff14'})}}}else if(bossPh===3)dogCD-=dt*1.2}\n")
s=s.replace("ctx.fillStyle='#ff4136';ctx.beginPath();ctx.moveTo(p1.x","ctx.fillStyle='#39ff14';ctx.beginPath();ctx.moveTo(p1.x")
R("const s=w/28;if(fl)","const s=w/28;if(!surv&&dogSet)text(bossPh===1?'PHASE 1: ALIEN THROW':bossPh===2?'PHASE 2: BEAM!':'PHASE 3: FURY!',x,y+16,Math.max(12,15*w/100),bossPh===3?'#ff4136':'#39ff14');if(fl)")
R("runner(x,y,s,anim*9,'boss-lao-mega-1.png'","runner(x,y,s,anim*(bossPh===3?20:9),'boss-lao-mega-1.png'")
R("runner(x,y,s*1.1,ph,","runner(x,y,Math.max(s*1.4,2.2),ph,")
# space background
a=s.index('function drawSky(){');b=s.index('\nfunction',a+5)
s=s[:a]+r"""function drawSky(){const hz=H*.28;let g=ctx.createLinearGradient(0,0,0,hz);g.addColorStop(0,'#0b0628');g.addColorStop(.7,'#2a1260');g.addColorStop(1,'#5b2a86');ctx.fillStyle=g;ctx.fillRect(0,0,W,hz+1);
 ctx.fillStyle='#fff';for(let i=0;i<40;i++){const x=(i*97.3)%W,y=(i*53.7)%hz,t=.5+.5*Math.sin(anim*3+i);ctx.globalAlpha=.3+.7*t;ctx.fillRect(x,y,1.6,1.6)}ctx.globalAlpha=1;
 ctx.fillStyle='#ff9f43';ctx.beginPath();ctx.arc(W*.78,hz*.45,Math.min(W,H)*.07,0,7);ctx.fill();ctx.strokeStyle='#ffd29a';ctx.lineWidth=3;ctx.beginPath();ctx.ellipse(W*.78,hz*.45,Math.min(W,H)*.12,Math.min(W,H)*.025,-.3,0,7);ctx.stroke();
 const ux=((anim*30)%(W+120))-60,uy=hz*.25+Math.sin(anim*2)*6;ctx.fillStyle='#9be7ff';ctx.beginPath();ctx.ellipse(ux,uy-6,12,9,0,0,7);ctx.fill();ctx.fillStyle='#8a8fa8';ctx.beginPath();ctx.ellipse(ux,uy,28,8,0,0,7);ctx.fill();ctx.fillStyle='#39ff14';for(const d of[-16,0,16]){ctx.beginPath();ctx.arc(ux+d,uy+2,2.5,0,7);ctx.fill()}
 ctx.fillStyle='#3d1f5c';ctx.beginPath();ctx.moveTo(0,hz);for(let x=0;x<=W;x+=W/8)ctx.lineTo(x,hz-18-14*Math.sin(x*.013+1));ctx.lineTo(W,hz);ctx.fill();
 ctx.fillStyle='#4e8a3a';ctx.fillRect(0,hz,W,H);ctx.fillStyle='#437a31';for(let k=0;k<12;k++){const z=k*8-(dist||0)%8;if(z<-3)continue;const p=proj(-1.6,z);ctx.fillRect(0,p.y,W,Math.max(1,3*p.s))}
}"""+s[b:]
a=s.index('function tree(x,y,s,k){');b=s.index('\nfunction',a+5)
s=s[:a]+"function tree(x,y,s,k){ctx.fillStyle=k%2?'#b388ff':'#39ffb0';ctx.strokeStyle='#1a0f2e';ctx.lineWidth=1.2*s;for(const [dx,h] of [[-5,22],[0,32],[6,18]]){ctx.beginPath();ctx.moveTo(x+dx*s-4*s,y);ctx.lineTo(x+dx*s,y-h*s);ctx.lineTo(x+dx*s+4*s,y);ctx.closePath();ctx.fill();ctx.stroke()}}"+s[b:]
R("text('WHISKER',W/2,ty,ts,'#ffdc00');text('PARADE',W/2,ty+ts*1.05,ts,'#ff7eb6')","text('APES',W/2,ty,ts,'#ffdc00');text('vs ALIENS',W/2,ty+ts*1.05,ts*.85,'#39ff14')")
s=s.replace("Grow your parade!","Grow your ape army!").replace("'Cat Tree'","'Ape Lab'")
