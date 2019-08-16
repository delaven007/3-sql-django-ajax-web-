
#user/form.py
from django import forms

class Reg2(forms.Form):
    username=forms.CharField(max_length=30,label='请输入用户名')
    password=forms.CharField(max_length=50,label="请输入密码")
    password2=forms.CharField(max_length=50,label="请再次输入密码")
    # rep=forms.BooleanField(label="记住密码")
    def clean_username(self):
        name=self.cleaned_data['username']
        if "*" in name:
            raise forms.ValidationError("0")      #()必须有，而且有字符
        return name
    def clean(self):
        pwd1=self.cleaned_data['password1']
        pwd2=self.cleaned_data['password2']
        if pwd1!=pwd2:
            raise forms.ValidationError("密码不一致，请重新输入")
        else:
            return self.cleaned_data   #注：此处必须返回clean_data






















