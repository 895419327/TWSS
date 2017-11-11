$(document).ready(function () {
    $('tr:even').addClass('even');

    $('.teaching_project_audit_pass').click(function () {
        var id = this.id;
        id = id.substring(0, id.length - 5);
        var location = $('#location_year').val() + ','
                     + $('#location_audit_status').val();
        MyAjax_Get('getpage', 'workload_audit_teaching_project_pass', id, null, location);
    });

    $('.teaching_project_audit_reject').click(function () {
        var id = this.id;
        id = id.substring(0, id.length - 7);
        var data = 'TeachingProject,' + id;
        MyAjax_Get('getpage', 'workload_audit_reject_page', data, '.workload_audit_reject_content');
    });

    $('.search_button').click(function () {
        $('#teaching_project_audit_search_form').ajaxSubmit({
            target: '.content_right',
            error: function () {
                alert('error!');
            }
        })
    });
});