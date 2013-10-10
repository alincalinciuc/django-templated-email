django-templated-email
======================

Send emails in django with html/txt templates


## Installation
Run the following command inside your django's project directory

```git
    git submodule add https://github.com/simion/django-templated-email.git templated_email
```

In setting.py file add "templated_email" to INSTALLED_APPS

```python
    INSTALLED_APPS = (
        ...
        'templated_email',
        ...
    )
```

Use the function. Example:

```python
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
```

Don't forget to create the template files. 

In your templates folder, create a folder named 'email_templates'. 

Place example-template.html or example-template.txt inside of it. 

Example:

```bash
    <project-path>/<app-path>/templates/email_templates/exmaple-template.html
```
