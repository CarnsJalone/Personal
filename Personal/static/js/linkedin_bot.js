$(document).ready(function(){

    var linkedin_mp4 = $("iframe.linkedin_bot_video")
    var sixteen_by_nine_divisor = .5625
    var starting_win_width = $(window).width()

    function update_video_height() {
        var video_height = linkedin_mp4.width() * sixteen_by_nine_divisor
        console.log(video_height)
        linkedin_mp4.css({
            "height" : video_height + "px"
        })
    }

    update_video_height()

    $(window).resize(function(event){
        update_video_height()
    })
    

})