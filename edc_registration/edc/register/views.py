from django.http import HttpResponse
from django.shortcuts import *
from django.core.mail import send_mail
from django.template.loader import get_template
from django.template import Context
from django.db.models import Q

from datetime import *
from pytz import timezone

from edc.register.models import *
from edc.register.forms import UserForm


INFO_EMAIL = ('EDCmanager@stfc.ac.uk',)
#INFO_EMAIL = ('andrew.harwood@stfc.ac.uk',)

def select_dataset(request):

   if request.method == 'POST':
      dataset = Dataset.objects.get(name=request.POST.get('datasetname'))
      return redirect('/register/user/%s' % dataset.id)
      
   datasets = Dataset.objects.filter(~Q(name__istartswith='Test'))
      
   return render_to_response('select_dataset.html', locals())
      
   
def register_user(request, datasetid):

   if request.method == 'POST':
      form = UserForm(request.POST)

      if form.is_valid():
         human = True
	 
         cd = form.cleaned_data
	 
         condition = Condition.objects.get(id=request.POST.get('conditionid'))
	 
         u = User(firstName    = cd['firstName'], 
	          lastName     = cd['lastName'],
	          title        = cd['title'],
		  emailaddress = cd['emailaddress'],
		  department   = cd['department'],
		  institute    = cd['institute'],
		  dataUse      = cd['dataUse'],
		  startdate    = datetime.now(timezone('Europe/London')),
		  condition    = condition,
		  )
         u.save()
#
#               Send out informational message
#	 
         emailTemplate = get_template('email.txt')
         d = {'user': u}
         emailMessage = emailTemplate.render(d)
         subject = 'EDC dataset registration: %s' % u.condition.dataset.name
         fromAddress = u.emailaddress
         send_mail(subject, emailMessage, fromAddress, INFO_EMAIL)

         emailTemplate = get_template('email_user.txt')
         d = {'user': u}
         emailMessage = emailTemplate.render(d)
         subject = 'EDC dataset registration: %s' % u.condition.dataset.name
         fromAddress = 'EDCmanager@stfc.ac.uk'
         send_mail(subject, emailMessage, fromAddress, (u.emailaddress,))

         return HttpResponseRedirect ('/register/thanks/')
   else:	 
      form = UserForm()

#
#   Get latest conditions for the given dataset
#         
   conditions = Condition.objects.filter(dataset__exact=datasetid).order_by('-version')[0] 
   return render(request, 'register_user.html', locals())
#   return render_to_response('register_user.html', locals())


def thanks (request):
   return render_to_response('thanks.html')
