from django.shortcuts import render, get_object_or_404
import urllib.request
import urllib.parse
import json
from .models import *

def samplePack_details(request, pk):
  # Get specified sample pack.
  request_samples = urllib.request.Request('models-api:8000/samples_in_packs', method='GET')
  request_pack = urllib.request.Request('models-api:8000/sample_packs' + pk)
  json_samples = urllib.request.urlopen(request_samples).read().decode('utf-8')
  json_pack = urllib.request.urlopen(request_pack).read().decode('utf-8')

  # We're processing a pack and all the samples in it, so
  # how do we treat this in our experience layer? Do we have
  # two JsonResponses for two separate views, and include the
  # sample views in the pack view?
  data = {
    'pack': pack,
    'samples': samples_ordered
  }

  return render(request, data)


def home(request, template_name='home.html'):
  top_packs = urllib.request.Request('models-api:8000/top5_packs')
  serializer = SamplePackSerializer(top_packs)
  return JsonResponse(serializer.data)
