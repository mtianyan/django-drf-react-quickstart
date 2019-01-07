from leads.models import Lead
from leads.serializers import LeadSerializer
from rest_framework import generics
# Create your views here.
class LeadListCreate(generics.ListCreateAPIView):
	"""
    get:
    返回所有已存在的lead对象的列表

    post:
    创建一个新的lead实例
	"""
	queryset = Lead.objects.all()
	serializer_class = LeadSerializer