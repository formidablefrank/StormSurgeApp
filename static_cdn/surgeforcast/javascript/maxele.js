(function(window,google,MAX){
    
    //set_up MAXleve kmlfile
    src = 'https://raw.githubusercontent.com/savanah18/Storm-Surge-Files/eb0f37b781dc742a16789b0f7c28d8873e4bf422/kml%20files/kmlmaxele1.kml';
    var myKmlOptions={
      suppressInfoWindows: false,
      preserveViewport: false,
    }

    MAX.kmlLayer=new google.maps.KmlLayer(src,myKmlOptions);


    /*var typhoonPath = new google.maps.KmlLayer({
      	url:typhoonPathSource,
      	map:map,
	*/	


}(window,google,window.MAX || (window.MAX={})));