from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

# Create your views here.
# def index(request):
# 	return render(request, "solo/solo.html")


class SoloPostView(LoginRequiredMixin, TemplateView):
	def get(self, request):
		result = request.session.get("result", False)
# 		if result:
# 			del request.session["result"]
		ctx = {}
		return render(request, 'solo/solo.html', {"result": result})


	def post(self, request):
		# print("123")
		ctx = request.POST
		# print("ctx")
		# print(ctx['field1'])
		new_field1 = ctx['field1'].strip().title()
		new_field2 = ctx['field2'].strip().title()
		return render(request, 'solo/solo.html', {'field1': new_field1, 'field2': new_field2})