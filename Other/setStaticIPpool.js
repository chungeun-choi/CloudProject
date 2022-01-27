importPackage(java.lang);
importPackage(java.util);


var ipAddress = input.ipPool;
var prefix = input.prefix.replace("/", ""); 
var poolMin = [254,126,62,30,14,6,2,0];//가용 ip를 지정하기위한 값
var valCheck = [255,128,64,32,16,8,4,2,0];//입력받은 IPpool의 validation check를 위한 값
//슈퍼넷팅을 지원하지 않음으로 prefix 값은 24보다 작을 수 없음
if (prefix < 24){
    logger.addError("SuperNetting is not supported!");
    ctxt.setFailed("Failed / wrong Subnet");
}
else {
    var selectMask = poolMin[parseInt(prefix) - 24];//prefix의 값이 1증가 할때마다 서브넷팅이 줄어듬으로  -24 후 배열값을 가져와서 계산
    
    var ipList = ipAddress.split(".");
    var checkP = parseInt(ipList[3])%valCheck[parseInt(prefix) - 24];//poolMin의 값을 가져오는 것과 동일
    //ip Pool의 값이 Pool로서 사용가능한 input값인지 확인하는 내용
    if (checkP!==0){ 
      logger.addError("You can't use Ip");  
      ctxt.setFailed("Failed / wrong Ip");
    }
    //가용 IP 정의
    StartCclass = parseInt(ipList[3])+1;
    endCclass = parseInt(ipList[3])+selectMask;
    var startIp = ipList[0]+"."+ipList[1]+"."+ipList[2]+"."+StartCclass.toString();
    var endIp = ipList[0]+"."+ipList[1]+"."+ipList[2]+"."+endCclass.toString();
    var subnetID = ipList[0]+"."+ipList[1]+"."+ipList[2]

    
    output.StaticIPPool = startIp+"-"+endIp;


   
}