

var returnd = []
var returnD = {
    "interface" :"",
    "nameif": "",
    "securityLevel":"",
    "ipAddress":""

};



var inputd = d.split("!");

//interface정규식 ex)interface Ethernet1/5,interface Port-channel1.xx
var portPatern = /interface ((\w)+[\/,\-](\w)+\.?(\w+)?)/;
//nameif 정규식 ex)nameif mgmt, nameif xxxxx-xx-OUTBOUND
var nameifPatern = /nameif (\w+)[\-]?(\w+)[\-]?(\w+)/;
//securityLevel 정규식 ex)security-level 0, security-level xx
var securityLevelPatern = /security-level\s(\w+)/;
//Ip Address 정규식 ex)ip address xxx.xxx.xxx.xxx, ip address xxx.xxx.xxx.xxx
var ipAddressPatern = /ip address (\w+.\w+.\w+.\w+)/


for (iterd1 in inputd){
    //정규식을 통해 매칭되는 패턴에서 필요 데이터 추출
    var portChannelD = portPatern.exec(inputd[iterd1])[0];
    var nameifD = nameifPatern.exec(inputd[iterd1])[0];
    var securityLevelD = securityLevelPatern.exec(inputd[iterd1])[0];
    var ipaddressD = ipAddressPatern.exec(inputd[iterd1])[0];
    
    //json 형태로 잡아준 key에 해당되는 value 값을 대입 
    returnD["interface"] = portChannelD.replace("interface ","") ;
    returnD["nameif"] = nameifD.replace("nameif ","");
    returnD["securityLevel"] = securityLevelD.replace("security-level ","");
    returnD["ipAddress"] = ipaddressD.replace("ip address ","");

    
    //key,value 형태의 데이터를 json 데이터로 형변환
    formJson = JSON.stringify(returnD)
    
    //returnd 배열에 추가
    returnd.push(formJson)
    
}


