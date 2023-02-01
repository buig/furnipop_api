from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnipop_api', '0021_itemspedidos_ida_lotespedidos_ida'),
    ]

    operations = [
        migrations.RunSQL(
            "update items_pedidos set idA=pedido_id where 1 = 1",
            reverse_sql= 
            "update items_pedidos set idA= null where 1 = 1",
            
        ),
        migrations.RunSQL(
            "update lotes_pedidos set idA=lote_id where 1 = 1",
            reverse_sql= 
            "update lotes_pedidos set idA=null where 1 = 1"
        )
    ]
