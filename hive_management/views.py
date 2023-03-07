from django.shortcuts import render, redirect, get_object_or_404
from hive_management.models import Hive, Note
from hive_management.forms import AddHiveForm, NoteForm

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html', {})

def hive_management(request):
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

    hives = Hive.objects.all().order_by('-created_on')
    context = {
        "hives": hives,
    }
    return render(request, 'hive_management.html', context)

def hive_detail(request, pk):
    hive = Hive.objects.get(pk=pk)
    notes = Note.objects.filter(hive=hive).order_by('-created_on')
    context = {
        "hive": hive,
        "notes": notes
    }
    return render(request, 'hive_detail.html', context)

def donate(request):
    return render(request, 'donate.html', {})

def new_hive(request):
    context = {
        'form': AddHiveForm,
    }
    return render(request, 'new_hive.html', context)

def edit_hive(request, pk):
    hive = get_object_or_404(Hive, pk=pk)
    form = AddHiveForm(request.POST or None, instance = hive)

    if form.is_valid():
        form.save()
        return redirect("hive_management")

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
            return redirect("hive_management")

    return render(request, "add_note.html", context)
