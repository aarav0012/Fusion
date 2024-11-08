# Generated by Django 3.1.5 on 2024-10-12 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iwdModuleV2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pageonedetails',
            name='page_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='iwdModuleV2.projects'),
        ),
        migrations.AddField(
            model_name='pagethreedetails',
            name='page_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='iwdModuleV2.projects'),
        ),
        migrations.AddField(
            model_name='pagetwodetails',
            name='page_id',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='iwdModuleV2.projects'),
        ),
        migrations.AlterField(
            model_name='addendum',
            name='key',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='iwdModuleV2.projects'),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='key',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='iwdModuleV2.projects'),
        ),
        migrations.AlterField(
            model_name='corrigendumtable',
            name='key',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='iwdModuleV2.projects'),
        ),
        migrations.AlterField(
            model_name='financialbiddetails',
            name='key',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='iwdModuleV2.projects'),
        ),
        migrations.AlterField(
            model_name='letterofintentdetails',
            name='key',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='iwdModuleV2.projects'),
        ),
        migrations.AlterField(
            model_name='nooftechnicalbidtimes',
            name='key',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='iwdModuleV2.projects'),
        ),
        migrations.AlterField(
            model_name='pageonedetails',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='pagethreedetails',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='pagetwodetails',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='prebiddetails',
            name='key',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='iwdModuleV2.projects'),
        ),
        migrations.AlterField(
            model_name='technicalbiddetails',
            name='key',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='iwdModuleV2.projects'),
        ),
        migrations.AlterField(
            model_name='workorderform',
            name='key',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='iwdModuleV2.projects'),
        ),
    ]
