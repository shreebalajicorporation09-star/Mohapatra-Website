async function loadPart(id,file){const el=document.getElementById(id);if(el){const r=await fetch(file);el.innerHTML=await r.text();}}
Promise.all([loadPart('head','page-head.html'),loadPart('foot','page-foot.html')]);
