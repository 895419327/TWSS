$(document).ready(function () {

    // 倒计时
    var firstbar = $('#firstbar');
    var time = 10;

    // 倒计时函数
    function countdown() {
        // 如果时间到则重定向到'/index'页面
        if (time <= 0)
            location.href = '/index';

        // 倒计时
        setTimeout(function () {
            firstbar.text(--time + '秒后返回登录界面');
            // 自调用 开始下一秒的倒计时
            countdown();
        }, 1000)
    }

    // 开始倒计时
    countdown();


    // 进度条动画
    // 选择进度条div
    var overbar = $('#overbar');
    // 初始宽度为0
    var width = 0;

    // 宽度增长函数
    function growth() {
        if (width > 280) {
            // 当长度大于280px时 右上角要有圆角边缘
            var set_radius = '0 ' + (width - 280) + 'px 0 0';
            overbar.css('border-radius', set_radius);
        }
        setTimeout(function () {
            // 每32毫秒增长1px
            overbar.css('width', width++ + 'px');
            // 自调用形成动画
            growth();
        }, 32);
    }

    growth();

});

function connect_admin() {
    alert('email: 895419327@qq.com\ntel: 18030066873');
}