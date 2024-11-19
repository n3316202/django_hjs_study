from rest_framework import serializers

from todo.models import Todo

class TodoSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True) #user 를 무시한다.
    class Meta:
        model = Todo
        fields = "__all__"

