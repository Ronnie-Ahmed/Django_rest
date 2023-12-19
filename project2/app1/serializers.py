from rest_framework import serializers
from .models import Student

class StudentSerializers(serializers.ModelSerializer):
    # my_discount=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Student
        fields=('name','age','description','email','get_discount')
        
    # def get_name(self,obj):
    #     return obj.get_discount()