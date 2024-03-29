from django.shortcuts import render, redirect, get_object_or_404
from hive_management.models import Hive, Note, Inspection, Treatment
from hive_management.forms import AddHiveForm, NoteForm, AddInspectionForm, AddTreatmentForm
from .utils import reports, divide
import datetime

# Create your views here.

def homepage(request):
    return render(request, 'homepage.html', {})

def hive_management(request):
    view = request.session.get('view')
    if view == 'grid' or view == 'list':
        pass
    else:
        request.session['view'] = 'grid'
        view = request.session.get('view')

    if request.method == 'POST':
        data = request.POST
        request.session['view'] = data.get('gridlist')
        view = request.session.get('view')

    if 'loc' in request.GET:
        hives = Hive.objects.filter(location=request.GET['loc']).order_by('name')
    else:
        hives = Hive.objects.all().order_by('name')

    # locations:
    locations = Hive.objects.values_list('location', flat=True).order_by('location').distinct()
    treatments = Treatment.objects.all()
    inspections = Inspection.objects.all()
    treatment_reports = reports.check_treatment()
    inspection_reports = reports.check_inspection()
    context = {
        "hives": hives,
        "treatment_reports": treatment_reports,
        "inspection_reports": inspection_reports,
        "treatments": treatments,
        "inspections": inspections,
        "view": view,
        "locations": locations,
        "c_p": request.get_full_path(),
    }
    return render(request, 'hive_management.html', context)

def hive_detail(request, pk):
    hive = Hive.objects.get(pk=pk)
    notes = Note.objects.filter(hive=hive).order_by('-created_on')
    inspections = Inspection.objects.filter(hive=hive).order_by('-created_on')
    treatments = Treatment.objects.filter(hive=hive).order_by('-created_on')
    context = {
        "hive": hive,
        "notes": notes,
        "inspections": inspections,
        "treatments": treatments
    }
    return render(request, 'hive_detail.html', context)

def donate(request):
    return render(request, 'donate.html', {})

def new_hive(request):
    if request.method == 'POST':
        new_hive_post = AddHiveForm(request.POST)
        if new_hive_post.is_valid():
            post = Hive(
                name = new_hive_post.cleaned_data['name'],
                location = new_hive_post.cleaned_data['location'],
                description = new_hive_post.cleaned_data['description'],
                supers = new_hive_post.cleaned_data['supers'],
                frames = new_hive_post.cleaned_data['frames'],
                color = new_hive_post.cleaned_data['color'],
                purpose = new_hive_post.cleaned_data['purpose'],
                strength = new_hive_post.cleaned_data['strength'],
                created_on = new_hive_post.cleaned_data['created_on']
            )
            post.save()
            return redirect("hive_detail", pk=post.pk)
    context = {
        'form': AddHiveForm,
    }
    return render(request, 'new_hive.html', context)

def edit_hive(request, pk):
    hive = get_object_or_404(Hive, pk=pk)
    form = AddHiveForm(request.POST or None, instance = hive)

    if form.is_valid():
        form.save()
        return redirect("hive_detail", pk=hive.pk)

    context = {
        "hive": hive,
        "form": form,
    }
    return render(request, "edit_hive.html", context)

def remove_hive(request, pk):
    hive = Hive.objects.get(pk=pk)
    context = {
        'hive': hive,
    }

    if request.method == "POST":
        hive.delete()
        return redirect("hive_management")

    return render(request, "remove_hive.html", context)

def add_note(request, pk):
    hive = Hive.objects.get(pk=pk)
    context = {
        'hive': hive,
        'form': NoteForm,
    }

    if request.method == 'POST':
        add_note_form = NoteForm(request.POST)
        if add_note_form.is_valid():
            note = Note(
                title = add_note_form.cleaned_data['title'],
                body = add_note_form.cleaned_data['body'],
                hive = hive
            )
            note.save()
            return redirect("hive_detail", pk=hive.pk)

    return render(request, "add_note.html", context)

def add_inspection(request, pk):
    hive = Hive.objects.get(pk=pk)
    context = {
        'hive': hive,
        'form': AddInspectionForm,
    }

    if request.method == 'POST':
        add_inspection_form = AddInspectionForm(request.POST)
        if add_inspection_form.is_valid():
            inspection = Inspection(
                name = add_inspection_form.cleaned_data['name'],
                description = add_inspection_form.cleaned_data['description'],
                created_on = add_inspection_form.cleaned_data['created_on'],
                queen = add_inspection_form.cleaned_data['queen'],
                eggs = add_inspection_form.cleaned_data['eggs'],
                open_brood = add_inspection_form.cleaned_data['open_brood'],
                sealed_brood = add_inspection_form.cleaned_data['sealed_brood'],
                honey = add_inspection_form.cleaned_data['honey'],
                varroa = add_inspection_form.cleaned_data['varroa'],
                hive = hive
            )
            inspection.save()
            return redirect("hive_detail", pk=hive.pk)

    return render(request, "add_inspection.html", context)

def add_treatment(request, pk):
    hive = Hive.objects.get(pk=pk)
    context = {
        'hive': hive,
        'form': AddTreatmentForm,
    }

    if request.method == 'POST':
        add_treatment_form = AddTreatmentForm(request.POST)
        if add_treatment_form.is_valid():
            treatment = Treatment(
                name = add_treatment_form.cleaned_data['name'],
                description = add_treatment_form.cleaned_data['description'],
                created_on = add_treatment_form.cleaned_data['created_on'],
                med_name = add_treatment_form.cleaned_data['med_name'],
                hive = hive
            )
            treatment.save()
            return redirect("hive_detail", pk=hive.pk)

    return render(request, "add_treatment.html", context)

def tutorials(request):
    return render(request, 'tutorials.html', {})

def divide_hives(request):
    offer_divide = divide.Divide()
    queen = offer_divide.make_divided_hive_queen()
    hives = offer_divide.make_divided_hive()

    if request.method == 'POST':
        post = Hive(
            name = 'New Hive',
            location = 'Not set',
            description = 'New hive created by dividing 3 hives',
            supers = 1,
            frames = 6,
            color = '#ffffff',
            purpose = 'Test',
            strength = 75,
            created_on = datetime.datetime.today().strftime('%Y-%m-%d')
        )
        post.save()

        if queen != False:
            queen.frames = queen.frames - 2
            queen.save()
            # queen.update(frames=queen.frames - 2)

        for hive in hives:
            hive.frames = hive.frames - 2
            hive.save()
            
        return redirect("edit_hive", pk=post.pk)

    context = {
        'queen': queen,
        'hives': hives,
    }
    return render(request, 'divide_hives.html', context)

def search(request):
    if request.method == "POST":
        query = request.POST.get('search')
        if query:
            hives_found = Hive.objects.filter(name__contains=query)
            inspections_found = Inspection.objects.filter(name__contains=query)
            treatments_found = Treatment.objects.filter(name__contains=query)
            notes_found = Note.objects.filter(title__contains=query)

        context = {
            'hives': hives_found,
            'inspections': inspections_found,
            'treatments': treatments_found,
            'notes': notes_found,
        }
    return render(request, "search.html", context)
