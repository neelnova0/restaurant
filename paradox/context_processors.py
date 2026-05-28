from .models import header, HOME, FOOTER, FooterContact, FOOTERINFO

def global_context(request):
    return {
        'abc': header.objects.all(),
        'dfe': HOME.objects.first(),
        'ghi': FOOTER.objects.all(),
        'jkl': FooterContact.objects.all(),
        'mno': FOOTERINFO.objects.first(),
    }
