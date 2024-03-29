# Named Entity Recognition API with spaCy and GiNZA

I wrote a blog post about this repository in Japanese.

[機械学習の推論WebAPIの実装をテンプレート化して使い回せるようした](https://zenn.dev/yag_ays/articles/eef1a8c8e1ee39)

![](docs/http_request.png)

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
