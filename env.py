import os
# Check if DEVELOPMENT is in the environment variables
DEVELOPMENT = 'DEVELOPMENT' in os.environ

# Email configuration
if DEVELOPMENT:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DEFAULT_FROM_EMAIL = 'powerprotein@example.com'
else:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = 'shahbakhat008@gmail.com'  
    EMAIL_HOST_PASSWORD = 'fkgm hwpd bxvv maln' 
    DEFAULT_FROM_EMAIL = 'shahbakhat008@gmail.com'  
