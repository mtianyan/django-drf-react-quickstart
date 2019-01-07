import xadmin
from xadmin import views
from .models import Lead
class BaseSetting(object):
	"""xadmin的基础信息配置"""
	enable_themes = True  # 开启主题功能
	use_bootswatch = True 

class GlobalSettings(object):
	"""xadmin通用信息配置"""
	site_title = "Leads Xadmin"
	site_footer = "mtianyan@qq.com"

# 注册设置信息到View
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)

class LeadAdmin(object):
	"""
	list_display: 后台展示哪些字段
	search_fields: 后台可搜索哪些字段
	list_filter: 后台过滤器可使用哪些字段
	"""
	list_display = ['name', 'email','message']
	search_fields = ['name', 'email','message']
	list_filter = ['name', 'email','message','created_at']

xadmin.site.register(Lead, LeadAdmin)