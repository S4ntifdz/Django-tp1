from django.shortcuts import render, redirect
from .forms import SignUpForm

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige al formulario de inicio de sesión
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
