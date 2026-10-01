from bs4 import BeautifulSoup
from pathlib import Path
p=Path('/mnt/data/site_v3/index.html')
s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
# Remove Projects nav and section entirely
for a in s.select('.main-nav a[href="#projects"]'):
    a.decompose()
proj=s.find(id='projects')
if proj: proj.decompose()
# More polished copy
repls={
    ('#home','h1'):'Engineering clarity.\nProject confidence.',
}
h1=s.select_one('#home h1')
if h1:
    h1.clear(); h1.append('Engineering clarity.'); h1.append(s.new_tag('br')); sp=s.new_tag('span'); sp.string='Project confidence.'; h1.append(sp)
hero_p=s.select_one('#home .hero-content p')
if hero_p: hero_p.string='Integrated civil consultancy for projects that demand accurate field data, disciplined engineering and dependable technical coordination.'
about_h=s.select_one('#about .section-head h2')
if about_h: about_h.string='Technical depth, coordinated through one dependable team.'
about_p=s.select_one('#about .section-head p')
if about_p: about_p.string='From site intelligence and testing to design review and project support, we connect the technical stages that shape confident project decisions.'
about_h3=s.select_one('#about .about-copy h3')
if about_h3: about_h3.string='Better information. Better engineering decisions.'
about_p2=s.select_one('#about .about-copy p')
if about_p2: about_p2.string='We combine field measurement, technical investigation, engineering review and execution support into a clear workflow—helping project teams move from uncertainty to actionable information.'
# About unique image
ai=s.select_one('#about .about-image-wrap img')
if ai: ai['src']='assets/service-design-engineering.jpg'; ai['alt']='Engineering design and technical consultancy workspace'
# Team section
th=s.select_one('.team-showcase .section-head h2')
if th: th.string='Where planning, design and execution meet.'
tp=s.select_one('.team-showcase .section-head p')
if tp: tp.string='A practical consultancy workflow built around collaboration, technical review and decisions that remain grounded in project realities.'
# Sectors
sh=s.select_one('#sectors .section-head h2')
if sh: sh.string='Built for complex sites, critical infrastructure and growing cities.'
sp=s.select_one('#sectors .section-head p')
if sp: sp.string='Our multidisciplinary capability supports the built environment—from structures and utilities to industrial assets, transport corridors and technical investigations.'
# Services
svh=s.select_one('#services .section-head h2')
if svh: svh.string='Technical services that turn site information into confident action.'
# unique service images
imgs={
 'Design Engineering Consultancy':'assets/service-design-engineering.jpg',
 'Project Management Consultancy':'assets/service-project-management.jpg',
}
for card in s.select('#services .service'):
    h=card.find('h3')
    if h and h.get_text(strip=True) in imgs:
        card.find('img')['src']=imgs[h.get_text(strip=True)]
# Gallery copy
gh=s.select_one('#gallery .section-head h2')
if gh: gh.string='Field evidence, captured with purpose.'
gp=s.select_one('#gallery .section-head p')
if gp: gp.string='A glimpse of the practical work behind our technical deliverables—surveying, control-point marking, investigation and site assessment.'
# Clients copy
ch=s.select_one('#clients .section-head h2')
if ch: ch.string='Relationships built through technical reliability.'
cp=s.select_one('#clients .section-head p')
if cp: cp.string='A selection of organizations and project partners connected with our work across infrastructure, industry, engineering and development.'
# CTA
cta=s.select_one('.cta h2')
if cta: cta.string='From field data to project delivery, let’s build with confidence.'
# footer stronger copy
fh=s.select_one('#contact .footer-intro h2')
if fh: fh.string='Let’s shape the next project with clarity.'
fp=s.select_one('#contact .footer-intro p')
if fp: fp.string='Tell us what the project needs. We bring the field, testing, engineering and project-support perspective needed to move the work forward with confidence.'
# remove any Projects footer links if present
for a in s.select('a[href="#projects"]'): a.decompose()
p.write_text(str(s),encoding='utf-8')
