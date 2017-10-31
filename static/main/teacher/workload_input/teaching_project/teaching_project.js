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
        MyAjax_Get('getpage', 'workload_input_teaching_project_add', null, '.teaching_project_add_content', extra_data);
    });

    $('.teaching_project_modify').click(function () {
        var id = this.id;
        id = id.substring(0, id.length - 7);
        MyAjax_Get('getpage', 'workload_input_teaching_project_add', id, '.teaching_project_add_content')
    });

    $('.teaching_project_delete').click(function () {
        var id = this.id;
        id = id.substring(0, id.length - 7);
        if (confirm("确认删除？"))
            MyAjax('/upload', 'teaching_project_delete', id);
    });

    $('.search_button').click(function () {
        $('#teaching_project_search_form').ajaxSubmit({
            target: '.content_right',
            error: function () {
                alert('error!');
            }
        })
    });
});