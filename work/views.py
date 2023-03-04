from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import WorkSerializer
from constants import secure

import requests


class WorkAPIView(APIView):
    serializer_class = WorkSerializer

    def get(self, request):
        if "articul" in request.query_params:
            r = requests.get(secure + request.query_params['articul'])
            lst = {}
            d = r.json()['data']['products'][0]
            lst['articul'] = d['id']
            lst['nameArticul'] = d['name']
            lst['brand'] = d['brand']
            return Response({'post': lst})
