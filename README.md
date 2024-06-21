pseudorec 페이지 추천모델 api용 레포지토리

개발용 uvicorn
```shell
uvicorn main:app --reload --port 7001
```

개발용 gunicorn
```shell
gunicorn -k uvicorn.workers.UvicornWorker -b 127.0.0.1:7001 --threads 2 main:app 
```

Docker
```shell
docker build -t pseudorec_models_api .
docker run -d -p 7001:7001 pseudorec_models_api
```

서버 배포 시
```shell
git clone https://github.com/Pseudo-Lab/recsys_service_deployment_api.git
cd recsys_service_deployment_api
vim .env.dev 작성
docker 실행
```