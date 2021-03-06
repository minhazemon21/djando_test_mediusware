from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('sku', models.SlugField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variant', models.CharField(max_length=255)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('variant_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.variant')),
            ],
        ),
        migrations.CreateModel(
            name='ProductVariantPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('stock', models.FloatField()),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('product_variant_one', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_variant_one', to='product.productvariant')),
                ('product_variant_three', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_variant_three', to='product.productvariant')),
                ('product_variant_two', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_variant_two', to='product.productvariant')),
            ],
        ),
    ]