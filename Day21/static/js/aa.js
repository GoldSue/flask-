document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');
    const mobileInput = form.querySelector('input[name="mobile"]');
    const pwdInput = form.querySelector('input[name="pwd"]');
    const errorSpan = form.querySelector('span.error');

    form.addEventListener('submit', e => {
        errorSpan.textContent = ''; // 清空错误信息

        // 简单手机号校验（中国手机号示例）
        const mobilePattern = /^1[3-9]\d{9}$/;
        if (!mobilePattern.test(mobileInput.value.trim())) {
            e.preventDefault();
            errorSpan.textContent = '请输入有效的手机号';
            mobileInput.focus();
            return;
        }

        // 密码不能为空
        if (pwdInput.value.trim() === '') {
            e.preventDefault();
            errorSpan.textContent = '请输入密码';
            pwdInput.focus();
            return;
        }
    });
});
