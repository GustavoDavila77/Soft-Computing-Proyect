from pymongo import MongoClient
from iniciar_db import fill_filter, fill_rules, fill_tipos
from iniciar_db import fill_facts
from Agendas import Agenda


#Conexión al Server de MongoDB Pasandole el host y el puerto
mongoClient = MongoClient('localhost',27017)

# Conexión a la base de datos 
db = mongoClient.AprendizajeES

filter_collections = db.filters
facts_collections = db.facts
rules_collections = db.rules
agenda_collections = db.agenda
tipos_collections = db.tipos

#update weighing/ponderación
def update_weighing():
  pass

def consecuent_tipos(id_consecuent,weighing_new):
  tipos = tipos_collections.find()
  for t in tipos:
    if t.get('id_hecho') == id_consecuent:
      id_tipo = t.get('_id')
      peso_tipo = t.get('weighing')
      peso_actualizar = peso_tipo + (1-peso_tipo) * weighing_new
      tipos_collections.update({"_id": id_tipo},{"$set": {"weighing":peso_actualizar}})    
      print('peso actualizado')

      #modificar punto-barrio de una ruta
      #collection.update({"edad":{"$gt":30}},{"$inc":{"edad":100}}, upsert = False, multi = True)
      #print('id_hecho encontrado: '+t.get('id_hecho'))

#update answer
#busco en los antecedentes de las reglas si esta ese id
def update_answer(id_hecho):
  #encuentra todos los antecedentes con el id_hecho
  rule_cursor = rules_collections.find({"antecedent":{"$in":[id_hecho]}})

  for rule in rule_cursor:
    id_rule = rule['_id']
    weighing = rule['weighing']
    consecuent = rule['consecuent']
    print('id_rule: '+ str(rule['_id']))

    #enviar el consecuent mirar con que tipo de aprendizaje coincide y actualizar peso
    consecuent_tipos(consecuent,weighing)

def agenda_insert(id_rule,weighing):
  agen = Agenda(id_rule,weighing)
  db.agenda.insert_one(agen.toDBCollection())
  print('se inserto agenda')

#User Questions
def questions():
    num_docs = facts_collections.count()
    print(num_docs)
    con1 = 0
    count = 0
    facts_pull = facts_collections.find()
    #print(type(facts_pull))

    for f in facts_pull:
        print(f.get("question"))
        
        #si la pregunta es de si/no
        if f.get("question_type") == 1:
            op_array = f.get("options")

            for index in range(len(op_array)):
                print(str(index+1) +'.' + op_array[index])
            
            answer = int(input('R: '))
            
            if answer == 1:
                id_hecho= str(f.get("_id"))
                print('id_hecho: '+ id_hecho)
                update_answer(id_hecho)
                con1 = con1 +1
    
#load, delete of collections
def load_filter():
  try:
    fill_filter()
    print('datos cargados a la colección')
  except:
    print('error al cargar datos a la colección')

def load_facts():
  try:
    fill_facts()
    print('datos cargados a la colección')
  except ValueError:
    print('error al cargar datos a la colección')

def load_rules():
  try:
    fill_rules()
    print('datos cargados a la colección')
  except ValueError:
    print('error al cargar datos a la colección')

def load_tipos():
  try:
    fill_tipos()
    print('datos cargados a la colección')
  except ValueError:
    print('error al cargar datos a la colección')

def delete_filter():
  try:
    filter_collections.delete_many({})
    print('filter borrada')
  except:
    print('error al borrar filter')

def delete_facts():
  try:
    facts_collections.delete_many({})
    print('facts borrada')
  except:
    print('error al borrar facts')

def delete_tipos():
  try:
    tipos_collections.delete_many({})
    print('tipos borrada')
  except:
    print('error al borrar facts')

def reset_agenda():
  try:
    agenda_collections.delete_many({})
    print('agenda borrada')
  except:
    print('error al borrar facts')

###### Menu #######
#********************* cargar filter
#load_filter()

#********************* cargar hechos
#load_facts()

#********************* cargar rules
#load_rules()

#********************* cargar tipos
load_tipos()
#**********************borrar filters
#delete_filter()

#**********************borrar facts
#delete_facts()

#**********************borrar tipos
delete_tipos()