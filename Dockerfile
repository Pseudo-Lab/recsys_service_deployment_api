# 베이스 이미지로 Python 3.10을 사용합니다.
FROM python:3.10

# 작업 디렉토리를 설정합니다.
WORKDIR /app

# Python 종속성을 설치합니다. (필요한 경우 requirements.txt를 사용합니다)
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 소스 코드를 복사합니다.
COPY . .

# FastAPI를 실행하기 위해 uvicorn을 설치합니다.
RUN pip install uvicorn

# 컨테이너가 시작될 때 FastAPI 서버를 실행합니다.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7001"]
