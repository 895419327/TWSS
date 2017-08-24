$(document).ready(function () {

    // 退出按钮动画
    // $('#logout').click(function () {
    //     var body = $('body');
    //     body.css('filter','blur(5px)');
    //     setTimeout(function () {
    //         var confirm_logout = confirm('确定退出吗?');
    //         if(confirm_logout == true){
    //             window.close();
    //         }
    //         else {
    //             body.css('filter','none');
    //         }
    //     },100);
    //
    // });

    // 禁用左侧菜单的双击选择文字，影响使用体验
    $('.left_unit').addClass('no_select');
    // 禁用全局按钮的双击选择文字
    $('.content_button').addClass('no_select');


    //左侧菜单动画
    $('.unit_title').click(function () {
        // 点击标题后 隐藏其他模块的子菜单 显示本模块的子菜单
        // $('.unit_options').slideUp('fast');
        // if($(this).next().css('display') === 'none'){
        //     $(this).next().slideDown('fast');
        // }

        // 点击标题后 显示本模块子菜单但不隐藏其他模块的
        $(this).next().slideToggle('fast');
    });

});

function MyAjax(action, forwhat, data_json) {
        var form = $('#request_form');
        var requestfor = $('#requestfor');
        var requestdata = $('#request_data');

        // 配置目标url
        form.attr('action', action);
        // 配置请求
        requestfor.val(forwhat);
        // 附上数据
        requestdata.val(data_json);

        // 提交
        form.ajaxSubmit({
            target: '#message',
            success: function () {
                var message = $('#message');
                message.slideDown('fast');
                setTimeout(function () {
                    message.slideUp('fast').text('');
                }, 5000);
            },
            error: function () {
                alert('未知错误');
            }
        });

        // 提交后重置目标url及请求
        form.attr('action', '');
        requestfor.val('');
        requestdata.val('');
    }