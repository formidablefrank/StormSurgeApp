from django.db import models

# Create your models here.
class Message(models.Model):
	message=models.CharField(max_length=1000)
	date_time=models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.message +"\t" +str(self.date_time)

class Typhoon(models.Model):
	typhoon_id=models.IntegerField(primary_key=True)
	typhoon_name=models.CharField(max_length=100)

	def __str__(self):
		return str(self.typhoon_id) + "\t" + self.typhoon_name

class SurgeEvent(models.Model):
	typhoon_id=models.ForeignKey(Typhoon,on_delete=models.CASCADE)
	event_id=models.IntegerField(unique=True)
	area=models.CharField(max_length=100)

	def __str__(self):
		return str(self.typhoon_id) + "\t" + str(self.event_id)


class MaxSurge(models.Model):
	event_id=models.ForeignKey(SurgeEvent,on_delete=models.CASCADE)
	MaxSurge_id=models.IntegerField(unique=True)
	kmlFile=models.CharField(max_length=200)

	def __str__(self):
		return str(self.event_id) + "\t" + str(self.MaxSurge_id) + "\t" + str(self.kmlFile)

class SurgeFrame(models.Model):
	event_id=models.ForeignKey(SurgeEvent,on_delete=models.CASCADE)
	date_time=models.DateTimeField(auto_now=False)
	customFile=models.CharField(max_length=200)


class Towns(models.Model):
	town_id=models.IntegerField(primary_key=True)
	town_name=models.CharField(max_length=100)
	lat=models.FloatField()
	lon=models.FloatField()

	def __str__(self):
		return str(self.town_id) + "\t" + str(self.town_name) + "\t" + str(self.lat) + "\t" + str(self.lon)


class Provinces(models.Model):
	province_id=models.IntegerField(primary_key=True)
	province_name=models.CharField(max_length=100)

	def __str__(self):
		return str(self.province_id) + "\t" + str(self.province_name)+"\n"

class MunCities(models.Model):
	mun_id=models.IntegerField(primary_key=True)
	mun_name=models.CharField(max_length=100)
	province_id=models.ForeignKey(Provinces,on_delete=models.CASCADE)
	lat=models.FloatField()
	lon=models.FloatField()

	def __str__(self):
		return str(self.mun_id) + "\t" + str(self.mun_name)+ "\t" + str(self.province_id.province_name)+ "\t" + str(self.lat)+ "\t" + str(self.lon)+"\n"


class EarliestSurge(models.Model):
	event_id=models.ForeignKey(SurgeEvent,on_delete=models.CASCADE)
	date_time=models.CharField(max_length=100)
	lat=models.FloatField()
	lon=models.FloatField()
	direction=models.CharField(max_length=100)
	

class AffectedLocations(models.Model):
	event_id=models.ForeignKey(SurgeEvent,on_delete=models.CASCADE)
	town_id=models.ForeignKey(Towns,on_delete=models.CASCADE)
	max_elev=models.FloatField()			

	def __str__(self):
		return str(self.event_id) + "\t" + str(self.town_id) + "\t" + str(self.max_elev)

class TriangleElement(models.Model):
	x_1=models.FloatField()
	y_1=models.FloatField()
	x_2=models.FloatField()
	y_2=models.FloatField()
	x_3=models.FloatField()
	y_3=models.FloatField()	

	def __str__(self):
		return str(self.x_1) + "\t" + str(self.y_1) + str(self.x_2) + "\t" + str(self.y_2)+ str(self.x_3) + "\t" + str(self.y_3)+"\n"


class ElevTimeSeries(models.Model):
	typhoon_id=models.ForeignKey(Typhoon,on_delete=models.CASCADE)
	timeStamp=models.IntegerField()
	elemNum=models.IntegerField()
	color=models.CharField(max_length=100)

	def __str__(self):
		return str(self.timeStamp) + "\t" + str(self.elemNum) + "\t" + str(self.color) +"\n"

class MaxElev(models.Model):
	elemNum=models.IntegerField()
	color=models.CharField(max_length=100)

	def __str__(self):
		return	str(self.elemNum) + "\t" + str(self.color) +"\n"	