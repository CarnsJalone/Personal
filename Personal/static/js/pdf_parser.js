$(document).ready(function(){

    var $input = $('#display_contents_uploaded_data_search_bar_input'); 
    var $container = $('#display_contents_uploaded_data_container');
    var $data = $('#display_contents_upload_data_pre');

    var pre = $('pre')

    var children = pre.children()
    
    $input.keyup(function(event){
        search();
    })

    function search() {

        data = $data.html()

        children.css({
            'background-color' : 'red'
        })

        children.each(function(){
            console.log($(this))
        })

 

        // console.log(children.html())

        console.log(grandchildren.html())

        // for (a=0; a<data.length; a++) {
        //     console.log(data[a])
        // }

    }


    //     var data = $data.html()

    //     console.log(data[0])

    //     br_replace_regex = /[a-zA-Z0-9.\n]*<br>[a-zA-Z0-9.\n]*/g;

    //     // TODO - need to fix this regex function so it only puts a </p> at the end of a line
    //     // end_line_replace_regex = /[\w\d\s\W\D\S]+\n/g

    //     data = data.replace('\n', '<p></p>')
    //     data = data.replace(br_replace_regex, '</p>\n<p>')

    //     var each_line = data.split("\n")

    //     for (i=0; i<each_line.length; i++) {

    //         var trimmed_lines = each_line[i].split(" ");

    //         for (j=0; j<trimmed_lines.length; j++) {

    //             seperated_words = trimmed_lines[j].trim()

    //             if ($input.val().length >=3) {

    //                 var substring = seperated_words.toUpperCase().includes($input.val().toUpperCase())

    //                 if (substring) {

    //                     // console.log($data.html()[j])

    //                     // console.log(trimmed_lines[0])
    //                     // trimmed_lines = trimmed_lines[0].replace("<p>", "<p id='highlighted'>")
    //                     // trimmed_lines.css({
    //                     //     'id' : 'highlighted'
    //                     // })
    //                     // console.log(trimmed_lines)

    //                     document.body.innerHTML = trimmed_lines[j]

    //                 }

    //             }

    //             // console.log(seperated_words)

    //         }

    //     }


    //     // for (i=0; i<each_line.length; i++) {

    //     //     var trimmed_lines = each_line[i].split(" ")

    //     //     // trimmed_lines.innerHTML = "<p>" + trimmed_lines + "</p>"

    //     //     for (j=0; j<trimmed_lines.length; j++) {

    //     //         seperated_words = trimmed_lines[j].trim()

    //     //         // seperated_words = seperated_words.toUpperCase()

    //     //         if ($input.val().length >=3) {

    //     //             var substring = seperated_words.toUpperCase().includes($input.val().toUpperCase())

    //     //             if (substring) {

    //     //                 console.log(each_line)
    //     //                 // console.log(typeof(seperated_words))
        
 
    //     //             }
    //     //         }
    //     //     }

    //     }

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


        // }

        // console.log(data)

        // console.log(each_line)

        // console.log(data)

        // for (i=0; i<data.length; i++) {
        //     console.log(data[i])
        //     console.log(typeof(data))
        // }



})