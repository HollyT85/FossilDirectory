from rest_framework import serializers
from .models import Rock

class RockSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Rock
        fields = ['id', 'owner', 'title', 'info', 'location', 'material',
        'size', 'era', 'tools', 'found', 'prepped', 'image', 'finished_image',
        'is_owner', 'profile_id', 'profile_image',
        ]