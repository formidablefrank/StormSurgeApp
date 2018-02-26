from django.shortcuts import render,get_object_or_404
from .models import *
from django.core import serializers

# Create your views here.
def index(request):

	all_messages=Message.objects.all()
	all_elements=TriangleElement.objects.all()
	all_max_elev=MaxSurge.objects.filter(MaxSurge_id__gt=2)
	all_affected_locations=AffectedLocations.objects.all()
	earliest_surge=EarliestSurge.objects.all()


	context={
		'all_messages' : all_messages,
		'all_affected_locations' : all_affected_locations,
		'all_elements' : all_elements,
		'all_max_elev' : all_max_elev,
		'earliest_surge' : earliest_surge,

	}

	return render(request,'surgeforcast/maxelev.html',context)



def viewElevTimeSeries(request):
	#all_elements=TriangleElement.objects.all()
	#all_elev_time_series=ElevTimeSeries.objects.filter(timeStamp__gt=1007) & ElevTimeSeries.objects.filter(timeStamp__lt=1080)
	#all_elev_time_series=all_elev_time_series.order_by('timeStamp','elemNum')
	all_affected_locations=AffectedLocations.objects.all()
	all_surge_frame=SurgeFrame.objects.all()
	context={
		'all_affected_locations' : all_affected_locations,
		'all_surge_frame' : all_surge_frame,
	}
	return render(request,'surgeforcast/viewelevtimeseries_old.html',context)




####################################################################################3
def detail(request,message_id):
	message=get_object_or_404(Message,pk=message_id)
	return render(request,'surgeforcast/index.html',{'message': message})


def upload_csv(request):
	data = {}
	if "GET" == request.method:
		return render(request, "surgeforcast/upload_csv.html", data)
	# if not GET, then proceed
	try:
		csv_file = request.FILES["csv_file"]
		if not csv_file.name.endswith('.csv'):
			messages.error(request,'File is not CSV type')
			return HttpResponseRedirect(reverse("surgeforcast:upload_csv"))
		#if file is too large, return
		if csv_file.multiple_chunks():
			messages.error(request,"Uploaded file is too big (%.2f MB)." % (csv_file.size/(1000*1000),))
			return HttpResponseRedirect(reverse("surgeforcast:upload_csv"))
 
		file_data = csv_file.read().decode("utf-8")        
 
		lines = file_data.split("\n")
		#loop over the lines and save them in db. If error , store as string and then display
		for line in lines:                        
			fields = line.split(",")
			data_dict = {}
			data_dict["x_1"] = fields[0]
			data_dict["y_1"] = fields[1]
			data_dict["x_2"] = fields[2]
			data_dict["y_2"] = fields[3]
			data_dict["x_3"] = fields[2]
			data_dict["y_3"] = fields[3]
			try:
				form = EventsForm(data_dict)
				if form.is_valid():
					form.save()                    
				else:
					logging.getLogger("error_logger").error(form.errors.as_json())                                                
			except Exception as e:
				logging.getLogger("error_logger").error(form.errors.as_json())                    
				pass
 
	except Exception as e:
		logging.getLogger("error_logger").error("Unable to upload file. "+repr(e))
		messages.error(request,"Unable to upload file. "+repr(e))
 
	return HttpResponseRedirect(reverse("surgeforcast:upload_csv"))