from django.contrib.auth.views import LoginView #mtavari point
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.urls import reverse_lazy
from.forms import UsernameLoginForm # chveni custom form

class CustomUsernameLoginView(LoginView):
    template_name = 'user/login.html' #login is template
    form_class = UsernameLoginForm
    success_url = reverse_lazy('movies:movie_list')

    def form_valid(self,form): #tu form is data validuria,sheasrulebs authenticacias

        username = form.cleaned_data['username']

        user = authenticate(self.request, username= username)

        if user is not None:

            login(self.request,user)
            return redirect(self.get_success_url()) #Tu users ver ipovis daaregistrirebs da gadagviyvans am urlze

        else:

            form.add_error('username','Invalid username')
            return self.form_invalid(form)