from django.shortcuts import render, redirect


def view_bag(request):
    """" A view to return the index page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')

    """ This is the session that stores the contents of the bag   """
    bag = request.session.get('bag', {})
    """ check if item is in bag,if so, increase quantity else keep quantity """
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else: 
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
    