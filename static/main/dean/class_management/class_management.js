$(document).ready(function () {

    // window.scrollTo(0, 0);

    $('tr:even').addClass('even');

    $('.search_button').click(function () {
        var grade = $('#class_management_grade').val();
        $('.main_content').prepend('<div class="loading">正在加载...</div>');
        MyAjax_Get('/getpage', 'class_management', grade);
    });

    $('.add_button').click(function () {
        var department = $(this).attr('id');
        var grade = $('#location_grade').val();
        var location = department + ' ' + grade;
        MyAjax_Get('getpage', 'class_management_add', null, '.class_management_add_content', location);
    });

    $('.class_management_modify').click(function () {
        var id = this.id;
        id = id.substring(0, id.length - 7);
        MyAjax_Get('getpage', 'class_management_add', id, '.class_management_add_content');
    });

    $('.class_management_delete').click(function () {
        var id = this.id;
        id = id.substring(0, id.length - 7);
        if (confirm("确认删除？"))
            MyAjax_Get('/upload', 'class_delete', id);
    });
});