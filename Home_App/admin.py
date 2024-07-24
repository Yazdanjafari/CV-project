from django.contrib import admin
from .models import Personal, Statistics, ProgrammingSkils, Certificates, SocialMedia, SendEmail, MyImage, Project



# Fix Persinal DB in admin panel
class PersonalAdmin(admin.ModelAdmin):
    list_display = ('First_Name', 'Last_Name', 'Birthday', 'Age', 'Website', 'City', 'Email')
    search_fields = ('First_Name', 'Last_Name', 'City', 'Email')
    
    def has_add_permission(self, request):
        # Can't Add filed in Personal DB
        return False

    def has_delete_permission(self, request, obj=None):
        # Can't Delete in Personal DB
        return False



# Fix Statistics DB in admin panel
class StatisticsAdmin(admin.ModelAdmin):
    list_display = ('Happy_Clients', 'Projects', 'Job_history_in_years', 'Awards')
    
    def has_add_permission(self, request):
        # Can't Add filed in Statistics DB
        return False

    def has_delete_permission(self, request, obj=None):
        # Can't Delete in Statistics DB
        return False




admin.site.register(Personal, PersonalAdmin) 
admin.site.register(Statistics, StatisticsAdmin)
admin.site.register(ProgrammingSkils)
admin.site.register(Certificates)
admin.site.register(SocialMedia)
admin.site.register(SendEmail)
admin.site.register(MyImage)
admin.site.register(Project)