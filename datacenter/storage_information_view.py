from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.models import format_duration
from django.utils.timezone import localtime
from datacenter.models import get_duration

def storage_information_view(request):
	not_leaved_visits = Visit.objects.filter(leaved_at=None)
	incomplete_visits = []
	for not_leaved_visit in not_leaved_visits:
		who_entered = not_leaved_visit.passcard
		entered_at = localtime(not_leaved_visit.entered_at)
		duration = format_duration(get_duration(not_leaved_visit))
	
	visit = {
            'who_entered': who_entered,
            'entered_at': entered_at,
            'duration': duration
        }
	incomplete_visits.append(visit)
    
	context = {
        'non_closed_visits': incomplete_visits,  
	}
	return render(request, 'storage_information.html', context)
