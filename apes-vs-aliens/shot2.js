const {chromium}=require('/workspace/games/pwtest/node_modules/playwright-core');
(async()=>{const b=await chromium.launch({executablePath:'/usr/bin/google-chrome',args:['--no-sandbox']});
const p=await b.newPage({viewport:{width:390,height:844}});await p.goto('file:///workspace/venture/game/apes-vs-aliens/index.html');await p.waitForTimeout(800);
await p.evaluate(()=>window.__av.startLevel(0));
for(const t of [3,5,7,8,9]){await p.evaluate(t=>{const g=window.__av;for(let i=0;i<60*t;i++){g.auto();g.step(1/60)}},t<7?1.2:0.12);await p.waitForTimeout(150);console.log(await p.evaluate(()=>window.__av.dist));await p.screenshot({path:'/tmp/g'+t+'.png'})}
await b.close()})();
