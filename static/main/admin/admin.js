$(document).ready(function () {

    $('#database_management_title').click(function () {
        $('.main_content').prepend('<div class="loading">正在加载...</div>');
        MyAjax_Get('/getpage', 'database_management');
    });

    $('#data_import_title').click(function () {
        $('.main_content').prepend('<div class="loading">正在加载...</div>');
        MyAjax_Get('/getpage', 'data_import');
    });
});