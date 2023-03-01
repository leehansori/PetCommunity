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
├─board
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

### 3. DDL 파일 : pet_community.ddl
### 4. 프로젝트 실행을 위한 설치 정보 : requirements.txt
### 5. swagger : swagger_API.yaml

![image](https://user-images.githubusercontent.com/109563345/222160213-df2610fe-a669-4893-b5ee-f2aca010cbd0.png)
![image](https://user-images.githubusercontent.com/109563345/222160565-eef9fb66-f833-4bf2-9681-549a6660fe05.png)
