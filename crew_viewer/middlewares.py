from django.contrib import admin

class AdminMiddleWare(object):
	def process_request(self, request):
		url = request.get_full_path()
		# admin.site.register(Bio, BioAdmin)
		# setattr(AdminMiddleWare, 'url', self.url)
		# return url
	# def dean(self):
	# 	print 'dean'
		# print request.path_info
		# print request.scheme