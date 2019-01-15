$(document).ready(function(){

    var $input = $('#display_contents_uploaded_data_search_bar_input'); 
    var $container = $('#display_contents_uploaded_data_container');
    var $data = $('#display_contents_upload_data_pre');

    function find_text() {
        console.log($input.val())
        console.log($input.val().length)

        $data.find($input.val())
    }

    $input.keyup(function(event){
        if ($input.val().length >= 3) {
            find_text()
        }
    })

})