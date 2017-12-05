$(document).ready(function () {
    var notice_text = $('.notice_div');
    notice_text.each(function () {
        var str = $(this).html();
        str = str.replace(/&lt;br&gt;/g, '<br>');
        $(this).html(str);
    });
});