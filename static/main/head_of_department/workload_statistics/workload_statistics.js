$(document).ready(function () {

    window.scrollTo(0, 0);

    $('tr:even').addClass('even');

    $('.search_button').click(function () {
        var year = $('#workload_statistics_year').val();
        var sortby = $('#workload_statistics_sortby').val();
        switch (sortby) {
            case "按教职工号":
                sortby = 'teacher';
                break;
            case "按教学工作量":
                sortby = 'course';
                break;
            case "按教研工作量":
                sortby = 'project';
                break;
            default:
                sortby = 'teacher';
        }
        $('.main_content').prepend('<div class="loading">正在计算...</div>');
        MyAjax_Get('/getpage', 'workload_statistics', year, '.content_right', sortby);
    });

    $('.sort_type').click(function () {
        var year = $('#original_year').val();
        var sortby = $(this).attr('id');
        $('.main_content').prepend('<div class="loading">正在计算...</div>');
        MyAjax_Get('/getpage', 'workload_statistics', year, '.content_right', sortby);
    });

    $('.export_button').click(function () {
        var id = $(this).attr('id');
        id = id.substring(0, id.length - 7);
        $('#export_department').attr('value', id);
        $('#workload_statistics_export_form').submit();
    });
});