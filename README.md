# petCommunity (이한솔)
1. 환경
- web server : flask (python)
- DB : postgresql

2. 프로젝트 구조
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
- test : API test를 위한 unittest
- utils : 기타 공통 메소드와 유효값 검증을 위한 error_handler

2. DDL 파일 : pet_community.ddl
3. 프로젝트 실행을 위한 설치 정보 : requirements.txt
