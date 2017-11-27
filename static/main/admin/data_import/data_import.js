$(document).ready(function () {
    $('#import').click(function () {
        MyAjax_Get('/getpage', 'data_import_a');
    });
});