from rest_framework import serializers
from .models import Customer, Investment, Stock, MutualFund
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
            model = Customer
            fields = ('pk','name', 'address', 'cust_number', 'city', 'state', 'zipcode', 'email', 'email', 'cell_phone')

class InvestmentSerializer(serializers.ModelSerializer):

    class Meta:
            model = Investment
            fields = ('pk','customer','cust_number', 'category', 'description', 'acquired_value', 'acquired_date', 'recent_value', 'recent_date')


class StockSerializer(serializers.ModelSerializer):

    class Meta:
            model = Stock
            fields = ('pk','customer', 'cust_number', 'symbol', 'name', 'shares', 'purchase_price', 'purchase_date')


class MutualFundSerializer(serializers.ModelSerializer):

    class Meta:
            model = MutualFund
            fields = ('pk','customer', 'cust_number', 'symbol','name','description','purchase_price', 'purchase_date','recent_value', 'recent_date')