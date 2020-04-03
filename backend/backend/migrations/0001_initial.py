# Generated by Django 3.0.4 on 2020-04-02 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('officeName', models.CharField(max_length=20)),
                ('officeCode', models.CharField(max_length=20)),
                ('attribution', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orgCode', models.CharField(max_length=20)),
                ('orgName', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=144)),
                ('address1', models.CharField(max_length=50)),
                ('address2', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('zipcode', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serviceCode', models.CharField(max_length=20)),
                ('serviceName', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=144)),
                ('premium', models.CharField(max_length=20)),
                ('allocation', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subID', models.CharField(max_length=20)),
                ('subRequestDate', models.DateField()),
                ('subStartDate', models.DateField()),
                ('subEndDate', models.DateField()),
                ('cancelationReason', models.CharField(max_length=50)),
                ('subType', models.CharField(max_length=20)),
                ('userName', models.CharField(max_length=20)),
                ('beneficiaryID', models.CharField(max_length=20)),
                ('serviceCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='needlist.Service')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fName', models.CharField(max_length=20)),
                ('mName', models.CharField(max_length=20)),
                ('lName', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('address1', models.CharField(max_length=20)),
                ('address2', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('zipcode', models.CharField(max_length=20)),
                ('empName', models.CharField(max_length=20)),
                ('userName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='needlist.Subscriber')),
            ],
        ),
        migrations.CreateModel(
            name='TrasferredSubscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transferID', models.CharField(max_length=20)),
                ('transferFrom', models.CharField(max_length=20)),
                ('transferTo', models.CharField(max_length=20)),
                ('requestDate', models.CharField(max_length=20)),
                ('transferDate', models.CharField(max_length=20)),
                ('subID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='needlist.Subscriber')),
            ],
        ),
        migrations.CreateModel(
            name='SubscriptionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='needlist.Subscriber')),
            ],
        ),
        migrations.CreateModel(
            name='OrganizationMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membershipStart', models.DateField()),
                ('membershipEnd', models.DateField()),
                ('nativeCountry', models.CharField(max_length=20)),
                ('citizenship', models.CharField(max_length=20)),
                ('isdelegate', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=10)),
                ('orgCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='needlist.Organization')),
                ('subID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='needlist.Subscriber')),
            ],
        ),
        migrations.CreateModel(
            name='Officer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subID', models.CharField(max_length=20)),
                ('startDate', models.DateField()),
                ('endDate', models.DateField()),
                ('officeCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='needlist.Office')),
            ],
        ),
    ]
