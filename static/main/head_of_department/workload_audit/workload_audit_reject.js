$(document).ready(function () {

    $('.workload_audit_reject_cross').click(function () {
        $('.workload_audit_reject').hide();
    });

    $('#workload_audit_reject_cancel').click(function () {
        $('.workload_audit_reject').hide();
    });

    $('#workload_audit_reject_submit').click(function () {
        $('#workload_audit_reject_form').ajaxSubmit({
            target: '.content_right',
            error:function () {
                alert('error!');
            }
        })
    });


});