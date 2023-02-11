from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from datacenter.models import format_duration
from datacenter.models import get_duration
from datacenter.models import is_visit_long
from django.utils.timezone import localtime
from django.shortcuts import get_object_or_404

def passcard_info_view(request, passcode):
	passcard = get_object_or_404(Passcard, passcode=passcode)
	passcard_visits = Visit.objects.filter(passcard=passcard)
	serialized_visits = []  
	for passcard_visit in passcard_visits:
		entered_at = localtime(passcard_visit.entered_at)
		duration = format_duration(get_duration(passcard_visit))
		is_strange = is_visit_long(passcard_visit)
		visit = {
			"entered_at": entered_at,
			"duration": duration,
			"is_strange": is_strange,
		}
		serialized_visits.append(visit)

	context = {
		'passcard': passcard,
		'this_passcard_visits': serialized_visits
		}
	return render(request, 'passcard_info.html', context)
