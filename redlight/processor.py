from results.models import auctions

def foos(request):
    # return {'this_list': auctions.objects.all()}
    k = auctions.objects.all()

    return {'this_list': k[:4], 'how_many': len(k)}
