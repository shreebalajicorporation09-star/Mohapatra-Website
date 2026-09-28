const menu=document.querySelector('.menu-toggle'),nav=document.querySelector('.main-nav');
if(menu)menu.addEventListener('click',()=>nav.classList.toggle('open'));
document.querySelectorAll('.main-nav a').forEach(a=>a.addEventListener('click',()=>nav.classList.remove('open')));
const year=document.getElementById('year'); if(year) year.textContent=new Date().getFullYear();
