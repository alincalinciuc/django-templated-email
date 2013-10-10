django-templated-email
======================

Send emails in django with html/txt templates


## Installation
1. Run the following command inside your django's project directory
```
    git clone https://github.com/simion/django-templated-email.git templated_email
```
2. In setting.py file add "templated_email" to INSTALLED_APPS
3. Use the function. Example:

    from templated_email import send_templated_email
    
    ...
    
    send_templated_email(
        "Example subject"
        None,
        ['test@email.com']  #must be a list or tuple
        'example-template',
        context,  # context variables to send in template
        # cc = []
        # bcc = []
    )
    
4. Create the template files. In your template folder, create a folder named 'email_templates'. Place example-template.html or example-template.txt inside of it. 
