[NES](http://nes-env.eba-9ycvw3yi.ap-northeast-2.elasticbeanstalk.com/)

# 🎨NES; Never Ending Story

NES팀은 젊은 예술가들이 직면할 수 밖에 없는 작품의 전시와 그에 따른 비용에 관한 문제를 어떻게 해소시켜 줄 수 있을지 고민하였습니다.

**'끝나지 않는 이야기’** 라는 뜻을 담고 있는 저희 팀 이름은 위와 같은 고민으로부터 출발했습니다.

NES 팀은 젊은 예술가들의 어려움에 공감하며 그들의 꿈을 이루는 것을 돕고자 **졸업 작품 중개 서비스**를 기획하였습니다.
<br>
<br>

* 개발기간: 2022.11.28 ~ 2022.12.15

## 팀원 소개
![NES Members](./NES.assets/%ED%8C%80%EC%9B%90%EC%86%8C%EA%B0%9C.png)


#### 백엔드 articles, orders 담당
* articles
    * 작품 CRUD
    * 페이지네이션
    * 댓글
    * 좋아요 비동기
    * 검색
    <br>

* orders
    * 가격 제시 화면 구현
    * 장바구니 추가 및 삭제
    * 주문 및 결제 (이니시스 API)

<br>
<br>

# 사용 기술 및 개발 계획

### 1) 사용 기술

**Front-end**

* HTML, CSS, Javascript
* Axios
* SimpleBar, sweetalert2

**Back-end**

* Django, Python
* SQLite3, PostgreSQL, Amazon S3, Amazon RDS, Elastic Beanst



### 2) 개발 계획

**총 개발 기간: 22.11.24 - 22.12.15**

* 사전 기획: 11.24 - 11.28
* 모델 설계: 11.25 - 11.28
* 디자인 설계: 11.28 - 12.01
* 메인 서비스 구축: 11.28 - 12. 13
* 서비스 점검 및 런칭: 12.14 - 12.15



# Modeling
## ERD 모델
![ERD 모델](./NES.assets/ERD.png)

## 와이어 프레임
![와이어 프레임](./NES.assets/%ED%99%94%EB%A9%B4%EC%84%A4%EA%B3%841.png)
![와이어 프레임2](./NES.assets/%ED%99%94%EB%A9%B4%EC%84%A4%EA%B3%842.png)




## 기능 소개

<br>

### Intro

![글자 로딩](./NES.assets/%EA%B8%80%EC%9E%90%20%EB%A1%9C%EB%94%A9.gif)

서비스 첫 화면 로딩 페이지

프로젝트의 기획 의도를 담은 3초 내의 로딩창

![티켓 출력](./NES.assets/%ED%8B%B0%EC%BC%93%20%EC%B6%9C%EB%A0%A5.gif)

로그인 후 NES 전시회 티켓 출력 페이지로 이동



### Main page (Articles App)

**Index**

* 카테고리 별 각 페이지로 이동

**Main**

* 카테고리 별 작품 출력
* 페이지네이션
* 검색

**Detail**

* 작품명, 제작 년도, 작가명 출력
* 좋아요 비동기 구현
* 댓글 비동기 구현
* 해당 작품의 작가만 작품 수정 및 삭제 가능한 버튼 출력
* 구매자일 경우 주문하기 버튼 출력



### Accounts App

**signup**

* 아이디 중복 확인
* 이메일 인증

**login**

* 일반 로그인 & 카카오 로그인

**Profile**

* 작가 인증을 위한 학교 이메일 인증 (ac.kr 혹은 eud가 들어간 이메일만 허용)
* 소셜 링크
* 등록한 작품 / 저장된 작품 / 구매 작품 / 판매 작품 / 장바구니 별 작품 출력
* 사용자 정보 수정
* 작품 등록

* 작가 데코레이터 생성



### Orders App

**Info**

* 작품 가격 및 작품 상세 정보 출력
* 가격 문의
* 장바구니 추가 및 구매하기 

**Mycart**

* 장바구니 추가 및 삭제

**Payment**

* 사용자의 결제정보 입력 및 저장
* 이니시스 API를 활용한 결제

**Offer**

* 구매자가 작가에게 가격을 제안할 시 제안한 가격으로 재설정

**Complete**

* 총 결제 금액 출력
* 구매한 작품 및 작가 정보 출력



### Notes App

**Index**

* 받은 편지함 및 보낸 편지함 목록 
* 상대방 읽음 여부 출력
* 페이지네이션
* 쪽지 상세보기 및 삭제 

**Send**

* 유저 프로필 및 아이디 출력
* 제목 및 내용 입력



### Questions App

**FQA**(Index)

* 자주 묻는 질문 출력
  * 아코디언으로 구현, 비동기

**Questions**

* 문의 작성 From 출력
  * 사용자 이름, 이메일, 문의 제목, 문의 내용, 이미지 
* 사용자가 작성한 문의들 출력



## 이슈 사항

⁉️ 주문 모델

▶️ 그림과 주문에 대한 관계가 제대로 이루어지지 않아 추후에 다시 재설계 해야 했었던 이슈



# Review

![후기](./NES.assets/%ED%9B%84%EA%B8%B0.png)