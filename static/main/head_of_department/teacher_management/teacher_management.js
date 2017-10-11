$(document).ready(function () {
    $('tr:even').addClass('even');

    $('.teacher_management_add_button').click(function () {
        MyAjax_Get('getpage', 'teacher_management_add', null, '.teacher_management_add_content')
    });
    
    $('.teacher_management_modify').click(function () {
        var id = this.id;
        id = id.substring(0, id.length - 7);
        MyAjax_Get('getpage', 'teacher_management_add', id, '.teacher_management_add_content');
    });

    $('.teacher_management_delete').click(function () {
        var id = this.id;
        id = id.substring(0, id.length - 7);
        if (confirm("确认删除？"))
            MyAjax('/upload', 'teacher_management_delete', id);
    });
});