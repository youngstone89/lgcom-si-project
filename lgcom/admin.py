from django.contrib import admin
from .models import (MyUser,IPAddress,Project,Contract,ContractMember,Officeplus)
from .forms import (UserCreationForm,UserChangeForm)
# Register your models here.



from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

class UserAdmin(BaseUserAdmin):
	form = UserChangeForm
	add_form = UserCreationForm 
	list_display= ('email', 'username')
	list_filter = ('is_admin',)
	fieldsets = (
		('Account Information', {'fields': ('email','username', 'password')}),
		('Permissions', {'fields': ('is_admin',)}),
		)
	add_fieldsets = (
	(None, {
	'classes': ('wide',),
	'fields': ('email', 'username', 'password1', 'password2')}
	),
	)

	search_fields = ('email',)
	ordering = ('email',)
	filter_horizontal = ()

admin.site.register(MyUser, UserAdmin)
admin.site.unregister(Group)
admin.site.register(IPAddress)
admin.site.register(Project)
admin.site.register(Contract)
admin.site.register(ContractMember)
admin.site.register(Officeplus)