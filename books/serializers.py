from rest_framework import serializers
from .models import Book
from django.core.exceptions import ValidationError


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model=Book
        fields=('title', 'subtitle', 'content', 'author', 'isbn', 'price')

    def validate(self, data):
        title=data.get('title', None)
        author=data.get('author', None)

        if title.isdigit():
            raise ValidationError({
                'status':False,
                "message": "kitob sarlavhasi raqamlardan tashkil topgan bolishi mumkin."
                }
            )
            # return data
        if Book.objects.filter(title=title, author=author):
            raise ValidationError({
                'status':False,
                "message": "kitob sarlavhasi va muallifi allaqachon bazada bor."
                }
            )
        return data
    
    # def validate_price(self, price):
    #     if price<0 or price>9999999999:
    #         raise ValidationError({
    #             'status':False,
    #             "message": "noto'g'ri narx kiritilgan"
    #             }
    #         )

    #autentifikatsiya
    #basic authentication-eskirgan, xavfli, 
    #session authentication-cookie yordamida eslab qoladi bir marta kirgan foydalanuvchini, faqat brauzerda ishlaydi.
    #token authentication-


        