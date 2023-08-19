
from rest_framework import serializers
## token sserializers

from . models import (
    JobUser,
    UserSkill,
    UserProfile,
    Company,
    Application,
    Job,
    Industry,
    Skill,
    Experience
)

class JobUserSerizlizer(serializers.ModelSerializer):
    class Meta:
        model = JobUser
        fields = ['id','email','password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = JobUser (
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()

        return user



class ApplicationSerizlizer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = "__all__"

class JObSerializer(serializers.ModelSerializer):
    applications = ApplicationSerizlizer(many=True,read_only=True)
    class Meta:
        model = Job
        fields = ['title','company','location','description','requirements','application_deadline','created_at','applications']


class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = "__all__"


class CompanySerializer(serializers.ModelSerializer):
    jobs = JObSerializer(many=True,read_only=True)
    class Meta:
        model = Company
        fields =['name','industry','headquarters','website','jobs']

class SkillSerizlizer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"

class UserSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSkill
        fields = '__all__'

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = "__all__"


class UserProfileSerializer(serializers.ModelSerializer):
    skills = UserSkillSerializer(many=True,read_only=True)
    experience =  ExperienceSerializer(many=True,read_only=True)
    applications = ApplicationSerizlizer(many=True,read_only=True)
    class Meta:
        model = UserProfile
        fields = ['user','image','banner','headline','about','skill','skills','experience','applications']







class TokenObtainPairResponseSerializer(serializers.Serializer):
    access = serializers.CharField()
    refresh = serializers.CharField()

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()
    


class TokenRefreshResponseSerializer(serializers.Serializer):
    access = serializers.CharField()

    def create(self, validated_data):
        raise NotImplementedError()

    def update(self, instance, validated_data):
        raise NotImplementedError()   