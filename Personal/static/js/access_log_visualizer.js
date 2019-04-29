$(document).ready(function() {
    var map_element = $("#access_log_map_map")

    function initMap() {
        var center = {lat: 44.5393, lng: -123.2799};

        var map = new google.maps.Map((map_element), 
        {
            zoom: 10, 
            center: center
        });

        var marker = new google.maps.Marker({
            position: center, 
            map: map
        })
    };

});