# Generated by Django 3.2.18 on 2023-05-12 15:37

import core.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0013_auto_20230317_1534'),
        ('medical', '0003_mutations'),
        ('medical_pricelist', '0002_itemspricelistmutation_servicespricelistmutation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemspricelist',
            old_name='item_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='servicespricelist',
            old_name='service_name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='itemspricelist',
            name='location',
            field=models.ForeignKey(blank=True, db_column='LocationId', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='location.location'),
        ),
        migrations.AddField(
            model_name='itemspricelist',
            name='uuid',
            field=models.CharField(db_column='PLItemUUID', default=uuid.uuid4, max_length=36, unique=True),
        ),
        migrations.AddField(
            model_name='itemspricelistdetail',
            name='item',
            field=models.ForeignKey(db_column='ItemID', on_delete=django.db.models.deletion.CASCADE, related_name='pricelist_details', to='medical.item'),
        ),
        migrations.AddField(
            model_name='itemspricelistdetail',
            name='items_pricelist',
            field=models.ForeignKey(db_column='PLItemID', on_delete=django.db.models.deletion.CASCADE, related_name='details', to='medical_pricelist.itemspricelist'),
        ),
        migrations.AddField(
            model_name='servicespricelist',
            name='location',
            field=models.ForeignKey(blank=True, db_column='LocationId', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='location.location'),
        ),
        migrations.AddField(
            model_name='servicespricelist',
            name='uuid',
            field=models.CharField(db_column='PLServiceUUID', default=uuid.uuid4, max_length=36, unique=True),
        ),
        migrations.AddField(
            model_name='servicespricelistdetail',
            name='service',
            field=models.ForeignKey(db_column='ServiceID', on_delete=django.db.models.deletion.CASCADE, related_name='pricelist_details', to='medical.service'),
        ),
        migrations.AddField(
            model_name='servicespricelistdetail',
            name='services_pricelist',
            field=models.ForeignKey(db_column='PLServiceID', on_delete=django.db.models.deletion.CASCADE, related_name='details', to='medical_pricelist.servicespricelist'),
        ),
        migrations.AlterField(
            model_name='itemspricelist',
            name='validity_from',
            field=core.fields.DateTimeField(db_column='ValidityFrom', default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='itemspricelistdetail',
            name='validity_from',
            field=core.fields.DateTimeField(db_column='ValidityFrom', default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='servicespricelist',
            name='validity_from',
            field=core.fields.DateTimeField(db_column='ValidityFrom', default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='servicespricelistdetail',
            name='validity_from',
            field=core.fields.DateTimeField(db_column='ValidityFrom', default=datetime.datetime.now),
        ),
    ]