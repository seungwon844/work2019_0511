from django.shortcuts import render
from django.http import HttpResponse
import re
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
import requests
from PIL import Image, ImageDraw, ImageFont
import pandas as pd                           # 엑셀 요청 처리
from io import BytesIO
from urllib.parse import quote
from django.views.generic import CreateView, UpdateView
from django.db import models
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from blog.models import Post
from shop.models import Item
from django.http import HttpResponse
from itertools import chain

# def post_list_latest(request):
#     latest = Post.objects.all().order_by('-updated_at')[:3]
#     return render(request, 'home/post_list_latest.html',
#                       {'post_list_latest': latest})
#
# def expensive_item(request):
#     ex = Item.objects.all().order_by('-price')[:3]
#     return render(request, 'home/expensive_item.html',
#                   {'expensive_item':ex})

def result_list(request):
    rs = list(chain(Post.objects.all().order_by('-updated_at')[:3], Item.objects.all().order_by('-price')[:3]))
    return render(request, 'home/result_list.html',
                      {'result_list': rs})


# def index(request):
#     return render(request, 'home/index.html')


