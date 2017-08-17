# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import MassProject, MassProjectReport
from .serializers import MassProjectSerializer, MassProjectReportSerializer
from rest_framework import generics

class MassProjectList(APIView):

    def get(self, request):
        massProjects = MassProject.objects.all()
        serializer = MassProjectSerializer(massProjects, many=True)
        return Response(serializer.data)

    def post(self):
        pass


class MassProjectReportList(generics.ListAPIView):
    #
    # def get(self, request):
    #     # massProjectReports = MassProjectReport.objects.all()
    #     massProjectReports = MassProjectReport.objects.all()
    #     serializer = MassProjectReportSerializer(massProjectReports, many=True)
    #     return Response(serializer.data)
    #
    # def post(self):
    #     pass
    serializer_class = MassProjectReportSerializer

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        return MassProjectReport.objects.filter(project_id=project_id)
