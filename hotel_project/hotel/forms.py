from django import forms


class DatePickerInput(forms.DateInput):
    input_type = 'date'

class TimePickerInput(forms.TimeInput):
    input_type = 'time'

class BookingForm(forms.Form):
    widget_time = TimePickerInput(attrs={
            'class': 'form-control datetimepicker-input',
            'style': 'max-width: 300px',
            'data-target': '#datetimepicker1'
        })
    
    widget_date = DatePickerInput(attrs={
            'class': 'form-control datetimepicker-input',
            'style': 'max-width: 300px',
            'data-target': '#datetimepicker1'
        })
    
    ROOM_TYPES = (
        ('SINGLE', 'SINGLE'),
        ('DOUBLE', 'DOUBLE'),
        ('KING', 'KING'),
        ('VIP', 'VIP'),
        ('PRESIDENTIAL', 'PRESIDENTIAL'),
    )
    room_type = forms.ChoiceField(choices=ROOM_TYPES, required=True)
    customer_id = forms.IntegerField(required=True)
    payment_id = forms.IntegerField(required=True)
    start_date = forms.DateField(widget=widget_date, required=True)
    start_time = forms.TimeField(widget=widget_time, required=True)
    end_date = forms.DateField(widget=widget_date, required=True)
    end_time = forms.TimeField(widget=widget_time, required=True)

