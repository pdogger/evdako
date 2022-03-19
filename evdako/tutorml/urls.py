from django.urls import include, path

from . import views


app_name = 'tutorml'
urlpatterns = [
    path("", views.index, name="index"),
    path("contacts/", views.contacts, name="contacts"),
    path("articles/<int:article_id>/", views.get_article, name="article"),
    path("faq/", views.faq, name="faq"),
    path("about/", views.about, name="about"),
    path("in_future/", views.in_future, name="in_future"),
    path("popular/", views.popular, name="popular"),
    path("new/", views.new, name="new"),
    path("datasets/<str:category>/", views.datasets, name="datasets"),
    path("ajax/get_predicted_lang/", views.get_predicted_lang, name="get_predicted_lang"),
    path("ajax/translate_text/", views.translate_text, name="translate_text"),
]
