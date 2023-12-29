# Fast-API-study

Fast API를 활용한 간단한 웹 애플리케이션 만들기

- **Fast API는 파이썬 표준 타입 힌트에 기초한 Python3.6+의 API를 빌드하기 위한 웹 프레임워크** 

## 서비스 소개 

- 할 일을 적고 수행 여부를 체크하는 ToDo 서비스 

### 서비스 기능 

#### GET 

- 전체 ToDo 조회

```
/api/v1/todos
```

- 단일 ToDo 조회 

```
/api/v1/todos/{id}
```

#### POST 

- ToDo 생성 

```
/api/v1/todos 
```

#### PATCH 

- ToDo 수정 

```
/api/v1/todos/{id}
```

#### DELETE 

- ToDo 삭제 

```
/api/v1/todos/{id} 
```

### 환경 설정 요구 사항 

- Python 3.10 + 
- Docker 
- MySQL 8.0 
- IDE : PyCharm 

#### Python 가상 환경 구축 

##### Windows 기준  

- 가상 환경 생성 

```
python -m venv todos 
```

- 디렉토리 이동 

```
cd todos
```

- 가상 환경 활성화 

```
Scripts\activate.bat 
```

- 가상 환경 비활성화 

```
deactivate 
```

#### FastAPI 설치 

- 생성된 가상환경 내에서 버전을 명시해 Fast API를 설치한다. 
- 이때, 버전을 명시하는 이유는 최신 버전은 fastapi가 pydantic v2를 사용하지만, 이 프로젝트는 v1을 사용하기 때문이다. 

```
pip install fastapi==0.97.0
```

##### +) 추가 uvicorn 설치 

- Fast API를 동작시키기 위해 필요한 라이브러리로, 일반적으로 Fast API와 같이 사용하게 된다. 

```
pip install uvicorn 
```

#### 코드 실행하기 

- todos의 src 폴더로 이동하여 명령어를 실행한다. 
- 모든 코드 블록은 복사하고 직접 사용할 수 있다. 
- 예제를 실행하려면, 코드를 main.py 파일에 복사하고 다음을 사용하여 uvicorn을 시작한다. 
- reload 옵션을 통해, 코드가 수정이 되면 자동으로 반영될 수 있게 한다. 

```
uvicorn main:app --reload 
```

- 코드를 작성하거나 복사, 편집할 때, 로컬에서 실행하는 것을 **강력히 장려** 

#### 데이터베이스 

- Docker를 이용해 MySQL Container를 생성하여 데이터를 다룬다. 

```
docker run -p 3306:3306 -e MYSQL_ROOT_PASSWORD=todos -e MYSQL_DATABASE=todos -d -v todos:/db --name todos mysql:8.0
```

- p 옵션으로 port를 지정 
- e 옵션으로 환경 변수를 설정
- d 옵션으로 백그라운드로 실행 
- v 옵션으로 볼륨을 지정 
- mysql:8.0을 통해 todos라는 이름의 container 생성 

[Reference - FastAPI 자습서](https://fastapi.tiangolo.com/ko/tutorial/)

[Reference - 인프런 강의](https://www.inflearn.com/course/%EC%8B%A4%EC%A0%84-fastapi-%EC%9E%85%EB%AC%B8)

[Reference - 참고 블로그](https://datamoney.tistory.com/344)