from django import template
from django.shortcuts import render, redirect
from .models import Hiking, Journal, Profile
from .forms import ProfileForm
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.template import loader, RequestContext
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from isodate import parse_duration
import requests
import io
import pdfkit


# Create your views here.

def main_menu(request):
    hike_object = Hiking.objects.all()
    return render(request, 'AppSuite/MainMenu.html', {'hike_object': hike_object})


# ---------------------Hiking----------------------------------------------------
def hiking_homepage(request):
    return render(request, 'AppSuite/HikingHomePage.html')


def add_hike(request):
    if request.method == 'POST' and request.FILES['Hike_Images']:
        Hike_Name = request.POST.get('Hike_Name', '')
        Hike_Length = request.POST.get('Hike_Length', '')
        Hike_TrailType = request.POST.get('Hike_TrailType', '')
        Hike_TimeOfYear = request.POST.get('Hike_TimeOfYear', '')
        Hike_Difficulty = request.POST.get('Hike_Difficulty', '')
        Hike_TrailHead = request.POST.get('Hike_TrailHead', '')
        Hike_Completed = request.POST.get('Hike_Completed', '')
        Hike_Notes = request.POST.get('Hike_Notes', '')
        Hike_Images = request.POST.get('Hike_Images', '')

        myfile = request.FILES['Hike_Images']
        fs = FileSystemStorage()  # defaults to   MEDIA_ROOT
        filename = fs.save(myfile.name, myfile)
        file_url = fs.url(filename)

        hiking = Hiking(Hike_Name=Hike_Name, Hike_Length=Hike_Length, Hike_TrailType=Hike_TrailType,
                        Hike_TimeOfYear=Hike_TimeOfYear, Hike_Difficulty=Hike_Difficulty, Hike_TrailHead=Hike_TrailHead,
                        Hike_Completed=Hike_Completed, Hike_Notes=Hike_Notes, Hike_Images=myfile)
        hiking.save()
        return render(request, 'AppSuite/hike_add.html', {'file_url': file_url})
    else:
        return render(request, 'AppSuite/hike_add.html')


def search_hike(request):
    hike_object = Hiking.objects.all()
    hike_search = request.GET.get('Hike_Name' or 'Hike_Length' or 'Hike_TrailType' or 'Hike_TimeOfYear'
                                  or 'Hike_Difficulty' or 'Hike_TrailHead' or 'Hike_Completed')
    if hike_search != '' and hike_search is not None:
        hike_object = hike_object.filter(Hike_Name__icontains=hike_search) | hike_object.filter(
            Hike_Length__icontains=hike_search) | hike_object.filter(
            Hike_TrailType__icontains=hike_search) | hike_object.filter(
            Hike_TimeOfYear__icontains=hike_search) | hike_object.filter(
            Hike_Difficulty__icontains=hike_search) | hike_object.filter(
            Hike_TrailHead__icontains=hike_search) | hike_object.filter(Hike_Completed__icontains=hike_search)
    else:
        "<p> Search not Available <p>"
    paginator = Paginator(hike_object, 5)
    page = request.GET.get('page')
    hike_object = paginator.get_page(page)
    return render(request, 'AppSuite/hike_search.html', {'hike_object': hike_object})


def export_hike(request):
    all_hikes = Hiking.objects.all()
    return render(request, 'AppSuite/hike_export.html', {'all_hikes': all_hikes})


def Hikes(request, id):
    hikes = Hiking.objects.get(pk=id)
    template = loader.get_template('AppSuite/Hike.html')
    c = {'hikes': hikes, 'request': request}
    html = template.render(c)
    options = {
        'page-size': 'Letter',
        'encoding': 'UTF-8',
        "enable-local-file-access": None
    }
    pdf = pdfkit.from_string(html, False, options)
    response = HttpResponse(pdf, content_type='application/pdf')
    filename = "Hike.pdf"
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
    return response

# --------------- Journaling-------------------------------------------------
def journal_homepage(request):
    return render(request, 'AppSuite/JournalHomePage.html')


# Create New Journal Entry
def add_new_journal_entry(request):
    if request.method == 'POST':
        Date_Time = request.POST.get('Date_Time', '')
        Journal_Entry = request.POST.get('Journal_Entry', '')

        journal = Journal(Date_Time=Date_Time, Journal_Entry=Journal_Entry)
        journal.save()

    return render(request, 'AppSuite/journal_add.html')


# Search and Display Journal Entries
def search_journal_entries(request):
    journal_object = Journal.objects.all()
    journal_search = request.GET.get('Journal_Entry')
    if journal_search != '' and journal_search is not None:
        journal_object = journal_object.filter(Date_Time=journal_search) | journal_object.filter(
            Journal_Entry=journal_search)
    paginator = Paginator(journal_object, 5)
    page = request.GET.get('page')
    journal_object = paginator.get_page(page)
    return render(request, 'AppSuite/journal_search.html', {'journal_object': journal_object})


def display_all_journal_entries(request):
    all_journal_entries = Journal.objects.all()
    return render(request, 'AppSuite/journal_display.html', {'all_journal_entries': all_journal_entries})


# --------------------------- Resume -------------------------------------------------
def resume_homepage(request):
    return render(request, 'AppSuite/ResumeHomePage.html')


# Create\Input Resume

def create_resume(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        summary = request.POST.get('summary', '')
        degree = request.POST.get('degree', '')
        school = request.POST.get('school', '')
        university = request.POST.get('university', '')
        previous_work = request.POST.get('previous_work', '')
        skills = request.POST.get('skills', '')
        profile = Profile(name=name, email=email, phone=phone, summary=summary, degree=degree, school=school,
                          university=university, previous_work=previous_work, skills=skills)
        profile.save()

    return render(request, 'AppSuite/resume_create.html')


# Export Specific Resume

def resume(request, id):
    user_profile = Profile.objects.get(pk=id)
    template = loader.get_template('AppSuite/resume.html')
    c = {'user_profile': user_profile, 'request': request}
    html = template.render(c)
    options = {
        'page-size': 'Letter',
        'encoding': 'UTF-8',
        "enable-local-file-access": None
    }
    pdf = pdfkit.from_string(html, False, options)
    response = HttpResponse(pdf, content_type='application/pdf')
    filename = "Resume.pdf"
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(filename)
    return response


def export_resume(request):
    myresumes = Profile.objects.all()
    return render(request, 'AppSuite/resume_download.html', {'myresumes': myresumes})


# Edit Resume
def edit_resume(request, id):
    user_resume = Profile.objects.get(id=id)
    form = ProfileForm(request.POST or None, instance=user_resume)

    if form.is_valid():
        form.save()
        return redirect('AppSuite:resume_homepage')

    return render(request, 'AppSuite/resume_editform.html', {'form': form, 'user_resume': user_resume})


# -------------------------Youtube --------------------------------------------------

def YoutubeHomePage(request):
    return render(request, 'AppSuite/YoutubeHomePage.html')


def youtube_search(request):
    videos = []

    if request.method == 'POST':
        search_url = 'https://www.googleapis.com/youtube/v3/search'
        video_url = 'https://www.googleapis.com/youtube/v3/videos'

        search_params = {
            'part': 'snippet',
            'q': request.POST['search'],
            'key': settings.YOUTUBE_DATA_API_KEY,
            'maxResults': 9,
            'type': 'video'
        }

        r = requests.get(search_url, params=search_params)

        results = r.json()['items']

        video_ids = []
        for result in results:
            video_ids.append(result['id']['videoId'])

        if request.POST['submit'] == 'lucky':
            return redirect(f'https://www.youtube.com/watch?v={video_ids[0]}')

        video_params = {
            'key': settings.YOUTUBE_DATA_API_KEY,
            'part': 'snippet,contentDetails',
            'id': ','.join(video_ids),
            'maxResults': 9
        }

        r = requests.get(video_url, params=video_params)

        results = r.json()['items']

        for result in results:
            video_data = {
                'title': result['snippet']['title'],
                'id': result['id'],
                'url': f'https://www.youtube.com/watch?v={result["id"]}',
                'duration': int(parse_duration(result['contentDetails']['duration']).total_seconds() // 60),
                'thumbnail': result['snippet']['thumbnails']['high']['url']
            }

            videos.append(video_data)

    context = {
        'videos': videos
    }

    return render(request, 'AppSuite/youtube_search.html', context)
