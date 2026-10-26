const {chromium}=require('/workspace/games/pwtest/node_modules/playwright-core');const O='/workspace/venture/game/';
(async()=>{const b=await chromium.launch({executablePath:'/usr/bin/google-chrome',args:['--no-sandbox']});const errs=[];
const p=await b.newPage({viewport:{width:390,height:844}});p.on('pageerror',e=>errs.push(e.message));p.on('requestfailed',q=>errs.push('FAIL '+q.url()));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
await p.goto('file:///workspace/venture/game/apes-vs-aliens/index.html');await p.waitForTimeout(900);await p.screenshot({path:O+'apes-vs-aliens-v2-menu.png'});
const n=await p.evaluate(()=>window.__av.LEVELS.length);
for(let L=0;L<n;L++){
 await p.evaluate(L=>window.__av.startLevel(L),L);
 if(L===0){await p.evaluate(()=>{const g=window.__av;for(let i=0;i<60*8.2;i++){g.auto();g.step(1/60)}});await p.waitForTimeout(150);await p.screenshot({path:O+'apes-vs-aliens-v2-gameplay.png'})}
 const r=await p.evaluate(()=>{const g=window.__av;let k=0,ph={};let shot=false;while(g.st==='play'&&k<60*400){g.auto();g.step(1/60);k++;ph[g.ph]=1;if(!shot&&g.ph===2&&g.warn>0){shot=true;break}}return [g.st,Math.round(g.dist),Math.round(g.count),Math.round(g.bossHp),shot]},);
 if(L===1&&r[4]){await p.waitForTimeout(150);await p.screenshot({path:O+'apes-vs-aliens-v2-boss.png'})}
 const r2=await p.evaluate(()=>{const g=window.__av;let k=0,phs=new Set();while(g.st==='play'&&k<60*400){g.auto();g.step(1/60);k++;phs.add(g.ph)}return [g.st,Math.round(g.dist),Math.round(g.count),Math.round(g.bossHp),[...phs].join('')]});
 console.log('L'+(L+1),r,r2)}
console.log('errs',errs);await b.close()})();
