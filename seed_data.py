import os
# pyrefly: ignore [missing-import]
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject1.settings')
django.setup()

from paradox.models import *

def seed():
    # --- 1. GLOBAL ELEMENTS (Header, Footer, Branding) ---
    print("Seeding Global Elements...")
    home, _ = HOME.objects.get_or_create(id=1, defaults={
        'brand_name': 'Bella Notte',
        'brand_tagline': 'Fine Italian Dining',
        'brand_logo': 'BN',
        'loader_logo': 'BN'
    })
    
    footer_info, _ = FOOTERINFO.objects.get_or_create(id=1, defaults={
        'brand_name': 'Bella Notte',
        'brand_tagline': 'Fine Italian Dining',
        'brand_line': 'Authentic Italian flavours in the heart of the city.',
        'footer_bottom': '© 2024 Bella Notte. All Rights Reserved.'
    })

    FooterContact.objects.get_or_create(address='123 Roma Street, Italia', defaults={
        'phone': '+39 06 123456',
        'timing': 'Mon-Sun: 12:00 PM - 11:00 PM'
    })

    # Header Navigation
    header.objects.get_or_create(nav_item='Home', defaults={'url': '/', 'order': 1})
    header.objects.get_or_create(nav_item='Menu', defaults={'url': '/menu/', 'order': 2})
    header.objects.get_or_create(nav_item='About', defaults={'url': '/about/', 'order': 3})
    header.objects.get_or_create(nav_item='Reservation', defaults={'url': '/reservation/', 'order': 4})
    header.objects.get_or_create(nav_item='Contact', defaults={'url': '/contact/', 'order': 5})

    # Footer Quick Links
    FOOTER.objects.get_or_create(title='Our Story', defaults={'footer_heading': 'Quick Links', 'url': '/about'})
    FOOTER.objects.get_or_create(title='Menu', defaults={'footer_heading': 'Quick Links', 'url': '/menu'})

    # --- 2. INDEX PAGE ---
    print("Seeding Index Page...")
    IndexHero.objects.get_or_create(id=1, defaults={
        'eyebrow': 'Est. 1998 · Roma, Italia',
        'title': 'Welcome to',
        'title_italic': 'Bella Notte',
        'subtitle': 'Where every dish tells a story. Handcrafted Italian cuisine prepared with passion, served with elegance.',
        'btn1_text': 'View Our Menu',
        'btn1_url': '/menu',
        'btn2_text': 'Book a Table',
        'btn2_url': '/reservation'
    })

    IndexStat.objects.get_or_create(label='Years of Excellence', defaults={'target_number': 25, 'suffix': '+'})
    IndexStat.objects.get_or_create(label='Menu Items', defaults={'target_number': 120, 'suffix': '+'})
    IndexStat.objects.get_or_create(label='Happy Guests', defaults={'target_number': 48, 'suffix': 'k+'})
    IndexStat.objects.get_or_create(label='Awards Won', defaults={'target_number': 12, 'suffix': ''})

    FeaturedDish.objects.get_or_create(name='Black Truffle Risotto', defaults={
        'description': 'Creamy Arborio rice infused with black truffle and aged Parmigiano Reggiano.',
        'price': '₹1,850',
        'badge': "Chef's Pick",
        'order': 1
    })

    IndexAbout.objects.get_or_create(id=1, defaults={
        'badge_num': '25',
        'badge_text': 'Years of\nPassion',
        'label': 'Our Story',
        'title': 'A Legacy of',
        'title_highlight': 'Italian Craftsmanship',
        'description1': 'Born in the cobblestoned alleys of Rome, Bella Notte was founded in 1998 by Chef Marco Rossetti.',
        'description2': 'We do not serve food — we share stories, memories, and the warmth of an Italian kitchen.'
    })

    IndexTestimonial.objects.get_or_create(author_name='Priya Mehta', defaults={
        'text': 'Bella Notte is simply extraordinary. The truffle risotto was the finest I have had outside of Piedmont.',
        'author_title': 'Food Critic · Mumbai',
        'stars': 5
    })

    IndexCTA.objects.get_or_create(id=1, defaults={
        'title': 'Reserve Your Table Tonight',
        'subtitle': 'Join us for an unforgettable evening of authentic Italian cuisine.',
        'btn_text': 'Book a Table',
        'btn_url': '/reservation'
    })

    # --- 3. ABOUT PAGE ---
    print("Seeding About Page...")
    AboutPage.objects.get_or_create(id=1, defaults={
        'heritage_section_label': 'Our Heritage',
        'heritage_section_title': 'A Journey Through',
        'heritage_title_highlight': 'Italian Flavors',
        'heritage_description': 'Founded in 1998, Bella Notte has been a staple of fine dining, bringing authentic recipes from the heart of Rome.',
        'heritage_button_text': 'Book a Table',
        'heritage_button_url': '/reservation',
        'quote': 'Cooking is an act of love, a gift, a way to share with others.',
        'quote_author': 'Chef Marco Rossetti',
        'mv_section_label': 'Our Values',
        'mv_section_title': 'What Defines',
        'mv_title_highlight': 'Bella Notte',
        'chef_section_title': 'Meet Our',
        'chef_section_highlight': 'Master Chefs',
        'chef_section_description': 'Our culinary team is led by world-renowned chefs dedicated to the art of Italian cooking.'
    })

    MissionValue.objects.get_or_create(title='Authenticity', defaults={
        'icon': 'bi bi-award-fill',
        'description': 'We stay true to traditional Italian recipes passed down through generations.'
    })
    MissionValue.objects.get_or_create(title='Quality', defaults={
        'icon': 'bi bi-star-fill',
        'description': 'Only the finest, locally-sourced ingredients make it to our kitchen.'
    })

    Chef.objects.get_or_create(name='Marco Rossetti', defaults={
        'role': 'Executive Chef & Founder',
        'order': 1
    })

    # --- 4. MENU PAGE ---
    print("Seeding Menu Page...")
    MenuPage.objects.get_or_create(id=1, defaults={
        'banner_title': 'Our',
        'banner_highlight': 'Menu'
    })

    cat_app, _ = MenuCategory.objects.get_or_create(name='Appetizers', defaults={'order': 1})
    cat_main, _ = MenuCategory.objects.get_or_create(name='Main Course', defaults={'order': 2})
    cat_des, _ = MenuCategory.objects.get_or_create(name='Desserts', defaults={'order': 3})

    MenuItem.objects.get_or_create(name='Bruschetta Classica', defaults={
        'category': cat_app,
        'description': 'Toasted sourdough with vine-ripened tomatoes, garlic, and fresh basil.',
        'price': '₹450',
        'is_vegan': True
    })
    MenuItem.objects.get_or_create(name='Lasagna Alla Bolognese', defaults={
        'category': cat_main,
        'description': 'Traditional beef ragu, creamy bechamel, and fresh pasta layers.',
        'price': '₹1,250'
    })
    MenuItem.objects.get_or_create(name='Classic Tiramisù', defaults={
        'category': cat_des,
        'description': 'Espresso-soaked ladyfingers with whipped mascarpone.',
        'price': '₹650'
    })

    # --- 5. CONTACT PAGE ---
    print("Seeding Contact Page...")
    ContactPage.objects.get_or_create(id=1, defaults={
        'banner_title': 'Get In',
        'banner_highlight': 'Touch',
        'banner_page_name': 'Contact',
        'form_small_title': 'Message Us',
        'form_title': 'Have a',
        'form_highlight': 'Question?',
        'form_description': 'Send us a message and we will get back to you as soon as possible.',
        'button_text': 'Send Message',
        'location_small_title': 'Visit Us',
        'location_title': 'Find',
        'location_highlight': 'Our Location',
        'location_description': 'Located in the heart of the city, easily accessible from all major landmarks.',
        'map_url': 'https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3022.142293761308!2d-73.98731968459391!3d40.75889497932681!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89c25855c6480299%3A0x55194ec5a1ae072e!2sTimes%20Square!5e0!3m2!1sen!2sus!4v1634567890123!5m2!1sen!2sus',
        'direction_url': 'https://goo.gl/maps/example',
        'phone_number': '+91 98765 43210'
    })

    ContactInfo.objects.get_or_create(title='Email Us', defaults={
        'icon': 'bi-envelope-fill',
        'description': 'hello@bellanotte.com\nsupport@bellanotte.com'
    })

    # --- 6. RESERVATION PAGE ---
    print("Seeding Reservation Page...")
    Reservation.objects.get_or_create(id=1, defaults={
        'res_section_label': 'Reservations',
        'res_section_title': 'Book Your Table',
        'res_section_divider_left': 'Join us for an unforgettable dining experience. We recommend booking at least 24 hours in advance.',
        'font_family': 'Online Reservation',
        'text_muted': 'Please fill out the form below to request a table.',
        'resName': 'Your Name',
        'resEmail': 'Your Email',
        'resPhone': 'Phone Number',
        'resGuests': 'Number of Guests',
        'resDate': 'Select Date',
        'resTime': 'Select Time',
        'resRequest': 'Special Requests',
        'res_submit': 'Confirm Reservation',
        'res_success_message': 'Thank you! Your reservation request has been received.'
    })

    ResDetail.objects.get_or_create(form_info_label='Reservation Policy', defaults={
        'form_info_icon': 'bi bi-info-circle-fill',
        'form_info_value': 'Groups larger than 10 require private dining booking.'
    })

    # --- 7. SIGNUP PAGE ---
    print("Seeding Signup Page...")
    SignupPage.objects.get_or_create(id=1, defaults={
        'banner_title': 'Join the',
        'banner_highlight': 'Family',
    })

    print("\nSUCCESS: All pages seeded successfully!")

if __name__ == '__main__':
    seed()
