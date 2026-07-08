#!/usr/bin/env python3
"""Assemble renewable-energy-unit.html from /tmp/re-slides.js"""
from pathlib import Path

slides_js = Path("/tmp/re-slides.js").read_text()
checkpoint = """
SLIDES.push({ type:'checkpoint', nav:'★ Report assessment (Week 8)', assessTab:'task',
  eyebrow:'Week 8 · Assessment',
  title:'Publish your information report',
  sub:'Review, proofread and publish your renewable energy report using the InfoReport tool. Open the assessment task for criteria — press Back any time to return here.',
  notes:`<h4>Week 8 assessment</h4><p>Students publish in InfoReport. Check intro, five body sections, conclusion, glossary and formal language.</p>` });
"""
marker = "SLIDES.push({ type:'divider', nav:'Week 8'"
if marker in slides_js and "★ Report assessment" not in slides_js:
    slides_js = slides_js.replace(marker, checkpoint + "\n" + marker, 1)

HEADER = r'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Year 5 English · Renewable Energy</title>
<style>
  :root{
    --bg0:#061318; --bg1:#0a1e24; --bg2:#0e2830;
    --ink:#eafff9; --ink-dim:#a8c9c4; --ink-faint:#6f938d;
    --panel:#0f2a30; --panel2:#123540; --line:#1f4a52;
    --cream:#fdf6e3; --cream-ink:#1c2b27;
    --amber:#f5c542; --amber2:#ffd766;
    --accent:#19b89a; --accent2:#37e3b0; --teal:#19b89a; --mint:#37e3b0;
    --p1:#ff5a6e; --p2:#37e3b0; --p3:#5aa9ff; --p4:#b88bff; --p5:#ffb347;
    --radius:18px;
    --font: "Segoe UI", system-ui, -apple-system, Roboto, Helvetica, Arial, sans-serif;
  }
  *{box-sizing:border-box;margin:0;padding:0}
  html,body{height:100%}
  body{font-family:var(--font);color:var(--ink);background:var(--bg0);display:flex;align-items:center;justify-content:center;overflow:hidden;}
  #app{width:100vw;height:100vh;display:flex;flex-direction:column;}
  #stageWrap{flex:1;display:flex;align-items:center;justify-content:center;padding:18px 18px 6px;min-height:0;}
  .slide{position:relative;width:min(1180px,100%);aspect-ratio:16/10;max-height:100%;
    background:radial-gradient(1200px 500px at 80% -10%, rgba(55,227,176,.10), transparent 60%), linear-gradient(160deg,var(--bg1),var(--bg2) 60%, #0b2428);
    border:1px solid var(--line);border-radius:26px;box-shadow:0 30px 80px rgba(0,0,0,.55), inset 0 1px 0 rgba(255,255,255,.04);
    padding:26px 38px 48px;overflow:hidden;display:flex;flex-direction:column;}
  .slide::before{content:"";position:absolute;inset:0 0 auto 0;height:5px;background:linear-gradient(90deg,var(--p1),var(--p5),var(--amber),var(--p2),var(--p3),var(--p4));opacity:.9;}
  .eyebrow{display:inline-flex;align-items:center;gap:8px;align-self:flex-start;background:rgba(25,184,154,.14);color:var(--accent2);border:1px solid rgba(25,184,154,.28);
    font-weight:800;letter-spacing:.14em;text-transform:uppercase;font-size:12px;padding:7px 14px;border-radius:999px;}
  h1.title{font-size:clamp(28px,3.6vw,46px);line-height:1.02;margin:10px 0 12px;letter-spacing:-.01em;}
  .slide.cover h1.title{font-size:clamp(40px,6vw,76px);}
  .cols{display:grid;grid-template-columns:1fr 1fr;gap:14px;flex:1;min-height:0;}
  .cols.wide-left{grid-template-columns:1.25fr .9fr;}
  .col{display:flex;flex-direction:column;gap:8px;min-height:0;overflow:hidden;}
  .col::-webkit-scrollbar{width:6px;} .col::-webkit-scrollbar-thumb{background:#1f4a52;border-radius:6px;}
  .col > .card.cream, .col > .steps{flex:0 1 auto;min-height:0;max-height:62%;overflow:auto;}
  .col > .imgframe, .col > .imgrow{flex:1 1 0;min-height:72px;min-width:0;width:100%;}
  .card{border-radius:var(--radius);padding:20px 22px;}
  .card.cream{background:var(--cream);color:var(--cream-ink);box-shadow:0 10px 30px rgba(0,0,0,.25);overflow:auto;}
  .card.dark{background:var(--panel);border:1px solid var(--line);}
  .tag{display:inline-block;font-weight:900;font-size:12px;letter-spacing:.1em;text-transform:uppercase;background:var(--amber);color:#3a2c00;padding:5px 12px;border-radius:999px;margin-bottom:12px;}
  .tag.read{background:var(--amber)} .tag.wow{background:#ff6b8a;color:#3a0010}
  .tag.do{background:var(--mint);color:#063a2c} .tag.try{background:#ffd766;color:#3a2c00}
  .card h3{font-size:clamp(18px,2vw,24px);margin-bottom:8px;}
  .card.cream p,.card.cream li{font-size:clamp(15px,1.45vw,19px);line-height:1.45;}
  .notice{margin-top:12px;background:#eaf7ef;border-left:5px solid var(--teal);color:#143b30;padding:10px 13px;border-radius:10px;font-size:14.5px;}
  .notice b{color:#0c5a44}
  .hook{background:var(--panel2);border:1px solid var(--line);border-radius:var(--radius);padding:10px 15px;}
  .hook .lbl{color:var(--amber2);font-weight:800;font-size:12px;letter-spacing:.08em;text-transform:uppercase;}
  .hook p{font-size:clamp(15px,1.5vw,20px);margin-top:5px;line-height:1.3;}
  .card.dark.wp{padding:14px 16px;}
  .wp h4{color:var(--ink);font-size:16px;margin-bottom:8px;}
  .wp-grid{display:grid;grid-template-columns:1fr 1fr;gap:7px;}
  .chip{background:#0c2428;border:1px solid var(--line);border-radius:11px;padding:7px 10px;}
  .chip b{display:block;font-size:14.5px;color:var(--mint);}
  .chip span{font-size:12px;color:var(--ink-dim);line-height:1.25;}
  .steps{background:var(--cream);color:var(--cream-ink);border-radius:var(--radius);padding:18px 20px;}
  .steps .tag{margin-bottom:14px}
  .steps .row{display:flex;gap:14px;align-items:flex-start;padding:12px 0;border-bottom:1px dashed #d8cda6;}
  .steps .row:last-child{border-bottom:none}
  .steps .num{flex:none;width:30px;height:30px;border-radius:50%;background:#0e2830;color:var(--mint);display:grid;place-items:center;font-weight:900;}
  .steps .row b{font-size:18px;display:block;} .steps .row span{font-size:15px;color:#4a5a54;}
  .exit{background:var(--panel);border:1px solid var(--line);border-radius:var(--radius);padding:16px 18px;}
  .exit h4{font-size:20px;margin-bottom:12px;}
  .exit-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px;}
  .echk{display:flex;gap:10px;align-items:center;background:#0c2428;border:1px solid var(--line);border-radius:12px;padding:10px 12px;font-size:14.5px;}
  .echk .bx{flex:none;width:24px;height:24px;border-radius:7px;background:var(--mint);color:#063a2c;display:grid;place-items:center;font-weight:900;}
  .imgframe{position:relative;border-radius:14px;overflow:hidden;border:1px solid var(--line);background:#0c2428;}
  .imgframe img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center;display:block;}
  .imgframe.diagram img{object-fit:contain;background:#061318;}
  .imgframe.fit img{object-fit:contain;}
  .imgframe .cap{position:absolute;left:0;right:0;bottom:0;z-index:1;background:linear-gradient(transparent,rgba(6,19,24,.92));color:#dffdf3;font-size:12.5px;padding:18px 12px 8px;font-weight:600;}
  .slide.cover{align-items:flex-start;justify-content:center;text-align:left;}
  .cover .sub{font-size:clamp(18px,2.2vw,26px);color:var(--ink-dim);max-width:760px;line-height:1.4;}
  .cover .meta{margin-top:auto;display:flex;gap:22px;flex-wrap:wrap;color:var(--ink-faint);font-weight:700;letter-spacing:.05em;}
  .cover .pill{background:rgba(25,184,154,.12);border:1px solid rgba(25,184,154,.25);color:var(--mint);padding:8px 16px;border-radius:999px;}
  .slide.divider{justify-content:center;}
  .divider .pkr{font-size:clamp(20px,3vw,30px);color:var(--ink-dim);font-weight:800;letter-spacing:.2em;text-transform:uppercase;}
  .divider h1{font-size:clamp(40px,6vw,72px);margin:10px 0 18px;}
  .divider .goals{display:flex;flex-direction:column;gap:12px;max-width:840px;}
  .divider .goal{display:flex;gap:14px;align-items:center;font-size:clamp(17px,1.9vw,22px);background:var(--panel);border:1px solid var(--line);padding:14px 18px;border-radius:14px;}
  .divider .goal i{flex:none;width:34px;height:34px;border-radius:10px;display:grid;place-items:center;font-style:normal;font-weight:900;color:#06251c;}
  .slide.checkpoint{justify-content:center;text-align:center;align-items:center;}
  .checkpoint h1{font-size:clamp(34px,5vw,60px)} .checkpoint p{font-size:clamp(18px,2vw,24px);color:var(--ink-dim);max-width:780px;margin:14px auto 24px;}
  .corner{position:absolute;right:26px;bottom:18px;color:var(--ink-faint);font-size:12px;letter-spacing:.08em;}
  .corner kbd{background:#0c2428;border:1px solid var(--line);border-radius:6px;padding:2px 7px;font-size:11px;}
  .screenlbl{position:absolute;left:38px;bottom:18px;color:var(--ink-faint);font-size:12px;letter-spacing:.12em;text-transform:uppercase;}
  .eyebrow-r{position:absolute;right:38px;top:30px;color:var(--ink-faint);font-size:12px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;}
  #nav{display:flex;align-items:center;justify-content:center;gap:10px;padding:10px;flex-wrap:wrap;}
  .btn{background:#0e2830;color:var(--ink);border:1px solid var(--line);border-radius:999px;padding:9px 16px;font-weight:700;font-size:14px;cursor:pointer;display:inline-flex;align-items:center;gap:7px;}
  .btn:hover{border-color:var(--mint);color:#fff;}
  .btn.primary{background:var(--mint);color:#06281f;border-color:var(--mint);}
  .btn.assess{background:linear-gradient(135deg,var(--amber),#ff9d3c);color:#3a2400;border:none;font-weight:900;}
  .btn.inforeport{background:linear-gradient(135deg,#5aa9ff,#37e3b0);color:#062028;border:none;font-weight:900;}
  .btn.inforeport.hidden{display:none;}
  #counter{font-weight:800;color:var(--ink-dim);min-width:74px;text-align:center;}
  select#jump{background:#0e2830;color:var(--ink);border:1px solid var(--line);border-radius:999px;padding:9px 12px;font-size:13px;max-width:230px;}
  #tnotes{position:fixed;right:0;top:0;height:100%;width:min(440px,90vw);transform:translateX(100%);transition:transform .28s ease;background:#082820;border-left:1px solid var(--line);z-index:40;box-shadow:-20px 0 60px rgba(0,0,0,.5);display:flex;flex-direction:column;}
  #tnotes.open{transform:none;}
  #tnotes header{padding:18px 20px;border-bottom:1px solid var(--line);display:flex;align-items:center;justify-content:space-between;}
  #tnotes header b{color:var(--amber2);letter-spacing:.04em;}
  #tnotes .body{padding:20px;overflow:auto;font-size:15.5px;line-height:1.55;color:var(--ink-dim);}
  #tnotes .body h4{color:var(--mint);margin:14px 0 6px;font-size:16px;}
  #tnotes .body ul{margin:6px 0 6px 18px;} #tnotes .body li{margin:4px 0;}
  #overlay{position:fixed;inset:0;background:rgba(3,12,14,.82);backdrop-filter:blur(6px);z-index:60;display:none;align-items:center;justify-content:center;padding:24px;}
  #overlay.open{display:flex;}
  .modal{width:min(1100px,100%);height:min(88vh,820px);background:linear-gradient(160deg,#0a1e24,#0e2830);border:1px solid var(--line);border-radius:22px;display:flex;flex-direction:column;overflow:hidden;box-shadow:0 40px 100px rgba(0,0,0,.6);}
  .modal header{padding:16px 22px;border-bottom:1px solid var(--line);display:flex;align-items:center;gap:14px;}
  .modal header h2{font-size:22px;margin-right:auto;}
  .tabs{display:flex;gap:8px;}
  .tab{background:#0e2830;border:1px solid var(--line);color:var(--ink-dim);padding:8px 16px;border-radius:999px;cursor:pointer;font-weight:700;font-size:14px;}
  .tab.active{background:var(--amber);color:#3a2400;border-color:var(--amber);}
  .modal .content{padding:24px;overflow:auto;flex:1;}
  .modal .content h3{color:var(--mint);margin:18px 0 8px;font-size:20px;}
  .modal .content p,.modal .content li{font-size:16px;line-height:1.55;color:var(--ink);}
  .modal .content ul{margin:6px 0 6px 20px}
  .panelpane{display:none} .panelpane.active{display:block}
  .rubric{width:100%;border-collapse:collapse;font-size:13px;margin-top:8px;}
  .rubric th,.rubric td{border:1px solid var(--line);padding:8px;vertical-align:top;text-align:left;}
  .rubric th{background:#0c2a30;color:var(--amber2);}
  .rubric td:first-child{background:#0c2428;color:var(--mint);font-weight:800;width:150px;}
  .rubric .A{background:rgba(55,227,176,.06)}
  .assess-doc .assess-open{margin-bottom:12px;} .assess-doc .assess-open a{color:var(--amber2);font-weight:800;}
  #pane-task.active{display:flex;flex-direction:column;min-height:0;flex:1;}
  .assess-pdfFrame{flex:1;min-height:min(68vh,640px);border-radius:14px;overflow:hidden;border:1px solid var(--line);background:#061318;}
  .assess-pdfFrame iframe{width:100%;height:100%;border:0;display:block;min-height:min(68vh,640px);}
  .modal footer{padding:14px 22px;border-top:1px solid var(--line);display:flex;justify-content:space-between;align-items:center;}
  .hint{color:var(--ink-faint);font-size:13px;}
  @media (max-width:720px){.cols{grid-template-columns:1fr;overflow:auto;}.wp-grid,.exit-grid{grid-template-columns:1fr;}select#jump{max-width:130px;}}
</style>
</head>
<body>
<div id="app">
  <div id="stageWrap"><div class="slide" id="slide"></div></div>
  <div id="nav">
    <button class="btn" id="prev">← Prev</button>
    <span id="counter">1 / 1</span>
    <select id="jump"></select>
    <button class="btn assess" id="assessBtn">📋 Assessment</button>
    <button class="btn inforeport hidden" id="inforeportBtn">✎ InfoReport</button>
    <button class="btn" id="notesBtn">Teacher notes</button>
    <button class="btn" id="presentBtn" title="Toggle fullscreen (F)">⛶ Present</button>
    <button class="btn" id="next">Next →</button>
  </div>
</div>
<aside id="tnotes">
  <header><b>Teacher Notes</b>
    <span><button class="btn" id="detachBtn">Detach ⧉</button>
    <button class="btn" id="notesClose">✕</button></span>
  </header>
  <div class="body" id="tnotesBody"></div>
</aside>
<div id="overlay">
  <div class="modal">
    <header>
      <h2>📋 Assessment — Information Report</h2>
      <div class="tabs">
        <button class="tab active" data-pane="task">Task</button>
        <button class="tab" data-pane="guide">Marking Guide</button>
      </div>
    </header>
    <div class="content">
      <div class="panelpane active" id="pane-task"></div>
      <div class="panelpane" id="pane-guide"></div>
    </div>
    <footer>
      <span class="hint">Tip: press <b>A</b> to open/close · Back returns you to your slide</span>
      <button class="btn primary" id="backBtn">← Back to my slide</button>
    </footer>
  </div>
</div>
<script>
const SLIDES = [];
'''

ENGINE = r'''
const ASSESS_PDF = 'Renewable-Energy-Information-Report.pdf';
const ASSESS_TASK = `
  <div class="assess-doc">
    <p class="assess-open"><a href="${encodeURI(ASSESS_PDF)}" target="_blank" rel="noopener">↗ Open assessment task PDF in new tab</a> — print or save</p>
    <div class="assess-pdfFrame"><iframe src="${encodeURI(ASSESS_PDF)}" title="Assessment — Renewable Energy information report"></iframe></div>
    <p style="margin-top:12px;color:var(--ink-dim);font-size:14px">If the PDF is not yet uploaded, use the marking guide tab for criteria. Students publish their report at <b>planomy.github.io/inforeport</b>.</p>
  </div>
`;
const ASSESS_GUIDE = `
  <p>Your information report is judged against these criteria. Aim for the <b>A</b> column!</p>
  <table class="rubric">
    <tr><th>Criterion</th><th class="A">A</th><th>B</th><th>C</th><th>D</th><th>E</th></tr>
    <tr><td>Text structure &amp; organisation</td>
      <td class="A">clear, logical structure with introduction, body sections and conclusion; effective headings and subheadings</td>
      <td>clear structure with most sections present; appropriate headings</td>
      <td>recognisable report structure with some sections</td>
      <td>partial structure; sections may be incomplete</td>
      <td>limited structure; ideas not clearly grouped</td></tr>
    <tr><td>Language features</td>
      <td class="A">precise technical vocabulary used accurately; formal, objective present-tense language throughout</td>
      <td>technical vocabulary mostly accurate; formal language with minor lapses</td>
      <td>some technical vocabulary; mostly formal language</td>
      <td>limited technical vocabulary; informal language at times</td>
      <td>minimal technical vocabulary; informal or inconsistent language</td></tr>
    <tr><td>Content knowledge</td>
      <td class="A">accurate, detailed information on five renewable energy types; advantages and disadvantages explained with evidence</td>
      <td>accurate information on most energy types with some detail</td>
      <td>basic accurate information on renewable energy types</td>
      <td>partial or general information; some inaccuracies</td>
      <td>minimal or inaccurate information</td></tr>
    <tr><td>Editing &amp; publishing</td>
      <td class="A">thoroughly proofread; spelling, punctuation and grammar accurate; published successfully in InfoReport</td>
      <td>mostly accurate editing; published in InfoReport</td>
      <td>some editing evident; report submitted</td>
      <td>limited editing; draft quality</td>
      <td>minimal editing or not submitted</td></tr>
  </table>
`;
const ASSESS_TAB_BY_NAV = {
  'L22A — Using the InfoReport Tool': 'task',
  'L22B — Content': 'task',
  'L23A — Drafting Body Sections': 'task',
  'L23B — Content': 'task',
  'L24A — Reviewing and Publishing': 'task',
  'L24B — Content': 'task',
  '★ Report assessment (Week 8)': 'task'
};
const INFOREPORT_URL = 'https://planomy.github.io/inforeport';
const INFOREPORT_NAV = new Set([
  'L22A — Using the InfoReport Tool','L22B — Content',
  'L23A — Drafting Body Sections','L23B — Content',
  'L24A — Reviewing and Publishing','L24B — Content',
  '★ Report assessment (Week 8)'
]);

function hook(q){ return `<div class="hook"><div class="lbl">Hook question</div><p>${q}</p></div>`; }
function wordpower(list){
  return `<div class="card dark wp"><h4>Word Power</h4><div class="wp-grid">${
    list.map(w=>`<div class="chip"><b>${w.t}</b><span>${w.d}</span></div>`).join('')}</div></div>`;
}
function readCard(r){
  return `<div class="card cream"><span class="tag ${r.wow?'wow':'read'}">${r.label||(r.wow?'WOW · READ':'READ')}</span>
    <h3>${r.heading}</h3>${(r.body||[]).map(p=>`<p style="margin-bottom:10px">${p}</p>`).join('')}
    ${r.notice?`<div class="notice"><b>Notice:</b> ${r.notice}</div>`:''}</div>`;
}
function exitCheck(items){
  return `<div class="exit"><h4>Exit check — I can…</h4><div class="exit-grid">${
    items.map(i=>`<div class="echk"><span class="bx">✓</span><span>${i}</span></div>`).join('')}</div></div>`;
}
function steps(s){
  return `<div class="steps"><span class="tag do">${s.label||'DO THIS'}</span>
    ${s.rows.map((r,i)=>`<div class="row"><div class="num">${i+1}</div><div><b>${r.t}</b><span>${r.d||''}</span></div></div>`).join('')}</div>`;
}
function renderBlock(b){
  switch(b.k){
    case 'read': return readCard(b);
    case 'hook': return hook(b.q);
    case 'wp': return wordpower(b.list);
    case 'steps': return steps(b);
    case 'exit': return exitCheck(b.items);
    case 'img': return `<div class="imgframe${b.diagram?' diagram':''}${b.fit?' fit':''}"><img src="${b.src}" alt="${b.alt||''}" loading="lazy">${b.cap?`<div class="cap">${b.cap}</div>`:''}</div>`;
    case 'html': return b.html;
    default: return '';
  }
}
function renderSlide(s){
  const el = document.getElementById('slide');
  el.className = 'slide ' + (s.type||'lesson');
  el.style.background = '';
  if(s.type==='cover' && s.bg){
    el.style.background = `linear-gradient(90deg, rgba(6,19,24,.95) 30%, rgba(6,19,24,.45) 70%, rgba(6,19,24,.25)), url('${s.bg}') right center / cover no-repeat`;
  }
  let html='';
  if(s.eyebrowR) html+=`<div class="eyebrow-r">${s.eyebrowR}</div>`;
  if(s.type==='cover'){
    html += `<span class="eyebrow">${s.eyebrow||''}</span><h1 class="title">${s.title}</h1><p class="sub">${s.sub||''}</p>
      <div class="meta">${(s.meta||[]).map(m=>`<span class="pill">${m}</span>`).join('')}</div>`;
  } else if(s.type==='divider'){
    html += `<div class="pkr">${s.eyebrow||''}</div><h1>${s.title}</h1>
      <div class="goals">${(s.goals||[]).map((g,i)=>`<div class="goal"><i style="background:var(--p${(i%5)+1})">${i+1}</i><span>${g}</span></div>`).join('')}</div>`;
  } else if(s.type==='checkpoint'){
    html += `<span class="eyebrow" style="align-self:center">${s.eyebrow||''}</span><h1>${s.title}</h1><p>${s.sub||''}</p>
      <button class="btn assess" style="padding:14px 26px;font-size:17px" onclick="openOverlay()">📋 Open assessment task</button>`;
  } else {
    if(s.eyebrow) html+=`<span class="eyebrow">${s.eyebrow}</span>`;
    html += `<h1 class="title">${s.title}</h1>`;
    html += `<div class="cols ${s.wideLeft?'wide-left':''}"><div class="col">${(s.left||[]).map(renderBlock).join('')}</div><div class="col">${(s.right||[]).map(renderBlock).join('')}</div></div>`;
  }
  if(s.screenlbl) html+=`<div class="screenlbl">${s.screenlbl}</div>`;
  html += `<div class="corner"><kbd>T</kbd> notes · <kbd>D</kbd> detach · <kbd>A</kbd> assessment · <kbd>I</kbd> InfoReport</div>`;
  el.innerHTML = html;
}
let idx = 0;
function syncInfoReportBtn(){
  const btn = document.getElementById('inforeportBtn');
  const show = INFOREPORT_NAV.has(SLIDES[idx]?.nav);
  btn.classList.toggle('hidden', !show);
}
function show(i){
  idx = Math.max(0, Math.min(SLIDES.length-1, i));
  renderSlide(SLIDES[idx]);
  document.getElementById('counter').textContent = `${idx+1} / ${SLIDES.length}`;
  document.getElementById('jump').value = idx;
  if(document.getElementById('tnotes').classList.contains('open')) fillNotes();
  syncInfoReportBtn();
}
function buildJump(){
  const sel=document.getElementById('jump'); sel.innerHTML='';
  SLIDES.forEach((s,i)=>{ const o=document.createElement('option'); o.value=i; o.textContent=`${i+1}. ${s.nav||s.title||('Slide '+(i+1))}`; sel.appendChild(o); });
}
function fillNotes(){
  document.getElementById('tnotesBody').innerHTML = SLIDES[idx].notes || '<p>No notes for this screen.</p>';
}
function openNotes(){ document.getElementById('tnotes').classList.add('open'); fillNotes(); }
function closeNotes(){ document.getElementById('tnotes').classList.remove('open'); }
function detachNotes(){
  const s=SLIDES[idx];
  const w=window.open('','tnotes','width=460,height=760');
  w.document.write(`<title>Teacher Notes — ${s.nav||s.title}</title><style>body{font-family:system-ui;background:#082820;color:#cfe;line-height:1.6;padding:22px;}h2{color:#ffd766}h4{color:#37e3b0;margin:14px 0 4px}ul{margin-left:18px}li{margin:4px 0}</style><h2>${s.nav||s.title}</h2>${s.notes||'<p>No notes.</p>'}`);
  w.document.close();
}
let savedIdxForOverlay=null;
function switchAssessTab(pane){
  document.querySelectorAll('#overlay .tab').forEach(x=>x.classList.remove('active'));
  document.querySelectorAll('#overlay .panelpane').forEach(x=>x.classList.remove('active'));
  document.querySelector(`#overlay .tab[data-pane="${pane}"]`)?.classList.add('active');
  document.getElementById('pane-'+pane)?.classList.add('active');
}
function openOverlay(forcedPane){
  savedIdxForOverlay=idx;
  const slide = SLIDES[idx];
  const pane = (typeof forcedPane === 'string' && forcedPane) || slide?.assessTab || ASSESS_TAB_BY_NAV[slide?.nav] || 'task';
  switchAssessTab(pane);
  document.getElementById('overlay').classList.add('open');
}
function closeOverlay(){ document.getElementById('overlay').classList.remove('open'); if(savedIdxForOverlay!=null) show(savedIdxForOverlay); }
function openInfoReport(){ window.open(INFOREPORT_URL, '_blank', 'noopener'); }
document.getElementById('prev').onclick=()=>show(idx-1);
document.getElementById('next').onclick=()=>show(idx+1);
document.getElementById('jump').onchange=e=>show(+e.target.value);
document.getElementById('notesBtn').onclick=openNotes;
document.getElementById('notesClose').onclick=closeNotes;
document.getElementById('detachBtn').onclick=detachNotes;
document.getElementById('assessBtn').onclick=()=>openOverlay();
document.getElementById('inforeportBtn').onclick=openInfoReport;
document.getElementById('backBtn').onclick=closeOverlay;
function toggleFullscreen(){
  const el=document.documentElement;
  if(!document.fullscreenElement){ (el.requestFullscreen||el.webkitRequestFullscreen||el.msRequestFullscreen).call(el); }
  else{ (document.exitFullscreen||document.webkitExitFullscreen||document.msExitFullscreen).call(document); }
}
function syncPresentBtn(){ document.getElementById('presentBtn').textContent = document.fullscreenElement ? '⤢ Exit' : '⛶ Present'; }
document.getElementById('presentBtn').onclick=toggleFullscreen;
document.addEventListener('fullscreenchange',syncPresentBtn);
document.addEventListener('webkitfullscreenchange',syncPresentBtn);
document.querySelectorAll('.tab').forEach(t=>t.onclick=()=>switchAssessTab(t.dataset.pane));
document.addEventListener('keydown',e=>{
  if(e.target.tagName==='SELECT') return;
  if(e.key==='ArrowRight') show(idx+1);
  else if(e.key==='ArrowLeft') show(idx-1);
  else if(e.key.toLowerCase()==='t'){ document.getElementById('tnotes').classList.contains('open')?closeNotes():openNotes(); }
  else if(e.key.toLowerCase()==='d') detachNotes();
  else if(e.key.toLowerCase()==='a'){ document.getElementById('overlay').classList.contains('open')?closeOverlay():openOverlay(); }
  else if(e.key.toLowerCase()==='i' && INFOREPORT_NAV.has(SLIDES[idx]?.nav)) openInfoReport();
  else if(e.key.toLowerCase()==='f') toggleFullscreen();
  else if(e.key==='Escape'){ closeOverlay(); closeNotes(); }
});
document.getElementById('pane-task').innerHTML = ASSESS_TASK;
document.getElementById('pane-guide').innerHTML = ASSESS_GUIDE;
buildJump(); show(0);
</script>
</body>
</html>
'''

out = Path("/Users/niccomino/Desktop/renewableenergy/renewable-energy-unit.html")
content = HEADER + slides_js + "\n" + ENGINE
out.write_text(content)
print(f"Wrote {out} ({len(content)} bytes, {content.count('SLIDES.push')} slides)")
