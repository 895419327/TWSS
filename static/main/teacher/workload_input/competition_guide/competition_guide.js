$(document).ready(function () {
    $('tr:even').addClass('even');

    $('.competition_guide_add_button').click(function () {
        MyAjax_Get('getpage', 'workload_input_competition_guide_add', null, '.competition_guide_add_content')
    });

    $('.competition_guide_modify').click(function () {
        var id = this.id;
        id = id.substring(0, id.length - 7);
        MyAjax_Get('getpage', 'workload_input_competition_guide_modify', id, '.competition_guide_add_content');
    });

    $('.competition_guide_delete').click(function () {
        var id = this.id;
        id = id.substring(0, id.length - 7);
        if (confirm("确认删除？"))
            MyAjax('/upload', 'competition_guide_delete', id);
    });
});