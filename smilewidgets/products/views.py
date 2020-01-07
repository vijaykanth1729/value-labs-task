from django.shortcuts import render
from rest_framework import generics
from .models import ProductPrice, GiftCard, Product
from .serializers import ProductPriceSerializer
from datetime import datetime, timedelta
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class ProductPriceView(generics.GenericAPIView):
    queryset = ProductPrice.objects.all()
    serializer_class = ProductPriceSerializer

    def get(self, request, *args, **kwargs):
        product_code = request.query_params.get("productCode")
        date = request.query_params.get("date")
        gift_card_code = request.query_params.get("giftCardCode", None)
        req_date = datetime.strptime(date, "%Y-%m-%d")
        black_friday_start = datetime(2018, 11, 23)

        if black_friday_start <= req_date <= black_friday_start + timedelta(days=3):
            name = "black_friday"
        elif req_date >= datetime(2019, 1, 1):
            name = "from2019"
        else:
            name = "default"
        price_obj = get_object_or_404(ProductPrice, name=name, product__code=product_code)
        price = price_obj.price
        discount_amount = 0
        if gift_card_code:
            gift = GiftCard.objects.filter(code=gift_card_code, date_start__lte=req_date)
            if gift:
                discount_amount = gift.first().amount
        print(price, discount_amount)
        res = "$" + str((price - discount_amount) / 100)
        return Response({"result": {"product price": res}}, status=200)


    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        product_prices = self.get_queryset()

        product_price = product_prices.filter(
            date_start__lte=serializer.validated_data.get('date'),
            date_end__gte=serializer.validated_data.get('date')) \
            .filter(product__code=serializer.validated_data.get('productCode')).first()

        if product_price is not None:
            price = product_price.price
            if serializer.validated_data.get('giftCardCode') is not None:
                gift_card = GiftCard.objects.get(code=serializer.validated_data.get('giftCardCode'))
                price -= gift_card.amount
        else:
            price = Product.objects.get(code=serializer.validated_data.get('productCode')).price

        return Response({'price': price})



