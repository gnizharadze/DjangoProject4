from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class UsernameOnlyBackend(BaseBackend):
    def authenticate(self, request, username=None, **kwargs):
        try:
            user = UserModel.objects.get(username=username)
            # For username-only authentication, no password check is performed.
            # Additional checks, like user activity status, can be included.
            if user.is_active: # [3]: ModelBackend checks is_active.
                return user
            else:
                return None
        except UserModel.DoesNotExist:
            try:
                user=UserModel.objects.create_user(username=username)

                user.is_active=True
                user.save()
                return user
            except Exception as e:
                print(f"Error creating user {username}: {e}")
                return None


    def get_user(self, user_id):
        # useris sesiidan dasabruneblad.user_id = primary key

        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None