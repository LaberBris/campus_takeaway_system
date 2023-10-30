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
        choices=[('1', '学生'), ('2', '老师'), ('3', '管理员')],
        widget=forms.Select(attrs={'class': 'form-control'}),
    )


class AddressForm(forms.Form):
    address = forms.CharField(label="地址", max_length=1024, widget=forms.TextInput(attrs={'class': 'form-control'}))


class ProfileForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=12, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(label="地址", max_length=1024, widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(label="手机号", max_length=12, widget=forms.TextInput(attrs={'class': 'form-control'}))
