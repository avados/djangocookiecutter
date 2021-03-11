from rest_framework import permissions



class CustomUser(permissions.IsAdminUser):
    pass

