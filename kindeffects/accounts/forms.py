from django import forms
# from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('name_kr', 'phone', 'store_regist', )


class CustomUserCreationForm(UserCreationForm):
    phone = forms.CharField(
        label='핸드폰 번호',
        widget=forms.TextInput(
            attrs={
                'type':'tel',
            }
        )
    )
    username = forms.CharField(
        label='아이디',
        help_text='문자, 숫자 그리고 @/./+/-/_만 가능합니다.'
    )
    name_kr = forms.CharField(
        label='사업자 이름'
    )
    store_regist = forms.CharField(
        label='사업자 등록번호'
    )

    class Meta():
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'name_kr', 'phone', 'store_regist', 'store')
        # fields = '__all__'