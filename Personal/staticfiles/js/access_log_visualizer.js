$(document).ready(function() {

    var visitorData = JSON.parse(document.getElementById("visitorData").textContent)
    visitorData = JSON.parse(visitorData)

    formattedVisitorArray = []
    
    visitorData.forEach((visitor, index) => {
        visitorDescription = `${visitor[5]} - ${visitor[4]}, ${visitor[6]} - ${visitor[2]}`
        visitorLongitude = visitor[7]
        visitorLatitude = visitor[8]
        visitorObject = {
            'visitorDescription' : visitorDescription, 
            'visitorLongitude' : visitorLongitude, 
            'visitorLatitude' : visitorLatitude
        }
        
        formattedVisitorArray.push(visitorObject)
    })

    var map_element = document.getElementById("access_log_map_map")
    var map;

    initMap = function() {

        var map_center_options = {
            center: {
                lat: 41.6528, 
                lng: -83.5379
            }, 
            zoom: 4,
            mapTypeId: 'satellite'
        }

        var infoWindow = new google.maps.InfoWindow({})

        map = new google.maps.Map(map_element, map_center_options)

        for (index = 0; index < formattedVisitorArray.length; index ++) {

            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(
                    formattedVisitorArray[index]["visitorLongitude"], 
                    formattedVisitorArray[index]["visitorLatitude"]
                ), 
                map: map
            })

            google.maps.event.addListener(
                marker, 
                'click', 
                (function(marker, index) {
                    return function() {
                        infoWindow.setContent(formattedVisitorArray[index]["visitorDescription"])
                        infoWindow.open(map, marker)
                    }
                }) (marker, index)
            )
        }
    };
});
