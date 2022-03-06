from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from reviews.models import Categorie, Comment, Genre, Review, Title

User = get_user_model()


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(
        read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'pub_date')


class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug',)
        model = Categorie


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug',)
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Categorie.objects.all(),
    )
    genre = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Genre.objects.all(),
        many=True,
    )
    rating = serializers.IntegerField(read_only=True)

    class Meta:
        fields = ('id', 'name', 'year', 'category',
                  'genre', 'description', 'rating',)
        model = Title


class TitleSerializerGet(serializers.ModelSerializer):
    category = CategorieSerializer()
    genre = GenreSerializer(many=True, required=True)
    rating = serializers.IntegerField(read_only=True)

    class Meta:
        fields = ('id', 'name', 'year', 'category',
                  'genre', 'description', 'rating')
        model = Title


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(
        read_only=True, default=serializers.CurrentUserDefault())
    title = TitleSerializer(required=False)

    class Meta:
        model = Review
        fields = ('id', 'author', 'title', 'text', 'score', 'pub_date')

    def validate(self, data):
        request = self.context.get('request')
        author = request.user
        title_id = self.context['request'].parser_context['kwargs']['title_id']
        title = get_object_or_404(Title, id=title_id)
        if (Review.objects.filter(author=author, title=title).exists()
           and request.method == 'POST'):
            raise serializers.ValidationError(
                'У вас уже есть отзыв на это произведение.')
        return super().validate(data)


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message='Пользователь с таким email уже существует!')
        ]
    )
    username = serializers.CharField(
        required=True,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message='Пользователь с таким username уже существует!'
            )
        ]
    )

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'username', 'bio', 'email', 'role'
        )


class UserEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(
        required=True,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message='Пользователь с таким email уже существует!')
        ]
    )
    username = serializers.CharField(
        required=True,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message='Пользователь с таким username уже существует!'
            )
        ]
    )

    def validate(self, data):
        if data['username'] == 'me':
            raise serializers.ValidationError(
                "Нельзя создать пользователя с указанным именем."
            )
        return data


class ConfirmationCodeSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    confirmation_code = serializers.CharField(required=True)


class SimpleUserSerializer(UserSerializer):
    class Meta:
        model = User
        read_only_fields = ('role',)
        fields = (
            'first_name', 'last_name', 'username', 'bio', 'email', 'role'
        )
