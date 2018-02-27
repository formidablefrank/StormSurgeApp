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
	 	console.log(src);
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
		}

		/*if(time>350){
			time=0;
		}
		showElev(UrlLoader.kmlFrames[time],kmlLayer);
		setTimeout(function(){requestAnimationFrame(animateKML)},1000);
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
