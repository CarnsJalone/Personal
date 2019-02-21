class Face_Image {

    constructor(img_array, canvas) {
        this.height = 50;
        this.width = 50;
        this.element;
        this.img_array = img_array
        this.canvas_width = canvas.width
        this.canvas_height = canvas.height
        this.centered_text_x = (this.canvas_width / 2) - (this.width / 2)
        this.centered_text_y = (this.canvas_height / 2) - (this.height / 2)
        this.reaction_times = []
        this.start_time = null
        this.end_time = null    
        this.x = this.random_x_position()
        this.y = this.random_y_position()
    }

    random_x_position() {

        // Calculates a random x coordinate in the first or third third of the canvas

        var one_third_canvas_width = (this.canvas_width / 3)
        var first_third_x = [0, one_third_canvas_width]
        var third_third_x = [(one_third_canvas_width * 2), this.canvas_width]

        var random_coord_first_third = Math.floor(Math.random() * (first_third_x[1] - first_third_x[0] + 1)) + first_third_x[0];
        var random_coord_third_third = Math.floor(Math.random() * (third_third_x[1] - third_third_x[0] + 1)) + third_third_x[0];

        var random_third_selection

        random_third_selection = Math.floor(Math.random() * 2)
        
        if (random_third_selection === 0) {
            this.x = random_coord_first_third
            if (this.x > this.canvas_width - this.width) {
                this.x = this.canvas_width - this.width
            } else if (this.x < 0) {
                this.x = 0
            }
        } else if (random_third_selection === 1) {
            this.x = random_coord_third_third
            if (this.x > this.canvas_width - this.width) {
                this.x = this.canvas_width - this.width
            } else if (this.x < 0) {
                this.x = 0
            }
        }
        return this.x
    }

    random_y_position() {

        // Calculates a random y coordinate in the first or third third of the canvas
        
        var one_third_canvas_height = (this.canvas_height / 3)
        var first_third_y = [0, one_third_canvas_height]
        var third_third_y = [(one_third_canvas_height * 2), this.canvas_height]

        var random_coord_first_third = Math.floor(Math.random() * (first_third_y[1] - first_third_y[0] + 1)) + first_third_y[0];
        var random_coord_third_third = Math.floor(Math.random() * (third_third_y[1] - third_third_y[0] + 1)) + third_third_y[0];

        var random_third_selection

        random_third_selection = Math.floor(Math.random() * 2)
        
        if (random_third_selection === 0) {
            this.y = random_coord_first_third
            if (this.y > this.canvas_height - this.height) {
                this.y = this.canvas_height - this.height
            } else if (this.y < 0) {
                this.y = 0
            }
        } else if (random_third_selection === 1) {
            this.y = random_coord_third_third
            if (this.y > this.canvas_height - this.height) {
                this.y = this.canvas_height - this.height
            } else if (this.y < 0) {
                this.y = 0
            }
        }
        return this.y
    }

    reset_positions() {
        this.x = this.random_x_position()
        this.y = this.random_y_position()
    }

    // Choose at random which way the face will face
    random_facing_image(img_array) {
        var img_selection = img_array[Math.floor(Math.random() * img_array.length)]
        return img_selection
    }

    // Draws the face on the screen at random x and y coordinates
    draw(context) {
        this.element = this.random_facing_image(this.img_array)
        context.drawImage(this.element, this.x, this.y, this.width, this.height)
    }

    // The main portion of the circle function
    transitive_circle(context) {
        this.circle_x = this.x + (this.width / 2)
        this.circle_y = this.y + (this.height / 2)
        this.circle_start_angle = 0
        this.circle_end_angle = (2 * Math.PI)

        var random_fill_array = [
            "#161B59", 
             "#2E3476", 
             "#494E8F", 
             "#6E73AB", 
             "#9FA3CC", 
             "#1D3B57", 
             "#4C8872", 
             "#78A091", 
             "#C5E1CB"
        ]

        var randomly_selected_fill = random_fill_array[Math.floor(Math.random() * random_fill_array.length)]
        

        for (var index = 1; index < 70; index++) {
            var incremental_wait = index * 15
            setTimeout(this.enlarge_circle.bind(this, context, index, randomly_selected_fill), incremental_wait)
        }
    }

    // Create a circle that flies from the clicked object to the edges of the screen then disappears
    enlarge_circle(context, index, randomly_selected_fill) {

        var previous_index = index - 1
        var current_radius = ((this.width * index) / 2)
        var previous_radius = ((this.width * previous_index) / 2)
        context.fillStyle = randomly_selected_fill
        context.beginPath()
        context.arc(this.circle_x, this.circle_y, current_radius, this.circle_start_angle, this.circle_end_angle)
        context.stroke()
        context.fill()
        context.save()

        context.fillStyle = 'white'
        context.beginPath()
        context.arc(this.circle_x, this.circle_y, previous_radius, this.circle_start_angle, this.circle_end_angle)
        context.stroke()
        context.fill()
        context.save()
    }

    // Verify whether or not face was properly clicked
    is_clicked(image, event) {
        var width = image.width
        var height = image.height
        var begin_x = image.x
        var begin_y = image.y
        var end_x = begin_x + width
        var end_y = begin_y + height 
        var buffer = 10
        var click_x = event.offsetX
        var click_y = event.offsetY
        var has_been_clicked = false

        if (click_x >= begin_x - buffer && click_x <= end_x + buffer && click_y >= begin_y - buffer && click_y <= end_y + buffer) {
            has_been_clicked = true
        } else {
            has_been_clicked = false
        }

        return has_been_clicked
    }

    clear_screen(context) {
        context.clearRect(0, 0, canvas.width, canvas.height)
    }

    clear_face(context) {
        context.clearRect(this.x, this.y, this.width, this.height)
    }

    start_counter() {
        this.start_time = new Date().getTime()
    }

    end_counter() {
        this.ellapsed_time = new Date().getTime() - this.start_time
        return this.ellapsed_time
    }

    reset_counter() {
        this.start_time = null
        this.ellapsed_time = null
    }

    random_delay() {
        var ms_array = [1100, 1200, 1300, 1400, 1500, 1700, 1900, 2100, 2500, 3000]
        var random_selection = ms_array[Math.floor(Math.random() * ms_array.length)]
        return random_selection
    }

    display_reaction_times(context) {
        context.font = "30px Arial"
        context.fillText(this.reaction_times, 0, this.centered_text_y)
    }

    main_load_loop(context) {
        var random_delay = this.random_delay()
        setTimeout(this.draw.bind(this, context), random_delay)
        setTimeout(this.start_counter.bind(this), random_delay)
    }

    click_event_loop(context, event, image) {

        var is_collision = this.is_clicked(image, event)

        if (is_collision) {
            var end_time = this.end_counter()
            this.reaction_times.push(end_time)
            this.clear_face(context);
            this.transitive_circle(context)
            this.reset_counter()
            this.reset_positions()
            this.clear_screen(context)
            this.main_load_loop(context)
        }
    }

    display_results(context) {
        this.clear_screen(context)
        this.display_reaction_times(context)
    }

    main_click_loop(context, event, image) {
        this.click_event_loop(context, event, image)
        this.send_reaction_times()
    }

    send_reaction_times() {
        return this.reaction_times
    }

}
