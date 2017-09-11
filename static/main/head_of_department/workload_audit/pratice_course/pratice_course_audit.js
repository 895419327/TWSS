$(document).ready(function () {
    $('tr:even').addClass('even');

    $('.pratice_course_audit_pass').click(function () {
        var id = this.id;
        id = id.substring(0, id.length - 5);
        MyAjax_Get('getpage', 'workload_audit_pratice_course_pass', id);
    });

    $('.pratice_course_audit_reject').click(function () {
        var id = this.id;
        id = id.substring(0, id.length - 7);
        if (confirm("确认驳回？"))
            MyAjax_Get('getpage', 'workload_audit_pratice_course_reject', id);
    });
    
    $('#pratice_course_audit_search_button').click(function () {
        $('#pratice_course_audit_search_form').ajaxSubmit({
            target: '.content_right',
            error:function () {
                alert('error!');
            }
        })
    });
});