from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_alter_product_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]