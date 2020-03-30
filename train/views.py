from django.shortcuts import render,get_object_or_404
from django.urls import reverse

from .models import human,student
from django.views import generic
from django.http import HttpResponseRedirect


class IndexView(generic.ListView):
    model = human
    context_object_name = 'all_human'
    template_name = 'train/index.html'


class DetailsView(generic.DetailView):
    model = human
    template_name = 'train/student_detail.html'


class ResultsView(generic.DetailView):
    model = human
    template_name = 'train/results.html'


def votes(request,zarfiat_id):
    humans = get_object_or_404(human, pk=zarfiat_id)

    try:
        selected = humans.student_set.get(pk=request.POST['students'])
    except(KeyError, student.DoesNotExist):
        return render(request,'train/student_detail.html',{
            'humans':humans , 'error_message':'nothing_selected'
        })
    else:
        selected.zarfiat -= 1
        selected.save()
        return HttpResponseRedirect(reverse('train:results',args=(humans.id,)))
