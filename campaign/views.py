from django.shortcuts import render


# Create your views here.
def issue_list(request):
    return render(request, 'issues/issue_list.html')

def issue_water(request):
    return render(request, 'issues/water.html')

def issue_air(request):
    return render(request, 'issues/air.html')

def issue_land(request):
    return render(request, 'issues/land.html')

def issue_waste(request):
    return render(request, 'issues/waste.html')

def issue_energy(request):
    return render(request, 'issues/energy.html')

def issue_forest(request):
    return render(request, 'issues/forest.html')
    
def issue_wildlife(request):
    return render(request, 'issues/wildlife.html')
