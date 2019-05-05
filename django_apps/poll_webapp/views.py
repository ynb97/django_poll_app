# Views file for poll
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Poll_options,Poll,Poll_votes
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import (
    ListView,
    DetailView,
    # CreateView
)

def home(request):
    return render(request, 'poll_webapp/home.html')

def about(request):
    return render(request, 'poll_webapp/about.html', {'title': 'About'})


def result(request):
    return render(request, 'poll_webapp/results.html')


@login_required
def vote(request, poll_id):
    voted = False
    opnid = request.POST['ops']
    optn = Poll_options.objects.filter(id=opnid).first()
    user1 = request.user
    question = get_object_or_404(Poll, pk=poll_id)
    print("Question: ",question)
    print("Selected choice: ", optn)
    # print(optn.question.id==int(poll_id))    
    if (Poll_votes.objects.filter(voter=user1)):
        for vote1 in Poll_votes.objects.filter(voter=user1).all():
            print(vote1.ans_text.question.id)
            print(int(poll_id))
            print(vote1.ans_text.question.id==int(poll_id))
            if(vote1.ans_text.question.id==int(poll_id)):
                voted = True
        
        print(voted)
        print(not voted)
        if(not voted):
            print("Inner else")
            newvote = Poll_votes(ans_text=optn, voter=user1)
            newvote.save()
            messages.success(request, f'Your vote has been recorded !')
            return redirect('poll-result')
        else:
            messages.warning(request, f'You have already voted for this poll, try another!')
            return redirect('poll-home')
    else:
        print("outer else")
        newvote = Poll_votes(ans_text=optn, voter=user1)
        newvote.save()
        messages.success(request, f'Your vote has been recorded !')
        return redirect('poll-result')
        # try:
        #     selected_choice = question.poll_options_set.get(pk=request.POST['ops.id'])
        # except (KeyError, Poll_options.DoesNotExist):
        #     #display the question voting form
        #     return render(request, 'poll_webapp/polls.html', {'question': question, 'error_message':"You didn't select a choice"})
        # else:

        #     # selected_choice.votes += 1
        #     # selected_choice.save()
        #     #Always submit an HttpResponseRedirect after successfully dealing with POST data
        #     #This prevents the form being posted twice if a user hits the back button
        #     return HttpResponseRedirect(reverse('poll-about'), args=(poll_id))

    # else:



# def polls(request):
    
#     return render(request, 'poll_webapp/polls.html', context, {'title': 'Live polls'})

context = {
        'polls_obj': Poll.objects.all(),
        'poll_ops': Poll.poll_options_set,
        'pollvotes':Poll_votes.objects.all() 
    }

class PollListView(ListView):
    model = Poll
    template_name = 'poll_webapp/polls.html'
    context_object_name = 'polls_obj'
    ordering = ['-date_posted']
    paginate_by = 2


class ResultListView(ListView):
    model = Poll
    template_name = 'poll_webapp/results.html'
    context_object_name = 'polls_obj'
    ordering = ['-date_posted']

# def candidates(request):
#   cand = {
#       'cand_obj': Poll_ans.objects.all()
#   }
#   return render(request, 'poll_webapp/candidates.html', cand)

class PollDetailView(DetailView):
    model = Poll
    # context_object_name = 'poll_ops'
    # def get_context_data(self, **kwargs):
    #     # xxx will be available in the template as the related objects
    #     context = super(PollDetailView, self).get_context_data(**kwargs)
    #     context['poll_ops'] = Poll_options.objects.filter('option_text')
    #     return context



# class Poll_votesCreateView(LoginRequiredMixin, CreateView):
#     model = Poll_votes
#     template_name = 'poll_webapp/poll_detail.html'
#     # fields = ['ans_text']
#     # success_url = reverse('poll_webapp/about.html')

#     def get_initial(self):
#         initial = super().get_initial()
#         # cpf - it's the name of the field on your current form
#         # self.args will be filled from URL. I'd suggest to use named parameters
#         # so you can access e.g. self.kwargs['cpf_initial']
#         initial['ops'] = self.args[0] 
#         return initial

#     def form_valid(self, form):
#         form.instance.voter = self.request.user
#         return super().form_valid(form)