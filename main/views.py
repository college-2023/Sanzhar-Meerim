from django.shortcuts import render


def home(request):
    return render(request, 'main/time_table.html')


def staff(request):
    return render(request, 'main/staff.html')


def clients(request):
    return render(request, 'main/clients.html')


def overview(request):
    return render(request, 'main/overview.html')


def analytics(request):
    return render(request, 'main/analytics.html')


def finance(request):
    return render(request, 'main/finance.html')


def payroll(request):
    return render(request, 'main/payroll.html')
