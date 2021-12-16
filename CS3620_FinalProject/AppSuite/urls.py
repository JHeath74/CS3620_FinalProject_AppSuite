from . import views
from django.urls import path, include

app_name = "AppSuite"

urlpatterns = [
    path('main_menu/', views.main_menu, name="main_menu"),

    path('hiking_homepage/', views.hiking_homepage, name="hiking_homepage"),
    path('add_hike/', views.add_hike, name="add_hike"),
    path('search_hike/', views.search_hike, name="search_hike"),
    path('export_hike/', views.export_hike, name="export_hike"),
    path('hikes/<int:id>/', views.Hikes, name="Hikes"),

    path('journal_homepage/', views.journal_homepage, name="journal_homepage"),  # Journal Home Page
    path('add_new_journal_entry/', views.add_new_journal_entry, name="add_new_journal_entry"),  # Add New Journal Entry
    path('search_journal_entries/', views.search_journal_entries, name="search_journal_entries"),  # Search Journal
    path('display_all_journal_entries/', views.display_all_journal_entries, name="display_all_journal_entries"),  # Display All Journal Entries

    path('resume_homepage/', views.resume_homepage, name="resume_homepage"),  # Resume HomePage
    path('create_resume/', views.create_resume, name="create_resume"),  # Create Resume
    path('resume/<int:id>/', views.resume, name="resume"),
    path('export_resume', views.export_resume, name="export_resume"),  # Export Specific Resume
    path('edit_resume/<int:id>', views.edit_resume, name="edit_resume"),  # Edit Specific Resume

    path('YoutubeHomePage/', views.YoutubeHomePage, name="YoutubeHomePage"),
    path('youtube_search/', views.youtube_search, name="youtube_search"),  # Youtube search


]
