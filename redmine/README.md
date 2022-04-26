## redmine 디렉토리 다운로드

레드마인 설치 tar 파일 다운로드


```python
wget https://www.redmine.org/releases/redmine-4.2.5.tar.gz
```

<span style='background-color: #ffdce0'>DB 설치는 postgres 또는 mysql 중 하나 만 설치하면 됩니다!</span>

## postgres 설치

### 설치 스크립트


```python
# Create the file repository configuration: #file repository 설정 생성 
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

# Import the repository signing key: #레포지토리 서명 키를 다운로드
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

# Update the package lists: #패키지 매니저를 통해 리스트 업데이터
sudo apt-get update

# Install the latest version of PostgreSQL.#postgres 최신 버전 설치
# If you want a specific version, use 'postgresql-12' or similar instead of 'postgresql': #만약 다른 버전 설치를 원할 시 posstgresql:[원하는버전]으로 설치
sudo apt-get -y install postgresql
```

### postgres 정상 설치 확인


```python
psql --version
```

### postgres 접속


```python
sudo -i -u postgres
psql
```

### redmin용 계정 생성 및 테이블 생성


```python
CREATE ROLE redmine LOGIN ENCRYPTED PASSWORD 'my_password' NOINHERIT VALID UNTIL 'infinity';
CREATE DATABASE redmine WITH ENCODING='UTF8' OWNER=redmine;
```

## Mysql 설치

### 설치 스크립트


```python
sudo apt update
sudo apt install mysql-server
sudo systemctl start mysql.service
#mysql version 확인
mysql -V
```


```python
redmin용 계정 생성 및 테이블 생성
```


```python
CREATE DATABASE redmine CHARACTER SET utf8mb4;
CREATE USER 'redmine'@'localhost' IDENTIFIED BY 'timegate1!';
GRANT ALL PRIVILEGES ON redmine.* TO 'redmine'@'localhost';
```

## redmine 구축 - 다운로드 받은 디렉토리를 통해서

### redmin에서 postgres connection 설정 정보 변경 / "config/database.yml.example to config/database.yml" 변경


```python
production:
  adapter: postgresql
  database: <your_database_name>
  host: <postgres_host>
  username: <postgres_user>
  password: "<postgres_user_password>" 
  encoding: utf8
  schema_search_path: <database_schema> (default - public)
```

### redmin에서 mysql connection 설정 정보 변경 / "config/database.yml.example to config/database.yml" 변경


```python
production:
  adapter: mysql2
  database: redmine
  host: localhost
  port: 3306
  username: redmine
  password: "my_password"
```

### 세션 저장소 암호 생성


```python
bundle exec rake generate_secret_token
```

### 데이터베이스 스키마 객체 생성


```python
RAILS_ENV=production bundle exec rake db:migrate
# ubuntu에서 설치시 다음과 같은 에러가 발생 시 ' apt-get install libopenssl-ruby1.8.' 입력하여 설치
Rake aborted!
no such file to load -- net/https
```


```python
ruby 관련 설치
```


```python
git clone https://github.com/rbenv/rbenv.git ~/.rbenvecho 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(rbenv init -)"' >> ~/.bashrc
exec $SHELL
#설정값 반영을 위해 인스턴스 다시시작 또는 ssh 링크 재접속 하기
git clone https://github.com/rbenv/ruby-build.git ~/.rbenv/plugins/ruby-build
echo 'export PATH="$HOME/.rbenv/plugins/ruby-build/bin:$PATH"' >> ~/.bashrc
exec $SHELL
#설정값 반영을 위해 인스턴스 다시시작 또는 ssh 링크 재접속 하기
rbenv install 2.5.9
rbenv global 2.5.9
ruby -v
```

### 의존성 관련 설치


```python
sudo apt-get install -y cmake libssl-dev libboost-all-dev libncurses5-dev libncursesw5-dev
```

### 의존성 패키지 추가 (bundler)


```python
gem install bundler
bundle install --without development test
```

### database 기본 데이터 설정


```python
RAILS_ENV=production bundle exec rake redmine:load_default_data
```

### redmine 실행


```python
#redmine이 존재하는 디렉토리에서 진행 '~/redmine-4.2.5/'
bundle exec rails server webrick -e production
```

### 필요 plugin 설치


```python
#redmine이 존재하는 디렉토리에서 'plugins'디렉토리로 이동하여 진행
git clone https://github.com/gatATAC/redmine_startpage #초기페이지 설정을 위한 plugin
git clone https://github.com/danmunn/redmine_dmsf.git #문서 관리 시스템 기능 plugin
git clone https://github.com/paginagmbh/redmine_lightbox2.git #게시글에 이미지 첨부시 라이트박스에서 미리 볼 수 있게 해주는 plugin
git clone https://github.com/akiko-pusu/redmine_banner.git #관리자 메세지를 표시하는 plugin
git clone https://github.com/jgraichen/redmine_dashboard.git #이슈 대시보드 plugin
git clone https://github.com/akiko-pusu/redmine_issue_templates #프로젝트 이슈 템플릿 plugin
git clone https://github.com/alexmonteiro/Redmine-Monitoring-Controlling #모니터링 관리 plugin -다운로드 후 이름 변경 mv ./Redmine-Monitoring-Controlling ./redmine_monitoring_controlling 
#관련 의존성 패키지 설치 
apt-get install -y ruby-xapian libxapian-dev poppler-utils antiword unzip catdoc libwpd-tools libwps-tools libwpd-tools libwps-tools gzip unrtf catdvi djview djview3 uuid uuid-dev xz-utils libemail-outlook-message-perl

```
