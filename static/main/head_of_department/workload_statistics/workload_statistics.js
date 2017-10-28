$(document).ready(function () {
    $('tr:even').addClass('even');

    $('.search_button').click(function () {
        var year = $('#workload_statistics_year').val();
        MyAjax_Get('/getpage', 'workload_statistics', year);
    });
});