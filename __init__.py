from django.core.mail import EmailMultiAlternatives, EmailMessage, get_connection
from django.template.loader import get_template
from django.template import Context, TemplateDoesNotExist
from django.contrib.sites.models import Site


def send_templated_email(subject, from_email, to, template_name,
                        context={}, fail_silently=False,
                        connection=None, template_prefix='email_templates/'):

    connection = connection or get_connection(fail_silently=fail_silently)

    try:
        plaintext = get_template('%s%s.txt' % (template_prefix, template_name))
    except TemplateDoesNotExist:
        plaintext = None

    try:
        html = get_template('%s%s.html' % (template_prefix, template_name))
    except  TemplateDoesNotExist:
        html = None

    if context.get('site', None) is None and Site._meta.installed:
        context['site'] = Site.objects.get_current()

    d = Context(context)

    text_content = plaintext.render(d) if plaintext else None
    html_content = html.render(d) if html else None

    result = 0

    if plaintext and html:
        print "plaintext and html"
        msg = EmailMultiAlternatives(subject, text_content, from_email,
                                     to, connection=connection)
        msg.attach_alternative(html_content, "text/html")
        result = msg.send(fail_silently=fail_silently)

    if plaintext and not html:
        print "plaintext and not html"
        msg = EmailMessage(subject, text_content, from_email, to,
                           connection=connection)
        result = msg.send(fail_silently=fail_silently)

    if html and not plaintext:
        print "html and not plaintext"
        msg=EmailMessage(subject, html_content, from_email, to,
                         connection=connection)
        msg.content_subtype = 'html'
        result = msg.send(fail_silently)

    return result
