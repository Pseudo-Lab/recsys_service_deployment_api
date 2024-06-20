pseudorec 페이지 추천모델 api용 레포지토리

```shell
uvicorn main:app --reload --port 7001
```

```shell
docker build -t pseudorec_models_api .
```

```shell
docker run -d -p 7001:7001 pseudorec_models_api
```
