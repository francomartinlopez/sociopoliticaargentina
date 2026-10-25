import json,sys,collections
sys.path.insert(0,'/home/claude/sociopolitica/datos/afinidades')
from check import load, ROSTER, NAMES
RAW='/home/claude/sociopolitica/datos/afinidades/raw/'
SEN='https://www.senado.gob.ar/votaciones/detalleActa/'
VOTMAP={'A':'afirmativo','N':'negativo','B':'abstencion','X':'ausente'}
V=[
 dict(id='presupuesto-2026',archivo='presupuesto2026.txt',fecha='2025-12-26',tema='Presupuesto 2026 (en general)',tipo='ley',fuentes=['https://www.tiempodesanjuan.com/politica/ley-presupuesto-2026-uno-uno-asi-votaron-los-senadores-la-provincia-n419854','https://www.elonce.com/uid-861351'],
      nota='Lista nominal de prensa (dos medios coinciden: 46-25-1, sin ausentes). El acta oficial de 2025 no pudo abrirse.'),
 dict(id='reforma-laboral-senado-1',acta=2623,archivo='2623.txt',fecha='2026-02-11',tema='Modernización laboral, media sanción (en general)',tipo='ley',nota='El acta oficial fecha la sesión el 11/02/2026 y registra la votación a la 01:21; la prensa la ubica en la madrugada del 12/02.'),
 dict(id='pliego-iglesias',acta=2655,archivo='2655.txt',fecha='2026-02-26',tema='Pliego de Fernando Iglesias, embajador ante Bélgica y la UE',tipo='pliego'),
 dict(id='mercosur-ue',acta=2656,archivo='2656.txt',fecha='2026-02-26',tema='Acuerdo Mercosur–Unión Europea (en general y particular)',tipo='tratado'),
 dict(id='glaciares',acta=2657,archivo='2657.txt',fecha='2026-02-26',tema='Modificación de la Ley de Glaciares 26.639 (en general)',tipo='ley'),
 dict(id='penal-juvenil',acta=2665,archivo='2665.txt',fecha='2026-02-27',tema='Régimen Penal Juvenil (en general)',tipo='ley'),
 dict(id='reforma-laboral-senado-2',acta=2678,archivo='2678.txt',fecha='2026-02-27',tema='Modernización laboral: aceptación de los cambios de Diputados (sanción definitiva)',tipo='ley'),
 dict(id='pliego-crexell',acta=2686,archivo='2686.txt',fecha='2026-04-09',tema='Pliego de Carmen Lucila Crexell, embajadora en Canadá',tipo='pliego'),
 dict(id='pliego-mahiques',acta=2691,archivo='2691.txt',fecha='2026-05-14',tema='Prórroga del mandato de Carlos Mahiques en Casación Penal (PE-176/25)',tipo='pliego'),
 dict(id='pliegos-judiciales-od29-41',acta=2764,archivo='2764.txt',fecha='2026-06-04',tema='Pliegos judiciales en bloque (O.D. 29 a 41/2026)',tipo='pliego'),
 dict(id='pliego-sosa',acta=2765,archivo='2765.txt',fecha='2026-06-04',tema='Pliego de María Julia Sosa, TOCF N°3 de La Plata',tipo='pliego',nota='Pliego enviado por el Ejecutivo y votado a favor por todo el bloque oficialista; se toma esa postura como la del gobierno.'),
 dict(id='pliegos-judiciales-od43-89',acta=2766,archivo='2766.txt',fecha='2026-06-04',tema='Pliegos judiciales en bloque (O.D. 43 a 89/2026)',tipo='pliego'),
 dict(id='propiedad-privada',archivo='propiedad2026.txt',fecha='2026-08-07',tema='Inviolabilidad de la Propiedad Privada, media sanción (en general)',tipo='ley',fuentes=['https://www.perfil.com/noticias/politica/ley-de-propiedad-privada-que-senadores-votaron-a-favor-y-cuales-en-contra.phtml','https://www.elonce.com/uid-882245','https://www.senado.gob.ar/prensa/24146/noticias'],
      nota='Lista nominal de prensa (Perfil y Elonce coinciden: 37-33-0, con 2 ausentes). La sesión empezó el 06/08 y siguió tras un cuarto intermedio; la prensa del Senado fecha la votación el 07/08. El acta oficial no está publicada (la lista del sitio termina el 04/06/2026).'),
]
PARCIALES=[
 dict(id='inocencia-fiscal',fecha='2025-12-26',tema='Inocencia Fiscal (sanción, en general)',tipo='ley',totales=dict(afirmativos=43,negativos=26,abstenciones=None,ausentes=3),
      votos={'ANDRADA, GUILLERMO EDUARDO':'X','UÑAC, SERGIO MAURICIO':'X','VIGO, ALEJANDRA MARÍA':'X'},
      fuentes=['https://www.ambito.com/c6228502','https://www.diariodecuyo.com.ar/politica/el-senado-sanciono-la-ley-de-inocencia-fiscal-y-se-elevan-los-desfasados-umbrales-por-evasion-1814564.html'],
      nota='Sin lista nominal. Solo se conocen los tres ausentes (Ámbito), que no cuentan para el índice. Diario de Cuyo confirma 43-26.'),
 dict(id='inocencia-fiscal-2',fecha='2026-09-17',tema='Inocencia Fiscal II (sanción, en general)',tipo='ley',totales=dict(afirmativos=44,negativos=23,abstenciones=None,ausentes=None),
      votos={'SCHNEIDER, SILVANA LORENA':'A','GODOY, JUAN CRUZ':'A','CAPITANICH, JORGE MILTON':'N','MÁRQUEZ, NADIA JUDITH':'A','CERVI, MARIO PABLO':'A','CORROZA, JULIETA':'A','FULLONE, ENZO PAOLO':'A','SORIA, MARTIN IGNACIO':'N','MARKS, ANA INÉS':'N'},
      fuentes=['https://www.perfil.com/noticias/nea/el-senado-aprobo-la-inocencia-fiscal-ii-como-votaron-los-senadores-de-chaco.phtml','https://www.lmneuquen.com/c1254124','https://elancasti.com.ar/politica-y-economia/el-senado-aprobo-general-la-ley-inocencia-fiscal-ii-n621847'],
      nota='Sin lista nominal completa. Hay votos individuales solo de Chaco (Perfil) y de Neuquén y Río Negro (LM Neuquén). Letra P cita un tuit con 43-23. Los votos conocidos entran al índice; el resto queda null.'),
]
votes={}; out_v=[]
for v in V:
    h,vv,bad=load(RAW+v['archivo']); assert not bad and len(vv)==72
    c=collections.Counter(vv.values())
    fuentes=v.get('fuentes') or [SEN+str(v['acta'])]
    emit=c['A']+c['N']+c['B']
    out_v.append(dict(id=v['id'],fecha=v['fecha'],tema=v['tema'],tipo=v['tipo'],posicion_gobierno='afirmativo',acta_senado=v.get('acta'),
        totales=dict(afirmativos=c['A'],negativos=c['N'],abstenciones=c['B'],ausentes=c['X']),
        disputada= max(c['A'],c['N'])/emit < 0.9 if emit else None,
        nominal='completa',fuentes=fuentes,nota=v.get('nota')))
    votes[v['id']]=vv
for p in PARCIALES:
    out_v.append(dict(id=p['id'],fecha=p['fecha'],tema=p['tema'],tipo=p['tipo'],posicion_gobierno='afirmativo',acta_senado=None,totales=p['totales'],
        disputada=True,nominal='parcial',fuentes=p['fuentes'],nota=p['nota']))
    votes[p['id']]=p['votos']
out_v.sort(key=lambda x:x['fecha'])
disp={x['id']:x['disputada'] for x in out_v}
def score(vv,ids):
    s=n=0
    for i in ids:
        x=vv.get(i)
        if x in ('A','N','B'): s+= {'A':1,'B':.5,'N':0}[x]; n+=1
    return (round(100*s/n,1) if n else None), n
def cat(p): return None if p is None else 'afin' if p>=200/3 else 'opositora' if p<=100/3 else 'neutral'
sens=[]
for name,prov,bloque,_ in ROSTER:
    vv={i:votes[i].get(name) for i in votes}
    ids=[x['id'] for x in out_v]
    pct,n=score(vv,ids); pctd,nd=score(vv,[i for i in ids if disp[i]])
    sens.append(dict(nombre=name,provincia=prov,bloque=bloque,pct_alineado=pct,votos_computados=n,pct_alineado_solo_disputadas=pctd,votos_computados_disputadas=nd,
        votos={i:(VOTMAP[vv[i]] if vv[i] else None) for i in ids}))
BLOQ_NOTAS={'REJAL, JESÚS FERNANDO':'Justicialista en el acta oficial de feb. 2026; Perfil y Elonce (agosto de 2026) lo listan en Justicia Social Federal.',
 'SCHNEIDER, SILVANA LORENA':'UCR en las actas oficiales; Perfil (17/09/2026) la presenta como La Libertad Avanza.',
 'JUEZ, LUIS ALFREDO':'La Libertad Avanza en las actas oficiales; Elonce (08/2026) lo lista como PRO.'}
for s in sens:
    if s['nombre'] in BLOQ_NOTAS: s['bloque_nota']=BLOQ_NOTAS[s['nombre']]
provs={}
for p in sorted(set(s['provincia'] for s in sens)):
    ss=[s for s in sens if s['provincia']==p]
    vals=[s['pct_alineado'] for s in ss if s['pct_alineado'] is not None]
    valsd=[s['pct_alineado_solo_disputadas'] for s in ss if s['pct_alineado_solo_disputadas'] is not None]
    prom=round(sum(vals)/len(vals),1); promd=round(sum(valsd)/len(valsd),1)
    provs[p]=dict(senadores=[s['nombre'] for s in ss],promedio=prom,categoria=cat(prom),promedio_solo_disputadas=promd,categoria_solo_disputadas=cat(promd))
out=dict(meta=dict(titulo='Alineamiento de los senadores con el gobierno nacional',periodo='desde el 10/12/2025',actualizado='2026-10-25',
  regla='Por senador: votos coincidentes con la postura del gobierno / votos emitidos (afirmativo, negativo o abstención). La abstención vale medio voto y las ausencias no cuentan. Por provincia: promedio simple de sus 3 senadores. Afín ≥ 2/3 (66,7 %), opositora ≤ 1/3 (33,3 %), neutral entre ambos.',
  postura_gobierno='En todas las votaciones incluidas el gobierno impulsaba el proyecto o el pliego, así que el voto alineado es siempre el afirmativo.',
  indice_alternativo='pct_alineado_solo_disputadas excluye las votaciones casi unánimes, en las que el lado ganador sumó 90 % o más de los votos emitidos (Mercosur–UE 69-3 y los dos bloques de pliegos judiciales 64-0). Esas votaciones suben el índice de todos por igual y no muestran alineamiento.',
  composicion='Composición desde el 10/12/2025 según el acta oficial 2623 (11/02/2026), con los bloques de esa fecha. Es la misma en todas las actas usadas: no hubo reemplazos.',
  advertencias=['El sitio del Senado publica actas nominales solo hasta el 04/06/2026. Las votaciones posteriores salen de listas de prensa.','Inocencia Fiscal (dic. 2025) e Inocencia Fiscal II (sep. 2026) no tienen lista nominal publicada; entran solo los votos individuales que se encontraron.']),
  votaciones=out_v,senadores=sens,provincias=provs)
json.dump(out,open('/home/claude/sociopolitica/datos/afinidades/senadores.json','w'),ensure_ascii=False,indent=1)
for p,d in provs.items(): print(f"{p:32s} {d['promedio']:5} {d['categoria']:9s} | {d['promedio_solo_disputadas']:5} {d['categoria_solo_disputadas']}")
print(collections.Counter(d['categoria'] for d in provs.values()), collections.Counter(d['categoria_solo_disputadas'] for d in provs.values()))
