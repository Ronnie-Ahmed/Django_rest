from django.urls import path
from myapp1 import views

urlpatterns = [
    # path('snippets/', views.snippet_list),
    # path('snippets/<int:pk>/', views.snippet_detail),
    path('snippets/',views.SnippestList.as_view()),
    path('snippets/<int:pk>/',views.SnippetDetails.as_view()),
    path('snip/',views.SnippestModelGenerics.as_view()),
    path('snip/<int:pk>',views.SnippestModelDetailsGenerics.as_view())
    
]