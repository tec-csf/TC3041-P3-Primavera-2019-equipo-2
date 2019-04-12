from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "password"))

def menu():
    inp=0
    while inp!="4":
        print("\nQueries disponibles:\n"
              "1. Ordenar todos los nodos por ID de manera ascendiente.\n"
              "2. Desplegar el ID de todos los nodos relacionados con el ID=116374117927631468606.\n"
              "3. Cuenta el total de relaciones que tiene el nodo con ID=116374117927631468606\n"
              "4. Cerrar programa\n")

              inp = input("Selecciona la opción que desees ejecutar:\n")
              if inp == "1":
                  with driver.session() as session:
                      session.read_transaction(ordena_asc)
              if inp == "2":
                  with driver.session() as session:
                      session.read_transaction(relacionado_con)
                          if inp == "3":
                              with driver.session() as session:
                                  session.read_transaction(count_relaciones)

def ordena_asc(tx):
    result = tx.run("MATCH (p:Person) return p.ID order by p.ID ASC;")
    for record in result:
        persona = record["p.ID"]
        print("ID de la persona = %s" % (persona))

def relacionado_con(tx):
    result = tx.run("MATCH (p:Person)-[r:KNOWS]->(s) WHERE p.ID="116374117927631468606" return s.ID;")
    for record in result:
        persona = record["s.ID"]
        print("La persona con el ID 116374117927631468606 conoce a las personas con ID %s" % (persona))

def count_relaciones(tx):
    result = tx.run("MATCH (p:Person)-[r:KNOWS]->() WITH p,count(r) as num WHERE p.ID="116374117927631468606" return p.ID, num;")
    for record in result:
        persona = record["p.ID"]
        cantidad = record["num"]
        print("La persona con el ID %s conoce a un total de %s personas" % (persona,num))

menu()
