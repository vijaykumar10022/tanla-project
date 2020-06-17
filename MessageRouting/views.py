from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from MessageRouting.models import Message
# Create your views here.
def create(request):
	name="airtel"
	ipaddress="12.12.12.12"
	prefix="123"
	data=Message(name=name,ipaddress=ipaddress,prefix=prefix)
	data.save()
	return HttpResponse("Created....!!")
def data(request,id):
	mydata=Message.objects.get(id=id)
	return JsonResponse({"name":mydata.name,
						 "ip":mydata.ipaddress,
						 "prefix":mydata.prefix})
def myroute(request):
	prefix="9194"
	gateway_id=10
	mydata=Message.objects.filter(prefix=prefix)
	if mydata:
		return HttpResponse("Exits...")
	else:
		data=Message(name="Tata",prefix=prefix,ipaddress="12.12.12.12")
		data.save()
		fdata=Message.objects.get(name="Tata")
		return JsonResponse({"id":fdata.id,
							 "prefix":fdata.prefix,
							 "gatway":{
							 "id":fdata.id,
							 "name":fdata.name,
							 "ip_address":fdata.ipaddress
							 }})
def routedata(request,id):
	mydata=Message.objects.get(id=id)
	if mydata:
		return JsonResponse({"name":mydata.name,
						 "ip":mydata.ipaddress,
						 "prefix":mydata.prefix})
	else:
		return HttpResponse("Not Exits...!!!")
def search(request,number):
	pre=[]
	result=[]
	n=str(number)
	data=Message.objects.all()
	for val in data:
		pre.append(val.prefix)
	for pr in pre:
		if n.startswith(pr):
			result.append(pr)
	m_pre=max(result)
	# print(result)
	# print(m_pre)
	fdata=Message.objects.get(prefix=m_pre)
	if fdata:
		return JsonResponse({"id":fdata.id,
							 "prefix":fdata.prefix,
							 "gatway":{
							 "id":fdata.id,
							 "name":fdata.name,
							 "ip_address":fdata.ipaddress
							 }})
	else:
		return HttpResponse("Not Exits...!!!")