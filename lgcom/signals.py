from django.db.models.signals import post_save 
from django.dispatch import receiver 
from .models import PartnerResourceState as prs, Project, Contract

@receiver(post_save,sender=prs)
def regularize_db(sender,**kwargs):
	#lgcom_project의 objects delete 후 pjt_code, pjt_name 넣은뒤 save()
	Project.objects.all().delete()
	master_queryset = prs.objects.all().order_by('pjt_code')

	for m in master_queryset.distinct('pjt_code'):
		pjt_obj = Project.objects.create(pjt_code=m.pjt_code,pjt_name=m.pjt_name)
		pjt_obj.save()


	#lgcom_contract의 objects delete 후 pjt object 별 contract_set에 crt_code, crt_name 넣은뒤 save()
	Contract.objects.all().delete()
	
	for p in Project.objects.all():
		for m in master_queryset.distinct('crt_code'):
			c = p.contract_set.create(crt_code=m.crt_code, crt_name=m.crt_name)
			c.save()


	#lgcom_contractmember의 objects delete 후 crt object 별 contractmember_set에 정보넣은뒤 save()
	ContractMember.objects.all().delete()
	for m in master_queryset:
		c = Contract.objects.get(crt_code=m.crt_code)
		c.contractmember_set.create(kor_name_crt_period_level=m.kor_name+";"+m.crt_period+";"+m.level,ptr_cpny=m.ptr_cpny,man_month =m.man_month,price=m.price)
		c.save()

	