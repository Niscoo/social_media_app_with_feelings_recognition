from django.http import JsonResponse
from django.shortcuts import render
from .models import Publication
from .forms import PublicationForm
from .bert_model import predict_sentiment

def publications_list(request):
    publications = Publication.objects.all()
    return render(request, 'publication_list.html', {'publications': publications})

def add_publication(request):
    if request.method == 'POST':
        form = PublicationForm(request.POST)
        if form.is_valid():
            publication_content = form.cleaned_data['content']
            sentiment = predict_sentiment(publication_content)  # Utilisation de votre fonction

            publication = form.save(commit=False)
            publication.sentiment = sentiment
            publication.save()

            response_data = {
                'success': True,
                'publication': {
                    'content': publication.content,
                    'sentiment': publication.sentiment,  # 'positive' ou 'negative'
                }
            }
            return JsonResponse(response_data)
        else:
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'error': errors}, status=400)

    return JsonResponse({'success': False, 'error': 'Méthode non autorisée'}, status=405)