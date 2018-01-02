$(document).ready(function () {

    $('tr:even').addClass('even');

    var classes = $('.course_classes');
    classes.each(function () {
        var str = $(this).html();
        str = str.replace(/\n/g, '<br>');
        $(this).html(str);
    });

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
        MyAjax_Get('getpage', 'workload_input_pratice_course_add', null, '.pratice_course_add_content', location)
    });

    $('.pratice_course_submit_audit').click(function () {
        var id = this.id;
        id = id.substring(0, id.length - 13);
        var location = $('#location_year').val() + ',' + $('#location_semester').val();
        MyAjax_Get('/upload', 'pratice_course_submit_audit', id, null, location);
    });

    $('.pratice_course_modify').click(function () {
        var id = this.id;
        id = id.substring(0, id.length - 7);
        MyAjax_Get('getpage', 'workload_input_pratice_course_add', id, '.pratice_course_add_content')
    });

    $('.pratice_course_delete').click(function () {
        var id = this.id;
        id = id.substring(0, id.length - 7);
        var location = $('#location_year').val() + ',' + $('#location_semester').val();
        if (confirm("确认删除？"))
            MyAjax_Get('/upload', 'pratice_course_delete', id, null, location);
    });

    $('.search_button').click(function () {
        $('#pratice_course_search_form').ajaxSubmit({
            target: '.content_right',
            error: function () {
                alert('error');
            }
        })
    });
});