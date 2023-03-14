from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response


from forms.models import LeaveForm, InventoryForm, FineSheetForm
from forms.serializers import LeaveFormSerializer, InventoryFormSerializer, FineSheetFormSerializer


from forms.permissions import IsHead

class LeaveFormViewSet(viewsets.ModelViewSet):
    queryset = LeaveForm.objects.all()
    serializer_class = LeaveFormSerializer
    permission_classes = [IsAuthenticated]

class InventoryFormViewSet(viewsets.ModelViewSet):
    queryset = InventoryForm.objects.all()
    serializer_class = InventoryFormSerializer
    permission_classes = [IsAuthenticated, IsHead]

class FineSheetFormViewSet(viewsets.ModelViewSet):
    queryset = FineSheetForm.objects.all()
    serializer_class = FineSheetFormSerializer
    permission_classes = [IsAuthenticated]

class VerifyFormsRequest(viewsets.ViewSet):

    def list(self, request):
        queryset1 = LeaveForm.objects.filter(Status='0') 
        serializer1 = LeaveFormSerializer(queryset1, many=True)
        queryset2 = InventoryForm.objects.filter(Status='0')
        serializer2 = InventoryFormSerializer(queryset2, many=True)
        queryset3 = FineSheetForm.objects.filter(Status='2')
        serializer3 = FineSheetFormSerializer(queryset3, many=True)
        return Response(serializer1.data, serializer2.data, serializer3.data)
        
    def update(self, request, pk=None):
        form_type = request.data['form_type']
        form_id = request.data['form_id']
        status = request.data['status']
        if form_type == 'LeaveForm':
            queryset = LeaveForm.objects.filter(id=form_id)
        
        elif form_type == 'InventoryForm':
            queryset = InventoryForm.objects.filter(id=form_id)

        elif form_type == 'FineSheetForm':
            queryset = FineSheetForm.objects.filter(id=form_id)

        else:
            return Response('Invalid form type')

        if status not in ['1', '2']:
            return Response('Invalid status')

        queryset.update(Status=status)
        return Response('Form updated successfully')