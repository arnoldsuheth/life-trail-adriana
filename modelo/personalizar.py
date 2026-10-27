#!/usr/bin/env python3
"""Gera uma cópia isolada do Life Trail. Somente Python 3, sem dependências."""
import argparse,base64,json,mimetypes,re
from pathlib import Path
parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('config',type=Path);parser.add_argument('--saida',type=Path,default=Path('dist'));args=parser.parse_args()
c=json.loads(args.config.read_text(encoding='utf-8'));root=args.config.resolve().parent
for field in ['nome','empresa']:
 if not re.fullmatch(r'[A-Za-zÀ-ÿ0-9][A-Za-zÀ-ÿ0-9 .-]{1,79}',c.get(field,'')):raise SystemExit('Use letras, números, espaços, pontos ou hífens em '+field)
slug=c.get('identificador','')
if not re.fullmatch(r'[a-z0-9][a-z0-9-]{2,59}',slug):raise SystemExit('Identificador precisa ser único: letras minúsculas, números e hífens.')
for field in ['cor_dourado','cor_violeta']:
 if not re.fullmatch(r'#[0-9a-fA-F]{6}',c[field]):raise SystemExit('Cor inválida: '+field)
def uri(key):
 p=(root/c[key]).resolve()
 if p.suffix.lower() not in ['.png','.jpg','.jpeg','.webp'] or not p.is_file():raise SystemExit('Imagem não encontrada: '+str(p))
 return 'data:'+mimetypes.guess_type(p.name)[0]+';base64,'+base64.b64encode(p.read_bytes()).decode()
s=Path(__file__).with_name('base.html').read_text(encoding='utf-8')
for old,new in {'__CLIENT_NAME__':c['nome'],'__CLIENT_FIRST_NAME__':c['nome'].split()[0],'__CLIENT_SLUG__':slug,'__CLIENT_COMPANY__':c['empresa'],'__AVATAR_URI__':uri('avatar_sem_fundo'),'__PORTRAIT_URI__':uri('retrato_com_fundo'),'__HERO_URI__':uri('fundo_principal')}.items():s=s.replace(old,new)
def js(x):return json.dumps(x,ensure_ascii=False).replace('<','\\u003c')
# Rotina limpa. Nunca copia lançamentos do cliente anterior.
state={'theme':'dark','waterCount':0,'habits':[{'id':i+1,'title':t,'done':False} for i,t in enumerate(c.get('habitos',[]))],'devocionalNote':'','workNotes':'','tasks':[{'id':i+1,'title':t,'done':False} for i,t in enumerate(c.get('tarefas',[]))],'workoutChecks':{},'transactions':[],'prayers':[],'gratitudeNotes':''}
s,n=re.subn(r'const defaultState = \{.*?\n        \};','const defaultState = '+js(state)+';',s,count=1,flags=re.S)
if n!=1:raise SystemExit('Estrutura da base mudou; revisão necessária.')
if c.get('treinos'):
 required=['Segunda','Terça','Quarta','Quinta','Sexta','Sábado']
 if any(d not in c['treinos'] or not c['treinos'][d].get('exercises') for d in required):raise SystemExit('Informe os seis dias e seus exercícios.')
 s,n=re.subn(r'const workoutDatabase = \{.*?\n        \};','const workoutDatabase = '+js(c['treinos'])+';',s,count=1,flags=re.S)
 if n!=1:raise SystemExit('Estrutura dos treinos mudou.')
# Ajuste de cores aplicado sobre o tema. As imagens são próprias de cada gerente.
css='html.noir-app.dark{--na-gold:'+c['cor_dourado']+';--na-gold-bright:'+c['cor_dourado']+';--na-violet:'+c['cor_violeta']+'}.noir-app button.primary,.noir-app .trail-btn.primary,.noir-app .glass-link.primary{background:'+c['cor_dourado']+'!important}'
s=s.replace('</head>','<style>'+css+'</style></head>')
if re.search(r'__(CLIENT|AVATAR|PORTRAIT|HERO)_',s):raise SystemExit('Configuração incompleta.')
out=args.saida/slug;out.mkdir(parents=True,exist_ok=True);(out/'index.html').write_text(s,encoding='utf-8')
print(out.resolve()/'index.html')
