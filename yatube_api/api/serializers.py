from rest_framework import serializers

from posts.models import Comment, Follow, Group, Post, User
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CurrentUserDefault
from rest_framework.validators import UniqueTogetherValidator

already_follow = 'Вы уже подписаны на этого пользователя.'
cannot_follow_yourself = 'Нельзя подписаться на себя'


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True
    )

    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
        default=CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )
    validators = UniqueTogetherValidator(
        queryset=Follow.objects.all(),
        fields=('user', 'following',),
        message=already_follow,
    ),

    def validate(self, data):
        if self.context['request'].user == data['following']:
            raise ValidationError(
                cannot_follow_yourself
            )
        return data

    class Meta:
        model = Follow
        fields = '__all__'
