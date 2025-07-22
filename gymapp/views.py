from django.shortcuts import render, redirect, get_object_or_404
from .models import Member

def member_list(request):
    members = Member.objects.all()
    return render(request, 'gymapp/member_list.html', {'members': members})

def member_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        membership_type = request.POST.get('membership_type')
        Member.objects.create(name=name, age=age, membership_type=membership_type)
        return redirect('member_list')
    return render(request, 'gymapp/member_form.html')

def member_update(request, id):
    member = get_object_or_404(Member, pk=id)
    if request.method == 'POST':
        member.name = request.POST.get('name')
        member.age = request.POST.get('age')
        member.membership_type = request.POST.get('membership_type')
        member.save()
        return redirect('member_list')
    return render(request, 'gymapp/member_form.html', {'member': member})

def member_delete(request, id):
    member = get_object_or_404(Member, pk=id)
    member.delete()
    return redirect('member_list')

def workout_plan(request):
    return render(request, 'gymapp/workout_plan.html')

def diet_plan(request):
    return render(request, 'gymapp/diet_plan.html')

