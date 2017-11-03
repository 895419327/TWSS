$(document).ready(function () {

    $('#database_dump_button').click(function () {
        $('#database_dump_form').submit();

        setTimeout(function () {
            MyAjax_Get('/getpage', 'database_management');
        }, 1000);
    });


});