$(document).ready(function () {

    window.scrollTo(0, 0);

    $('tr:even').addClass('even');

    $('.change_head_of_department').click(function () {
        var id = this.id;
        id = id.substring(0, id.length - 7);
        MyAjax_Get('getpage', 'department_management_modify', id, '.department_management_add_content');
    });
});