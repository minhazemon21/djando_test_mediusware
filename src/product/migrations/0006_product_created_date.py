from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_alter_productvariant_variant'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]