# Generated by Django 2.1.5 on 2019-03-05 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_simulasi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Peminjaman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_barang', models.CharField(max_length=255)),
                ('no_seri', models.CharField(max_length=255)),
                ('kondisi_barang', models.CharField(max_length=255)),
                ('id_karyawan', models.CharField(max_length=255)),
                ('tanggal_pinjam', models.CharField(max_length=255)),
                ('tanggal_kembali', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
            ],
        ),
    ]
