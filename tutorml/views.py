from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
from django.http import HttpResponse, JsonResponse
from django.utils import timezone

from .models import FAQ, Article, Choice, Dataset, Question, Subscription
from .forms import SubscriptionForm
from .neural.lang_detect import predict_input
from .neural.translator import translate


def index(request):
    articles = Article.objects.filter(pub_date__lte=timezone.now())
    popular_articles = articles.order_by('-views')[:2]
    datasets = Dataset.objects
    return render(request, "tutorml/index.html",
                  {"articles_number": articles.count(),
                   "datasets_number": datasets.count(),
                   "popular_articles": popular_articles})


def get_article(request, article_id):
    article = get_object_or_404(Article.objects.filter(pub_date__lte=timezone.now()), pk=article_id)
    article.views += 1
    article.save()
    return render(request, f"tutorml/article{article.id}.html", {"article": article})


def faq(request):
    faqs = get_list_or_404(FAQ)
    return render(request, "tutorml/faq.html", {"faqs": faqs})


def contacts(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("tutorml:contacts")
    else:
        form = SubscriptionForm()
    return render(request, "tutorml/contacts.html", {"form": form})


def about(request):
    views = {"Фото и видео": 0, "Текст": 0, "Аудио": 0, "Прочее": 0}
    articles = Article.objects.filter(pub_date__lte=timezone.now())
    for article in articles:
        views[article.category] += article.views

    subs = {"Туториалы": Subscription.objects.filter(notify_tutorials=True).count(),
            "Датасеты": Subscription.objects.filter(notify_datasets=True).count()}

    choices = get_object_or_404(Question, pk=1).choice_set.all()
    choices_dict = {choice.text: choice.votes for choice in choices}

    return render(request, "tutorml/about.html", {"categories": list(views.keys()),
                                                  "views":  list(views.values()),
                                                  "sub_types": list(subs.keys()),
                                                  "sub_count": list(subs.values()),
                                                  "choices_text": list(choices_dict.keys()),
                                                  "choices_votes": list(choices_dict.values()),})


def in_future(request):
    question = get_object_or_404(Question, pk=1)
    if request.method == "POST":
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            return render(request, 'tutorml/in_future.html', {
                'question': question,
                'error_message': "Вы не выбрали ответ!",
            })
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return redirect("tutorml:in_future")
    return render(request, "tutorml/in_future.html", {'question': question})


def popular(request):
    articles = Article.objects.filter(pub_date__lte=timezone.now())
    popular_articles = articles.order_by('-views')
    return render(request, "tutorml/popular.html", {"articles": popular_articles})


def new(request):
    articles = Article.objects.filter(pub_date__lte=timezone.now())
    new_articles = articles.order_by('-pub_date')
    return render(request, "tutorml/new.html", {"articles": new_articles})


def datasets(request, category):
    datasets = Dataset.objects.filter(category=category)
    return render(request, f"tutorml/datasets_{category}.html", {"datasets": datasets})


def nn(request):
    return render(request, "tutorml/nn.html")


# AJAX views
def get_predicted_lang(request):
    text = request.POST["inputValue"]
    if text == '':
        return JsonResponse({"response": f'Введите хоть что-то!'})
    language, prob = predict_input(text)
    return JsonResponse({"response": f"Распознанный язык: {language}, вероятность: {prob}%"})


def translate_text(request):
    text = request.POST["inputValue"]
    if text == '':
        return JsonResponse({"response": f'Введите хоть что-то!'})
    translated_text = translate(text)
    return JsonResponse({"response": f'Перевод: "{translated_text[0]}"'})
