

class BaseService:
    
    @classmethod
    def get_by_id(cls,id):
        product = cls.model.objects.filter(id=id)[0]
        return product
    @classmethod
    def get_name_by_id(cls,id):
        name = cls.model.objects.filter(id=id).values_list('name', flat=True).first()
        return name
    
    @classmethod
    def get_all(cls):
        return cls.model.objects.all()