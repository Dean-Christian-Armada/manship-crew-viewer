from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . models import *

# Create your views here.

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

def picture(request, code):
    template = ''
    context_dict = {}
    return HttpResponse("Hello %s waiting for picture request" % code)
    # return render(request, template, context_dict)

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

    template='crew/autocomplete.html'
    context_dict = {}
    context_dict['bios'] = Bio.objects.filter(
        Q(code__icontains=q, b_d='') |
        Q(first_name__icontains=q, b_d='') |
        Q(middle_name__icontains=q, b_d='') |
        Q(last_name__icontains=q, b_d='')
    ).distinct()
    return render(request, template, context_dict)