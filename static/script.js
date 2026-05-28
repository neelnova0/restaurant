/* ===================================================
   BELLA NOTTE RESTAURANT — script.js
   All UI Interactions & Form Validations
   =================================================== */

/* ─── Page Loader ─────────────────────────────────── */
document.addEventListener('DOMContentLoaded', function () {
  const loader = document.getElementById('pageLoader');
  if (loader) {
    setTimeout(() => {
      loader.classList.add('hidden');
      document.body.style.overflow = '';
    }, 1200);
  }
  document.body.style.overflow = 'hidden';

  /* ─── Init all modules ─────────────────────────── */
  initNavbar();
  initScrollAnimations();
  initBackToTop();
  initMenuFilter();
  initTestimonialsCarousel();
  initReservationForm();
  initContactForm();
  initLoginForm();
  initSignupForm();
  initCounters();
  initCartToast();
});

/* ─── Navbar: sticky + active link ───────────────── */
function initNavbar() {
  const navbar = document.getElementById('mainNavbar');
  if (!navbar) return;

  const onScroll = () => {
    if (window.scrollY > 60) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  };
  window.addEventListener('scroll', onScroll, { passive: true });

  // Mark active nav link
  const links = navbar.querySelectorAll('.nav-link');
  const current = location.pathname.split('/').pop() || 'index.html';
  links.forEach(link => {
    const href = link.getAttribute('href');
    if (href && href === current) {
      link.classList.add('active');
    } else if (current === '' && href === 'index.html') {
      link.classList.add('active');
    }
  });
}

/* ─── Scroll Reveal Animations ───────────────────── */
function initScrollAnimations() {
  const elements = document.querySelectorAll('.reveal');
  if (!elements.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

  elements.forEach(el => observer.observe(el));
}

/* ─── Back To Top ────────────────────────────────── */
function initBackToTop() {
  const btn = document.getElementById('backToTop');
  if (!btn) return;

  window.addEventListener('scroll', () => {
    if (window.scrollY > 500) {
      btn.classList.add('visible');
    } else {
      btn.classList.remove('visible');
    }
  }, { passive: true });

  btn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}

/* ─── Menu Category Filter ───────────────────────── */
function initMenuFilter() {
  const filterBtns = document.querySelectorAll('.filter-btn');
  const menuItems = document.querySelectorAll('.menu-item');
  if (!filterBtns.length || !menuItems.length) return;

  filterBtns.forEach(btn => {
    btn.addEventListener('click', function () {
      // Toggle active state
      filterBtns.forEach(b => b.classList.remove('active'));
      this.classList.add('active');

      const cat = this.dataset.cat;

      menuItems.forEach(item => {
        const itemCat = item.dataset.cat;
        if (cat === 'all' || itemCat === cat) {
          item.classList.remove('menu-item-hidden');
          // Re-animate
          item.style.animation = 'none';
          item.offsetHeight; // reflow
          item.style.animation = '';
          item.style.animationName = 'fadeInUp';
          item.style.animationDuration = '0.45s';
          item.style.animationFillMode = 'both';
        } else {
          item.classList.add('menu-item-hidden');
        }
      });
    });
  });
}

/* ─── Testimonials Carousel ──────────────────────── */
function initTestimonialsCarousel() {
  const slides = document.querySelectorAll('.testimonial-slide');
  if (!slides.length) return;

  let current = 0;

  const show = (idx) => {
    slides.forEach((s, i) => {
      s.style.display = i === idx ? 'block' : 'none';
    });
  };

  show(0);

  const prevBtn = document.getElementById('testimonialPrev');
  const nextBtn = document.getElementById('testimonialNext');

  if (nextBtn) {
    nextBtn.addEventListener('click', () => {
      current = (current + 1) % slides.length;
      show(current);
    });
  }

  if (prevBtn) {
    prevBtn.addEventListener('click', () => {
      current = (current - 1 + slides.length) % slides.length;
      show(current);
    });
  }

  // Auto-play
  setInterval(() => {
    if (document.hasFocus()) {
      current = (current + 1) % slides.length;
      show(current);
    }
  }, 6000);
}

/* ─── Animated Counters ──────────────────────────── */
function initCounters() {
  const counters = document.querySelectorAll('.stat-num[data-target]');
  if (!counters.length) return;

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const el = entry.target;
        const target = parseInt(el.dataset.target, 10);
        const suffix = el.dataset.suffix || '';
        let start = 0;
        const duration = 2000;
        const step = Math.ceil(target / (duration / 16));
        const timer = setInterval(() => {
          start += step;
          if (start >= target) {
            el.textContent = target + suffix;
            clearInterval(timer);
          } else {
            el.textContent = start + suffix;
          }
        }, 16);
        observer.unobserve(el);
      }
    });
  }, { threshold: 0.5 });

  counters.forEach(c => observer.observe(c));
}

/* ─── Cart Toast ─────────────────────────────────── */
function initCartToast() {
  const addBtns = document.querySelectorAll('.btn-add-cart, .btn-order');
  if (!addBtns.length) return;

  const toast = document.getElementById('cartToast');
  const bsToast = toast ? new bootstrap.Toast(toast, { delay: 2500 }) : null;

  addBtns.forEach(btn => {
    btn.addEventListener('click', function () {
      const name = this.closest('.dish-card, .menu-card')
        ?.querySelector('.dish-name, .menu-card-name')?.textContent;
      if (toast) {
        const toastMsg = document.getElementById('cartToastMsg');
        if (toastMsg && name) {
          toastMsg.textContent = `"${name}" added to your order!`;
        }
        bsToast.show();
      }
    });
  });
}

/* ─── Helpers ────────────────────────────────────── */
function isValidEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

function isValidPhone(phone) {
  return /^\+?[\d\s\-().]{7,15}$/.test(phone);
}

function showError(fieldId, msg) {
  const field = document.getElementById(fieldId);
  const err = document.getElementById(fieldId + 'Error');
  if (field) field.classList.add('is-invalid');
  if (err) { err.textContent = msg; err.classList.add('show'); }
}

function clearError(fieldId) {
  const field = document.getElementById(fieldId);
  const err = document.getElementById(fieldId + 'Error');
  if (field) field.classList.remove('is-invalid');
  if (err) err.classList.remove('show');
}

function clearAllErrors(ids) {
  ids.forEach(id => clearError(id));
}

/* ─── Reservation Form ───────────────────────────── */
function initReservationForm() {
  const form = document.getElementById('reservationForm');
  if (!form) return;

  // Set minimum date to today
  const dateInput = document.getElementById('resDate');
  if (dateInput) {
    const today = new Date().toISOString().split('T')[0];
    dateInput.setAttribute('min', today);
  }

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    const fields = ['resName', 'resEmail', 'resPhone', 'resDate', 'resTime', 'resGuests'];
    clearAllErrors(fields);
    let valid = true;

    const name = document.getElementById('resName')?.value.trim();
    const email = document.getElementById('resEmail')?.value.trim();
    const phone = document.getElementById('resPhone')?.value.trim();
    const date = document.getElementById('resDate')?.value;
    const time = document.getElementById('resTime')?.value;
    const guests = document.getElementById('resGuests')?.value;

    if (!name || name.length < 2) { showError('resName', 'Please enter your full name.'); valid = false; }
    if (!email || !isValidEmail(email)) { showError('resEmail', 'Please enter a valid email address.'); valid = false; }
    if (!phone || !isValidPhone(phone)) { showError('resPhone', 'Please enter a valid phone number.'); valid = false; }
    if (!date) { showError('resDate', 'Please select a date.'); valid = false; }
    if (!time) { showError('resTime', 'Please select a time.'); valid = false; }
    if (!guests) { showError('resGuests', 'Please select number of guests.'); valid = false; }

    if (valid) {
      form.submit();
    }
  });
}

/* ─── Contact Form ───────────────────────────────── */
function initContactForm() {
  const form = document.getElementById('contactForm');
  if (!form) return;

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    const fields = ['contactName', 'contactEmail', 'contactSubject', 'contactMessage'];
    clearAllErrors(fields);
    let valid = true;

    const name = document.getElementById('contactName')?.value.trim();
    const email = document.getElementById('contactEmail')?.value.trim();
    const subject = document.getElementById('contactSubject')?.value.trim();
    const message = document.getElementById('contactMessage')?.value.trim();

    if (!name || name.length < 2) { showError('contactName', 'Please enter your name.'); valid = false; }
    if (!email || !isValidEmail(email)) { showError('contactEmail', 'Please enter a valid email.'); valid = false; }
    if (!subject || subject.length < 3) { showError('contactSubject', 'Please enter a subject.'); valid = false; }
    if (!message || message.length < 10) { showError('contactMessage', 'Message must be at least 10 characters.'); valid = false; }

    if (valid) {
      form.submit();
    }
  });
}

/* ─── Login Form ─────────────────────────────────── */
function initLoginForm() {
  const form = document.getElementById('loginForm');
  if (!form) return;

  // Password toggle
  const toggleBtn = document.getElementById('togglePassword');
  const passwordInput = document.getElementById('loginPassword');
  if (toggleBtn && passwordInput) {
    toggleBtn.addEventListener('click', () => {
      const type = passwordInput.type === 'password' ? 'text' : 'password';
      passwordInput.type = type;
      toggleBtn.innerHTML = type === 'password'
        ? '<i class="bi bi-eye"></i>'
        : '<i class="bi bi-eye-slash"></i>';
    });
  }

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    const fields = ['loginEmail', 'loginPassword'];
    clearAllErrors(fields);
    let valid = true;

    const email = document.getElementById('loginEmail')?.value.trim();
    const password = document.getElementById('loginPassword')?.value;

    if (!email) { showError('loginEmail', 'Please enter your email or username.'); valid = false; }
    if (!password || password.length < 6) { showError('loginPassword', 'Password must be at least 6 characters.'); valid = false; }

    if (valid) {
      form.submit();
    }
  });
}

/* ─── Signup Form ────────────────────────────────── */
function initSignupForm() {
  const form = document.getElementById('signupForm');
  if (!form) return;

  // Password toggle
  ['toggleSignupPassword', 'toggleConfirmPassword'].forEach(id => {
    const btn = document.getElementById(id);
    const inputId = id === 'toggleSignupPassword' ? 'signupPassword' : 'signupConfirm';
    const input = document.getElementById(inputId);
    if (btn && input) {
      btn.addEventListener('click', () => {
        const type = input.type === 'password' ? 'text' : 'password';
        input.type = type;
        btn.innerHTML = type === 'password'
          ? '<i class="bi bi-eye"></i>'
          : '<i class="bi bi-eye-slash"></i>';
      });
    }
  });

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    const fields = ['signupName', 'signupEmail', 'signupPhone', 'signupPassword', 'signupConfirm'];
    clearAllErrors(fields);
    let valid = true;

    const name = document.getElementById('signupName')?.value.trim();
    const email = document.getElementById('signupEmail')?.value.trim();
    const phone = document.getElementById('signupPhone')?.value.trim();
    const password = document.getElementById('signupPassword')?.value;
    const confirm = document.getElementById('signupConfirm')?.value;

    if (!name || name.length < 2) { showError('signupName', 'Please enter your full name.'); valid = false; }
    if (!email || !isValidEmail(email)) { showError('signupEmail', 'Please enter a valid email.'); valid = false; }
    if (!phone || !isValidPhone(phone)) { showError('signupPhone', 'Please enter a valid phone number.'); valid = false; }
    if (!password || password.length < 8) { showError('signupPassword', 'Password must be at least 8 characters.'); valid = false; }
    if (!confirm) { showError('signupConfirm', 'Please confirm your password.'); valid = false; }
    else if (password && password !== confirm) { showError('signupConfirm', 'Passwords do not match.'); valid = false; }

    if (valid) {
      form.submit();
    }
  });
}
