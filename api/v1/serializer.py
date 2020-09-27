from django.contrib.auth.models import User, Group
from dynamic_rest.serializers import DynamicModelSerializer
from dynamic_rest.fields import DynamicRelationField

class UserSerializer(DynamicModelSerializer):
  groups = DynamicRelationField('GroupSerializer', many=True, deferred=True)

  class Meta:
    model = User
    deferred_fields = ['user_permissions']
    exclude = ['password', 'last_login', 'is_superuser', 'is_staff']

class GroupSerializer(DynamicModelSerializer):
  class Meta:
    model = Group
    deferred_fields = ['permissions']
    exclude = []
