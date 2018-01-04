$(document).ready(function () {

    // window.scrollTo(0, 0);

    $('tr:even').addClass('even');

    $('.experiment_course_audit_pass').click(function () {
        var id = this.id;
        id = id.substring(0, id.length - 5);
        var location = $('#location_year').val() + ','
            + $('#location_semester').val() + ','
            + $('#location_audit_status').val();
        MyAjax_Get('getpage', 'workload_audit_experiment_course_pass', id, null, location);
    });

    $('.experiment_course_audit_reject').click(function () {
        var id = this.id;
        id = id.substring(0, id.length - 7);
        var data = 'ExperimentCourse,' + id;
        MyAjax_Get('getpage', 'workload_audit_reject_page', data, '.workload_audit_reject_content');
    });

    $('.search_button').click(function () {
        $('#experiment_course_audit_search_form').ajaxSubmit({
            target: '.content_right',
            error: function () {
                alert('error');
            }
        })
    });
});