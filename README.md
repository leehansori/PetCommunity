# petCommunity (이한솔)
### 1. 환경
- web server : flask (python)
- DB : postgresql

### 2. 프로젝트 구조
```txt
pet_community
│  config.py 
│  __init__.py
│  
├─board // 게시판 관련 API, DB 메소드 정의
│  │  boardManager.py
│  └─ board_api.py
│          
├─member
│  │  member_api.py
│  └─ memManager.py  
│          
├─test
│  └─ api_unittest.py
│          
└─utils
    │  common.py
    │  error_handler.py
    └─ response.py
```

- board : 게시판 관련 API, DB 메소드 정의
- member : 회원 관련 API, DB 메소드 정의
- test : API test를 위한 unittest (API가 정의 되어 있습니다.)
- utils : 기타 공통 메소드와 유효값 검증을 위한 error_handler
---
- pet_community.ddl : pet_community.ddl
- requirements.txt : 프로젝트 실행을 위한 설치 정보
- swagger_API.yaml : swagger
![image](https://user-images.githubusercontent.com/109563345/222160213-df2610fe-a669-4893-b5ee-f2aca010cbd0.png)
![image](https://user-images.githubusercontent.com/109563345/222160565-eef9fb66-f833-4bf2-9681-549a6660fe05.png)


### 3. 추가 미션
1. 사용자 Password 를 암호화하여 저장합니다.
-> werkzeug.security의 generate_password_hash 활용
2. 사용자의 입력 데이터 유효성 검증 기능을 포함합니다.
-> flask_request_validator 활용
3. Swagger 나 OpenAPI 를 활용하여 개발합니다.
-> swagger를 yaml 파일로 작성. 또한 API 테스트를 위해 unittest 형식으로 작성. (api_unittest.py)
