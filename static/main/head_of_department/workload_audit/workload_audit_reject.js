$(document).ready(function () {

    $('.add_cross').click(function () {
        $('.add_popup').hide();
    });

    $('.add_cancel').click(function () {
        $('.add_popup').hide();
    });

    $('.add_submit').click(function () {
        $('#workload_audit_reject_form').ajaxSubmit({
            target: '.content_right',
            error:function () {
                alert('error!');
            }
        })
    });


});