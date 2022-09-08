from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm  # 회원가입할때
from django.contrib.auth.forms import UserChangeForm    # 회원수정할때


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()




class CustomUserChangeForm(UserChangeForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        # fields = '__all__'
        fields = ('email', 'first_name', 'last_name',)