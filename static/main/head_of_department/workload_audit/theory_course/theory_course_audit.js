$(document).ready(function () {
    $('.theory_course_audit_pass').click(function () {
        var id = this.id;
        id = id.substring(0, id.length - 5);
        MyAjax_Get('getpage', 'workload_audit_theory_course_pass', id);
    });

    $('.theory_course_audit_reject').click(function () {
        var id = this.id;
        id = id.substring(0, id.length - 7);
        MyAjax_Get('getpage', 'workload_audit_theory_course_reject', id);
    });
});