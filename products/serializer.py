from rest_framework import serializers
from .models import Category,Products,File


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title','description','avatar')
        
        
class FileSerializer(serializers.ModelSerializer):
    file_type = serializers.SerializerMethodField()
    class Meta:
        model = File
        fields = ('title','fil','file_type')
        
    def get_file_type(self,obj):
        return obj.get_file_type_display()
        

class ProductsSerializer(serializers.HyperlinkedModelSerializer):
    categories = CategorySerializer(many=True)
    file_set = FileSerializer(many= True)
    class Meta:
        model = Products
        fields = ('id','title','description','avatar','categories','url','file_set')


