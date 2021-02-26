from django.shortcuts import render


def index(request):
    """" A view to a users profile """
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
