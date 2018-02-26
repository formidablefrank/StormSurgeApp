(function(window,google,UrlLoader){
  UrlLoader.kmlFrames=[];x=-1

  //src="\static\surgeforcast\kml files\km";
	src="http://localhost:8000/static/surgeforcast/kml/kml";

  var iterator;
  for(iterator=801;iterator<=1151;iterator++){
    //UrlLoader.kmlFrames[iterator-801]='https://raw.githubusercontent.com/savanah18/Storm-Surge-Files/9c93663227a344674d7419cd01fffc8c19c4f674/kml%20files/kml'+iterator+'.kml'
    UrlLoader.kmlFrames[iterator-801]=src+iterator+'.kml'
		//src='https://raw.githubusercontent.com/savanah18/Storm-Surge-Files/master/kml%20files/kml'+iterator+1+'.kml';
		//UrlLoader.kmlFrames[iterator-80]=new google.maps.KmlLayer(src,myKmlOptions);	
  }


}(window,google,window.UrlLoader ||(window.UrlLoader={})));