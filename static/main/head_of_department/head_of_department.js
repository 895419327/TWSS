$(document).ready(function () {

    $('#teacher_management_title').click(function () {
        $('.main_content').prepend('<div class="loading">正在加载...</div>');
        MyAjax_Get('/getpage', 'teacher_management');
    });

    $('#workload_statistics_title').click(function () {
        $('.main_content').prepend('<div class="loading">正在加载...</div>');
        MyAjax_Get('/getpage', 'workload_statistics');
    });
});