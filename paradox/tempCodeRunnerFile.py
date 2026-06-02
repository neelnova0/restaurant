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
