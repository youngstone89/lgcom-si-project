from django.contrib import admin
from .models import MyUser
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
# admin.site.register(IPAddress)
# admin.site.register(Project)
# admin.site.register(Contract)
# admin.site.register(ContractMember)
# admin.site.register(Officeplus)

def update_master_table(modeladmin, request, queryset):
	import psycopg2
	import csv
	file = open("C:\\Users\\youngstone\\python-utils\\db\\import\\postgresql\\partner_resource_state\\project_contract_matster.csv")
	csv_data = csv.read(file)
	for row in csv_data:
		queryset.update(row)
    
update_master_table.short_description = "Update Master Table with the lastest file"


from .models import PartnerResourceState, Project, Contract, ContractMember

class PartnerResourceStateAdmin(admin.ModelAdmin):

	list_display= ('team', 'pjt_code','pjt_name', 'crt_code','crt_name', 'pm_name','sm_si', 'ptr_cpny','kor_name', 'crt_period','man_month', 'level','price')
	list_filter = ('pm_name','sm_si','pjt_name')
	actions = [update_master_table]

class ProjectAdmin(admin.ModelAdmin):

	list_display= ('pjt_code','pjt_name')


class ContractAdmin(admin.ModelAdmin):

	list_display= ('crt_code','crt_name','project')

class ContractMemberAdmin(admin.ModelAdmin):

	list_display= ('kor_name_crt_period_level','ptr_cpny','man_month','price','contract')




admin.site.register(PartnerResourceState,PartnerResourceStateAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Contract,ContractAdmin)
admin.site.register(ContractMember,ContractMemberAdmin)
