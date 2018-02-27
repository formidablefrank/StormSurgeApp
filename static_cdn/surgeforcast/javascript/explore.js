var options={
	center: {lat: 11.19420390014348, lng: 125.18313347849372},
	zoom: 11,
	mapTypeId: 'terrain',
};
element=document.getElementById("map-canvas");
//map
var map=new google.maps.Map(element,options); 


console.log(elements.length)
var triangleCoords=[];
var i;
for(i=0;i<elements.length;i++){
	var triangleCoord=[
		{lat: parseFloat(elements[i][1]), lng: parseFloat(elements[i][0])},
		{lat: parseFloat(elements[i][3]), lng: parseFloat(elements[i][2]) },
		{lat: parseFloat(elements[i][5]), lng: parseFloat(elements[i][4])},
		{lat: parseFloat(elements[i][1]), lng: parseFloat(elements[i][0]) }		
	]
	triangleCoords.push(triangleCoord);
}

// Construct the polygon.

var triangles=[]

var j;
for(j=0;j<elements.length;j++){
	var triangle=new google.maps.Polygon({
		paths:triangleCoords[j],
		strokeColor: '#FF0000',
		strokeOpacity: 0,
		strokeWeight: .5,
		fillColor: '#'+time_series[j].substr(3),
		fillOpacity: .5
	})
	triangles.push(triangle);
	triangles[j].setMap(map);
}


var anim;
var time_offset=1008;
time=0;
function animateKML() {
	//kmlLayer.setMap(null);
	/*if(time>255){
		time=0;	
	}
	col=((time).toString(16));
	var k;
	for(k=0;k<elements.length;k++){
		triangles[k].setOptions({fillColor:'#'+col+'0000'});
	}*/

	if (time>(time_series.length/elements.length)-1){
		time=0;
	}	
	console.log(time)
	var k;
	for(k=0;k<elements.length;k++){
		triangles[k].setOptions({fillColor: '#'+ (time_series[time*elements.length+k].substr(3))})

		/*if(time_series[time*elements.length+k]=="#00ffffff"){
		triangles[k].setOptions({fillOpacity: 0})
		}*/

	}
	//bermudaTriangle.setOptions({fillColor:'#'+col+'0000'})
	//bermudaTriangle2.setOptions({fillColor:'#'+'0000'+col})
	time++;
	anim=requestAnimationFrame(animateKML);
}    

function cancelAnimation(){
	cancelAnimationFrame(anim);
}



var el = document.getElementById("startBtn");
if (el.addEventListener)
  el.addEventListener("click", animateKML, false);
else if (el.attachEvent)
  el.attachEvent('onclick', animateKML);	

var el2 = document.getElementById("stopBtn");
if (el2.addEventListener)
  el2.addEventListener("click", cancelAnimation, false);
else if (el2.attachEvent)
  el2.attachEvent('onclick', cancelAnimation);	

