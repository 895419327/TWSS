$(document).ready(function () {

    $('.add_cross').click(function () {
        $('.add_popup').hide();
    });

    $('.add_cancel').click(function () {
        $('.add_popup').hide();
    });

    $('.add_submit').click(function () {
        $('#location_year_post').val($('#location_year').val());
        $('#location_semester_post').val($('#location_semester').val());
        $('#location_audit_status_post').val($('#location_audit_status').val());

        $('#workload_audit_reject_form').ajaxSubmit({
            target: '.content_right',
            error: function () {
                alert('error!');
            }
        })
    });


});