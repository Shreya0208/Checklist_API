from core.views import (TestApiViews, ChecklistsApiViews, ChecklistItemsCreateApiViews, ChecklistApiViews,
                        ChecklistItemsApiViews)
from django.urls import path

urlpatterns = [

    path('',TestApiViews.as_view()),
    path('api/checklists',ChecklistsApiViews.as_view()),
    path('api/checklist/<int:pk>',ChecklistApiViews.as_view()),
    path('api/checklistitems/create',ChecklistItemsCreateApiViews.as_view()),
    path('api/checklistitem/<int:pk>',ChecklistItemsApiViews.as_view()),

]
