$(document).ready(function () {

    toCenter();

    $('.blur_area').css('filter', 'blur(10px)');
    document.documentElement.style.overflow = 'hidden';

    $('tr:even').addClass('even');

    var classes = $('.course_classes');
    classes.each(function () {
        var str = $(this).html();
        str = str.replace(/\n/g, '<br>');
        $(this).html(str);
    });

    $('.add_cross').click(function () {
        $('.blur_area').css('filter', 'none');
        document.documentElement.style.overflow = 'auto';
        $('.add_popup').hide();
    });

});