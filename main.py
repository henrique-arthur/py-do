from flask import Flask
from routes import routes

# docker-compose build (buildar e pegar imagens do docker)
# docker-compose up (subir o container)
# docker-compose up -d (subir o container em segundo plano)
# docker-compose down (derrubar o container)
# docker-compose ps (verificar os containers)
# docker-compose exec -it flask bash (entrar no container)
# docker logs -f flask (verificar os logs do container)
# sudo chmod 777 data/db

print('initializing')

app = Flask(__name__)

app.register_blueprint(routes)


# TODO VERIFICAR PORQUE NÃO ESTA PRINTAND OOS LOGS NO DOCKER
# SOMENTE QUANDO REINICIA