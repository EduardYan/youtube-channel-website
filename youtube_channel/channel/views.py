from django.shortcuts import render

def home(request):
    """
    Principal route /
    """

    return render(request, 'channel/home.html')

def subscribe(request):
    """
    Route for subscribe to the channel
    """

    return render(request, 'channel/subscribe.html')

def about(request):
    """
    Route for render the about page
    """

    return render(request, 'channel/about.html')
