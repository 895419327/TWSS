$(document).ready(function () {

    $('#global_settings_title').click(function () {
        $('.main_content').prepend('<div class="loading">正在加载...</div>');
        MyAjax_Get('/getpage', 'global_settings');
    });

    $('#notice_settings_title').click(function () {
        $('.main_content').prepend('<div class="loading">正在加载...</div>');
        MyAjax_Get('/getpage', 'notice_settings');
    });

    $('#department_management_title').click(function () {
        $('.main_content').prepend('<div class="loading">正在加载...</div>');
        MyAjax_Get('/getpage', 'department_management');
    });

    $('#teacher_management_title').click(function () {
        $('.main_content').prepend('<div class="loading">正在加载...</div>');
        MyAjax_Get('/getpage', 'teacher_management');
    });

    $('#class_management_title').click(function () {
        $('.main_content').prepend('<div class="loading">正在加载...</div>');
        MyAjax_Get('/getpage', 'class_management');
    });

    $('#workload_statistics_title').click(function () {
        $('.main_content').prepend('<div class="loading">正在加载...</div>');
        MyAjax_Get('/getpage', 'workload_statistics');
    });

    $('#workload_K_value_title').click(function () {
        $('.main_content').prepend('<div class="loading">正在加载...</div>');
        MyAjax_Get('/getpage', 'workload_K_value');
    });
});