from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
from .models import Question
# from django.template import loader
from django.shortcuts import get_object_or_404 # from django.http import Http404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Choice
from django.db.models import F
from django.views import generic



def index(request):
#    return HttpResponse("Hello, world. e7aed7e0 is the polls index.")

    latest_question_list = Question.objects.order_by("-pub_date")[:5] #`objects` is the `model manager` for the `Question` model, which provides methods to interact with the database (return `queryset` (#TMI which is a lazy object)), such as all(), filter(), exclude(), order_by(), etc.
#    output = ", ".join([q.question_text for q in latest_question_list]) #remove this and use template instead
#    return HttpResponse(output)

    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, "polls/index.html", context)

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list" #variable name in template. Implicitly its `question_list`

    # this is subtitute for model = Question. This is us filtering. Implicitly `Question.objects.all()` is performed by `model = Question`.
    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]




def detail(request, question_id):
#    return HttpResponse("You're looking at question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"



def results(request, question_id):
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"




def vote(request, question_id):
    # return HttpResponse("You're voting on question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1 #avoid RACE CONDITION
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

from django.http import HttpRequest, HttpResponse
def owner(request: HttpRequest) -> HttpResponse:
    response = HttpResponse()
    response.write("Hello, world. 23e93b1f dfcb89d6 is the polls index.")
    return response