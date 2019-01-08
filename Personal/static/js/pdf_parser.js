$(document).ready(function(){

    var $input = $('#display_contents_uploaded_data_search_bar_input'); 
    var $container = $('#display_contents_uploaded_data_container');
    var $data = $('#display_contents_upload_data_pre');

    $input.keyup(function(event){
        search();
    })

    function search() {


        var data = $data.html()

        data = data.replace("<p>", "").replace("</p>", "").replace(/[.\w\d\s]*-<\/p><p>[.\w\d\s]*/g, "\n").replace(/\n/ig, '')

        var each_line = data.split("<br>")

        // console.log(each_line)

        for (i=0; i<each_line.length; i++) {

            var trimmed_lines = each_line[i].split(" ")

            // trimmed_lines.innerHTML = "<p>" + trimmed_lines + "</p>"

            for (j=0; j<trimmed_lines.length; j++) {

                seperated_words = trimmed_lines[j].trim()

                // seperated_words = seperated_words.toUpperCase()

                if ($input.val().length >=3) {

                    var substring = seperated_words.includes($input.val().toUpperCase())

                    if (substring) {


        
 
                    }
                }
            }

        }

        //     for (j=0; j<trimmed_lines.length; j++) {


        //         seperated_words = trimmed_lines[j].trim()

        //         seperated_words = seperated_words.toUpperCase()

        //         if ($input.val().length >=3) {

        //             var substring = seperated_words.includes($input.val().toUpperCase())

        //             if (substring) {

        //                 console.log(data[trimmed_lines])

        //                 // substring.html("<span id='immediate_search_terms'" + data[substring] + "></span>")

        //                 // Highlight the actual words searched
        //                 // substring.innerHTML(substring + "<id=immediate_search_terms>")

        //                 console.log(trimmed_lines)
        //             }

        //         }

        //     }


        }

        // console.log(data)

        // console.log(each_line)

        // console.log(data)

        // for (i=0; i<data.length; i++) {
        //     console.log(data[i])
        //     console.log(typeof(data))
        // }



})