from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=12, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码", max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class SignupForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=12, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码", max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=20, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label="手机号", max_length=12, widget=forms.TextInput(attrs={'class': 'form-control'}))
    userType = forms.ChoiceField(
        label="用户类型",
        choices=[('1', '管理员'), ('2', '顾客'), ('3', '商户')],
        widget=forms.Select(attrs={'class': 'form-control'}),
    )