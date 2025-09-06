from django.shortcuts import render, redirect, get_object_or_404
from .forms import PatientForm, VisitForm
from .models import Patient
from django.db.models import Q

def add_patient(request):
    if request.method == "POST":
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save()  # сохраняем и получаем объект
            return redirect('patients:patient_detail', pk=patient.pk)
    else:
        form = PatientForm()
    return render(request, 'patients/add_patient.html', {'form': form})


def patient_list(request):
    query = request.GET.get('q')  # берём строку из поля поиска
    if query:
        patients = Patient.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(phone__icontains=query) |
            Q(iin__icontains=query)
        )
    else:
        patients = Patient.objects.all()
    return render(request, 'patients/patient_list.html', {
        'patients': patients,
        'query': query
    })

def edit_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)  # получаем пациента по ID или 404
    if request.method == "POST":
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect("patients:patient_list")
    else:
        form = PatientForm(instance=patient)

    return render(request, "patients/edit_patient.html", {"form": form, "patient": patient})

def delete_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == "POST":
        patient.delete()
        return redirect('patients:patient_list')
    return render(request, 'patients/delete_patient.html', {'patient': patient})

def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    return render(request, 'patients/patient_detail.html', {'patient': patient})

def add_visit(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == "POST":
        form = VisitForm(request.POST)
        if form.is_valid():
            visit = form.save(commit=False)
            visit.patient = patient
            visit.save()
            return redirect('patients:patient_detail', pk=patient.pk)
    else:
        form = VisitForm()
    return render(request, 'patients/add_visit.html', {'form': form, 'patient': patient})
