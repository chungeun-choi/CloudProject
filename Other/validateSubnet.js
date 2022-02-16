importPackage(java.lang);
importPackage(java.util);

var subnet = input.subnetMask.split(".");
var subnetrange = ["0","128","192","224","240","248","252","254","255"];

for(count in subnet){
	subnet[count]=parseInt(subnet[count]);
}

if(subnet[0]<subnet[1]||subnet[1]<subnet[2]||subnet[2]<subnet[3]){
	logger.addError("Wrong SubnetMask!");
	ctxt.setFailed(input.subnetMask);
}

for(count in subnet){
	if(subnetrange.indexOf(subnet[count].toString()) == -1){
        logger.addError(subnet[count]+" You can't use it!!")
        ctxt.setFailed(input.subnetMask);
	}
}