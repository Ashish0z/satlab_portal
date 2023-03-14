from rest_framework import serializers
from forms.models import LeaveForm, FineSheetForm, InventoryForm
from datetime import date
from django.contrib.auth import get_user_model

class LeaveFormSerializer(serializers.ModelSerializer):
    SATLAB_USER = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())
    MeetingDate = serializers.DateField(format="%d-%m-%Y")
    Date = serializers.DateField(format="%d-%m-%Y")
    class Meta:
        model = LeaveForm
        fields = ('SATLAB_USER', 'Date', 'Comments', 'Status', 'MeetingDate', 'MeetingType', 'Reason')
        read_only_fields = ('SATLAB_USER', 'Date', 'Status')

    def create(self, validated_data, request):
        Leave = LeaveForm.objects.create(
            SATLAB_USER = self.context['request'].user,
            Date = date.today(),
            Comments = validated_data['Comments'],
            Status = '0',
            MeetingDate = validated_data['MeetingDate'],
            MeetingType = validated_data['MeetingType'],
            Reason = validated_data['Reason']
        )
        Leave.save()
        return Leave

class FineSheetFormSerializer(serializers.ModelSerializer):
    SATLAB_USER = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())
    Date = serializers.DateField(format="%d-%m-%Y")
    MeetingDate = serializers.DateField(format="%d-%m-%Y")
    MembersFined = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all(), many=True)

    class Meta:
        model = FineSheetForm
        fields = ('SATLAB_USER', 'Date', 'Comments', 'Status', 'FineSheetAmount',
        'FineSheetReason', 'MembersFined', 'MeetingDate', 'MeetingType')
        read_only_fields = ('SATLAB_USER', 'Date', 'Status')
    
    def create(self, validated_data, request):
        FineSheet = FineSheetForm.objects.create(
            SATLAB_USER = self.context['request'].user,
            Date = date.today(),
            Comments = validated_data['Comments'],
            Status = '2',
            FineSheetAmount = validated_data['Fine'],
            FineSheetReason = validated_data['Reason'],
            MembersFined = validated_data['Members'],
            MeetingDate = validated_data['MeetingDate'],
            MeetingType = validated_data['MeetingType']
        )
        FineSheet.save()
        return FineSheet


class InventoryFormSerializer(serializers.ModelSerializer):
    SATLAB_USER = serializers.PrimaryKeyRelatedField(queryset=get_user_model().objects.all())
    Date = serializers.DateField(format="%d-%m-%Y")
    class Meta:
        model = InventoryForm
        fields = ('SATLAB_USER', 'Date', 'Comments', 'Status', 'EquipmentName',
        'EquipmentQuantity', 'EquipmentDescription', 'EquipmentType', 'EquipmentPrice',
        'Purpose', 'VendorDetails', 'ProjectName', 'SubSystemName')
        read_only_fields = ('SATLAB_USER', 'Date', 'Status')

    def create(self, validated_data, request):
        Inventory = InventoryForm.objects.create(
            SATLAB_USER = self.context['request'].user,
            Date = date.today(),
            Comments = validated_data['Comments'],
            Status = '0',
            EquipmentName = validated_data['EquipmentName'],
            EquipmentQuantity = validated_data['EquipmentQuantity'],
            EquipmentDescription = validated_data['EquipmentDescription'],
            EquipmentType = validated_data['EquipmentType'],
            EquipmentPrice = validated_data['EquipmentPrice'],
            Purpose = validated_data['Purpose'],
            VendorDetails = validated_data['VendorDetails'],
            ProjectName = validated_data['ProjectName'],
            SusSystemName = validated_data['SusSystemName']
        )
        Inventory.save()
        return Inventory

