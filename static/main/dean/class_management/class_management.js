$(document).ready(function () {
    $('tr:even').addClass('even');
    
    $('.add_button').click(function () {
        MyAjax_Get('getpage', 'class_management_add', null, '.class_management_add_content')
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
            MyAjax_Get('/upload', 'class_management_delete', id);
    });
});