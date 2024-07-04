from rest_framework import serializers

from logistic.models import Product, StockProduct, Stock


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['address', 'positions']

    def create(self, validated_data):

        positions = validated_data.pop('positions')

        stock = super().create(validated_data)

        for item in positions:
            position = StockProduct(
                stock=stock,
                product=item['product'],
                quantity=item['quantity'],
                price=item['price']
            )
            position.save()

        return stock

    def update(self, instance, validated_data):

        positions = validated_data.pop('positions')

        stock = super().update(instance, validated_data)

        for item in positions:
            StockProduct.objects.update_or_create(
                stock=stock,
                product=item['product'],
                defaults={
                    'quantity': item['quantity'],
                    'price': item['price']
                }

            )

        return stock
