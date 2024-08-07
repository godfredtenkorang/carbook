from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking, FeaturedBooking
from rental.models import CarForRent, FeaturedCarForRent
from django.contrib import messages


def book_vehicle(request, vehicle_slug):
    vehicle = get_object_or_404(CarForRent, slug=vehicle_slug)
    if request.method == 'POST':
        email = request.POST['email']
        phone = request.POST['phone']
        pick_up_location = request.POST['pick_up_location']
        drop_off_location = request.POST['drop_off_location']
        car_type = request.POST['car_type']
        location = request.POST['location']
        pick_up_date = request.POST['pick_up_date']
        drop_off_date = request.POST['drop_off_date']
        pick_up_time = request.POST['pick_up_time']
        booking = Booking(vehicle=vehicle, email=email, phone=phone, pick_up_location=pick_up_location, drop_off_location=drop_off_location, car_type=car_type, location=location, pick_up_date=pick_up_date, drop_off_date=drop_off_date, pick_up_time=pick_up_time)
        booking.save()
        messages.success(request, 'Your form as been sent successfully!')
        return render(request, 'booking/vehicle_book.html', {'title': 'Book'})
    return render(request, 'booking/vehicle_book.html', {'title': 'Book'})

def books_vehicle(request, featured_slug):
    vehicle = get_object_or_404(FeaturedCarForRent, slug=featured_slug)
    if request.method == 'POST':
        email = request.POST['email']
        phone = request.POST['phone']
        pick_up_location = request.POST['pick_up_location']
        drop_off_location = request.POST['drop_off_location']
        car_type = request.POST['car_type']
        location = request.POST['location']
        pick_up_date = request.POST['pick_up_date']
        drop_off_date = request.POST['drop_off_date']
        pick_up_time = request.POST['pick_up_time']
        booking = FeaturedBooking(vehicle=vehicle, email=email, phone=phone, pick_up_location=pick_up_location, drop_off_location=drop_off_location, car_type=car_type, location=location, pick_up_date=pick_up_date, drop_off_date=drop_off_date, pick_up_time=pick_up_time)
        booking.save()
        messages.success(request, 'Your form as been sent successfully!')
        return render(request, 'booking/vehicle_books.html', {'title': 'Book'})
    return render(request, 'booking/vehicle_books.html', {'title': 'Book'})
