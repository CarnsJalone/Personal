$(document).ready(function(){

    var update_logs_form = $("#update_logs_form_form");
    var update_logs_submit_button = $("#update_logs_submit_button");
    var update_logs_status_outer_container = $("#update_logs_status_outer_container");
    var update_logs_status_inner_container = $("#update_logs_status_inner_container");

    hideUpdateLogs()

    update_logs_submit_button.click(function(event){
        event.preventDefault();
        $.ajax({
            type: "GET",
            url: "update_access_logs/triggered", 
            dataType: "json", 
            success: function(updateStatus) {
                currentUpdateStatus = updateStatus["status"]
                stackTrace = updateStatus["stackTrace"]

                showUpdateLogs(currentUpdateStatus, stackTrace)

            }

        })
    })

    function hideUpdateLogs() {
        update_logs_status_outer_container.css({
            'display' : 'none'
        })
    }

    function showUpdateLogs(currentStatus, stackTrace) {
        update_logs_status_outer_container.css({
            'display' : 'block'
        })

        update_logs_status_inner_container.html(
            "<p>Current Status: " + currentStatus + "</p>" +
            "<br>" +
            "<p>Stack Trace: " + stackTrace + "</p>"
        )
    }
})