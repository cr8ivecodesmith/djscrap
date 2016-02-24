from django.shortcuts import render

from rest_framework import serializers
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job


class JobListApi(ListAPIView):
    # Resource: /scrapyd/api/jobs/
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = (IsAuthenticated,)

    paginate_by = 10
    paginate_by_param = 'param_size'
    max_paginate = 100


class JobUpdateApi(RetrieveUpdateAPIView):
    # Resource: /scrapyd/api/jobs/:spider_id/:job_name.json
    model = Job
    serializer_class = JobSerializer
    permission_classes = (IsAuthenticated,)
    lookup_fields = ('spider__id', 'name')
