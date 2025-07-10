#!/bin/bash

# Exécute la requête SQL sur galera1
echo "== galera1 =="
docker exec -it galera1 mysql -uroot -pgalerapass -e "USE events_db; SELECT * FROM events;"

# Exécute la requête SQL sur galera2
echo "== galera2 =="
docker exec -it galera2 mysql -uroot -pgalerapass -e "USE events_db; SELECT * FROM events;"
