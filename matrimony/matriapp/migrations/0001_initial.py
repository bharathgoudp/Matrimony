# Generated by Django 2.2.6 on 2020-01-29 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ag', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ageto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agto', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Castee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cst', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Cityy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cty', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Countryy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuntry', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Heightt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hgt', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='MotherTonguee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locallang', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Raasii',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rasi', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Religionn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relig', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Starr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chukka', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Statee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stat', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Subcastee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcst', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Weightt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wght', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Matridata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=25)),
                ('CreateProfile', models.CharField(max_length=20)),
                ('Gender', models.CharField(max_length=15)),
                ('Mobile', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('Dosham', models.CharField(max_length=20)),
                ('MaritalStatus', models.CharField(max_length=25)),
                ('NoofChildren', models.CharField(max_length=20)),
                ('FamilyStatus', models.CharField(max_length=20)),
                ('FamilyType', models.CharField(max_length=20)),
                ('FamilyValues', models.CharField(max_length=25)),
                ('AnyDisability', models.CharField(max_length=25)),
                ('HighestEducation', models.CharField(max_length=30)),
                ('Occupation', models.CharField(max_length=25)),
                ('Bodytype', models.CharField(max_length=25)),
                ('Educationdetail', models.CharField(max_length=35)),
                ('Occupationdetail', models.CharField(max_length=35)),
                ('Eatinghabit', models.CharField(max_length=35)),
                ('Drinkinghabit', models.CharField(max_length=35)),
                ('Birthtime', models.DateTimeField()),
                ('Fatherstatus', models.CharField(max_length=30)),
                ('Motherstatus', models.CharField(max_length=30)),
                ('NoofBrothers', models.CharField(max_length=20)),
                ('Brothersmarried', models.CharField(max_length=25)),
                ('NoofSisters', models.CharField(max_length=25)),
                ('Sistersmarried', models.CharField(max_length=30)),
                ('Familylocation', models.CharField(max_length=30)),
                ('Contactno', models.IntegerField()),
                ('Ancestralorigin', models.CharField(max_length=30)),
                ('Hobbies_interes', models.CharField(max_length=500)),
                ('hobothers', models.CharField(max_length=50)),
                ('FavouriteMusic', models.CharField(max_length=50)),
                ('favOthers', models.CharField(max_length=50)),
                ('Sportsfi', models.CharField(max_length=50)),
                ('sportOthers', models.CharField(max_length=50)),
                ('spokenLang', models.CharField(max_length=50)),
                ('langothers', models.CharField(max_length=50)),
                ('Matritalstatus', models.CharField(max_length=50)),
                ('Have_childeren', models.CharField(max_length=50)),
                ('prefredheigth', models.CharField(max_length=50)),
                ('Physical_status', models.CharField(max_length=50)),
                ('Eatinghabits', models.CharField(max_length=50)),
                ('Drinkinghabits', models.CharField(max_length=50)),
                ('Smokinghabit', models.CharField(max_length=50)),
                ('kujaDosham', models.CharField(max_length=50)),
                ('Agefrom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matriapp.Agee')),
                ('Ageto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matriapp.Ageto')),
                ('Caste', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matriapp.Castee')),
                ('Height', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matriapp.Heightt')),
                ('MotherTongue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matriapp.MotherTonguee')),
                ('Pobcity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matriapp.Cityy')),
                ('Pobcountry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matriapp.Countryy')),
                ('Pobstate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matriapp.Statee')),
                ('Raasi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matriapp.Raasii')),
                ('Religion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matriapp.Religionn')),
                ('Star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matriapp.Starr')),
                ('Subcaste', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matriapp.Subcastee')),
                ('Weight', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matriapp.Weightt')),
            ],
        ),
    ]
