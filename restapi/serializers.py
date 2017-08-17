from rest_framework import serializers
from .models import MassProject, MassProjectReport

class MassProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = MassProject
        fields = '__all__'

class MassProjectReportSerializer(serializers.ModelSerializer):

    class Meta:
        model = MassProjectReport
        fields = ('id', 'e_sent', 'initial', 'subscribed', 'unsubscribed', 'bounced', 'mozart_rows', 'e_sent_today', 'e_sent_week', 'e_sent_month', 'freq_0', 'freq_1m', 'freq_3m', 'freq_6m', 'freq_recu_4m', 'project_id', 'created_at')
