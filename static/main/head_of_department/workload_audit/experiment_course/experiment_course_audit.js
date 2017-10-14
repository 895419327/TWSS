$(document).ready(function () {
    $('tr:even').addClass('even');

    $('.experiment_course_audit_pass').click(function () {
        var id = this.id;
        id = id.substring(0, id.length - 5);
        MyAjax_Get('getpage', 'workload_audit_experiment_course_pass', id);
    });

    $('.experiment_course_audit_reject').click(function () {
        var id = this.id;
        id = id.substring(0, id.length - 7);
        if (confirm("确认驳回？"))
            MyAjax_Get('getpage', 'workload_audit_experiment_course_reject', id);
    });

    $('.search_button').click(function () {
        $('#experiment_course_audit_search_form').ajaxSubmit({
            target: '.content_right',
            error:function () {
                alert('error!');
            }
        })
    });
});