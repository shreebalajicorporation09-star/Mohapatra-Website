from pathlib import Path
from bs4 import BeautifulSoup
p=Path('/mnt/data/mohapatra_work/index.html')
s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
# Add a premium client introduction / capability band before the logo grid.
clients=s.select_one('#clients')
if clients and not clients.select_one('.client-overview'):
    grid=clients.select_one('.client-grid')
    overview=s.new_tag('div', attrs={'class':'client-overview'})
    overview.append(BeautifulSoup('''
<div class="client-overview-copy">
  <span class="client-kicker">CLIENT NETWORK</span>
  <h3>A cross-sector network built around dependable technical delivery.</h3>
  <p>Our portfolio reflects work connected with infrastructure, engineering, industrial, energy, utilities and development environments. Each engagement is supported by field intelligence, technical discipline and clear coordination.</p>
  <div class="client-tags"><span>Infrastructure</span><span>Industrial</span><span>Energy &amp; Utilities</span><span>Engineering &amp; Development</span></div>
</div>
<div class="client-metrics">
  <div><strong>33+</strong><small>Client &amp; partner brands featured</small></div>
  <div><strong>6</strong><small>Core technical service areas</small></div>
  <div><strong>Pan-India</strong><small>Project support capability</small></div>
</div>
''','html.parser'))
    grid.insert_before(overview)
    # Add a subtle logo-grid label
    label=s.new_tag('div', attrs={'class':'logo-grid-label'})
    label.string='SELECTED CLIENTS & PARTNERS'
    grid.insert_before(label)
# Add classes to major sections for unique visual treatment
for sec in s.find_all('section'):
    sid=sec.get('id')
    if sid:
        sec['data-section']=sid
# Make service descriptions more polished
repls={
'Testing of sand, sandstone, stone aggregate and soil samples.':'Laboratory-focused testing of sand, sandstone, stone aggregate and soil samples for dependable material assessment.',
'Rebound Hammer, UPV, Cover Meter, Half Cell, Carbonation, load/deflection, crack measurement and pile testing.':'Rebound Hammer, UPV, Cover Meter, Half Cell, carbonation, load/deflection, crack measurement and pile testing for structural assessment.',
'Planning, soil investigation, feasibility/DPR, architectural and structural engineering, tendering, BOQ and construction drawings.':'Planning, soil investigation, feasibility/DPR, architectural and structural engineering, tendering, BOQ and construction documentation.',
'Construction supervision, quality, drawing review, HSE, planning, progress reporting, cost control and commissioning support.':'Construction supervision, quality assurance, drawing review, HSE, planning, progress reporting, cost control and commissioning coordination.',
'Forest and environmental clearances, air and water quality monitoring and related technical support.':'Forest and environmental clearances, air and water quality monitoring, documentation and associated technical support.'}
for text in s.find_all(string=True):
    if text.strip() in repls:
        text.replace_with(repls[text.strip()])
# Slightly more polished hero copy
hero_p=s.select_one('.hero p')
if hero_p:
    hero_p.string='Integrated civil consultancy combining field surveying, testing, engineering design and project support for decisions that stand up in the real world.'
# Remove external font links so local opening is dependable; CSS fallbacks remain.
for link in s.find_all('link'):
    href=link.get('href','')
    if 'fonts.googleapis.com' in href:
        link.decompose()
# Update title
s.title.string='Mohapatra Enterprises | Civil Consultancy & Engineering'
p.write_text(str(s),encoding='utf-8')
