MATCH (p:Person) return p.ID order by p.ID ASC;

MATCH (p:Person)-[r:KNOWS]->(s) WHERE p.ID="116374117927631468606" return s.ID;

MATCH (p:Person)-[r:KNOWS]->() WITH p,count(r) as num WHERE p.ID="116374117927631468606" return p.ID, num;
