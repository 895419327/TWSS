$(document).ready(function () {
    $('.search_button').click(function () {
        var year = $('#workload_count_year').val();
        var audit_status = $('#workload_count_audit_status').val();
        MyAjax_Get('/getpage', 'teacher_workload_count', year, '.content_right', audit_status);
    });
});