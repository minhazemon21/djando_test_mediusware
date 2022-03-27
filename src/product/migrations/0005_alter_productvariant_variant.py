from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_productvariant_product_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productvariant',
            name='variant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_variant', to='product.variant'),
        ),
    ]