$(document).ready(function () {
    $('.search_button').click(function () {
        var year = $('#workload_count_year').val();
        MyAjax_Get('/getpage', 'workload_count', year);
    });
});