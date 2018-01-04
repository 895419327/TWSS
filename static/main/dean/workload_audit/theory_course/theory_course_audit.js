$(document).ready(function () {

    // window.scrollTo(0, 0);

    $('tr:even').addClass('even');

    var classes = $('.course_classes');
    classes.each(function () {
        var str = $(this).html();
        str = str.replace(/\n/g, '<br>');
        $(this).html(str);
    });

    $('.theory_course_audit_pass').click(function () {
        var id = this.id;
        id = id.substring(0, id.length - 5);
        var location = $('#location_year').val() + ','
            + $('#location_semester').val() + ','
            + $('#location_audit_status').val();
        MyAjax_Get('getpage', 'workload_audit_theory_course_pass', id, null, location);
    });

    $('.theory_course_audit_reject').click(function () {
        var id = this.id;
        id = id.substring(0, id.length - 7);
        var data = 'TheoryCourse,' + id;
        MyAjax_Get('getpage', 'workload_audit_reject_page', data, '.workload_audit_reject_content');
    });

    $('.search_button').click(function () {
        $('#theory_course_audit_search_form').ajaxSubmit({
            target: '.content_right',
            error: function () {
                alert('error');
            }
        })
    });
});