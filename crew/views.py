import os
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from . models import *

# Create your views here.
@login_required
def info(request, code):
    bio = Bio.objects.get(b_d='', code=code)
    service = Service.objects.filter(s_d='', code=code).order_by('-s_start')
    contract = Contract.objects.filter(con_d='', code=code).order_by('-con_pdos')
    doc = Doc.objects.filter(d_d='', code=code).order_by('cert')
    rank = bio.rank
    rank = Rank.objects.get(rank=rank)
    vessel = bio.last_vessel
    vessel = Vessel.objects.get(vessel=vessel)
    principal = vessel.principal
    principal = Principal.objects.get(principal=principal)
    vessel_type = vessel.vessel_type
    vessel_type = Vtype.objects.get(vessel_type=vessel_type)


    template = 'crew/view-info.html'
    context_dict = { 'bio':bio, 'service':service, 'contract':contract, 'doc':doc, 
                    'rank':rank, 'vessel':vessel, 'principal':principal, 'vessel_type':vessel_type }
    # return HttpResponse("Hello %s" % code)
    return render(request, template, context_dict)
@login_required
def picture(request, code):
    template = 'crew/view-picture.html'
    # media = settings.MEDIA_URL
    picture = os.listdir('media')
    picture = [ x for x in picture if code in x]
    picture = sorted(picture, reverse=1)
    if not picture:
        picture = '9999.DEFAULT.pix'
    else:
        picture = picture[0]

    context_dict = {'picture':picture}
    # return HttpResponse("Hello %s waiting for picture request" % code)
    return render(request, template, context_dict)
@login_required
def contract(request, contract):
    contract = Contract.objects.get(contract=contract)
    wage = contract.wage
    wage = Wage.objects.get(w_rec=wage)
    code = contract.code
    bio = Bio.objects.get(b_d='', code=code)
    principal = contract.principal
    principal = Principal.objects.get(principal=principal)
    rank = bio.rank
    rank = Rank.objects.get(rank=rank)

    senior = [wage.w_sen_1, wage.w_sen_2, wage.w_sen_3, wage.w_sen_4, wage.w_sen_5, wage.w_sen_6, 
                wage.w_sen_7, wage.w_sen_8, wage.w_sen_9, wage.w_sen_10, wage.w_sen_11]

    senior_rank = [wage.w_sen_rank_1, wage.w_sen_rank_2, wage.w_sen_rank_3, wage.w_sen_rank_4, 
                wage.w_sen_rank_5, wage.w_sen_rank_6, wage.w_sen_rank_7, wage.w_sen_rank_8, 
                wage.w_sen_rank_9, wage.w_sen_rank_10, wage.w_sen_rank_11]

    senior_amount = contract.con_seniority - 1
    senior_rank_amount = contract.con_seniority_rank - 1

    senior_amount = senior[senior_amount]
    senior_rank_amount = senior_rank[senior_rank_amount]

    template = 'crew/contract.html'
    context_dict = { 'contract':contract, 'bio':bio, 'wage':wage, 'principal': principal, 'rank': rank,
                    'senior_amount':senior_amount, 'senior_rank_amount':senior_rank_amount }
    return render(request, template, context_dict)

def navigation_autocomplete(request):
    q = request.GET.get('q', '')
    principal = ''
    vessel_type = ''
    last_vessel = ''
    rank = ''
    status = ''

    if q:
        code = Q(code__icontains=q, b_d='')
        first_name = Q(first_name__icontains=q, b_d='')
        middle_name = Q(middle_name__icontains=q, b_d='')
        last_name = Q(last_name__icontains=q, b_d='')
        
        bios = Bio.objects.filter(
            code |
            first_name |
            middle_name |
            last_name
        ).distinct() 

        if request.GET.get('principal'):
            principal = request.GET.get('principal')
            bios = bios.filter(last_vessel__principal=principal)
        if request.GET.get('vessel_type'):
            vessel_type = request.GET.get('vessel_type')
            bios = bios.filter(last_vessel__vessel_type=vessel_type)
        if request.GET.get('last_vessel'):
            last_vessel = request.GET.get('last_vessel')
            bios = bios.filter(last_vessel=last_vessel)
        if request.GET.get('rank'):
            rank = request.GET.get('rank')
            bios = bios.filter(rank=rank)
        if request.GET.get('status'):
            status = request.GET.get('status')
            bios = bios.filter(status=status)

        template='crew/autocomplete.html'
        context_dict = {'bios': bios}
        return render(request, template, context_dict)
    else:
        pass