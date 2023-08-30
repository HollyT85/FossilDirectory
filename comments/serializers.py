from rest_framework import serializers
from .models import RockComments


class RockCommentSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = RockComments
        fields = [
            'id', 'owner', 'rock_post', 'created_at', 'updated_at',
            'comment', 'is_owner', 'profile_id', 'profile_image'
        ]


class RockCommentDetailSerializer(RockCommentSerializer):

    rock = serializers.ReadOnlyField(source='rock.id')