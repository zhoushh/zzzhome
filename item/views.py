from django.shortcuts import render
from . import models
import time
# Create your views here.


def index(request):
    items = models.Item.objects.all()
    return render(request, 'index.html', {'items': items})


def query_by_pos(request):
    positions = models.Position.objects.all()
    return render(request, 'query_by_pos.html', {'positions': positions})


def query_by_pos_show(request, pos_id):
    items = models.Item.objects.filter(itempstn=pos_id)
    return render(request, 'query_by_pos.html', {'items': items})


# 在L中查找包含s的元素
def find(L,s):
    return [x for x in L if s in x]


def query_by_name(request):
    items = models.Item.objects.all()
    nameToQuery = request.POST.get('nameToQuery ', 'ntq')
    items = [item for item in items if nameToQuery in item.itemname]
    return render(request, 'query_by_name.html', {'items': items})


def item_detail(request, item_id):
    item = models.Item.objects.get(pk=item_id)
    return render(request, 'item_detail.html', {'item': item})


def change_status(request, item_id):
    item = models.Item.objects.get(pk=item_id)
    if item.itemstatus == '使用':
        item.itemstatus = '放置'

    elif item.itemstatus == '放置':
        item.itemstatus = '使用'

    item.itemmodtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    item.save()
    return render(request, 'item_detail.html', {'item': item})


