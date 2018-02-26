(function(window,google,MAX,UrlLoader){
	//map options
	var options={
		center: {lat: 11.19420390014348, lng: 125.18313347849372},
		zoom: 5,

	};
	element=document.getElementById("map-canvas");
	//map
	var map=new google.maps.Map(element,options); 
	//kmls   
  var kmlLayer=MAX.kmlLayer;
  kmlLayer.setMap(map);
  //frames
  //kmlLayer.setMap(null);
  //kmlLayer.setUrl(UrlLoader.kmlFrames[0]);
  kmlLayer.setMap(map);
  //kmlLayer.setMap(null);
  //var kmlLayers=UrlLoader.kmlFrames;


  var requestAnimationFrame=window.requestAnimationFrame ||
                            window.mozRequestAnimationFrame ||
                            window.webkitRequestAnimationFrame ||
                            window.msRequestAnimationFrame;

  function showElev(src,kmlLayer){ 
	  //kmlLayer.setMap(null);
	  //map.setZoom(zoom:map.getZoom());
   //myKmlOptions={
     // suppressInfoWindows: false,
      //preserveViewport: false,
    //}
	  //newkml=new google.maps.KmlLayer(src,myKmlOptions);	
	 // newkml.setMap(map);
    kmlLayer.setUrl(src);

    kmlLayer.setOptions({preserveViewport:false,suppressInfoWindows:false	});
    map.setZoom(map.getZoom());
    kmlLayer.setMap(map);
  };

  var time=0;
  var continueAnimating=true;
	function animateKML() {
		//kmlLayer.setMap(null);
		if(!continueAnimating){return;}
		if(time>35000){
		 time=0;
		}
		if(time%100==0){
		  showElev(UrlLoader.kmlFrames[time/100],kmlLayer);
		  console.log(UrlLoader.kmlFrames[time/100]);
		}

		/*if (time>35){
			time=0;
		}
		showElev(UrlLoader.kmlFrames[time],kmlLayer)*/

		//showElev(UrlLoader.kmlFrames[time],kmlLayer);
		/*if(time>1750){
			time=0;
			kmlLayers[35].setMap(null);
			kmlLayers[0].setMap(map);
		}
		else if(Math.floor(time/50)> 0){
			//document.write(kmlLayers[time%10].getUrl());	
			if(time%50==0 ){
				kmlLayers[Math.floor(time/50)-1].setMap(null);
			}
			else if(time%50==25){
				kmlLayers[Math.floor(time/50)].setMap(map);
			}
			
		}*/
		/*date_now=new Date();
		time_now=date_now.getTime();
		if ((time_now-time_then) > 0.3){
			counter++;	
			if (kmlLayers[counter]!=undefined && kmlLayers[counter-1]!=undefined){
				kmlLayers[counter].setMap(map);
				kmlLayers[counter-1].setMap(null);				
			}

		}
		time_then=time_now;
		*/
		time++;
		requestAnimationFrame(animateKML);

	}

	var el = document.getElementById("startBtn");
	if (el.addEventListener)
	  el.addEventListener("click", animateKML, false);
	else if (el.attachEvent)
	  el.attachEvent('onclick', animateKML);	

}(window,google,window.MAX ||(window.MAX={}),window.UrlLoader ||(window.UrlLoader={})));