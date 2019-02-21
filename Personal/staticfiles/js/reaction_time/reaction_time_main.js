
document.addEventListener("DOMContentLoaded", function() {


    var reaction_time_start = document.getElementById("reaction_time_start_button")
    var introductory_container = document.getElementById("reaction_time_introductory_outer_div")

    reaction_time_start.addEventListener("click", () => {
        introductory_container.className = "hidden";
        inner_loop()
    })

    function inner_loop() {

        // Get the canvas from the DOM
        var canvas = document.getElementById("canvas")
        var canvas_div = document.getElementById("main_canvas_div")

        // Make it visible
        canvas.className = "visible"
        canvas_div.className = "visible"

        if (canvas.getContext) {
            var context = canvas.getContext('2d');
            console.log("Supported");
    
        } else {
            var unsupported_h1 = document.createElement("h1");
            var unsupported_canvas_message = "<h1>Sorry but your browser doesn't support this feature...</h1>";
            unsupported_h1.append(unsupported_canvas_message)
            canvas.appendChild(unsupported_h1)
            return
        } 

        // Get the elements from the DOM
        var left_face_element = document.getElementById("my_face_left")
        var right_face_element = document.getElementById("my_face_right")

        // Declare the array to pass into the constructor
        var face_array = [left_face_element, right_face_element]

        // Set the dimensions of the canvas
        var computed_style = getComputedStyle(canvas)
        canvas.width = parseInt(computed_style.getPropertyValue('width'))
        canvas.height = parseInt(computed_style.getPropertyValue('height'))

        var canvas_dimensions = {
            width: canvas.width,
            height: canvas.height
        }

        // Insantiate the Class
        var face_object = new Face_Image(face_array, canvas_dimensions)

        // Declare the empty array where the reaction times will be pushed
        var reaction_times = []

        // Initial Face Load
        face_object.main_load_loop(context)

        // Iterate over the index to append each value one by one
        var index = 0

        // Inner Loop
        canvas.addEventListener("click", function(event) {
            if (reaction_times.length <= 9){
                var reaction_time = face_object.send_reaction_times()
                face_object.main_click_loop(context, event, face_object)
                reaction_times.push(reaction_time[index])
                index++
            } else {
                // Outer Loop
                outer_loop(reaction_times)
            }
        });
    }

    function outer_loop(reaction_times) {
        remove_canvas()
        var avg_reaction_time = compute_avg_reaction_time(reaction_times)
        var closest_reaction_time = locate_nearest_reaction_time(avg_reaction_time)
        append_results_to_DOM(closest_reaction_time, avg_reaction_time)
    }

    // Remove the canvas from visibility
    function remove_canvas() {
        var canvas = document.getElementById("canvas")
        canvas.className = "hidden";
    }

    // Find the average of each click
    function compute_avg_reaction_time(reaction_times) {
        var sum = 0
        var divisor = reaction_times.length
        reaction_times.forEach(function(reaction_time, index) {
            sum += parseInt(reaction_time)
        })
        var avg_reaction_time = sum / divisor
        avg_reaction_time = Math.floor(avg_reaction_time)
        return avg_reaction_time
    } 


    // Recursively locate nearest reaction time read by JSON data and return array of results
    function locate_nearest_reaction_time(avg_reaction_time) {

        var goal = avg_reaction_time

        var reaction_time_data = window.reaction_times

        var age_group_array = [
            "Ages 18 to 30",
            "Ages 31 to 40",
            "Ages 41 to 50",
            "Ages 51 to 60",
            "Ages 61 to 70",
            "Ages 71 to 80"
        ]

        var reaction_time_by_age_group = reaction_time_data["Reaction_Times"][0]["Age Group"]

        var closest_reaction_time_array = []

        for (var i=0; i<age_group_array.length; i++) {

            var temp_reaction_time_array = []

            var each_age_group = reaction_time_by_age_group[i][age_group_array[i]];

            for (var j = 0; j < 9; j++) {
                var each_score = each_age_group[j]["Score"]
                temp_reaction_time_array.push(each_score)
                
            }   

            var closest_result = temp_reaction_time_array.reduce(function(prev, curr) {
                return Math.abs(curr - goal) < Math.abs(prev - goal) ? curr : prev


            })

            for (var j = 0; j < 9; j++) {
                if (each_age_group[j].Score == closest_result) {
                    closest_reaction_time_array.push({
                        "Ages" : age_group_array[i],
                        "Data" : each_age_group[j]
                    })
                }

            }
        }

        return closest_reaction_time_array
    }
            

    // append the results to the DOM
    function append_results_to_DOM(closest_reaction_time_array, avg_reaction_time) {
        var results_div = document.getElementById("reaction_time_display_results_container")
        results_div.className = "visible";

        var avg_score_span = document.getElementById("reaction_time_avg_score")
        var avg_score_paragraph = document.getElementById("reaction_time_display_results_p");
        var data_span = document.getElementById("reaction_time_data_span");

        if (isNaN(avg_reaction_time)) {
            avg_score_paragraph.innerHTML = "Hang on a second... Can't seem to locate your reaction time..."
            // return 
        } else {
            avg_score_span.innerHTML = avg_reaction_time.toString()
        }
        var data_chunk;

        data_chunk = ""

        closest_reaction_time_array.forEach(function(entry, index) {
            var age_group = entry["Ages"]
            var score = entry["Data"]["Score"]
            var percentile = entry["Data"]["Percentile"]

            data_chunk += "<p>From " + age_group;
            data_chunk += " you are in the " + percentile + " percentile";
            data_chunk += " with the closest median score being " + score + ".</p>"

            data_span.innerHTML = data_chunk
        })
    }
      


})