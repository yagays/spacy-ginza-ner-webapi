# FastAPI ML Template
## Run Web API
### Local

```sh
$ sh run.sh
#   poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 9000
```

### Docker
```sh
$ docker build -f Dockerfile -t spacy-ginza-ner-webapi .
$ docker run -p 9000:9000 --rm --name spacy-ginza-ner-webapi -t -i spacy-ginza-ner-webapi
```

### Docker Compose

```sh
$ docker compose up --build
```

## Request Commands

```sh 
$ curl --request POST --url http://127.0.0.1:9000/api/v1/predict --header 'Content-Type: application/json' --data '{"input_text": "2018年の夏にフランスに行った。ジベルニー村のジャン・クロード・モネの家で池に浮かぶ睡蓮を見た。"}'
```

```sh
$ http POST http://127.0.0.1:9000/api/v1/predict input_text="2018年の夏にフランスに行った。ジベルニー村のジャン・クロード・モネの家で池に浮かぶ睡蓮を見た。"
```

## Development
### Run Tests and Linter

```
$ poetry run tox
```

## Reference

- [tiangolo/full\-stack\-fastapi\-postgresql: Full stack, modern web application generator\. Using FastAPI, PostgreSQL as database, Docker, automatic HTTPS and more\.](https://github.com/tiangolo/full-stack-fastapi-postgresql)
- [eightBEC/fastapi\-ml\-skeleton: FastAPI Skeleton App to serve machine learning models production\-ready\.](https://github.com/eightBEC/fastapi-ml-skeleton)