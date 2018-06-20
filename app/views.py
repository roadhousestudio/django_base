from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from django.views.generic import View


class HomeView(TemplateView):
    template_name = 'home.html'


class WordsSimilarityView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(WordsSimilarityView, self).dispatch(
            request,
            *args,
            **kwargs
        )

    def post(self, *args, **kwargs):
        word_1 = self.request.POST.get("word_1", "")
        word_2 = self.request.POST.get("word_2", "")

        print(word_1)
        print(word_2)

        return JsonResponse(
            {'foo': 'bar'}
        )
