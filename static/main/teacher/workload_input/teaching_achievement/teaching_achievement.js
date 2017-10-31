$(document).ready(function () {
    $('tr:even').addClass('even');

    $('.audit_reject').hover(
        function () {
            $(this).children().show();
        },
        function () {
            $(this).children().hide();
        }
    );

    $('.add_button').click(function () {
        var extra_data = $(this).attr('id');
        MyAjax_Get('getpage', 'workload_input_teaching_achievement_add', null, '.teaching_achievement_add_content', extra_data);
    });

    $('.teaching_achievement_modify').click(function () {
        var id = this.id;
        id = id.substring(0, id.length - 7);
        MyAjax_Get('getpage', 'workload_input_teaching_achievement_add', id, '.teaching_achievement_add_content')
    });

    $('.teaching_achievement_delete').click(function () {
        var id = this.id;
        id = id.substring(0, id.length - 7);
        if (confirm("确认删除？"))
            MyAjax('/upload', 'teaching_achievement_delete', id);
    });

    $('.search_button').click(function () {
        $('#teaching_achievement_search_form').ajaxSubmit({
            target: '.content_right',
            error: function () {
                alert('error!');
            }
        })
    });
});