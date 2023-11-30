
from django.contrib.auth.base_user import BaseUserManager
class UserManager(BaseUserManager):
    use_in_migrations=True

    def create_user(self, email,first_name,last_name,dob,gender,highestqualification,specialisation,address,password=None,**extra_fields):
        if not email:
            raise ValueError("You have not provided a valid e-mail address")
        email=self.normalize_email(email)
        user=self.model(email=email,first_name=first_name,last_name=last_name,dob=dob,gender=gender,highestqualification=highestqualification,specialisation=specialisation,address=address,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return None
    #def create_user(self,email,password=None,**extra_fields):
        #extra_fields.setdefault('is_staff', False)
        #extra_fields.setdefault('is_superuser', False)
        #return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email,first_name, last_name,dob,gender,highestqualification,specialisation,address, password=None,**extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active',True)
        return self.create_user(email,first_name,last_name,dob,gender,highestqualification,specialisation,address, password, **extra_fields)
    
