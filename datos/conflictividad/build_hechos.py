import json,collections,sys,os
import numpy as np
BASE=os.path.dirname(os.path.abspath(__file__))
# Período: últimos 12 meses hasta la fecha de corte (argumento AAAA-MM-DD)
CORTE=sys.argv[1] if len(sys.argv)>1 else '2026-10-30'
DESDE=str(int(CORTE[:4])-1)+CORTE[4:]
PROV={'BUENOS AIRES','CATAMARCA','CHACO','CHUBUT','CIUDAD AUTONOMA DE BUENOS AIRES','CORDOBA','CORRIENTES','ENTRE RIOS','FORMOSA','JUJUY','LA PAMPA','LA RIOJA','MENDOZA','MISIONES','NEUQUEN','RIO NEGRO','SALTA','SAN JUAN','SAN LUIS','SANTA CRUZ','SANTA FE','SANTIAGO DEL ESTERO','TIERRA DEL FUEGO','TUCUMAN'}
CATS={'paro','toma','pol','mil','mpac','mvio','aten','carc','saq'}
DANOS={'sin daños','menores','importantes','graves'}
# coordenadas de ciudad (centro urbano), por prefijo de 'lugar'
COORD=[('San Fernando del Valle de Catamarca',-28.4696,-65.7795),('San Miguel de Tucumán',-26.8083,-65.2176),('Santa Fe',-31.6333,-60.7000),
 ('Santiago del Estero',-27.7951,-64.2615),('Santa Rosa',-36.6167,-64.2833),('La Plata',-34.9214,-57.9545),('La Rioja',-29.4131,-66.8558),
 ('Bahía Blanca',-38.7183,-62.2663),('Paraná',-31.7319,-60.5238),('Concordia',-31.3929,-58.0209),('Corrientes',-27.4692,-58.8306),
 ('Resistencia',-27.4606,-58.9839),('Formosa',-26.1849,-58.1731),('Posadas',-27.3671,-55.8961),('Jardín América',-27.0436,-55.2297),
 ('Rawson',-43.3002,-65.1023),('Esquel',-42.9114,-71.3195),('Cipolletti',-38.9333,-67.9833),('Viedma',-40.8135,-62.9967),
 ('Añelo',-38.3544,-68.7881),('Ushuaia',-54.8019,-68.3030),('Río Grande',-53.7877,-67.7095),('Las Heras',-46.5419,-68.9353),
 ('Andalgalá',-27.5819,-66.3175),('Fiambalá',-27.6866,-67.6147),('Tartagal',-22.5164,-63.8013),('Coronel Juan Solá',-23.4667,-62.8833),
 ('Benjamín Paz',-26.7000,-65.2833),
 ('Esquina',-30.0144,-59.5272),('Chascomús',-35.5750,-58.0089),('Pampa del Indio',-26.0500,-59.9333),('San Vicente',-26.9958,-54.4831),('San Luis',-33.3017,-66.3378),
 ('CABA',-34.6037,-58.3816),('Nacional',-34.6037,-58.3816),('General Roca',-39.0333,-67.5833),('Rosario',-32.9468,-60.6393),
 ('San Salvador de Jujuy',-24.1858,-65.2995),('Mendoza',-32.8895,-68.8458),('Córdoba',-31.4201,-64.1888),('Mar del Plata',-38.0055,-57.5426),
 ('Neuquén',-38.9516,-68.0591),('San Juan',-31.5375,-68.5364),('Salta',-24.7821,-65.4232),('Río Gallegos',-51.6230,-69.2168),
 ('San Fernando',-34.4417,-58.5594),('La Matanza',-34.7219,-58.5306),('Moreno',-34.6500,-58.7900),('Avellaneda',-34.6625,-58.3653),
 ('Pilar',-34.4587,-58.9142),('Puente Neuquén–Cipolletti',-38.9339,-67.9903)]
L=[json.loads(l) for l in open(os.path.join(BASE,'ev.jsonl'))]
out=[];err=[]
L=[e for e in L if DESDE<=e['fecha']<=CORTE]
for i,e in enumerate(sorted(L,key=lambda x:(x['fecha'],x['lugar']))):
    assert e['provincia'] in PROV, e; assert e['categoria'] in CATS, e
    c=[x for x in COORD if e['lugar'].startswith(x[0])]
    if not c: err.append(e['lugar']); continue
    nivel,just=e['danos']; nivel=None if nivel not in DANOS else nivel
    r=dict(id=f"h{i+1:03d}",fecha=e['fecha'],categoria=e['categoria'],lugar=e['lugar'],provincia=e['provincia'],lat=c[0][1],lon=c[0][2],
       personas_min=e['personas_min'],personas_max=e['personas_max'],detenidos=e['detenidos'],procesados=e['procesados'],muertos=e['muertos'],heridos=e['heridos'],
       danos=dict(nivel=nivel,justificacion=just),descripcion=e['descripcion'],fuentes=e['fuentes'])
    if e.get('nota'): r['nota']=e['nota']
    out.append(r)
if err: print('SIN COORD',err); sys.exit(1)
meta=dict(titulo='Conflictividad social en Argentina: hechos significativos',periodo=DESDE+' a '+CORTE,actualizado=CORTE,
  categorias={'paro':'Paros sindicales','toma':'Tomas de empresas (y de organismos, aclarado en nota)','pol':'Conflictos policiales (incluye acuartelamientos)','mil':'Conflictos militares','mpac':'Manifestaciones pacíficas','mvio':'Manifestaciones con violencia o incidentes','aten':'Atentados e intentos de asesinato','carc':'Motines en cárceles y comisarías','saq':'Saqueos'},
  convenciones={'personas_min/personas_max':'Rango entre la estimación más baja (policía o prensa) y la más alta (organizadores). Si hay una sola cifra, va en las dos puntas o solo en la que corresponde según quién la dio; ver nota. null = ninguna fuente dio una cifra.',
   'detenidos/heridos/muertos':'Cifra publicada; si las fuentes difieren se toma la más completa y las demás van en nota. null = no informado. 0 = la fuente dice expresamente que no hubo, o la crónica completa no menciona ninguno (en ese caso está aclarado).',
   'procesados':'Personas con imputación o cargos formales informados; null si no se informó. Ver nota en cada caso.',
   'danos.nivel':'sin daños | menores | importantes | graves; null = sin dato.',
   'lat/lon':'Coordenadas del centro de la ciudad, no del punto exacto. Los paros nacionales se ubican en CABA y llevan aclaración en nota.'},
  advertencias=['Cobertura parcial: '+str(len(out))+' hechos. Es una selección de hechos significativos con crónica verificable, no un censo: faltan muchas marchas semanales de jubilados, cortes de ruta y paros provinciales. Santiago del Estero, Formosa, La Rioja y San Juan siguen con 3 casos, y Tucumán, San Luis, Chaco, Corrientes y Tierra del Fuego con 4.','Muchos hechos tienen una sola fuente; algunos se apoyan en medios partidarios o militantes (La Izquierda Diario, FARCO, El Cohete a la Luna) y otros en crónicas previas del mismo día. Está indicado en cada nota.','No se encontraron saqueos ni conflictos militares en el período con las búsquedas hechas. Eso no prueba que no los haya habido.'])
piq=dict(fuente='Diagnóstico Político, citado por Chequeado (01/03/2026) y por La Nación (13/01/2026)',
  urls=['https://chequeado.com/nota/javier-milei-en-la-apertura-de-sesiones-2026-hemos-terminado-con-los-piquetes-de-una-vez-por-todas-los-cuales-pasaron-de-9-mil-por-ano-a-0','https://www.lanacion.com.ar/politica/los-piquetes-se-redujeron-mas-del-527-desde-que-asumio-milei-hay-menos-protestas-de-las-nid13012026/'],
  anual={'2023':8239,'2024':5996,'2025':3893},
  provincias_2025={'BUENOS AIRES':616,'SANTA FE':369,'NEUQUEN':304,'MISIONES':269,'CIUDAD AUTONOMA DE BUENOS AIRES':240},
  mensual=None,
  nota='No se encontró una serie mensual publicada para oct. 2025–oct. 2026. Las notas de prensa a las que se accedió citan solo los totales anuales y el ranking provincial de 2025. 2025 es el valor más bajo desde 2011, según DP.')
json.dump(dict(meta=meta,hechos=out,piquetes=piq),open(os.path.join(BASE,'hechos.json'),'w'),ensure_ascii=False,indent=1)
print(len(out),collections.Counter(h['categoria'] for h in out),collections.Counter(h['provincia'] for h in out))
print('con >=2 fuentes',sum(len(h['fuentes'])>=2 for h in out))

# puntos.json: coordenadas de pantalla del mapa base (argentina.json, 420x900).
# Ciudades ya proyectadas por geo.mjs: se reutiliza su punto exacto (tomado del puntos.json anterior).
# Ciudades nuevas: polinomio de grado 3 en (lat, lon) ajustado sobre las ya proyectadas (error < 0,2 px en validación cruzada).
old=json.load(open(os.path.join(BASE,'hechos.json')))  # recién escrito
prevh=json.load(open(os.path.join(BASE,'puntos_ref.json')))
ref={tuple(k.split(',')): v for k,v in prevh.items()}
ref={(float(a),float(b)):v for (a,b),v in ref.items()}
def F(la,lo,d=3): return [la**i*lo**j for i in range(d+1) for j in range(d+1-i)]
X=np.array([F(*k) for k in ref]);Bm=np.array(list(ref.values()))
Cf=[np.linalg.lstsq(X,Bm[:,j],rcond=None)[0] for j in range(2)]
pts={}
for h in out:
    k=(h['lat'],h['lon'])
    if k not in ref:
        f=np.array(F(*k)); ref[k]=[round(float(f@Cf[0]),1),round(float(f@Cf[1]),1)]
    pts[h['id']]=ref[k]
json.dump(pts,open(os.path.join(BASE,'puntos.json'),'w'),separators=(',',':'))
json.dump({f"{a},{b}":v for (a,b),v in ref.items()},open(os.path.join(BASE,'puntos_ref.json'),'w'),ensure_ascii=False,indent=0)
print('puntos',len(pts))
