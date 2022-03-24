#!/bin/sh

echo "Elastic Search Docker Cotainer 설치스크립트 입니다 설치하고자 하는 version을 입력해주세요 ex) 7.3.0 "
read version

echo "입력 받은 vesion으로 설치를 진행할게요~"
#Elastic search, Kibana 이미지 받기 version 7.3.0
docker pull docker.elastic.co/elasticsearch/elasticsearch:$version && docker pull docker.elastic.co/kibana/kibana:$version
if [ $? -eq 0 ]  
then
    echo "log: >>>>>>>>>> Images have been installed."
    echo "log: >>>>>>>>>> Create docker Network for ElasitcSearch and Kibana"
    echo "Elastic Search에서 사용할 Docker Network 명을 입력해주세요!"
    read ESnetwork
    docker network create $ESnetwork
    if [ $? -eq 0 ] 
    then
        echo "log: >>>>>>>>>> Create docker Container for ElasitcSearch and Kibana"
        echo "ElasticSearch container 생성을 시작할게요, ES용 container 명을 입력해주세요!"
        read esname
        echo "Kibana container 생성을 시작할게요, kibana용 container 명을 입력해주세요!"
        read kibname
        docker run -d --name $esname --net $ESnetwork -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:$version &&
        docker run -d --name $kibname --net $ESnetwork -p 5601:5601 -e "ELASTICSEARCH_HOSTS=http://$esname:9200" docker.elastic.co/kibana/kibana:$version
        if [ $? -eq 0 ] 
        then
            echo "log: >>>>>>>>>> Success!"
        else
            echo "log: >>>>>>>>>> Falid Delete docker Container" 
            docker rm $esname && docker rm $kibana
        fi    
    else
        echo "log: >>>>>>>>>> Create docker network falied,  Docker Network 생성에 실패하였어요 중복된 값이 있는지 확인부탁드려요"
        docker network rm $ESnetwork

    fi
else
    echo "log: >>>>>>>>>> Failed"
    docker rmi -f docker.elastic.co/elasticsearch/elasticsearch:$version && docker rmi -f docker.elastic.co/kibana/kibana:$version
fi    



echo "Analyzer 설치를 진행하시겠어요? Y 또는 N으로 입력 바랍니다"
read answer 

if [[ $answer = "y" || $answer = "Y" ]]
    then 
        docker exec -it $esname bash bin/elasticsearch-plugin install analysis-nori
        if [ $? -eq 0 ] 
        then
            echo "nori plugin Success"
            echo "Plugin 반영을 위해 Elastic Search를 재부팅 할게요"
            docker stop $esname && docker start $esname
            echo "ElasticSearch 서비스가 실행 되기까지 기다려주세요!"
        else
            echo "log: >>>>>>>>>> Falid install analysis-nori, ElasticSearch실행 여부 확인필요"

        fi
    elif [[ $answer = "n" || $answer = "N" ]]
        then
            echo "OK"
    else
        echo " '$answer'란 값은 처리할 수 없는 값입니다"        
    fi





