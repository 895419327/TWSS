$(document).ready(function () {

    $('#notice_title').click(function () {
        $('.main_content').prepend('<div class="loading">正在加载...</div>');
        MyAjax_Get('/getpage', 'notice_page');
    });

    $('#workload_count_title').click(function () {
        $('.main_content').prepend('<div class="loading">正在加载...</div>');
        MyAjax_Get('/getpage', 'teacher_workload_count');
    });
});