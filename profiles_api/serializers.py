from rest_framework import serializers
from profiles_api import models
class HelloSerializer(serializers.Serializer):
    """Serializers a name fiels for test our APIView"""
    name = serializers.CharField(max_length=10)
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','height','weight','age','gender','date_added','is_doctor','is_staff','password')
        extra_kwargs = {
        'password':{
        'write_only':True,
        'style':{'input_type':'password'}
        }
        }
    def create(self, validated_data):
        if (validated_data['is_doctor']==False):
            user = models.UserProfile.objects.create_user(
        email=validated_data['email'],
        name = validated_data['name'],
        height = validated_data['height'],
        weight = validated_data['weight'],
        age = validated_data['age'],
        gender = validated_data['gender'],
        is_doctor = validated_data['is_doctor'],
        password = validated_data['password']
            )
            return user
        elif (validated_data['is_doctor']==True):
            user = user = models.UserProfile.objects.create_superuser(
        email=validated_data['email'],
        name = validated_data['name'],
        height = validated_data['height'],
        weight = validated_data['weight'],
        age = validated_data['age'],
        gender = validated_data['gender'],
        is_doctor = validated_data['is_doctor'],
        password = validated_data['password']
            )
            return user
    def update(self,instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop("password")
            instance.set_password(password)
        return super().update(instance,validated_data)

class ProfileVitalsSerializer(serializers.ModelSerializer):
    """Serialises the vitals"""
    class Meta:
        model = models.ProfileVitals
        fields=('id','user_profile','heart_rate','spo2','breathing_rate','blood_pressure','is_evaluated','assign_to','date_added')
        extra_kwargs = {'user_profile':{'read_only':True}}
class ActualVitalsSerializer(serializers.ModelSerializer):
    """Serialises the actual vitals"""
    class Meta:
        model = models.ActualVitals
        fields=('id','user_profile','heart_rate','spo2','breathing_rate','blood_pressure','equipment','comments','date_added')
        extra_kwargs = {'user_profile':{'read_only':True}}
