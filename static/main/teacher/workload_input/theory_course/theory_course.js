$(document).ready(function () {

    $('tr:even').addClass('even');

    $('.theory_course_add_button').click(function () {
        MyAjax_Get('getpage', 'theory_course_add', null, '.theory_course_add_content')
    });

    $('.theory_course_modify').click(function () {
        var id = this.id;
        id = id.substring(0, id.length - 7);
        MyAjax_Get('getpage', 'theory_course_modify', id, '.theory_course_add_content');
    });

    $('.theory_course_delete').click(function () {
        var id = this.id;
        id = id.substring(0, id.length - 7);
        if (confirm("确认删除？"))
            MyAjax('/upload', 'theory_course_delete', id);
    });
});