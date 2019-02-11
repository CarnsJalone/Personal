$(document).ready(function(){

    set_responsive_header_class()

    function detect_breakpoint(win_width) {
        var breakpoint_upper, breakpoint_lower, breakpoint_case
    
        var breakpoints = [
            [0, 400, 1], // Between 0 and 400 pixels
            [401, 550, 2], // Between 401 and 550 pixels
            [551, 767, 3], // Between 551 and 767 pixels
            [768, 992, 4], // Between 768 and 992 pixels
            [993, 1200, 5], // Between 993 and 1200 pixels
            [1201, 1500, 6], // Between 1201 and 1500 pixels
            [1501, 5000, 7] // 1501 pixels and up
        ]

        for (var i=0; i<breakpoints.length; i++) {
            breakpoint_lower = breakpoints[i][0]
            breakpoint_upper = breakpoints[i][1]
            breakpoint_case = breakpoints[i][2]
            
            if (win_width >= breakpoint_lower && win_width < breakpoint_upper) {
                return breakpoint_case
            }
        }
    }

    function set_trigger_height() {
        var breakpoint_case = detect_breakpoint($(window).width())
        var trigger_height;

        if (breakpoint_case == 1) {
            trigger_height = 50;
            // Between 0 and 400 pixels
            return trigger_height
        } else if (breakpoint_case == 2) {
            trigger_height = 75;
            // Between 401 and 550 pixels
            return trigger_height
        } else if (breakpoint_case == 3) {
            trigger_height = 150;
            // Between 551 and 767 pixels
            return trigger_height
        } else if (breakpoint_case == 4) {
            trigger_height = 200;
            // Between 768 and 992 pixels
            return trigger_height
        } else if (breakpoint_case == 5) {
            trigger_height = 225
            // Between 993 and 1200 pixels
            return trigger_height
        } else if (breakpoint_case == 6) {
            trigger_height = 250;
            // Between 993 and 1200 pixels
            return trigger_height
        } else if (breakpoint_case == 7) {
            // 1201 pixels and up
            trigger_height = 300
            return trigger_height
        } else trigger_height = 0
            return trigger_height

    }

    function set_responsive_header_class() {
        var trigger_height = set_trigger_height()
        var mountain = $("#vector_mountain_img")
        var target_header = $(".target_header")

        // Iterate through headers to locate which we want to trigger
        target_header.each(function(index, each_header){
            if ($(each_header).offset().top >= ($(mountain).offset().top + trigger_height)) {
                $(each_header).attr("class", "target_header about_me_blue_text_highlight");
            } else {
                $(each_header).attr("class", "target_header about_me_off_white_text_highlight")
            }
        })
    }

    $(window).scroll(function(event){
        set_responsive_header_class()
    })
})