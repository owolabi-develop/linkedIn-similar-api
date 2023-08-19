from django.shortcuts import render

# Create your views here.
from rest_framework import filters
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import status
from . serializers import (
     TokenObtainPairResponseSerializer,
    TokenRefreshResponseSerializer,
)
from drf_spectacular.utils import extend_schema
# Create your views here.
from rest_framework import viewsets,permissions,parsers
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

from .serializers import (
    JObSerializer,
    JobUserSerizlizer,
    ApplicationSerizlizer,
    UserSkillSerializer,
    SkillSerizlizer,
    ExperienceSerializer,
    CompanySerializer,
    IndustrySerializer,
    UserProfileSerializer
)

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    permission_classes =[permissions.IsAuthenticated]

    @extend_schema(tags=["UserProfile"],summary='create new user_profile')
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @extend_schema(tags=["UserProfile"],summary='get all user_profile')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @extend_schema(tags=["UserProfile"],summary='get new user_profile by id')
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @extend_schema(tags=["UserProfile"],summary='update user_profile details')
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @extend_schema(tags=["UserProfile"],summary='partial update user_profile')
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @extend_schema(tags=["UserProfile"],summary='delete user_profile')
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class IndustryViewSet(viewsets.ModelViewSet):
    serializer_class = IndustrySerializer
    queryset = Industry.objects.all()
    permission_classes =[permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['=name']

    @extend_schema(tags=["Industry"],summary='create new industry')
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    
    
    @extend_schema(tags=["Industry"],summary='get all industry')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @extend_schema(tags=["Industry"],summary='get new industry by id')
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @extend_schema(tags=["Industry"],summary='update industry details')
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @extend_schema(tags=["Industry"],summary='partial update industry')
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @extend_schema(tags=["Industry"],summary='delete industry')
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)



class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    permission_classes =[permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['=name','=industry__name']

    @extend_schema(tags=["Company"],summary='create new company')
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @extend_schema(tags=["Company"],summary='get all company')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @extend_schema(tags=["Company"],summary='get new company by id')
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @extend_schema(tags=["Company"],summary='update company details')
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @extend_schema(tags=["Company"],summary='partial update company')
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @extend_schema(tags=["Company"],summary='delete company')
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class ExperienceViewSet(viewsets.ModelViewSet):
    serializer_class = ExperienceSerializer
    queryset = Experience.objects.all()
    permission_classes =[permissions.IsAuthenticated]

    @extend_schema(tags=["Experience"],summary='create new experience')
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @extend_schema(tags=["Experience"],summary='get all experience')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @extend_schema(tags=["Experience"],summary='get new experience by id')
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @extend_schema(tags=["Experience"],summary='update experience details')
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @extend_schema(tags=["Experience"],summary='partial update experience')
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @extend_schema(tags=["Experience"],summary='delete experience')
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class SkillViewViewSet(viewsets.ModelViewSet):
    serializer_class = SkillSerizlizer
    queryset = Skill.objects.all()
    permission_classes =[ permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['=name']

    @extend_schema(tags=["Skill"],summary='create new skill')
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @extend_schema(tags=["Skill"],summary='get all skill')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @extend_schema(tags=["Skill"],summary='get new skill by id')
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @extend_schema(tags=["Skill"],summary='update skill details')
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @extend_schema(tags=["Skill"],summary='partial update skill')
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @extend_schema(tags=["Skill"],summary='delete skill')
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    


class UserSkillViewSet(viewsets.ModelViewSet):
    serializer_class = UserSkillSerializer
    queryset = UserSkill.objects.all()
    permission_classes =[ permissions.IsAuthenticated]

    @extend_schema(tags=["UserSkill"],summary='create new user_skill')
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @extend_schema(tags=["UserSkill"],summary='get all user_skill')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @extend_schema(tags=["UserSkill"],summary='get new user_skill by id')
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @extend_schema(tags=["UserSkill"],summary='update user_skill details')
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @extend_schema(tags=["UserSkill"],summary='partial update user_skill')
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @extend_schema(tags=["UserSkill"],summary='delete user_skill')
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class JobUserViewSet(viewsets.ModelViewSet):
    serializer_class = JobUserSerizlizer
    queryset = JobUser.objects.all()
    permission_classes = [permissions.AllowAny]
    authentication_classes = []
    throttle_scope = 'users'


    @extend_schema(tags=["Auth"],summary='create new user')
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @extend_schema(tags=["Auth"],summary='get all users')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @extend_schema(tags=["Auth"],summary='get new user by id')
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @extend_schema(tags=["Auth"],summary='update user details')
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @extend_schema(tags=["Auth"],summary='partial update user details')
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @extend_schema(tags=["Auth"],summary='delete user')
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    


class JobViewSet(viewsets.ModelViewSet):
    serializer_class = JObSerializer
    queryset = Job.objects.all()
    permission_classes =[ permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['=title','=company__name','=location']

    @extend_schema(tags=["Jobs"],summary='create new job')
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @extend_schema(tags=["Jobs"],summary='get all job')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @extend_schema(tags=["Jobs"],summary='get new job by id')
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @extend_schema(tags=["Jobs"],summary='update job details')
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @extend_schema(tags=["Jobs"],summary='partial update job')
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @extend_schema(tags=["Jobs"],summary='delete job')
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    



class ApplicationsViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicationSerizlizer
    queryset = Application.objects.all()
    permission_classes =[permissions.IsAuthenticated]

    @extend_schema(tags=["Applications"],summary='create new applications')
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    @extend_schema(tags=["Applications"],summary='get all applications')
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    @extend_schema(tags=["Applications"],summary='get new application by id')
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @extend_schema(tags=["Applications"],summary='update application details')
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @extend_schema(tags=["Applications"],summary='partial update application')
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @extend_schema(tags=["Applications"],summary='delete application')
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)



class DecoratedTokenObtainPairView(TokenObtainPairView):
    @extend_schema(tags=['Auth'],summary='get token',
        responses={
            status.HTTP_200_OK: TokenObtainPairResponseSerializer,
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)



class DecoratedTokenRefreshView(TokenRefreshView):
    @extend_schema(tags=['Auth'],summary='refresh token',
        responses={
            status.HTTP_200_OK: TokenRefreshResponseSerializer,
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)