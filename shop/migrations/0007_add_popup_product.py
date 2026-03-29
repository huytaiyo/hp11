# Generated manually to add product relation to Popup
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_popup'),
    ]

    operations = [
        migrations.AddField(
            model_name='popup',
            name='product',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='popups',
                to='shop.product',
                help_text='Chọn sản phẩm để chuyển đến khi bấm MUA NGAY',
            ),
        ),
    ]
