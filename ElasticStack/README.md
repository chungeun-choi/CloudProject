Elastic Search, kibana  설치 가이드


1.	설치 스크립트 실행 – ‘1번 설치항목’폴더 확인

	 스크립트를 실행하기에 앞서 ‘Docker’ 프로그램이 설치 및 실행되고 있어야 함, Elastic Search에서 사용하게 될 포트가 open 되어 있어야함

	해당 스크립트는 Bash shell 기준으로 작성 되었음

1) Docker container에 사용하게 될 Elastic Search, Kibana 의 이미지 version을 입력
    <img width="417" alt="image" src="https://user-images.githubusercontent.com/65060314/159914307-2cbb4694-0f06-4566-82f7-6c9af01cf8ba.png">

 
2) 각각의 Docker container 끼리의 통신을 위한 Docker Network 이름을 입력

 

3) ‘Elastic Search 용 container Name’ 과 ‘Kibana container Name’ 을 입력

 

4) 애널라이저 설치 – 필요시 설치, Y 또는 N 으로 응답

 

*설치 도중 해당 내용으로 에러 발생 시 내부 방화벽 장비에서 설정이 되어있는지 확인필요
 


2.	데이터 인덱싱을 위한 인덱스 템플릿 생성 – ‘2번 템플릿 생성’ 폴더 확인

*포스트맨 파일은 Global 변수 관련 설정 후 사용


1)	전달 된 템플릿 Json 내용을 Kiabana Web을 통해 생성 (내부 template 내용은 포스트맨 파일 내용에서 사용)
	Kibana web 주소는 {{host IP}}:{{지정포트(Defalut는5601 )}}
 

2) 포스트맨을 통한 템플릿 생성

 


 
3.	Kibana Web을 활용한 데이터 Import – ‘3번 import할 CSV 파일’ 폴더 참고



1)	Kibana 웹페이지 왼쪽하단의 ‘더보기’ 버튼 클릭

 

2)	데이터 import 페이지 이동

 
1.	왼쪽 메뉴바에서 ‘Machine Learning’ 클릭
2.	상단 메뉴바에서 ‘Data Visualizer’ 클릭
3.	 ‘Import data’에서 ‘Upload File’ 클릭 
 
3)	CSV 파일을 선택한 뒤 하단의 ‘import’ 버튼 클릭 

 

 

4)	저장되는 ‘Index name’을 템플릿의 ‘index_pattern’으로 등록한 이름으로 등록 
 
	해당 이름 형태로 저장하는 이유 : template 형태의 인덱스로 저장하기 위해

4.	검색 –‘4번 검색’ 폴더 참고

*포스트맨 파일은 환경변수 관련 설정 후 사용
Json 형태로 된 Query를 통해 검색 가능
	‘.postman_collection.json’ 파일은 포스트맨에서 사용가능
	‘.json’ 파일에는 search 데이터 내용 존재
단일 검색 Query 

	포트스맨 파일에서 해당 내용은 단일 검색 Query

 
Multi Query를 활용한 검색
	Multi Query를 활용한 검색 시 내부 json 데이터에서 “index”의 value 값 변경 필요!! 
 



