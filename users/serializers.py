from rest_framework import serializers
from users.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email','dept',
                  'mobileNumber', 'designation', 'degree', 'year', 'alternateEmail',
                  'subSystem', 'presentSystem', 'Experience',
                  'topicWorkingOn', 'profilePic', 'hobbies', 'softwaresKnown')
        read_only_fields = ('id', 'username', 'designation')

    # def to_representation(self, instance):
    #     response = super(UserSerializer, self).to_representation(instance)
    #     fields_to_pop = ['id', 'mobileNumber', 'alternateEmail']
    #     if instance.username != self.context['request'].user:
    #         response = [response.pop(field, '') for field in fields_to_pop]
    #     return response

#Serializer to Register User
class RegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2',
              'designation')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        return attrs
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            designation=validated_data['designation']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
