$(document).ready(function(){


    var me = $("#home_me_living_life_div")

    function activate_animation() {
        me.attr("class", "active_animation")
    }
    
    function deactivate_animation() {
        me.removeClass("active_animation")
    }

    activate_animation()
})