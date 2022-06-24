from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status

from post.serializers import JobPostSerializer
from .models import (
    JobPostSkillSet,
    JobType,
    JobPost,
    Company
)
from django.db.models.query_utils import Q


class SkillView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        skills = self.request.query_params.getlist('skills', '')
        print("skills = ", end=""), print(skills)

        return Response(status=status.HTTP_200_OK)


class JobView(APIView):

    def post(self, request):
        job_type = int( request.data.get("job_type", None) )
        company_name = request.data.get("company_name", None)
        jobpost_serializer = JobPostSerializer(data=request.data)
        
        if jobpost_serializer.is_valid():
            jobpost_serializer.save()
            return Response(jobpost_serializer,status=status.HTTP_200_OK)
        
        return Response(jobpost_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
            
    
    def get(self, request):
        # job_type = request.data.get("job_type", None)
        # company_name = request.data.get("company_name", None)
        company = Company.objects.all()
        jobpost_serializer = JobPostSerializer(company, many=True).data
        

        return Response(jobpost_serializer,status=status.HTTP_200_OK)

