$(document).ready(function(){

    var $input = $('#display_contents_uploaded_data_search_bar_input'); 
    var $container = $('#display_contents_uploaded_data_container');
    var $data = $('#display_contents_upload_data_pre');

    $input.keyup(function(event){
        search();
    })

    function search() {

        var data = $data.html()

        console.log(typeof($data))

        // for (i=0; i<data.length; i++) {
        //     console.log(data[i])
        //     console.log(typeof(data))
        // }

    }

})