const {chromium}=require('/workspace/games/pwtest/node_modules/playwright-core');const D='/workspace/venture/game/apes-vs-aliens';
(async()=>{const b=await chromium.launch({executablePath:'/usr/bin/google-chrome',args:['--no-sandbox']});const errs=[];
const p=await b.newPage({viewport:{width:390,height:844}});p.on('pageerror',e=>errs.push(e.message));p.on('requestfailed',q=>errs.push('FAIL '+q.url()));
await p.goto('file://'+D+'/index.html');await p.waitForTimeout(800);await p.screenshot({path:'/workspace/venture/game/apes-vs-aliens-menu.png'});
await p.evaluate(()=>{const g=window.__av;g.startLevel(0);for(let i=0;i<60*7.5;i++){g.auto();g.step(1/60)}});await p.waitForTimeout(400);await p.screenshot({path:'/workspace/venture/game/apes-vs-aliens-gameplay.png'});
let r=await p.evaluate(()=>{const g=window.__av;let k=0;while(g.st==='play'&&g.dist<g.LEVELS[0].len+10&&g.bossHp>=g.LEVELS[0].boss*0.6&&k<60*200){g.auto();g.step(1/60);k++}return [g.st,g.dist,g.count,g.bossHp]});console.log(r);
await p.waitForTimeout(400);await p.screenshot({path:'/workspace/venture/game/apes-vs-aliens-boss.png'});
r=await p.evaluate(()=>{const g=window.__av;let k=0;while(g.st==='play'&&k<60*120){g.step(1/60);k++}return [g.st,g.count,g.bossHp]});console.log('end',r);
console.log('errs',errs);await b.close()})();
