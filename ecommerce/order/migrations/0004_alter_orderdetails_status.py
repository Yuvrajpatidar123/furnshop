# Generated by Django 4.1.4 on 2023-06-03 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_orderdetails_totalprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetails',
            name='status',
            field=models.CharField(choices=[('Order has been shiped', 'Order has been shiped'), ('Your order has been recieved in the nearest to you', 'Your order has been recieved in the nearest to you'), ('Out for delivery', 'Out for delivery'), ('Dilivered', 'Dilivered')], default='Order has been placed', max_length=50),
        ),
    ]
