from rest_framework import serializers

from post.models import Company as CompanyModel
from post.models import JobPost as JobPostModel
from post.models import JobPostSkillSet as JobPostSkillSetModel


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyModel
        fields = '__all__'
        

class JobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPostModel
        fields = ["job_type", "company", 
                  "job_description", "salary"]
        
        
class JobPostSkillSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPostSkillSetModel
        fields = "__all__"
    
        