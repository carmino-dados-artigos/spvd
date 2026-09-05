(() => {
  const tbody = document.querySelector('#base-completa tbody');
  if (!tbody) return;
  const search = document.querySelector('#base-search');
  const sizeSel = document.querySelector('#base-page-size');
  const status = document.querySelector('#base-status');
  const info = document.querySelector('#base-page-info');
  const prev = document.querySelector('#base-prev');
  const next = document.querySelector('#base-next');
  let rows = [], filtered = [], page = 1;

  function parseCSV(text) {
    const out=[]; let row=[], field='', q=false;
    for(let i=0;i<text.length;i++){
      const c=text[i], n=text[i+1];
      if(q){ if(c==='"' && n==='"'){field+='"';i++;} else if(c==='"'){q=false;} else field+=c; }
      else { if(c==='"') q=true; else if(c===','){row.push(field);field='';} else if(c==='\n'){row.push(field.replace(/\r$/,''));out.push(row);row=[];field='';} else field+=c; }
    }
    if(field.length || row.length){row.push(field.replace(/\r$/,''));out.push(row);}
    return out;
  }
  function escapeHTML(v){return String(v).replace(/[&<>"']/g,m=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#039;'}[m]));}
  function apply(){
    const q=(search.value||'').trim().toLowerCase();
    filtered = q ? rows.filter(r=>r.some(v=>String(v).toLowerCase().includes(q))) : rows;
    page=1; render();
  }
  function render(){
    const size=Number(sizeSel.value)||50;
    const pages=Math.max(1,Math.ceil(filtered.length/size));
    page=Math.min(page,pages);
    const start=(page-1)*size, current=filtered.slice(start,start+size);
    tbody.innerHTML=current.map(r=>'<tr>'+r.map(v=>`<td>${escapeHTML(v)}</td>`).join('')+'</tr>').join('');
    status.textContent=`${filtered.length.toLocaleString('pt-BR')} registros encontrados de ${rows.length.toLocaleString('pt-BR')}.`;
    info.textContent=`Página ${page} de ${pages} · registros ${filtered.length ? start+1 : 0}–${Math.min(start+size,filtered.length)}`;
    prev.disabled=page<=1; next.disabled=page>=pages;
  }
  fetch('downloads/dados/processados/base_longitudinal.csv')
    .then(r=>{if(!r.ok) throw new Error('Falha ao carregar CSV'); return r.text();})
    .then(t=>{ const all=parseCSV(t); rows=all.slice(1); filtered=rows; render(); })
    .catch(e=>{status.innerHTML='Não foi possível carregar a tabela automaticamente. Execute o site por um servidor local (por exemplo, <code>python -m http.server</code>) ou use o botão de download do CSV.'; console.error(e);});
  search.addEventListener('input',apply); sizeSel.addEventListener('change',()=>{page=1;render();});
  prev.addEventListener('click',()=>{if(page>1){page--;render();window.scrollTo({top:document.querySelector('#base-completa').offsetTop-130,behavior:'smooth'});}});
  next.addEventListener('click',()=>{const size=Number(sizeSel.value)||50,pages=Math.max(1,Math.ceil(filtered.length/size));if(page<pages){page++;render();window.scrollTo({top:document.querySelector('#base-completa').offsetTop-130,behavior:'smooth'});}});
})();