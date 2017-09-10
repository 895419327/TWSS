$(document).ready(function () {

    var modify_button = $('#user_info_modify');

    // 修改功能
    var modifying = false;

    modify_button.click(function () {
        // 判断修改状态
        // 未修改状态时为'修改'按钮
        if (!modifying) {
            modifying = true;
            modify_button.text('保存');
            modify_button.css('color', 'red');
            $('.user_info_can_modify').each(function () {
                var data = $(this).text();
                var name = $(this).attr('name');
                var width = $(this).css('width');
                $(this).html("<input class='user_info_modify_area' "+ "value=" + data +" name=" + name + ">");

                $(this).css('width', width);
                $(this).children().css('width', width);
                // 这里要手动设置width避免td自动调整宽度
            });

            // 点击'修改'时模拟点击选择第一个可修改的文本框
            $('.user_info_modify_area:first').trigger('select');
            return;
        }

        // 修改状态时为'保存'按钮

        if (modifying) {
            modifying = false;
            modify_button.text('修改');
            modify_button.css('color', 'black');
            // 将数据储存为json字符串

            var form = $('#user_info_form');
            form.ajaxSubmit({
                target: '.content_right',
                success: function () {
                    alert('修改成功！');
                },
                error: function () {
                    alert('error!')
                }
            });
        }
    });
});