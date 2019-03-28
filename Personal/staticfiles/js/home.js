$(document).ready(function(){


    var me_div = $("#home_me_living_life_div")
    var me_img = $("#home_me_living_life_img")
    var nav = $("#main_header_outer")

    var me_div_position = me_div.position()
    var me_div_top = me_div_position.top
    var me_div_left = me_div_position.left
    var me_div_height = me_div.height()

    var me_img_position = me_img.position()    
    var me_img_top = me_img_position.top
    var me_img_left = me_img_position.left
    
    var nav_height = nav.height()
    
    var distance = me_div_top - nav_height
    
    var increment = distance / 2
    var flight_speed = 600;

    function flight_animation() {
        me_div.css({
            "zIndex" : -1
        })
        me_img.animate({
            opacity: 1
        }, flight_speed, 'linear', function(){
            me_div.animate({
                top: nav_height - me_div_height + "px"
            }, flight_speed - 300, 'linear', function(){
                me_div.css({
                    "transform" : "rotate(-180deg)"
                })
                me_div.animate({
                    left: me_div_left + "px"
                }, flight_speed, 'linear', function() {
                    me_div.animate({
                        top: $(window).height() + me_div_height + "px"
                    }, flight_speed, 'linear', function(){
                        me_div.animate({
                            left: $(window).width() + me_div.width() + "px",
                        }, flight_speed, 'linear', function(){
                            me_div.animate({
                                top: me_div_top
                            }, flight_speed, 'linear', function(){
                                me_div.css({
                                    "transform" : "rotate(-90deg)"
                                })    
                                me_div.animate({
                                    left: 0 - (me_div.height() * 4)
                                }, flight_speed, 'linear', function(){
                                    me_div.css({
                                        "transform" : "rotate(90deg)"
                                    })
                                    me_div.animate({
                                        left: $(window).width() + me_div.height()
                                    }, flight_speed + 400, 'linear', function(){
                                        me_div.animate({
                                            top: $(window).height() + me_div.height()
                                        }, flight_speed, 'linear', function(){
                                            me_div.css({
                                                "transform" : "rotate(90deg):"
                                            })
                                            me_div.animate({
                                                top: $(window).height() + me_div_height + "px"
                                            }, flight_speed, 'linear', function(){
                                                me_div.animate({
                                                    left: me_div_left + "px"
                                                }, flight_speed, 'linear', function() {
                                                    me_div.css({
                                                        "transform" : "rotate(0deg)"
                                                    })
                                                    me_div.animate({
                                                        top: me_div_top
                                                    }, flight_speed, 'linear', function(){
                                                        me_img.animate({
                                                            opacity: .25
                                                        }, flight_speed, 'linear', function(){})
                                                    });
                                                });
                                            });
                                        });
                                    });
                                });
                            });
                        })
                    });
                });
            });
        })

        

        

        

        

        

        

        

        

        

        
        

        // me_img.animate({
        //     opacity: 0
        // }, 'linear', function(){})

        
    }
    
    // function deactivate_animation() {
    //     me.removeClass("active_animation")
    // }

    flight_animation()
})