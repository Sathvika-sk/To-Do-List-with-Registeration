from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from .models import newuser
class EmailBackend(ModelBackend):
    def authenticate(self, email=None, password=None, **kwargs):
        self.UserModel = newuser
        u=get_user_model()
        e=newuser.objects.get(email=email)
        print(e)
        if not email:
            return None
        if e.password==password:
            return(newuser.objects.get(email=email))
        else:
            raise 
        '''try:
            user = self.UserModel.objects.get(email=email)
            print(user)
        except self.UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return "incorrect password"'''
    def get_user(self,id):
        UserModel=get_user_model()

        try:
            return UserModel.objects.get(pk=id)
        except UserModel.DoesNotExist:
            return None
    



