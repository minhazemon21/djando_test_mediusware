from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_product_created_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productimage',
            name='file_path',
        ),
        migrations.AddField(
            model_name='productimage',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]