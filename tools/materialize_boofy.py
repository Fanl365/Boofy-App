#!/usr/bin/env python3
from pathlib import Path
import json, sys
root=Path('.').resolve(); PROT='beefyfinance'
def rb(t):
 out=[]
 for line in t.splitlines(keepends=True):
  low=line.lower()
  if '@author' in low or 'copyright' in low: out.append(line); continue
  if 'blockchain-addressbook' in low: line=line.replace('beefyfinance',PROT)
  line=line.replace('BOOFY','BOOFY').replace('Boofy','Boofy').replace('boofy','boofy').replace(PROT,'boofyfinance')
  out.append(line)
 return ''.join(out)
for p in list(root.rglob('*')):
 if not p.is_file() or '.git' in p.parts or '.github' in p.parts: continue
 if p.name in {'LICENSE','LICENSE.md','COPYING','NOTICE'}: continue
 try: t=p.read_text(encoding='utf-8')
 except: continue
 n=rb(t)
 if n!=t: p.write_text(n,encoding='utf-8')
for p in sorted([x for x in root.rglob('*') if '.git' not in x.parts and '.github' not in x.parts],key=lambda x:len(x.parts),reverse=True):
 n=p.name.replace('BOOFY','BOOFY').replace('Boofy','Boofy').replace('boofy','boofy')
 if n!=p.name and p.exists() and not p.with_name(n).exists(): p.rename(p.with_name(n))
p=root/'package.json'
if p.exists():
 try:
  d=json.loads(p.read_text()); d['name']='boofy-app'; d['repository']='boofyfinance/boofy-app'; p.write_text(json.dumps(d,indent=2)+'\n')
 except: pass
(root/'BOOFY_TEAM.md').write_text('# Boofy Development Team\n\n- **Fan Long** — Co-Founder\n- **David Woo** — Developer\n- **Tyler Casselman** — Developer\n- **Albert Jones** — Developer\n\nCurrent Boofy team; upstream legal attribution is preserved.\n')
(root/'BOOFY_MIGRATION_NOTICE.md').write_text('# Boofy Migration Notice\n\nRebranding does not create or verify blockchain deployments. Replace upstream addresses, transaction hashes, token symbols, pool IDs, treasury/governance/multisig and social/domain values only with verified Boofy values before production.\n')
print('Boofy App materialized')
