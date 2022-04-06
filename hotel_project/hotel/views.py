from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, FormView
from .models import User, Receptionist, Room, RoomStatus, RoomType, Booking, Payment, PaymentType, Reservation
from .forms import BookingForm
from datetime import datetime

class Validate:
    def check_availability(room, start_time, end_time):
        check = []
        booking_list = Reservation.objects.filter(room_id=room)
        for booking in booking_list:
            if booking.start_time > end_time or booking.end_time < start_time:
                check.append(True)
            else:
                check.append(False)    
        return all(check)        
            
class RoomList(ListView):
    model = Room       
    
class BookingList(ListView):
    model = Booking    

class CustomerList(ListView):
    model = User   
    
class BookingView(FormView):
    form_class = BookingForm
    template_name = 'hotel/booking.html'
    
    def form_valid(self, form):
        data = form.cleaned_data
        room_type_id = RoomType.objects.filter(room_type=data['room_type'])
        room_list = Room.objects.filter(room_type_id=data['room_type_id'])
        if available_rooms := [room for room in room_list if Validate.check_availability(room, data['start_time'], data['end_time'])]:
            return self.form_valid_2(available_rooms, data)
        else:
            return HttpResponse("All the rooms are booked for the room type!")

    def form_valid_2(self, available_rooms, data):
        room = available_rooms[0]
        customer_id = User.objects.filter(id=data['customer_id']).first()
        staff_id = self.request.user
        payment_id = Payment.objects.filter(id=data['payment_id'])
        start_date_data=datetime.combine(data['start_date'], data['start_time'])
        end_date_data=datetime.combine(data['end_date'], data['end_time'])

        booking = Booking.objects.create(
            room_id = room,
            customer_id = customer_id,
            staff_id = staff_id,
            payment_id = payment_id,
            # instance = form.save(commit=False)
            )
        booking.save()
        return HttpResponse(booking)


def homepage(request):
    return render(request, 'hotel/home.html', {})

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

def admin_list(request):
    return render(request, 'hotel/admin_list.html', {})

def admin_create(request):
    return render(request, 'hotel/admin_create.html', {})

def show_admin():
    pass

def edit_admin():
    pass

def delete_admin():
    pass

def logs():
    pass




