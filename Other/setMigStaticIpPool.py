import re
import subprocess
import pymysql
import logging    

#logger 정의
logger = logging.getLogger()
logger.setLevel(logging.INFO)

_dbUser = ''
_dbPass = ''
_dbAddress = ''


def lncGetStaticIpPollPolicyCount(input1,input2,input3) :
    #db 접속 후 IP Pool에 대한 갯수를 조회

    
    #DB 접속
    conn = pymysql.connect(_dbAddress, user=_dbUser, passwd=_dbPass, port=3306, use_unicode=True, charset='utf8')
    cursor = conn.cursor()

    searchSentence = '{0}_%_{1}_{2}_%'.format(input1,input2,input3)

    sql = "SELECT 데이터베이스 캃럼 FROM 데이터베이스 명 WHERE 조건 칼럼 LIKE '"+searchSentence #NFV는 제외

    cursor.execute(sql)
    rd = cursor.fetchall()
    
    #서브넷 생성 객수를 제한하기위한 로직
    if rd[0] > 12 : 
        logger.info("Additional subnet creation is not possible.")
    else :
        nextNumber = int(rd[0])+1 if rd[1]!=NULL else 0

    
    conn.close()

    return nextNumber

def checkIplist(subnetIpPool,checkPoint) :
    #IP 대역 체크를 위한 함수
    return True if subnetIpPool==checkPoint else False


def lncCudGetGroupipByName() :
    #네트워크 장비의 Group ID를 가져오기 위한 함수

    #DB 접속
    conn = pymysql.connect(_dbAddress, user=_dbUser, passwd=_dbPass, port=3306, use_unicode=True, charset='utf8')
    cursor = conn.cursor()

    sql = ""#GroupId를 가져오기위한 조회 sql 문

    cursor.execute(sql)
    rd = cursor.fetchall()

    conn.close()

    return rd[0]


def createNaming(input1,input2,input3,input4) :
    #규칙화된 이름으로 변경하기 위한 함수

    newNetworkName = '{0}_{1}_{2}_{3}_%'.format(input1,input2,input3,input4)
    newUserGroupName = '{0}_{1}'.format(input1,input2)

    return newNetworkName,newUserGroupName


    
def findStaticPool(userName,password,fpIp,contextName,urlCmd,usemod) :
    
    
    url='curl -k -s -u '+userName+':'+password+' -A ASDM https://'+fpIp+'/gadmin/exec/changeto+context+'+contextName+'/'+urlCmd
    status, getObj=subprocess.getstatusoutput(url)
    
    #값을 가져오지 못하거나 오류를 출력 하였을 떄 
    if "failed" in getObj or status>0:
        print("{}".format(getObj))

    test = r'(?P<test>\d{1,3}\.\d{1,3}\.\d{1,3})'
    test2 = r'(?P<test>\w_\w_\w)'
    
    if usemod == 'IPPool':
        t1 = re.findall(test,getObj)
    else :
        t1 = re.findall(test2,getObj)

    poolList = []
    for _d in t1 :
        poolList.append(_d+'\.0')

    return poolList



