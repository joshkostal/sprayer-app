from django.contrib.auth.models import User, Group
from rest_framework import serializers

from sprayer.models import Spray, SprayApplication, Owner, Field, FieldSeason


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class SpraySerializer(serializers.HyperlinkedModelSerializer):
    # This is for being able to see the user_id in the request and not be able to set it
    # user = serializers.PrimaryKeyRelatedField(
    #     read_only=True,
    #     default=serializers.CurrentUserDefault()
    # )

    # This does not show the user in the request
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )

    id = serializers.ReadOnlyField()

    class Meta:
        model = Spray
        fields = ('id', 'name', 'user')


class SprayApplicationSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = SprayApplication
        fields = ('cost', 'amount', 'date', 'spray', 'field_season')


class OwnerSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.UUIDField(required=False)

    class Meta:
        model = Owner
        fields = ('id', 'name')


class FieldSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer()
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
    )
    id = serializers.ReadOnlyField()

    class Meta:
        model = Field
        fields = ('id', 'name', 'owner', 'user')

    def create(self, validated_data):
        owner_data = validated_data.pop('owner')
        if 'id' in owner_data.keys():
            if Owner.objects.filter(id=owner_data['id']).exists():
                owner = Owner.objects.get(id=owner_data['id'])
            else:
                owner = Owner.objects.create(name=owner_data['name'])
        else:
            owner = Owner.objects.create(name=owner_data['name'])

        instance = Field.objects.create(**validated_data, owner=owner)
        return instance


class FieldSeasonSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = FieldSeason
        fields = ('crop_type', 'num_acres', 'start_date', 'end_date', 'field')
