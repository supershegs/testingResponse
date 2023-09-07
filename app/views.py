from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from django.utils.decorators import method_decorator

from .c_date import current_day_of_week,formatted_utc_time


# Create your views here.

class ResponseView(APIView):

    @method_decorator(name='get', decorator=swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter('slack_name', openapi.IN_QUERY, description="Slack Name", type=openapi.TYPE_STRING),
            openapi.Parameter('track', openapi.IN_QUERY, description="Track", type=openapi.TYPE_STRING),
        ],
        responses={
            status.HTTP_200_OK: openapi.Response(
                "Success response",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'slack_name': openapi.Schema(type=openapi.TYPE_STRING),
                        'current_day': openapi.Schema(type=openapi.TYPE_STRING),
                        "utc_time": openapi.Schema(type=openapi.TYPE_STRING),
                        'track': openapi.Schema(type=openapi.TYPE_STRING),
                        "github_file_url": openapi.Schema(type=openapi.TYPE_STRING),
                        "github_repo_url": openapi.Schema(type=openapi.TYPE_STRING),
                        "status_code": openapi.Schema(type=openapi.TYPE_NUMBER),
                    },
                ),
            ),
            status.HTTP_400_BAD_REQUEST: openapi.Response("Bad request", 
                schema=openapi.Schema(type=openapi.TYPE_OBJECT,
                properties={'error': openapi.Schema(type=openapi.TYPE_STRING),}
                )),
        },
    ))
    def get(self, request):
        slack_name = request.query_params.get('slack_name')
        track = request.query_params.get('track')
        if slack_name is None or track is None:
            slack_name = request.data.get('slack_name')
            track = request.data.get('track')
        
        if slack_name is None or track is None:
            return Response({'error': 'Both slack_name and track parameters are required.'}, status=400)

        response_data = {
            'slack_name': slack_name,
            'current_day': current_day_of_week,
            "utc_time": formatted_utc_time,
            'track': track,
            "github_file_url": "https://github.com/username/repo/blob/main/file_name.ext",
            "github_repo_url": "https://github.com/username/repo",
            "status_code": 200,
        }

        return Response(response_data)
