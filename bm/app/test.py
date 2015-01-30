from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect

def test(request):
	if request.is_ajax():
		if len(request.GET) == 0:
			return HttpResponse('1')
		for i in request.GET: # Issue #13
			username = i
			break
		users = User.objects.all()
		for user in users:
			if user.username == username:
				# print('exists')
				return HttpResponse('0')
		else:
			# print('does not exist')
			return HttpResponse('1')