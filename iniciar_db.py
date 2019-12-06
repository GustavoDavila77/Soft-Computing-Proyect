from pymongo import MongoClient
from Filtros import Filter
from Fact import Fact
from Rules import Rule
from tipo_aprendizaje import Tipo

# Creo una lista de objetos Ruta a insertar en la BD
filters = [Filter("caracteristica"),Filter("tipo de aprendizaje")]

facts = [Fact("5de98b24187f6d3718c915e5","involucrarse en actividades nuevas","¿Se involucra totalmente y sin prejuicios en experiencias academicas nuevas?",1,['si','no']),
        Fact("5de98b24187f6d3718c915e5","actuar sin pensar","¿Tiende a actuar primero y pensar después?",1,['si','no']),
        Fact("5de98b24187f6d3718c915e5","planes largo plazo","¿Le aburre ocuparse de planes a largo plazo?",1,['si','no']),
        Fact("5de98b24187f6d3718c915e5","trabajar en grupo","¿Prefiere trabajar en grupo?",1,['si','no']),
        Fact("5de98b24187f6d3718c915e5","interpretar datos","¿Le cuesta asimilar, analizar e interpretar datos?",1,['si','no']),
        Fact("5de98b24187f6d3718c915e5","trabajar solo","¿le cuesta trabajar solo?",1,['si','no']),
        Fact("5de98b24187f6d3718c915e5","perspectivas","¿Le gusta analizar desde muchas perspectivas?",1,['si','no']),
        Fact("5de98b24187f6d3718c915e5","conclusion","¿recoge datos y analiza detalladamente antes de llegar a una conclusión?",1,['si','no']),
        Fact("5de98b24187f6d3718c915e5","implicaciones","¿es precavido/a y analiza las implicaciones de cualquier acción antes de ponerse en movimiento?",1,['si','no']),
        Fact("5de98b24187f6d3718c915e5","observar","¿en las reuniones observa y escucha antes de hablar procurando pasar desapercibido/a?",1,['si','no']),
        Fact("5de98b24187f6d3718c915e5","secuencias","¿piensa de manera secuencial, paso a paso?",1,['si','no']),
        Fact("5de98b24187f6d3718c915e5","sintetizar info","¿le gusta analizar y sintetizar la información?",1,['si','no']),
        Fact("5de98b24187f6d3718c915e5","juicios subjetivos","¿se siente incomodo/a con juicios subjetivos?",1,['si','no']),
        Fact("5de98b24187f6d3718c915e5","ambiguedad","¿se siente incomodo/a con actividades sin una lógica clara o que implique ambiguedad?",1,['si','no']),
        Fact("5de98b24187f6d3718c915e5","practica","¿le gusta buscar ideas y ponerlas en practica?",1,['si','no']),
        Fact("5de98b24187f6d3718c915e5","resolver problemas reales","¿le gusta resolver problemas que se apliquen en la realidad?",1,['si','no']),
        Fact("5de98b24187f6d3718c915e5","mejorar","¿siempre esta buscando una mejor manera de hacer las cosas?",1,['si','no']),
        Fact("5de98b24187f6d3718c915e5","teoria-practica","¿aprende mejor con actividades que relacionen teoria y practica?",1,['si','no']),
        Fact("5de98b24187f6d3718c915e5","sin finalidad","¿se le dificulta aprender con actividades que no tienen una finalidad aparente?",1,['si','no'])
        ]

rules = [Rule("5de9c9a3187f6d23648e4f5b","5de9c9c596e2ab2fd42a2578",0.4),
        Rule("5de9c9a3187f6d23648e4f5c","5de9c9c596e2ab2fd42a2578",0.7),
        Rule("5de9c9a3187f6d23648e4f5d","5de9c9c596e2ab2fd42a2578",0.5),
        Rule("5de9c9a3187f6d23648e4f5e","5de9c9c596e2ab2fd42a2578",0.2),
        Rule("5de9c9a3187f6d23648e4f5f","5de9c9c596e2ab2fd42a2578",0.3),
        Rule("5de9c9a3187f6d23648e4f60","5de9c9c596e2ab2fd42a2578",0.4),
        Rule("5de9c9a3187f6d23648e4f61","5de9ca5496e2ab2fd42a2579",0.5),
        Rule("5de9c9a3187f6d23648e4f62","5de9ca5496e2ab2fd42a2579",0.7),
        Rule("5de9c9a3187f6d23648e4f63","5de9ca5496e2ab2fd42a2579",0.4),
        Rule("5de9c9a3187f6d23648e4f64","5de9ca5496e2ab2fd42a2579",0.3),
        Rule("5de9c9a3187f6d23648e4f65","5de9ca7496e2ab2fd42a257a",0.5), 
        Rule("5de9c9a3187f6d23648e4f66","5de9ca7496e2ab2fd42a257a",0.3), 
        Rule("5de9c9a3187f6d23648e4f67","5de9ca7496e2ab2fd42a257a",0.4),
        Rule("5de9c9a3187f6d23648e4f68","5de9ca7496e2ab2fd42a257a",0.5),
        Rule("5de9c9a3187f6d23648e4f69","5de9ca9d96e2ab2fd42a257b",0.2), 
        Rule("5de9c9a3187f6d23648e4f6a","5de9ca9d96e2ab2fd42a257b",0.8),
        Rule("5de9c9a3187f6d23648e4f6b","5de9ca9d96e2ab2fd42a257b",0.3),
        Rule("5de9c9a3187f6d23648e4f6c","5de9ca9d96e2ab2fd42a257b",0.5),
        Rule("5de9c9a3187f6d23648e4f6d","5de9ca9d96e2ab2fd42a257b",0.6)
        ]

types = [Tipo("5de9c9c596e2ab2fd42a2578","estudiante activo",0.0),
                Tipo("5de9ca5496e2ab2fd42a2579","estudiante reflexivo",0.0),
                Tipo("5de9ca7496e2ab2fd42a257a","estudiante teórico",0.0),
                Tipo("5de9ca9d96e2ab2fd42a257b","estudiante pragmático",0.0)
                ]
#Conexión al Server de MongoDB Pasandole el host y el puerto
mongoClient = MongoClient('localhost',27017)


# Conexión a la base de datos --nombre db 
db = mongoClient.AprendizajeES

# Obtenemos una colecciones para trabajar con ellas
collection = db.filters

fact_collections = db.facts

rule_collections = db.rules

type_collections = db.tipos

# ingresamos los objetos rutas (o documentos en Mongo) en la coleccion filters
def fill_filter():
    try:
        for filter in filters:
            #convierte el objeto en colección
            obj = collection.insert_one(filter.toDBCollection())
            print('id de doc insert: '+ str(obj.inserted_id))
    except:
        print("imposible finished the process")
    
def fill_facts():
    try:
        for fact in facts:
            #convierte el objeto en colección
            obj = fact_collections.insert_one(fact.toDBCollection())
            print('id de doc insert: '+ str(obj.inserted_id))
    except ValueError:
        print("imposible to connect with database")

def fill_rules():
    try:
        for rule in rules:
            #convierte el objeto en colección
            obj = rule_collections.insert_one(rule.toDBCollection())
            print('id de doc insert: '+ str(obj.inserted_id))
    except ValueError:
        print("imposible to connect with database")

def fill_tipos():
    try:
        for t in types:
            #convierte el objeto en colección
            obj = type_collections.insert_one(t.toDBCollection())
            #print('id de doc insert: '+ str(obj.inserted_id))
    except ValueError:
        print("imposible to connect with database") 

# PASO FINAL: Cerrar la conexion
mongoClient.close()
