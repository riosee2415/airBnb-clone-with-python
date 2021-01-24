# Generated by Django 2.2.5 on 2021-01-24 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210124_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='프로필사진'),
        ),
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, default='', verbose_name='사용자정보'),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthdate',
            field=models.DateField(blank=True, null=True, verbose_name='생년월일'),
        ),
        migrations.AlterField(
            model_name='user',
            name='currency',
            field=models.CharField(blank=True, choices=[('usd', 'USD'), ('krw', 'KRW')], max_length=5, null=True, verbose_name='화폐유형'),
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10, null=True, verbose_name='성별'),
        ),
        migrations.AlterField(
            model_name='user',
            name='language',
            field=models.CharField(blank=True, choices=[('ENG', 'English'), ('KOR', 'Korean')], max_length=5, null=True, verbose_name='언어유형'),
        ),
        migrations.AlterField(
            model_name='user',
            name='superhost',
            field=models.BooleanField(default=False, verbose_name='호스트권한'),
        ),
    ]