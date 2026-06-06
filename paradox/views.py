# pyrefly: ignore [missing-import]
from django.shortcuts import render, redirect
# pyrefly: ignore [missing-import]
from django.contrib.auth import authenticate, login, logout
# pyrefly: ignore [missing-import]
from django.contrib.auth.models import User
# pyrefly: ignore [missing-import]
from django.contrib.auth.decorators import login_required
# pyrefly: ignore [missing-import]
from django.contrib import messages
from .models import *
import datetime

def index(request):
    hero = IndexHero.objects.first()
    stats = IndexStat.objects.all()
    dishes = FeaturedDish.objects.all()
    about = IndexAbout.objects.first()
    testimonials = IndexTestimonial.objects.all()
    cta = IndexCTA.objects.first()

    context = {
        'hero': hero,
        'stats': stats,
        'dishes': dishes,
        'about': about,
        'testimonials': testimonials,
        'cta': cta,
    }
    return render(request, 'index.html', context)

def contact(request):
    # SINGLE DATA
    contact_page = ContactPage.objects.first()
    # LOOP DATA
    contact_infos = ContactInfo.objects.all()
    
    context = {
        'contact_page': contact_page,
        'contact_infos': contact_infos,
    }
    return render(request, 'contact.html', context)

def reservation(request):
    ABC = ResDetail.objects.all()
    DFE = Reservation.objects.first()

    if request.method == 'POST':
        name = request.POST.get('resName')
        email = request.POST.get('resEmail')
        phone = request.POST.get('resPhone')
        guests = request.POST.get('resGuests')
        date_str = request.POST.get('resDate')
        time = request.POST.get('resTime')
        req = request.POST.get('resRequest')

        if date_str:
            date_obj = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        else:
            date_obj = datetime.date.today()

        booking = Booking(
            name=name,
            email=email,
            phone=phone,
            guests=guests,
            date=date_obj,
            time=time,
            request=req
        )
        if request.user.is_authenticated:
            booking.user = request.user
        booking.save()

        messages.success(request, 'Your reservation request has been submitted successfully!')
        return redirect('reservation')

    context = {
        'ABC': ABC,
        'DFE': DFE
    }
    return render(request, 'reservation.html', context)

def about(request):
    # SINGLE DATA
    about_page = AboutPage.objects.first()
    # LOOP DATA
    mission_values = MissionValue.objects.all()
    chefs = Chef.objects.all()

    context = {
        'about_page': about_page,
        'mission_values': mission_values,
        'chefs': chefs,
    }
    return render(request, 'about.html', context)


def menu(request):
    menu_page = MenuPage.objects.first()
    categories = MenuCategory.objects.all().prefetch_related('items')

    context = {
        'menu_page': menu_page,
        'categories': categories,
    }
    return render(request, 'menu.html', context)


def signup(request):
    if request.method == 'POST':
        name = request.POST.get('signupName')
        email = request.POST.get('signupEmail')
        password = request.POST.get('signupPassword')
        confirm = request.POST.get('signupConfirm')

        if password != confirm:
            messages.error(request, 'Passwords do not match.')
            return redirect('signup')
        
        if User.objects.filter(username=email).exists():
            messages.error(request, 'Email is already registered.')
            return redirect('signup')

        user = User.objects.create_user(username=email, email=email, password=password)
        user.first_name = name
        user.save()

        login(request, user)
        return redirect('dashboard')

    signup_page = SignupPage.objects.first()
    context = {
        'signup_page': signup_page,
    }
    return render(request, 'signup.html', context)

def login_view(request):
    if request.method == 'POST':
        email_or_username = request.POST.get('loginEmail')
        password = request.POST.get('loginPassword')

        user = authenticate(request, username=email_or_username, password=password)
        
        # If user is not found by username, try searching by email
        if user is None:
            try:
                user_obj = User.objects.get(email=email_or_username)
                user = authenticate(request, username=user_obj.username, password=password)
            except User.DoesNotExist:
                pass
            except User.MultipleObjectsReturned:
                # In case multiple users have the same email, pick the first one
                user_obj = User.objects.filter(email=email_or_username).first()
                if user_obj:
                    user = authenticate(request, username=user_obj.username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.first_name or user.username}!')
            if user.is_staff:
                if not user.is_superuser:
                    # pyrefly: ignore [missing-import]
                    from django.utils import timezone
                    today = timezone.localdate()
                    # Create a new attendance entry for this shift login
                    StaffAttendance.objects.create(
                        staff_member=user,
                        date=today,
                        status='Present',
                        login_time=timezone.now(),
                        is_logged_in=True
                    )
                    return redirect('staff_dashboard')
                else:
                    return redirect('admin_portal')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid email or password.')
            return redirect('login')

    return render(request, 'login.html')

# pyrefly: ignore [missing-import]
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def logout_view(request):
    if request.user.is_authenticated and request.user.is_staff and not request.user.is_superuser:
        # pyrefly: ignore [missing-import]
        from django.utils import timezone
        today = timezone.localdate()
        # Find the latest active shift record to check out
        attendance = StaffAttendance.objects.filter(staff_member=request.user, date=today, is_logged_in=True).last()
        if not attendance:
            attendance = StaffAttendance.objects.filter(staff_member=request.user, date=today).last()
        if attendance:
            attendance.is_logged_in = False
            attendance.logout_time = timezone.now()
            attendance.save()
    logout(request)
    return redirect('index')

@login_required
def customer_dashboard(request):
    if request.user.is_staff:
        return redirect('admin_portal')
    
    bookings = Booking.objects.filter(user=request.user).order_by('-date', '-time')
    total_count = bookings.count()
    approved_count = bookings.filter(status__in=['Approved', 'Accepted', 'Reserved']).count()
    pending_count = bookings.filter(status='Pending').count()
    
    context = {
        'bookings': bookings,
        'total_count': total_count,
        'approved_count': approved_count,
        'pending_count': pending_count,
    }
    return render(request, 'customer_dashboard.html', context)

@login_required
def admin_portal(request):
    if not request.user.is_superuser:
        return redirect('dashboard')
    
    if request.method == 'POST':
        action = request.POST.get('action')
        if action in ['approve', 'accept', 'reject']:
            booking_id = request.POST.get('booking_id')
            if booking_id:
                booking = Booking.objects.get(id=booking_id)
                if action in ['approve', 'accept']:
                    booking.status = 'Approved'
                    messages.success(request, f"Booking request for {booking.name} was successfully approved!")
                elif action == 'reject':
                    booking.status = 'Rejected'
                    messages.warning(request, f"Booking request for {booking.name} has been rejected.")
                booking.save()
        elif action == 'assign_table':
            booking_id = request.POST.get('booking_id')
            table_id = request.POST.get('table_id')
            if booking_id and table_id:
                booking = Booking.objects.get(id=booking_id)
                table = RestaurantTable.objects.get(id=table_id)
                
                # If there was a previously assigned table, free it up
                if booking.assigned_table:
                    old_table = booking.assigned_table
                    old_table.status = 'Available'
                    old_table.save()

                booking.assigned_table = table
                booking.status = 'Reserved'
                booking.save()

                table.status = 'Reserved'
                table.save()
                messages.success(request, f"Table {table.number} successfully assigned to booking.")
        elif action == 'update_table_status':
            table_id = request.POST.get('table_id')
            new_status = request.POST.get('status')
            if table_id and new_status:
                table = RestaurantTable.objects.get(id=table_id)
                table.status = new_status
                table.save()
                messages.success(request, f"Table {table.number} status updated to {new_status}.")
        elif action == 'delete':
            booking_id = request.POST.get('booking_id')
            if booking_id:
                try:
                    booking = Booking.objects.get(id=booking_id)
                    if booking.assigned_table:
                        table = booking.assigned_table
                        table.status = 'Available'
                        table.save()
                    booking_name = booking.name
                    booking.delete()
                    messages.success(request, f"Booking for {booking_name} has been successfully deleted!")
                except Booking.DoesNotExist:
                    messages.error(request, "Booking does not exist.")
        return redirect('admin_portal')

    bookings = Booking.objects.all().order_by('-created_at')
    attendances = StaffAttendance.objects.all().order_by('-date', '-login_time')
    leaves = LeaveRequest.objects.all().order_by('-applied_on')

    # Query tables and calculate metrics
    tables = RestaurantTable.objects.all().order_by('number')
    available_tables_list = RestaurantTable.objects.filter(status='Available').order_by('number')

    total_tables = tables.count()
    total_capacity = sum(t.capacity for t in tables)
    vip_tables_count = tables.filter(category='VIP').count()

    occupied_tables_count = tables.filter(status='Occupied').count()
    available_tables_count = tables.filter(status='Available').count()
    reserved_tables_count = tables.filter(status='Reserved').count()

    context = {
        'bookings': bookings,
        'attendances': attendances,
        'leaves': leaves,
        'tables': tables,
        'available_tables_list': available_tables_list,
        'total_tables': total_tables,
        'total_capacity': total_capacity,
        'vip_tables_count': vip_tables_count,
        'occupied_tables_count': occupied_tables_count,
        'available_tables_count': available_tables_count,
        'reserved_tables_count': reserved_tables_count,
    }
    return render(request, 'admin_portal.html', context)

@login_required
def admin_staff_management(request):
    if not request.user.is_superuser:
        return redirect('dashboard')

    if request.method == 'POST':
        action = request.POST.get('action')
        if action in ['accept_leave', 'reject_leave']:
            leave_id = request.POST.get('leave_id')
            if leave_id:
                leave = LeaveRequest.objects.get(id=leave_id)
                if action == 'accept_leave':
                    leave.status = 'Approved'
                    messages.success(request, f"Leave request for {leave.staff_member.username} was approved successfully!")
                elif action == 'reject_leave':
                    leave.status = 'Rejected'
                    messages.warning(request, f"Leave request for {leave.staff_member.username} was rejected.")
                leave.save()
        elif action == 'register_staff':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            role = request.POST.get('role')
            if username and email and password and role:
                if User.objects.filter(username=username).exists():
                    messages.error(request, f"User with username '{username}' already exists.")
                else:
                    new_user = User.objects.create_user(
                        username=username,
                        email=email,
                        password=password
                    )
                    new_user.is_staff = True
                    new_user.is_superuser = (role == 'admin')
                    new_user.save()
                    messages.success(request, f"New {role.capitalize()} '{username}' successfully registered!")
        return redirect('admin_staff_management')

    attendances = StaffAttendance.objects.all().order_by('-date', '-login_time')
    leaves = LeaveRequest.objects.all().order_by('-applied_on')
    staff_members = User.objects.filter(is_staff=True).order_by('-is_superuser', 'username')

    context = {
        'attendances': attendances,
        'leaves': leaves,
        'staff_members': staff_members,
    }
    return render(request, 'admin_staff_management.html', context)

@login_required
def staff_dashboard(request):
    if not request.user.is_staff or request.user.is_superuser:
        return redirect('dashboard')

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'leave_request':
            start_date_str = request.POST.get('start_date')
            end_date_str = request.POST.get('end_date')
            reason = request.POST.get('reason')
            if start_date_str and end_date_str and reason:
                start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d').date()
                end_date = datetime.datetime.strptime(end_date_str, '%Y-%m-%d').date()
                LeaveRequest.objects.create(
                    staff_member=request.user,
                    start_date=start_date,
                    end_date=end_date,
                    reason=reason
                )
                messages.success(request, 'Leave request submitted successfully.')
            return redirect('staff_dashboard')

    # pyrefly: ignore [missing-import]
    from django.utils import timezone
    today = timezone.localdate()

    attendances = StaffAttendance.objects.filter(staff_member=request.user).order_by('-date', '-login_time')
    leaves = LeaveRequest.objects.filter(staff_member=request.user).order_by('-applied_on')

    today_attendance = attendances.filter(date=today).first()

    # Calculate active working days (present) and total approved leave days
    working_days = attendances.filter(status='Present').count()
    
    approved_leaves = leaves.filter(status='Approved')
    leave_days = 0
    for leave in approved_leaves:
        leave_days += (leave.end_date - leave.start_date).days + 1

    context = {
        'attendances': attendances,
        'leaves': leaves,
        'working_days': working_days,
        'leave_days': leave_days,
        'today_attendance': today_attendance,
    }
    return render(request, 'staff_dashboard.html', context)
