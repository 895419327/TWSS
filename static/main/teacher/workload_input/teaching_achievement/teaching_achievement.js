$(document).ready(function () {
    $('tr:even').addClass('even');

    $('.teaching_achievement_add_button').click(function () {
        MyAjax_Get('getpage', 'workload_input_teaching_achievement_add', null, '.teaching_achievement_add_content')
    });

    $('.teaching_achievement_modify').click(function () {
        var id = this.id;
        id = id.substring(0, id.length - 7);
        MyAjax_Get('getpage', 'workload_input_teaching_achievement_modify', id, '.teaching_achievement_add_content');
    });

    $('.teaching_achievement_delete').click(function () {
        var id = this.id;
        id = id.substring(0, id.length - 7);
        if (confirm("确认删除？"))
            MyAjax('/upload', 'teaching_achievement_delete', id);
    });
    
    $('#teaching_achievement_search_button').click(function () {
        $('#teaching_achievement_search_form').ajaxSubmit({
            target: '.content_right',
            error:function () {
                alert('error!');
            }
        })
    });
});