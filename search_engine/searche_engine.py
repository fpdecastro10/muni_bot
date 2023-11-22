import pandas as pd
import joblib

file_1 = {
    "path" : "./ordenanzas/ORD_13306.pdf",
    "nro_ordenanza" : "13306",
    "text" : """
    Articulo 1°.- DECLARASE como Ciudadano IIustre de la ciudad de Cordoba, en los terminos de la Ordenanza N° 12254, al Dr. Alejandro Roman Peirone, en reconocimiento a su trayectoria como Cardiologo Intervencionista Pediatrico.
    
    Articulo 2°.- COMUNIQUESE, publiquese, dese copia al Registro Municipal y archivese.
    """,
    "affair" :"Declara Ciudadano Ilustre de la Ciudad de Córdoba al DR. ALEJANDRO ROMÁN PEIRONE." 
}

file_2 = {
    "path" : "./ordenanzas/ORD_13376.pdf",
    "nro_ordenanza" : "13376",
    "text" : """
    Articulo 1°.- DESIGNASE con el nombre de “PLAZA HEROINAS DE MALVINAS” al espacio verde, cuya designacion catastral es: Distrito 31, Zona 05, Manzana 043 y Pamela 001, comprendido entre las calles Cabo Segundo Roque Luis Soria y Adoratrices de Barrio Inaudi de esta ciudad.
    
    Articulo 2°.- INCORPORASE en las bases oficiales la tematica correspondiente.
    Breve resena sobre el nombre:
        • Heroinas de Malvinas: aquellas mujeres que participaron de la “Guerra de las Malvinas”; conflicto belico desatado entre Argentina e Inglaterra desde el 2 de abril de 1982 hasta el 14 de junio del mismo aho. Algunas Io hicieron como personal militar y otras como civiles, se desempenaron como enfermeras, instrumentadoras quirurgicas, comisarios de abordo, tecnicas, oficiales, cadetes y radio operadoras. No solo brindaron sus saberes profesionales sino que tambien fueron el acompahamiento emocional de los soldados heridos en combate.
    
    Articulo 3°.- ACTUALIZASE la cartografia oficial de la ciudad, por medio de la Direccion de Catastro Municipal.

    Articulo 4°.- PROCEDASE a confeccionar la inscripcion de identificacion correspondiente que llevara la siguiente denominacion: “PLAZA HEROINAS DE MALVINAS”.

    Articulo 5°.- COMUNIQUESE, publiquese, dese copia al Registro Municipal y archivese.

""",
"affair" : "Designa con el nombre \"PLAZA HEROÍNAS DE MALVINAS\"."
}

file_3 = {
    "path" : "./ordenanzas/ORD_13213.pdf",
    "nro_ordenanza" : "13213",
    "text": """
    ARTíCULO 1°._DECLÁRESE como Ciudadano Ilustrede la ciudad de Córdoba, en los términos de la Ordenanza W 12254 al Señor lUIS RAMÓN lEHNER ROSALES, en reconocimiento por su trayectoria como físicoteórico, profesor, investigador y escritor.-----------

    ARTíCULO 2°._COMUNíQUESE, publíquese, dese copia al Registro Municipal y archívese.--

    DADA EN LA SALA DE SESIONES DEL CONCEJO DELIBERANTE DE LA CIUDAD DE CÓRDOBA, A LOS VEINTICINCO DrAS DEL MES DE NOVIEMBRE DE DOS MIL VEINTIUNO .- -
    """,
    "affair" : "Declara como Ciudadano Ilustre de la ciudad de Córdoba al Señor LUIS RAMÓN LEHNER ROSALES"
}
file_4 = {
    "path" : "./ordenanzas/ORD_13215.pdf",
    "nro_ordenanza" : "13215",
    "text": """
    ARTíCULO 1°.- ESTABL^CESE como “Semana de Concientizacion sobre el Trato Adecuado a Personas con Discapacidad", la primera semana del mes de diciembre de cada afio, en el marco de la conmemoraci6n del Dla Internacional de las Personas con Discapacidad, que se celebra el 3 de diciembre de cada afio.-----------------------------------------------------------------------------

    ARTíCULO 2°.- IMPLEMENTANSE, durante la primera semana del mes de diciembre de cada aflo, actividades de difusidn, promocidn de eventos, educacidn, concientizacion y capacitacidn sobre el Trato Adecuado a Personas con Discapacidad.-----------------------------------

    ARTíCULO 3°.- DESIGNASE a la Direccion de Proteccidn de Derechos. Participacion e Inclusión de las Personas con Discapacidad, o la que en un future la reemplace, como Autoridad de Aplicación de la presente Ordenanza.------------------------------------------------------------

    ARTíCULO 4°.- DER6GASE la Ordenanza N° 12926.

    ARTiCULO 5°.- COMUNÍQUESE, publíquese, dese copia al Registro Municipal y archívese.-

    DADA EN LA SALA DE SESIONES DEL CONCEJO DELIBERANTE DE LA CIUDAD DE CORDOBA, A LOS DOS DlAS DEL MES DE DICIEMBRE DE DOS MIL VEINTIUNO.------------
    """,
    "affair" : "Establece la “ Semana de Concientización sobre el Trato Adecuado a Personas con Discapacidad\""
} 

file_5 = {
    "path" : "./ordenanzas/ORD_13373.pdf",
    "nro_ordenanza" : "13373",
    "text": """
    Articulo 1°.- INSTITÚYASE el día 20 de agosto de cada afio como el “Dia Municipal del Activismo por la Diversidad Sexual”

    ARTíCULO 2°._COMUNíQUESE, publíquese, dese copia al Registro Municipal y archívese.--

    DADA EN LA SALA DE SESIONES DEL CONCEJO DELIBERANTE DE LA CIUDAD DE CÓRDOBA, A LOS VEINTICINCO DrAS DEL MES DE NOVIEMBRE DE DOS MIL VEINTIUNO .- -
    """,
    "affair" : "Instituye el dia 20 de Agosto como el \"Dia Municipal del Activismo por la Diversidad Sexual\""
}

# Hay que traducrila bien
file_6 = {
    "path" : "./ordenanzas/ORD_13205.pdf",
    "nro_ordenanza" : "13205",
    "text": """
    ARTICULO 1°.- RATIFICASE el Convenio Marco de Adhesion al Programa del Sistema Provincial de Historia Clinica Electronica Unica (HCEU), firmado el dia 3 de septiembre de 2021, entre el Ministerio de Salud de la Provincia de Cordoba, representado por el Ministro, Dr. Diego Hernan CARDOZO, y la Municipalidad de Cordoba representada por el Intendente, Dr. Martin LLARYORA; el que, como Anexo Unico, con dos (2) fojas forma parte integrante de la presente OrdenanZa.

    ARTICULO 2°.- COMUNIQUESE, publiquese, dese copia al Registro Municipal y archivese.--

    DADA EN LA SALA DE SESIONES DEL CONCEJO DELIBERANTE DE LA CIUDAD DE CORDOBA, ALOS VEINTIOCHO DIAS DEL MES DE OCTUBRE DE DOS MIL VEINTIUNO.--

    CONVENIO MARCO ADEHSION AL PROGRAMA DEL SISTEMA PROVINCIAL DE HISTORIA CLINICA ELECTRONICA UNICA (HCEU) ENTRE EL MINISTERIO DE SALUD DE LA PROVINCIA DE CORDOBA Y LA MUNICIPALIDAD DE CORDOBA
    
    Entre el Ministerio: de Salud de la Provincia de Córdoba, en adelante “el Ministerio” representado en este acto por su titular, Dr. Hestan Cardozo, con domicilio en
    Av. Vélez Sarsfiekd 2311 de la Ciudad de Cérdoba; y, por ta wlsicte Munitipalided de
    ee = Municipalidad”, representada en este acto por su Sefior
    inienvonte,. De. hartih Miguel Llaryora, con domicilio en Av. Marcelo T. de Alvear N° 120
    de fa Ciudad de Cérdoba, se acuerda la formalzacién del présente Convenio Marco

    que se regira por las siguientes clausulas: | | oo

    PRIMERA: Mediante el presente Convenio Marco “La Municipalidad’ adhiere al
    EN de! Sistema Provincial de Historia Cliniea Electronica Unica GiCEU), creado
    por 7 Ley Provincial. N° 10.590; e| cual tiene por finalidad estebleces tai de |
    Pre reciproca y vinculos de caracter permanente entre las ‘lad a jos sires
    de rene la implementacién del Sistema Provincial de Historia aden ya. referido
    oe la interrelacién, y asimismo lograr mayor eficacia en el ae de los fi
    propios de la mericionada Ley. — ~ | _

    

    —ae En el contexto del presente Convenio Marco, las partes disefiaran y
    ween convenios especificos en jos cuales se éetablecorir: cbjelioos y etna
    aan caer * ee designados para la direccién: y Hise tee de
    ee i os einaiearins de trabajo, los presupuestos correspondientes y las formas

    @ pago en caso de corresponder. ane went
    """
}

file_7 = {
    "path" : "./ordenanzas/ORD_13379.pdf",
    "nro_ordenanza" : "13379",
    "text": """
    Articulo 1°.- FACÚLTASE al Departamento Ejecutivo Municipal a ceder en comodato por el término de noventa y nueve (99) afios a la Asociacién de Rehabilitaci6n del Nifio Aislado (A.R.E.N.A), el uso continuado y exclusivo de parte del inmueble de Dominio Privado Municipal, designado catastralmente como Distrito 04, Zona 07, Manzana 004 y Parcela 001, cuya superficie es de 649,50 m?, perteneciente a una superficie mayor de 3.047 m?, ubicado en la calle Félix Aguilar, entre las calles Misiones y Paraguay, de Barrio Observatorio de esta ciudad.

    Articulo 2°.- COMUNIQUESE, publiquese, dese copia al Registro Municipal y archivese.

    DADA EN LA SALA DE SESIONES DEL CONCEJO DELIBERANTE DE LA CIUDAD DE CORDOBA, ALOS DIEZ DIAS DEL MES DE AGOSTO DE DOS MIL VEINTITRES.
    """,
    "affair" : "Facultra al DEM a ceder en comodato parte del inmueble de Dominio Privado Municipal"
}

file_8 = {
    "path" : "./ordenanzas/ORD_13389.pdf",
    "nro_ordenanza" : "13389",
    "text": """
    Articulo 1°.- DESIGNASE con el nombre de “PLAZOLETA ESCUADRON ALACRAN” al espacio verde sin nombre oficial, Nomenclatura Catastral Vigente: Distrito 04, Zona 09, Manzana 059 y Parcela 001, ubicado en Avenida Poeta Leopoldo Lugones entre calles Rondeau y Transito Caceres de Allende de Barrio Nueva Cérdoba de esta ciudad.

    Articulo 2°.- INCORPORASE en las bases oficiales la tematica correspondiente.

Breve resefia sobre el nombre:

Escuadron Alacran de Gendarmeria Nacional: Grupo de Gendarmeria altamente entrenado; incorporado al Ejército al llegar el Conflicto Bélico del Atlantico Sur, se autodenominaron con este nombre. Compuesto por 65 oficiales y suboficiales que participaron activamente en la defensa de las Islas Malvinas, muriendo en combate siete (7) de SUS integrantes.

Articulo 3°.- ACTUALIZASE la cartografia oficial de la ciudad, a través de la Direccién de Catastro Municipal.

Articulo 4°.- PROCEDASE a confeccionar la inscripcién de identificacién correspondiente que llevara la siguiente denominacion:

“PLAZOLETA ESCUADRON ALACRAN”, en honor a los Gendarmes caidos en Malvinas.

Articulo 5°.- COMUNIQUESE, publiquese, dese copia al Registro Municipal y archivese.

DADA EN LA SALA DE SESIONES DEL CONCEJO DELIBERANTE DE LA CIUDAD DE CORDOBA, A LOS CATORCE DIAS DEL MES DE SEPTIEMBRE DE DOS MIL VEINTITRES.
    """,
    "affair" : "Designa con el nombre \"PLAZOLETA ESCUADRÓN ALACRÁN\""
}

file_9 = {
    "path" : "./ordenanzas/ORD_13375.pdf",
    "nro_ordenanza" : "13375",
    "text": """
    Articulo 1°.- RATIFICASE el “Acuerdo Marco para el aprovechamiento Bioenergético de
gases asociados al Tratamiento de Lodos Cloacales de la ciudad de Cérdoba para la
Generacion Eléctrica Renovable”, firmado el dia 17 de abril de 2023, entre el Gobierno de la
Provincia de Cordoba, representado por el Ministro de Servicios Publicos, Dr. Ing. Fabian
LOPEZ; la Empresa Provincial de Energia de Cordoba, representada por su Presidente, Ing.
Luis GIOVINE; y la Municipalidad de Cérdoba, representada por el Intendente, Dr. Martin
LLARYORA; el que como Anexo Unico con cinco (5) fojas forma parte integrante de la
presente Ordenanza.

Articulo 2°.- COMUNIQUESE, publiquese, dese copia al Registro Municipal y archivese.

DADA EN LA SALA DE SESIONES DEL CONCEJO DELIBERANTE DE LA CIUDAD DE
CORDOBA, ALOS TRES DIAS DEL MES DE AGOSTO DE DOS MIL VEINTITRES.
    """,
    "affair" : "Ratifica el \"Acuerdo Marco para el aprovechamiento Bioenergético de gases asociados al Tratramiento\""
}

file_10 = {
    "path" : "./ordenanzas/ORD_13380.pdf",
    "nro_ordenanza" : "13380",
    "text": """
        Articulo 1°.- DESIGNANSE con los nombres que a continuacién se detallan, las arterias
comprendidas en el Distrito 10, Zonas 01 y 02, por innominadas, de los Barrios Altos del
Chateau y Parque Chateau Carreras de esta ciudad:

Parque del Chateau: a la actual calle Publica sin nombre oficial, que corre en sentido Este -
Oeste, comprendida entre manzanas Nomencliatura Catastral Vigente: 10-01-055 a 10-01-
066, 10-01-069 y 10-02-001; en el tramo comprendido entre calles Palo Santo y Ramén
Carcano.

Timbo: a la actual calle Publica sin nombre oficial, que corre en sentido Este - Oeste,
comprendida entre manzanas Nomencliatura Catastral Vigente: 10-01-066 a 10-01-068: en el
tramo comprendido entre calles Ambay y Quina.

Guindo: a la actual calle Publica sin nombre oficial, que corre en sentido Este - Oeste,
comprendida entre manzanas Nomenclatura Catastral Vigente: 10-01-064, 10-01-065, 10-
01-067 y 10-01-068; en el tramo comprendido entre calles Ambay y Quina.

Palo Santo: a la actual calle Publica sin nombre oficial, que corre en sentido Norte - Sur,
comprendida entre manzanas Nomenciatura Catastral Vigente: 10-01-060, 10-01-061, en el

tramo comprendido entre Manzanas 10-01-060 y 10-01-0671.

Curupay: a la actual calle Publica sin nombre Oficial, que corre en sentido Este - Oeste,
comprendida entre manzanas Nomenclatura Catastral Vigente: 10-01-033, 10-01-034, 10-
01-043, 10-01-044, y 10-01-054, en el tramo comprendido entre Manzana 10-01-033 y calle
Ambay.

Yerba Mate: a la actual calle Publica sin nombre oficial, que corre en sentido Este - Oeste,

comprendida entre manzanas Nomencliatura Catastral Vigente: 10-01-054, 10-01-055, 10-1573 - 2023. A 450 arios de la fundaci6n de la ciudad de Cérdoba”

01-058 y 10-01-059; en el tramo comprendido entre Manzanas 10-01-054, 10-01-059 y calle
Quina.

Quina: a la actual calle Publica sin nombre oficial, que corre en sentido Norte - Sur,
comprendida entre manzanas Nomenclatura Catastral Vigente: 10-01-055, 10-01-058, 10-
01-063, 10-01-065 a 10-01-067 y 10-01-069; en el tramo comprendido entre calles Timbé y
Yerba Mate.

Araucaria: a la actual calle Publica sin nombre oficial, que corre en sentido Norte - Sur,
comprendida entre manzanas Nomenclatura Catastral Vigente: 10-01-058, 10-01-063 a 10-
01-065, 10-01-067 y 10-01-068; en el tramo comprendido entre calles Timbé y Parque del
Chateau.

Ambay: a la actual calle Publica sin nombre oficial, que corre en sentido Norte - Sur,
comprendida entre manzanas Nomenclatura Catastral Vigente: 10-01-054, 10-01-055, 10-
01-058, 10-01-059, 10-01-062, 10-01-064 y 10-01-068, en el tramo comprendido entre calles
Timbo y Curupay.

Mandioca: a la actual calle Publica sin nombre oficial, que corre en sentido Norte - Sur,
comprendida entre manzanas Nomencliatura Catastral Vigente: 10-01-003, 10-01-005, 10-
01-056, 10-01-057, 10-01-066, 10-02-001 y 10-02-002; en el tramo comprendido entre calles
Soldado Ramon Angel Cabrera y Manzana 10-01-003.

Articulo 2°.- INCORPORANSE en las bases oficiales la tematica correspondiente de los
nombres propuestos en el articulo 1° de la presente Ordenanza. Los mismos refieren en su
mayoria a especies arbéreas nativas maduras, con diversas especies de flora y fauna
asociadas, en conjunto con el medio que las rodea conformando los ecosistemas forestales
naturales nativos, que en la Provincia de Cérdoba se identifica con el Bosque del Chaco
Humedo, Bosque del Chaco Serrano, Bosque del Espinal y Bosque del Caldén Pampeano.

Breve resefia sobre los nombres:

Parque del Chateau: predio de 14 hectareas que alberga multiples ejemplares de
nuestro bosque nativo, que rodea a la antigua casona de finales del siglo XIX
conocida como Chateau Carreras. Es una fracci6n del antiguo casco de estancia del
matrimonio David Carreras Ponce de Leén y Rosario Gavier, que luego de varias

refuncionalizaciones y puestas en valor, actualmente constituye un destacado y
visitado espacio de recreacién para el disfrute de la naturaleza y la prdactica
deportiva.

Timb6: especie encontrada en paises como Argentina, Brasil, Paraguay y Uruguay.
Su altura total puede alcanzar entre 25 y 45 metros, sus flores son blanco

amarillentas y sus frutos una legumbre negruzca.

Guindo: se encuentra en la ecorregién de los bosques patagénicos de Argentina y

Chile. Sus flores son verde amarillentas y sus frutos son conocidos como aquenios.

Palo Santo: esta presente en las ecorregiones de Argentina (Chaco Seco), Bolivia y
Paraguay. Puede alcanzar una altura de 6 a 20 metros.

Curupay: Sus ejemplares se encuentran en Brasil, Bolivia, Paraguay y en Argentina.
Forma parte de las ecorregiones Catamarca, Cérdoba, Chaco, Corrientes, Entre
Rios, Formosa, Jujuy, Misiones, Salta, Santiago del Estero y Tucuman. Su altura
puede variar entre unos 10 a 35 metros. Sus flores son amarillentas o color crema y

sus frutos son vainas.

Yerba Mate: esta especie puede encontrarse desde Colombia hasta Argentina. Su
Cultivo es propicio en las provincias de Corrientes y Misiones. No sdlo tiene uso
alimenticio, sino también medicinal.

Quina: en Argentina pertenece a las ecorregiones del espinal, estepa patagonia,
monte de llanuras, mesetas y pampa. Se encuentra presente también en paises
como Brasil y Uruguay. Su altura puede alcanzar un metro. Sus flores son blancas.

Araucaria: forma parte del paisaje patagénico de Argentina y Chile. Su altura ronda
los 30 a 50 metros teniendo un diametro de 1 y 1,5 metros. Sus flores son amarillo

anaranjadas y sus frutos son pifas de castafio oscuras.

Ambay: en Argentina sus ejemplares se encuentran en las ecorregiones del Chaco
Humedo, Esteros del Ibera y la Selva Paranaense. Su altura puede llegar a alcanzar
entre 3 a 15 metros y es conocida por sus propiedades medicinales. La especie

existe en otros paises como Brasil y Paraguay.

Mandioca: especie existente en paises como Argentina, Brasil, Paraguay y Uruguay.
En Argentina se encuentra en las ecorregiones de los Esteros del Ibera y la Selva
Paranaense. Su altura puede llegar a alcanzar entre 2 a 5 metros.

Articulo 3°.- ACTUALIZASE la cartografia oficial de la ciudad, a través de la Direccién de
Catastro Municipal.

Articulo 4°.- PROCEDASE a confeccionar las inscripciones de_ identificacién
correspondientes que llevaran la siguiente denominacion:

“Parque del Chateau”
“Timbo”
“Guindo”

“Palo Santo”
“Curupay”
“Yerba Mate”
“Quina”
“Araucaria”
“Ambay”
“Mandioca”.

Articulo 5°.- COMUNIQUESE, publiquese, dese copia al Registro Municipal y archivese.

DADA EN LA SALA DE SESIONES DEL CONCEJO DELIBERANTE DE LA CIUDAD DE
CORDOBA, ALOS DIECISIETE DIAS DEL MES DE AGOSTO DE DOS MIL VEINTITRES.

""",
"affair" : "Designa nombres a calles de Barrio Altos del Chateau y Parque Chateau Carreras"
}


file_11 = {
    "path" : "./ordenanzas/ORD_13387.pdf",
    "nro_ordenanza" : "13387",
    "text": """
    Articulo_1°.- PROHIBICION DE VEHICULOS DE TRACCION A SANGRE ANIMAL.
Prohibase la circulacién de vehiculos de traccién a sangre animal y su utilizacién para el
transporte de cargas y/o personas, en todas sus formas y cualquiera sea la especie, en la
via publica de la ciudad de Cérdoba.

Articulo 2°. EXCEPCION. Quedan exceptuados de la prohibicién del articulo 1° de la
presente Ordenanza, las Fuerzas Armadas nacionales, las Fuerzas de Seguridad
nacionales, provinciales y municipales y la utiizacién o circulacién de vehiculos de traccién a
sangre animal en desfiles, muestras y exhibiciones.

Articulo 3°.- AUTORIDAD DE APLICACION. La Autoridad de Aplicacién de la presente
Ordenanza es la Secretaria de Gestion Ambiental y Sostenibilidad, 0 fa que en el futuro la
reemplace

Articulo 4°.- ATRIBUCIONES DE LA AUTORIDAD DE APLICACION. La Autoridad de
Aplicacién tiene las siguientes atribuciones:

a) Entregar motovehiculos 0 herramientas de trabajo en el marco del “Programa de
Modernizacién de Medios de Trabajo para Recuperadores Urbanos”, por si o a través
del Ente de Servicios y Obras Publicas —Ordenanza N° 12479-, procurando la
capacitacién y reinsercién laboral a los fines de alcanzar la inclusién social;

b) Disponer las medidas necesarias respecto de los animales recuperados en el marco
de la presente Ordenanza, previa evaluacién del estado de salud, pudiendo dar
intervencién al Ente Municipal BioCérdoba -Ordenanza N° 13078- para su recepcién,
evaluacion, guarda, tenencia y cuidado;

) Planificar, coordinar y ejecutar acciones conjuntas con organizaciones sin fines de
lucro cuyo objeto sea la defensa, proteccién, rescate y/o rehabilitaci6n de animales,
respecto de la recepcién, tenencia, guarda y ct

 
do de animales recuperados;

q) Planificar, coordinar, articular y ejecutar demas acciones con el Ente de Servicios y
Obras Publicas ~Ordenanza N° 12479- y con el Ente Municipal BioCordoba —
Ordenanza N° 13078-, conforme a sus respectivas atribuciones;

e) Dictar las disposiciones necesarias para el cumplimiento de la presente Ordenanza, y

f) Establecer el cronograma del articulo 9° de la presente Ordenanza.

Articulo MODIFICASE el articulo 220 de la Ordenanza N° 12468 —Cédigo de
Convivencia Ciudadana-, el que queda redactado de la siguiente manera:

 

“Art. 220° QUIEN circule en vehiculo de traccién a sangre animal o lo utilice para
transporte de carga o personas en la via publica, seré sancionado con multa de treinta
(30) a cincuenta (50) (U.E.M,). Cuando en el vehiculo de traccién a sangre animal
hubiere personas menores de edad, la sancién se agravaré de cincuenta (50) a sesenta
(60) (U.E.M.). Accesoriamente, e! Juez puede disponer e! decomiso de la carga y el
secuestro del vehiculo y el animal. En cuyo supuesto deberd articular con la Secretaria
de Gesti6n Ambiental y Sostenibilidad, o la que en un futuro la sustituya, a los fines de
la recepcién, evaluaci6n, quarda, tenencia y cuidado del animal.”

Articuio 6°.- INCORPORASE como articulo 220 bis de la Ordenanza N° 12468 ~Cédigo de
Convivencia Ciudadana-, el siguiente texto:

“Art. 220° bis.- QUIEN contratare, utilizare 0 aprovechare el transporte de cargas o
personas con vehiculos de traccién a sangre animal, seré sancionado con multa de
treinta (30) a cincuenta (50) (U.E.M.).”

Articulo 7°. MODIFICASE el articulo 6° de la Ordenanza N° 9981 -Cédigo de Transito-, el
cual queda redactado de la siguiente manera:

“Art. 6°- A efectos de la an) de la presente Ordenanza, se adoptan las

siguientes definiciones:

ACCIDENTE DE TRANSITO: Es un suceso o acontecimiento subito, inesperado y no
premeditado, causado, al menos, por un vehiculo motorizado en movimiento en la via

publica y a raiz del que se producen dafios materiales, lesiones o muertes.

ACERA: Sector de la via publica, ubicado entre la calzada y la linea de edificacién
municipal 0 baranda de puentes, destinado exclusivamente al desplazamiento de

peatones.

ACOPLADO: Vehiculo no automotor destinado a ser remolcado, cuya construccién es
tal que ninguna parte de su peso se transmite a otro vehiculo; se incluyen en esta
definicién las casas rodantes.

AUTOMOTOR: Vehiculo provisto de un dispositivo mecanico de autopropulsi6n,

utilizado para el transporte de personas, animales o cosas por la via publica.

AUTOMOVIL: Automotor para el transporte de personas de hasta ocho (8) plazas -
excluido el conductor - con cuatro o mas ruedas, y los de tres ruedas que excedan los
mil (1.000) kg. de peso.

AUTOPISTA: Via multicarril sin cruces a nivel con otra calle o ferrocarril, con calzadas
separadas fisicamente y con limitaciébn de ingreso directo desde los predios frentistas

lindantes.

AVENIDA: Via publica multicarril, de circulacién en zonas urbanas, integrada por las

aceras y la calzada, presentando esta ultima un ancho de mas de nueve (9) metros.

BALIZA: Sefial fija o mévil con luz propia o retrorreflectora, que se coloca como

advertencia o aviso de precaucién.

BANQUINA: Zona adyacente a la calzada de una carretera, destinada a brindar mayor

seguridad al transito de vehiculos.

BICICLETA: Vehiculo de dos ruedas que es propulsado por mecanismos, con el
esfuerzo de quien lo utiliza, pudiendo ser multiple, de hasta cuatro (4) ruedas alineadas.

CALLE: Via publica de circulacién en onas urbanas, integrada por las aceras y la
calzada, presentando esta ultima un ancho de hasta nueve (9) metros.
CALZADA: Sector de la via publica destinado exclusivamente al transito de vehiculos.

CAMION: Vehiculo automotor destinado al transporte de carga, de mas de tres mil
quinientos (3.500) kg. de peso total.

CAMIONETA: Automotor destinado al transporte de carga de hasta tres mil quinientos
(3.500) kg. de peso total.

CARGA GENERAL: Elementos que se transportan acondicionados en lios, fardos, a
granel, cuyas unidades son de dimensiones inferiores a las del vehiculo que las
transporta.

CARGA INDIVISIBLE: Aquellos elementos que, por sus caracteristicas, forman
unidades que de algun modo exceden las dimensiones normales del vehiculo que los
transporta, tales como vigas, perfiles y varillas de hierro, rollizos, columnas de hierro o
madera, bloques de piedra, piezas estructurales, maquinas, etcétera.

CARGA UTIL: Es el peso de Ia carga de un vehiculo, excluido el peso propio del
mismo.

CARGA Y DESCARGA: Accién de trasladar cosas desde o hacia vehiculos detenidos
en la via publica.

CARRIL: Parte de la calzada, debidamente sefializada, destinada al transito de una
sola hilera de vehiculos.

CICLOMOTOR: Vehiculo biciclo accionado a motor de hasta setenta (70) cc. de
cilindrada.

CICLOVIA: Sector de Ia via especialmente dispuesto para la circulacién de peatones,
bicicletas y Vehiculos Eléctricos de Movilidad Individual (VEMI).

CONDUCTOR: Persona que tiene a su cargo y bajo su responsabilidad el manejo por la

via publica de un vehiculo, teniendo también la obligacién de respetar y hacer respetar

a sus transportados la normativa de transito vigente.

CONTENEDOR: Estructura modular transportable, destinada al transporte de carga y a

prestar servicio temporario y estatico en la via publica e incapaz de movilizarse sino por
medio de una unidad adaptada a esos efectos.

DARSENA: Construcci6n vial ubicada fuera de! borde de las calzadas, de las vias de
circulaci6n principal, destinada a detencion transitoria de vehiculos para operaciones de

ascenso o descenso de pasajeros, carga o descarga o para realizar un giro.

ENCRUCIJADA: Sector de la via en donde se cruzan dos o més calles, caminos,

carreteras.

GRUA: Vehiculo automotor especialmente adaptado para trasladar otro vehiculo
mediante un dispositivo de enganche o transporte.

MAQUINARIA ESPECIAL: Todo artefacto disefiado para un fin especifico distinto a
circular y dotado de un dispositivo de autopropulsién o de elementos que le permiten ser

remolcado en la via publica.

MICROOMNIBUS O COLECTIVO: Automotor para el transporte de pasajeros con
capacidad de once (11) a treinta (30) personas sentadas como maximo, excluido el
conductor.

MOTOCICLETA: Vehiculo biciclo accionado a motor, de mas de setenta (70) cc. de
cilindrada.

MOTOVEHICULO: Seran considerados motovehiculos, a los fines de esta Ordenanza,
los siguientes vehiculos autopropulsados a motor: ciclomotores, motocicletas, triciclos y
cuadriciclos.

OMNIBUS: Automotor con capacidad superior a treinta (30) pasajeros sentados
excluidos el conductor, acompafiante o guarda.

PESO TOTAL: Es el peso de un vehiculo, detenido y en orden de marcha incluido el de

su conductor y de cualquier otra persona transportada.
PESO MAXIMO APROXIMADO: Es el peso maximo permitido, incluyéndose la tara y la
carga Util.

REMIS: Vehiculo automotor habilitado por la Autoridad de Aplicacié6n destinado al

transporte de personas, con o sin equipaje, cuyos servicios Unicamente pueden
contratarse, en forma personal o por teléfono, a través de agencias autorizadas y deben
ser retribuidos de conformidad a lo que indique su cuentakildmetros.

SEMIAUTOPISTA: Via multicarril con cruces a nivel con otras calles o vias férreas.
REMOLQUE: Todo vehiculo apto para ser arrastrado por un automotor.

SENAL DE TRANSITO: Dispositivo, marca o signo colocado o erigido por la autoridad
competente, que tiene por fin dirigir, advertir, regular e informar sobre las contingencias
que se presentan al usuario de la via publica.

TARA: Es el peso del vehiculo desprovisto de su carga Util.

TAXI: Vehiculo automotor habilitado por la Autoridad de Aplicacién destinado
exclusivamente al transporte de personas, con o sin equipaje, cuyos servicios pueden
ser contratados en la via publica y deben ser retribuidos mediante el pago de la suma
de dinero que indique el reloj taximetro.

TROLEBUS: Vehiculo impulsado por energia eléctrica, que circula montado sobre
ruedas neumaticas, destinado al transporte de pasajeros.

VEHICULO DE TRACCION A SANGRE ANIMAL: es aquel cuya propulsién esté
generada por la energia proveniente de la accién muscular de animales.

VEHICULO DETENIDO: Es aquél que se encuentra inmovilizado en la via publica, por
el tiempo estrictamente necesario para el ascenso y descenso de pasajeros y carga o

descarga de equipajes.

VEHICULO ELECTRICO DE MOVILIDAD INDIVIDUAL (VEMI): Vehiculo concebido
para la micro movilidad urbana que esta dotado de una Unica plaza y es propulsado

exclusivamente por motores eléctricos.

VEHICULO ESTACIONADO: Vehiculo detenido en la via publica, con o sin conductor,
por mas tiempo que el necesario para el ascenso y descenso de pasajeros, carga oO

descarga de equipajes.

VIA PUBLICA: Todo espacio incorporado’ al dominio publico utilizado para el

desplazamiento de personas de un lugar a otro, por si o mediante vehiculos,
incluyéndose en esta definicién a los caminos, carreteras, puentes, alcantarillas, aceras,

calles, pasajes, sendas, pasos de cualquier naturaleza y areas incorporadas al mismo
fin, por la autoridad competente.”

Articulo 8°.- INCORPORASE como inciso m) al articulo 74 de la Ordenanza N° 9981 —
Cédigo de Transito— el siguiente texto:

“Art. 74°.- ESTAN prohibidas en la via publica, las siguientes conductas:

m) Conducir un vehiculo de traccién a sangre animal.”

Articulo 9°.- CLAUSULA TRANSITORIA. Las prohibiciones establecidas en el articulo 1°
de la presente Ordenanza, en los articulos 220 y 220 bis de la Ordenanza N° 12468 —Cédigo
de Convivencia Ciudadana- y en el articulo 74 inciso m) de la Ordenanza N° 9981 —Cédigo
de Transito— se aplicaran de forma progresiva dentro del plazo de un (1) afio a partir de la
entrada en vigencia de la presente Ordenanza, conforme al cronograma que establezca la
Autoridad de Aplicacién, sin perjuicio de las acciones conducentes a la implementacién de la
Ordenanza en el menor tiempo posible, procurando la prevencién, concientizacién y
colaboraci6n de las partes involucradas.

Articulo 10.- DEROGASE la Ordenanza N° 10125 -Inscripcién de vehiculos de traccién a
sangre-.

Articulo 11.- COMUNIQUESE, publiquese, dese copia al Registro Municipal y archivese.

DADA EN LA SALA DE SESIONES DEL CONCEJO DELIBERANTE DE LA CIUDAD DE
CORDOBA, ALOS SIETE DIAS DEL MES DE SEPTIEMBRE DE DOS MIL VEINTITRES.
""",
"affair" : "Prohibe circulacion de vehiculos de traccion a sangre animal (Modifica Ord. 12468 y 9981 y deroga la"
}

dict_files = [
    file_1,
    file_2,
    file_3,
    file_4,
    file_5,
    # file_6,
    file_7,
    file_8,
    file_9,
    file_10,
    file_11
]

def list_of_files(keys, list_files):
    return_dict = {}
    for file in list_files:
        for key in keys:
            if key in return_dict:
                return_dict[key].append(file[key])
            else:
                return_dict[key] = [file[key]]
    return return_dict

df_ordenanza = pd.DataFrame(list_of_files(["path","nro_ordenanza","text","affair"],dict_files))

def query_search_engine(query):
    tokenized_query = query.lower().split(" ")
    loaded_bm25_model = joblib.load('modelo_bm25.pkl')
    results = loaded_bm25_model.get_top_n(tokenized_query, df_ordenanza.values, n=3)
    return results
