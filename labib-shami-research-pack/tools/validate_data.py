#!/usr/bin/env python3
"""Validate curated academic web data; standard library only. Run from any directory."""
from pathlib import Path
import json,re,sys
root=Path(__file__).resolve().parents[1]
items={}
for name,path in [('publications','publications/publications.json'),('reports','policy/taub_center_reports.json'),('media','media/media.json'),('sources','sources/source_registry.json')]:
    items[name]=json.loads((root/path).read_text(encoding='utf-8'))
issues=[]
for kind,records in items.items():
    seen=set()
    for i,r in enumerate(records,1):
        if not r.get('id'):issues.append(f'{kind} line {i}: missing id');continue
        if r['id'] in seen:issues.append(f'{kind}: duplicate id {r["id"]}')
        seen.add(r['id'])
        if not r.get('url') or not r['url'].startswith('https://'):issues.append(f'{kind}: bad URL {r["id"]}')
dois=set()
for p in items['publications']:
    d=p.get('doi','')
    if d and not re.match(r'^10\.\d{4,9}/\S+$',d):issues.append('Invalid DOI '+d)
    if d in dois and d:issues.append('Duplicate DOI '+d)
    dois.add(d)
    if p['year']<1900 or p['year']>2100:issues.append('bad year '+p['id'])
    if p.get('pdf_included'):issues.append('Unexpected full PDF flag for '+p['id'])
ids={s['id'] for s in items['sources']}
for typ in ('publications','reports','media'):
    for p in items[typ]:
        for s in p.get('source_ids',[]):
            if s not in ids:issues.append(typ+' '+p['id']+' unknown source '+s)
for k,v in items.items():print(f'{k}: {len(v)} records')
if issues:
    print('\nERRORS:');print('\n'.join(issues));sys.exit(1)
print('PASS: unique identifiers, DOI format, URL syntax, source references and rights flags')
