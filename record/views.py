from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import FormView
from .models import Recording,Specialist
from .forms import RecordingForm



class SpecialistList(ListView):
    model = Specialist
    template_name='specialist.html'
    context_object_name = 'specialists'


class RecordingView(FormView):
    form_class = RecordingForm
    template_name = 'recording.html'

    def form_valid(self, form):
        fcd = form.cleaned_data
        curr_specialist=Specialist.objects.get(id= self.kwargs['specialist_id'])
        response_dict={"form":form,
                       "doctor":curr_specialist,
                       "curr_date":fcd['date'],
                       "curr_time":fcd['time']}

        if Recording.objects.filter(date=fcd['date'],time=fcd['time'],specialist=curr_specialist).count()==0:
            Recording.objects.create(date=fcd['date'],time=fcd['time'],
                                     name=fcd['name'],
                                     brand=fcd['brand'],
                                     specialist=curr_specialist)
            return render(self.request,'recording.html',response_dict)

        else:
            response_dict["message"]="Вы уже зарегистрированны на это время"
            return render(self.request,'recording.html',
                          response_dict)

    def get_context_data(self, **kwargs):
        context = super(RecordingView, self).get_context_data(**kwargs)
        context['specialist']=Specialist.objects.get(id= self.kwargs['specialist_id'])
        return context

