from django.shortcuts import render

def homepage(request):
    return render(request, 'hotel/home.html', {})

def room_lists():
    pass

def single_room():
    pass

def room_booking():
    pass

def room_payment():
    pass

def room_checkin():
    pass

def room_checkout():
    pass

def admin_login(request):
    return render(request, 'hotel/login.html', {})

def dashboard(request):
    return render(request, 'hotel/dashboard.html', {})

def admin_list():
    pass

def admin_create():
    pass

def show_admin():
    pass

def edit_admin():
    pass

def delete_admin():
    pass

def logs():
    pass
