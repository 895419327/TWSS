$(document).ready(function () {

    window.scrollTo(0, 0);

    $('tr:even').addClass('even');

    $('.competition_guide_audit_pass').click(function () {
        var id = this.id;
        id = id.substring(0, id.length - 5);
        var location = $('#location_year').val() + ','
            + $('#location_audit_status').val();
        MyAjax_Get('getpage', 'workload_audit_competition_guide_pass', id, null, location);
    });

    $('.competition_guide_audit_reject').click(function () {
        var id = this.id;
        id = id.substring(0, id.length - 7);
        var data = 'CompetitionGuide,' + id;
        MyAjax_Get('getpage', 'workload_audit_reject_page', data, '.workload_audit_reject_content');
    });

    $('.search_button').click(function () {
        $('#competition_guide_audit_search_form').ajaxSubmit({
            target: '.content_right',
            error: function () {
                alert('error!');
            }
        })
    });
});