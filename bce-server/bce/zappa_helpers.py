from django.contrib.auth.models import User


def create_superuser():
    User.objects.create_superuser('admin', 'admain@phoexer.com', 'ncdBXf5KBFTKyeFqLp8E')