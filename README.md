# rescuethebirds
Rescue the birds backend

docker build . -t jaefinger/rescuethebirbs
docker run -d --name birbstest -p 8000:8000 jaefinger/rescuethebirbs