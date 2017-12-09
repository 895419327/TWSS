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
        var location = $('#location_year').val() + ',' + $('#location_semester').val();
        MyAjax_Get('getpage', 'workload_input_teaching_achievement_add', null, '.teaching_achievement_add_content', location);
    });

    $('.teaching_achievement_modify').click(function () {
        var id = this.id;
        id = id.substring(0, id.length - 7);
        MyAjax_Get('getpage', 'workload_input_teaching_achievement_add', id, '.teaching_achievement_add_content')
    });

    $('.teaching_achievement_delete').click(function () {
        var id = this.id;
        id = id.substring(0, id.length - 7);
        var location = $('#location_year').val() + ',' + $('#location_semester').val();
        if (confirm("确认删除？"))
            MyAjax_Get('/upload', 'teaching_achievement_delete', id, null, location);
    });

    $('.search_button').click(function () {
        $('#teaching_achievement_search_form').ajaxSubmit({
            target: '.content_right',
            error: function () {
                alert('连接服务器失败');
            }
        })
    });
});