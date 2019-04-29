$(document).ready(function() {

    var map_element = document.getElementById("access_log_map_map")
    var map;

    initMap = function() {

        var map_center_options = {
            center: {
                lat: 41.536531, 
                lng: -83.528592
            }, 
            zoom: 10
        }

        map = new google.maps.Map(map_element, map_center_options)

        var marker_options = {
            position: map_center_options.center,
            map: map
        }

        var marker = new google.maps.Marker(marker_options)

    };
});
