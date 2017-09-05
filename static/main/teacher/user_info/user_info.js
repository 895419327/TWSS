$(document).ready(function () {

    // 修改按钮下拉菜单动画
    var modify_button = $('#user_info_modify');
    var modify_button_menu = $('.user_info_modify_menu');
    modify_button.hover(
        // mouse over
        function () {
            modify_button_menu.slideDown('fast');
        },
        // mouse leave
        function () {
            modify_button_menu.slideUp('fast');
        }
    );

    // 导出按钮下拉菜单动画
    var export_button_menu = $('.user_info_export_menu');
    $('#user_info_export').hover(
        // mouse over
        function () {
            export_button_menu.slideDown('fast');
        },
        // mouse leave
        function () {
            export_button_menu.slideUp('fast');
        }
    );

    // 修改功能
    var modifying = false;
    var button_user_info_modify_able = true;

    modify_button.click(function () {
        // 判断修改状态
        // 未修改状态时为'修改'按钮
        if(!modifying){
            modifying = true;
            modify_button.text('保存');
            modify_button.css('color','red');
            $('.user_info_can_modify').each(function () {
                var data = $(this).text();
                var width = $(this).css('width');
                $(this).html("<input class='user_info_modify_area' value="+ data +">");
                $(this).css('width', width);
                $(this).children().css('width', width);
                // 这里要手动设置width避免td自动调整宽度
            });

            // 点击'修改'时模拟点击选择第一个可修改的文本框
            $('.modify_area:first').trigger('select');
            return;
        }

        // 修改状态时为'保存'按钮
        // 判断按钮是否可用
        if(button_user_info_modify_able === false) {
            alert('操作过于频繁，请稍后再试');
            return;
        }

        // 判断数据是否合法
        // 获取手机号
        var phone_number = $('#user_info_phone_number').children();
        if(phone_number.val().length !== 11){
            alert('手机号格式不符合');
            return;
        }

        if(modifying){
            modifying = false;
            modify_button.text('修改');
            modify_button.css('color','black');
            // 将数据储存为json字符串
            var datas_jsonstr = '{';
            $('.user_info_can_modify').each(function () {
                var title = $(this).prev('th').text();
                var data = $(this).children().val();
                datas_jsonstr += '"'+ title +'": "' + data + '",';
                $(this).html(data);
            });
            datas_jsonstr = datas_jsonstr.substring(0, datas_jsonstr.length-1);
            datas_jsonstr += '}';

            var form = $('#request_form');
            var requestfor = $('#requestfor');
            var requestdata = $('#request_data');
            // 配置目标url
            form.attr('action', '/upload');
            // 配置请求的excel为'user_info'
            requestfor.val('user_info');
            // 附上数据
            requestdata.val(datas_jsonstr);
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
                    alert('服务器连接失败');
                }
            });

            // 提交后重置目标url及请求
            form.attr('action', '');
            requestfor.val('');
            requestdata.val('');

            // 禁用该按钮 防止多次点击增加服务器负担
            button_user_info_modify_able = false;
            // 5秒后恢复按钮
            setTimeout(function () {
                button_user_info_modify_able = true;
            }, 5000);
        }
    });


    // 点击'导出为Excel'后向服务器发送请求及表单
    var button_user_info_to_excel = $('#user_info_to_excel');
    var button_user_info_to_excel_able = true;

    button_user_info_to_excel.click(function () {
        // 判断按钮是否可用
        if(button_user_info_to_excel_able === false) {
            alert('操作过于频繁，请稍后再试');
            return;
        }

        var form = $('#request_form');
        var requestfor = $('#requestfor');
        // 配置目标url
        form.attr('action', '/download');
        // 配置请求的excel为'user_info'
        requestfor.val('user_info');
        // 提交
        form.submit();

        // 提交后重置目标url及请求
        form.attr('action', '');
        requestfor.val('');

        // 禁用该按钮 防止多次点击增加服务器负担
        button_user_info_to_excel_able = false;
        // 5秒后恢复按钮
        setTimeout(function () {
            button_user_info_to_excel_able = true;
        }, 5000);
    });

});