from policy.models import Policy
from rest_framework import serializers
class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = ('id','policy_name', 'start_date', 'end_date', 'life_assureddetails', 'payment_information', 'premium_details')
