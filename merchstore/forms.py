from django import forms
from .models import Transaction, Product


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['amount']


class CreateProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None) 
        super().__init__(*args, **kwargs)
        
        if user:
            self.fields['owner'].disabled = True
            self.initial['owner'] = user.profile  
        

class UpdateProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['owner'].disabled = True
        if self.instance and self.instance.pk:
            if self.instance.stock == 0:
                self.instance.status = 'out of stock'
                self.initial['status'] = 'out of stock'
            else:
                self.instance.status = 'available'
                self.initial['status'] = 'available'
