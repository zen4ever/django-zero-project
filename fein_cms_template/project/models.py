from django.utils.translation import ugettext_lazy as _

from feincms.module.page.models import Page
from feincms.content.richtext.models import RichTextContent
from feincms.content.contactform.models import ContactFormContent
from feincms.content.image.models import ImageContent

Page.register_extensions('datepublisher', 'translations') # Example set of extensions

Page.register_templates({
    'title': _('Standard template'),
    'path': 'page.html',
    'regions': (
        ('main', _('Main content area')),
        ('navbar', _('Navbar'), 'inherited'),
        ('sidebar', _('Sidebar'), 'inherited'),
        ),
    })

Page.create_content_type(RichTextContent, cleanse=True)
Page.create_content_type(ImageContent, POSITION_CHOICES=(
    ('block', _('block')),
    ('left', _('left')),
    ('right', _('right')),
    ))
Page.create_content_type(ContactFormContent, regions=('main',))
