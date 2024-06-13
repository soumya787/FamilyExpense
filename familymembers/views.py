from datetime import datetime

from django.shortcuts import render

# Create your views here.
from familymembers.models import FamilyMember, Expenses


def home(request):
    return render(request, 'index.html')


def addmemberlogic(request):
    f1 = FamilyMember()
    f1.name = request.POST['memberName']
    f1.mobile = request.POST['memberPhone']
    f1.income = request.POST['memberIncome']
    f1.occupation = request.POST['memberOccupation']
    f1.save()
    return render(request, 'addmember.html')


def f1(request):
    return render(request, 'addmember.html')


def f2(request):
    data = FamilyMember.objects.all()
    return render(request, 'display.html', {'x' : data} )


def editfunction(request, id):
    member = FamilyMember.objects.get(id=id)

    if request.method=='POST':
        member.name = request.POST['memberName']
        member.mobile = request.POST['memberPhone']
        member.income = request.POST['memberIncome']
        member.occupation = request.POST['memberOccupation']
        member.save()
        data = FamilyMember.objects.all()
        return render(request, 'display.html', {'x': data})

    return render(request, 'editing.html', {'x':member})

def deletefunction(request, id):
    member = FamilyMember.objects.get(id=id)
    member.delete()
    data = FamilyMember.objects.all()
    return render(request, 'display.html', {'x': data})


def addexpensefunction(request):
    family = FamilyMember.objects.all()
    return render(request, 'addexpense.html', {'x' : family} )


def saveexpensedatafunction(request):
    exp = Expenses()
    exp.membername_id = request.POST['name']
    exp.purpose = request.POST['purpose']
    exp.expense = float(request.POST['expense'])
    exp.save()
    return render(request, 'addexpense.html', {'x': FamilyMember.objects.all()})


def showexpensefunction(request):
    expenses_data = Expenses.objects.all()
    family_data = FamilyMember.objects.all()
    return render(request, 'show_expenses.html', {'x':expenses_data, 'y':family_data} )


def editexpensefunction(request, id):
    expense = Expenses.objects.get(id=id)
    family = FamilyMember.objects.all()
    if request.method == 'POST':
        expense.membername_id = request.POST['name']
        expense.purpose = request.POST['purpose']
        expense.expense = float(request.POST['expense'])
        expense.save()
        expenses_data = Expenses.objects.all()
        family_data = FamilyMember.objects.all()
        return render(request, 'show_expenses.html', {'x': expenses_data,
                                                      'y': family_data})

    return render(request,'editexpense.html', {'x' : expense, 'y':family})


def deleteexpensefunction(request, id):
    return None