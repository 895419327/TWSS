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
        MyAjax_Get('getpage', 'workload_input_pratice_course_add', null, '.pratice_course_add_content')
    });

    $('.pratice_course_modify').click(function () {
        var id = this.id;
        id = id.substring(0, id.length - 7);
        MyAjax_Get('getpage', 'workload_input_pratice_course_add', id, '.pratice_course_add_content')
    });

    $('.pratice_course_delete').click(function () {
        var id = this.id;
        id = id.substring(0, id.length - 7);
        if (confirm("确认删除？"))
            MyAjax('/upload', 'pratice_course_delete', id);
    });

    $('.search_button').click(function () {
        $('#pratice_course_search_form').ajaxSubmit({
            target: '.content_right',
            error: function () {
                alert('error!');
            }
        })
    });
});