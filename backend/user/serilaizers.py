from rest_framework import serializers
from .models import Profile
from investment.serilaizers import InvestmentSerializer

class ProfileSerializers(serializers.ModelSerializer):
    investments = InvestmentSerializer(many=True, required=False)

    class Meta:
        model= Profile
        fields = ('id', 'username', 'password', 'email', 'investments')
        extra_kwargs = {
            'password': {'write_only':True}
        }