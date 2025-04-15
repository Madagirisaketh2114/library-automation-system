# Generated by Django 4.0.8 on 2023-01-07 18:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=250)),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
                ('author', models.TextField(blank=True, null=True)),
                ('publisher', models.CharField(max_length=250)),
                ('date_published', models.DateTimeField()),
                ('status', models.CharField(choices=[('1', 'Active'), ('2', 'Inactive')], default=1, max_length=2)),
                ('delete_flag', models.IntegerField(default=0)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'List of Books',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('1', 'Active'), ('2', 'Inactive')], default=1, max_length=2)),
                ('delete_flag', models.IntegerField(default=0)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'List of Categories',
            },
        ),
        migrations.CreateModel(
            name='studentregistermodels',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=100)),
                ('student_name', models.CharField(max_length=100)),
                ('student_phone', models.CharField(max_length=12)),
                ('mail_id', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=250)),
                ('first_name', models.CharField(max_length=250)),
                ('middle_name', models.CharField(blank=True, max_length=250, null=True)),
                ('last_name', models.CharField(max_length=250)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=20)),
                ('contact', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=250)),
                ('department', models.CharField(blank=True, max_length=250, null=True)),
                ('course', models.CharField(blank=True, max_length=250, null=True)),
                ('status', models.CharField(choices=[('1', 'Active'), ('2', 'Inactive')], default=1, max_length=2)),
                ('delete_flag', models.IntegerField(default=0)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'List of Students',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('1', 'Active'), ('2', 'Inactive')], default=1, max_length=2)),
                ('delete_flag', models.IntegerField(default=0)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lmsApp.category')),
            ],
            options={
                'verbose_name_plural': 'List of Categories',
            },
        ),
        migrations.CreateModel(
            name='Borrow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowing_date', models.DateField()),
                ('return_date', models.DateField()),
                ('status', models.CharField(choices=[('1', 'Pending'), ('2', 'Returned')], default=1, max_length=2)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_id_fk', to='lmsApp.books')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_id_fk', to='lmsApp.students')),
            ],
            options={
                'verbose_name_plural': 'Borrowing Transactions',
            },
        ),
        migrations.AddField(
            model_name='books',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lmsApp.subcategory'),
        ),
    ]
