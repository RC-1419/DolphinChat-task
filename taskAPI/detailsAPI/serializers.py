from rest_framework import serializers

class userDetailsSerializer(serializers.Serializer):
    firstname = serializers.CharField(required= True)
    lastname = serializers.CharField(default= '')
    email = serializers.CharField(required= True)
    address1 = serializers.CharField(required= True)
    address2 = serializers.CharField(default= '')
    address3 = serializers.CharField(default= '')
    class Meta:
        fields = '__all__'