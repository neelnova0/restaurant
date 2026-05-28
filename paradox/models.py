# pyrefly: ignore [missing-import]
from django.db import models
# pyrefly: ignore [missing-import]
from django.contrib.auth.models import User

# =========================
# CONTACT PAGE
# =========================

class ContactPage(models.Model):
    # BANNER SECTION
    banner_title = models.CharField(max_length=100)
    banner_highlight = models.CharField(max_length=100)
    banner_page_name = models.CharField(max_length=100)
    banner_image = models.ImageField(upload_to='contact/banner/')

    # FORM SECTION
    form_small_title = models.CharField(max_length=100)
    form_title = models.CharField(max_length=100)
    form_highlight = models.CharField(max_length=100)
    form_description = models.TextField()
    button_text = models.CharField(max_length=100)

    # LOCATION SECTION
    location_small_title = models.CharField(max_length=100)
    location_title = models.CharField(max_length=100)
    location_highlight = models.CharField(max_length=100)
    location_description = models.TextField()
    map_url = models.TextField()
    direction_url = models.URLField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return "Contact Page Content"

    class Meta:
        verbose_name = "Contact Page"


class ContactInfo(models.Model):
    icon = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


# =========================
# GLOBAL ELEMENTS (HEADER/FOOTER)
# =========================

class HOME(models.Model):
    loader_logo = models.CharField(max_length=200, blank=True, null=True)
    brand_logo = models.CharField(max_length=200, blank=True, null=True)
    brand_name = models.CharField(max_length=200, blank=True, null=True)
    brand_tagline = models.CharField(max_length=200, blank=True, null=True)
    remarks = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f"{self.brand_name} Settings"


class header(models.Model):
    nav_item = models.CharField(max_length=200, blank=True, null=True)
    url = models.CharField(max_length=200, default="#")
    order = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.nav_item

    class Meta:
        ordering = ['order']


class FOOTER(models.Model):
    footer_heading = models.CharField(max_length=200)
    footer_detail = models.CharField(max_length=500)
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200, default="#")

    def __str__(self):
        return self.footer_heading 


class FOOTERINFO(models.Model):
    brand_logo = models.CharField(max_length=200, blank=True, null=True)
    brand_name = models.CharField(max_length=200, blank=True, null=True)
    brand_tagline = models.CharField(max_length=200, blank=True, null=True)
    brand_line = models.CharField(max_length=200, blank=True, null=True)
    footer_bottom = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.brand_name 


class FooterContact(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    timing = models.CharField(max_length=100)

    def __str__(self):
        return self.address


# =========================
# RESERVATION PAGE
# =========================

class Reservation(models.Model):
    res_section_label = models.CharField(max_length=200, blank=True, null=True)
    res_section_title = models.CharField(max_length=200, blank=True, null=True)
    res_section_divider_left = models.CharField(max_length=200, blank=True, null=True)
    font_family = models.CharField(max_length=200, blank=True, null=True)
    text_muted = models.CharField(max_length=200, blank=True, null=True)
    resName = models.CharField(max_length=200, blank=True, null=True)
    resEmail = models.CharField(max_length=200, blank=True, null=True)
    resPhone = models.CharField(max_length=200, blank=True, null=True)
    resGuests = models.CharField(max_length=200, blank=True, null=True)
    resDate = models.CharField(max_length=200, blank=True, null=True)
    resTime = models.CharField(max_length=200, blank=True, null=True)
    resRequest = models.CharField(max_length=200, blank=True, null=True)
    res_submit = models.CharField(max_length=200, blank=True, null=True)
    res_success_message = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return "Reservation Page Content"


class ResDetail(models.Model):
    form_info_icon = models.CharField(max_length=200, blank=True, null=True)
    form_info_label = models.CharField(max_length=200, blank=True, null=True)
    form_info_value = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.form_info_label


# =========================
# ABOUT PAGE
# =========================

class AboutPage(models.Model):
    # --- HERITAGE SECTION ---
    heritage_section_label = models.CharField(max_length=200, blank=True, null=True)
    heritage_section_title = models.CharField(max_length=200, blank=True, null=True)
    heritage_title_highlight = models.CharField(max_length=200, blank=True, null=True)
    heritage_description = models.TextField(blank=True, null=True)
    heritage_image = models.ImageField(upload_to='about/heritage/', blank=True, null=True)
    heritage_button_text = models.CharField(max_length=100, blank=True, null=True)
    heritage_button_url = models.CharField(max_length=200, default='reservation.html', blank=True, null=True)
    quote = models.CharField(max_length=300, blank=True, null=True)
    quote_author = models.CharField(max_length=200, blank=True, null=True)

    # --- MISSION & VISION SECTION ---
    mv_section_label = models.CharField(max_length=200, blank=True, null=True)
    mv_section_title = models.CharField(max_length=200, blank=True, null=True)
    mv_title_highlight = models.CharField(max_length=200, blank=True, null=True)

    # --- CHEF SECTION ---
    chef_section_title = models.CharField(max_length=200, blank=True, null=True)
    chef_section_highlight = models.CharField(max_length=200, blank=True, null=True)
    chef_section_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return "About Page Content"

    class Meta:
        verbose_name = "About Page"
        verbose_name_plural = "About Page"


class MissionValue(models.Model):
    icon = models.CharField(max_length=100, help_text="Bootstrap icon class, e.g. bi bi-heart-fill")
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order']
        verbose_name = "Mission & Value"
        verbose_name_plural = "Missions & Values"


class Chef(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='about/chefs/', blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True, default="#")
    linkedin_url = models.URLField(blank=True, null=True, default="#")
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']
        verbose_name = "Chef"
        verbose_name_plural = "Chefs"


# =========================
# INDEX PAGE
# =========================

class IndexHero(models.Model):
    eyebrow = models.CharField(max_length=200, default="Est. 1998 · Roma, Italia")
    title = models.CharField(max_length=200)
    title_italic = models.CharField(max_length=200)
    subtitle = models.TextField()
    bg_image = models.ImageField(upload_to='index/hero/', blank=True, null=True)
    btn1_text = models.CharField(max_length=100, default="View Our Menu")
    btn1_url = models.CharField(max_length=200, default="menu.html")
    btn2_text = models.CharField(max_length=100, default="Book a Table")
    btn2_url = models.CharField(max_length=200, default="reservation.html")

    def __str__(self):
        return "Index Hero Section"

    class Meta:
        verbose_name = "Index Hero"
        verbose_name_plural = "Index Hero"


class IndexStat(models.Model):
    target_number = models.IntegerField(help_text="The number to animate to")
    suffix = models.CharField(max_length=10, blank=True, null=True, help_text="e.g. +, k+")
    label = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.label

    class Meta:
        ordering = ['order']
        verbose_name = "Index Stat"
        verbose_name_plural = "Index Stats"


class FeaturedDish(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.CharField(max_length=50)
    image = models.ImageField(upload_to='index/dishes/')
    badge = models.CharField(max_length=50, blank=True, null=True, help_text="e.g. Chef's Pick, Signature")
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']
        verbose_name = "Featured Dish"
        verbose_name_plural = "Featured Dishes"


class IndexAbout(models.Model):
    badge_num = models.CharField(max_length=10)
    badge_text = models.CharField(max_length=100, help_text="Text inside the year badge")
    main_image = models.ImageField(upload_to='index/about/')
    accent_image = models.ImageField(upload_to='index/about/')
    label = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    title_highlight = models.CharField(max_length=100)
    description1 = models.TextField()
    description2 = models.TextField()

    def __str__(self):
        return "Index About Section"

    class Meta:
        verbose_name = "Index About Section"


class IndexTestimonial(models.Model):
    text = models.TextField()
    author_name = models.CharField(max_length=100)
    author_title = models.CharField(max_length=100)
    author_image = models.ImageField(upload_to='index/testimonials/')
    stars = models.PositiveIntegerField(default=5, help_text="Number of stars (1-5)")
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Testimonial from {self.author_name}"

    class Meta:
        ordering = ['order']
        verbose_name = "Index Testimonial"
        verbose_name_plural = "Index Testimonials"


class IndexCTA(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField()
    btn_text = models.CharField(max_length=100, default="Book a Table")
    btn_url = models.CharField(max_length=200, default="reservation.html")

    def __str__(self):
        return "Index CTA Banner"

    class Meta:
        verbose_name = "Index CTA Banner"


# =========================
# MENU PAGE
# =========================

class MenuPage(models.Model):
    banner_title = models.CharField(max_length=200)
    banner_highlight = models.CharField(max_length=200)
    banner_image = models.ImageField(upload_to='menu/banner/')
    
    def __str__(self):
        return "Menu Page Settings"


class MenuCategory(models.Model):
    name = models.CharField(max_length=100, help_text="e.g. Appetizers, Main Course, Desserts")
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']
        verbose_name = "Menu Category"
        verbose_name_plural = "Menu Categories"


class MenuItem(models.Model):
    category = models.ForeignKey(MenuCategory, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.CharField(max_length=50)
    image = models.ImageField(upload_to='menu/items/', blank=True, null=True)
    is_vegan = models.BooleanField(default=False)
    is_spicy = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order']
        verbose_name = "Menu Item"
        verbose_name_plural = "Menu Items"


# =========================
# SIGNUP PAGE
# =========================

class SignupPage(models.Model):
    banner_title = models.CharField(max_length=200)
    banner_highlight = models.CharField(max_length=200)
    banner_image = models.ImageField(upload_to='signup/banner/', blank=True, null=True)

    def __str__(self):
        return "Signup Page Settings"


# =========================
# TRANSACTIONAL MODELS
# =========================

class RestaurantTable(models.Model):
    CATEGORY_CHOICES = (
        ('Regular', 'Regular'),
        ('VIP', 'VIP'),
        ('Family', 'Family'),
    )
    STATUS_CHOICES = (
        ('Available', 'Available'),
        ('Occupied', 'Occupied'),
        ('Reserved', 'Reserved'),
    )
    number = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Regular')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Available')

    def __str__(self):
        return f"Table {self.number} ({self.category} - {self.status})"


class Booking(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('Reserved', 'Reserved'),
    )

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='bookings')
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    guests = models.CharField(max_length=50)
    date = models.DateField()
    time = models.CharField(max_length=50)
    request = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    assigned_table = models.ForeignKey(RestaurantTable, on_delete=models.SET_NULL, null=True, blank=True, related_name='bookings')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.name} on {self.date} at {self.time}"


class StaffAttendance(models.Model):
    STATUS_CHOICES = (
        ('Present', 'Present'),
        ('Absent', 'Absent'),
    )

    staff_member = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_staff': True})
    date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Present')
    login_time = models.DateTimeField(null=True, blank=True)
    logout_time = models.DateTimeField(null=True, blank=True)
    is_logged_in = models.BooleanField(default=False)
    marked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.staff_member.username} - {self.date} - {self.status}"

class LeaveRequest(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    )
    staff_member = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_staff': True})
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.staff_member.username} - Leave ({self.start_date} to {self.end_date})"
