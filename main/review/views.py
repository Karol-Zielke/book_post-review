from django.shortcuts import render, get_object_or_404
from .models import PostReview


def review_list(request):
    reviews = PostReview.published.all()
    return render(request, 'main/review/list.html', {'reviews': reviews})


def single_review(request, year, month, day, review):
    review = get_object_or_404(PostReview, slug=review,
                               status='published',
                               publish__year=year,
                               publish__month=month,
                               publish__day=day)
    return render(request, 'main/review/detail.html', {'review': review})
