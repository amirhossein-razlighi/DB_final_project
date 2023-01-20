# Generated by Django 4.1.5 on 2023-01-20 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('airlineid', models.AutoField(primary_key=True, serialize=False)),
                ('airlinename', models.CharField(blank=True, max_length=150, null=True)),
            ],
            options={
                'db_table': 'airline',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('flightnumber', models.AutoField(primary_key=True, serialize=False)),
                ('flightdate', models.DateTimeField()),
            ],
            options={
                'db_table': 'flight',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('userid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'manager',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('userid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'supervisor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('surveyid', models.AutoField(primary_key=True, serialize=False)),
                ('activationinterval', models.DateTimeField()),
                ('isactive', models.BooleanField()),
            ],
            options={
                'db_table': 'survey',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('ticketnumber', models.AutoField(primary_key=True, serialize=False)),
                ('seatnumber', models.CharField(max_length=150)),
                ('firstname', models.CharField(blank=True, max_length=150, null=True)),
                ('lastname', models.CharField(blank=True, max_length=150, null=True)),
                ('passportnumber', models.CharField(blank=True, max_length=150, null=True)),
                ('gender', models.TextField(blank=True, null=True)),
                ('price', models.FloatField()),
            ],
            options={
                'db_table': 'ticket',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('userid', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'voter',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Assistancy',
            fields=[
                ('mainmanagerid', models.OneToOneField(db_column='mainmanagerid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='surveysApp.manager')),
            ],
            options={
                'db_table': 'assistancy',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('surveyid', models.OneToOneField(db_column='surveyid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='surveysApp.survey')),
                ('questionnumber', models.IntegerField()),
                ('questiontext', models.CharField(max_length=150)),
                ('isobligatory', models.BooleanField()),
                ('respondertype', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'question',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Takesurvey',
            fields=[
                ('voterid', models.OneToOneField(db_column='voterid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='surveysApp.voter')),
                ('starttime', models.DateTimeField()),
            ],
            options={
                'db_table': 'takesurvey',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('voterid', models.OneToOneField(db_column='voterid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='surveysApp.takesurvey')),
                ('questionnumber', models.IntegerField()),
                ('answertext', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'answers',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CheckQuestion',
            fields=[
                ('surveyid', models.OneToOneField(db_column='surveyid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='surveysApp.question')),
                ('questionnumber', models.IntegerField()),
                ('result', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'check_question',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Chooses',
            fields=[
                ('voterid', models.OneToOneField(db_column='voterid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='surveysApp.takesurvey')),
                ('questionnumber', models.IntegerField()),
                ('choicenumber', models.IntegerField()),
            ],
            options={
                'db_table': 'chooses',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Descriptivequestion',
            fields=[
                ('surveyid', models.OneToOneField(db_column='surveyid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='surveysApp.question')),
                ('questionnumber', models.IntegerField()),
            ],
            options={
                'db_table': 'descriptivequestion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Multichoicequestion',
            fields=[
                ('surveyid', models.OneToOneField(db_column='surveyid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='surveysApp.question')),
                ('questionnumber', models.IntegerField()),
            ],
            options={
                'db_table': 'multichoicequestion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('surveyid', models.OneToOneField(db_column='surveyid', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='surveysApp.multichoicequestion')),
                ('questionnumber', models.IntegerField()),
                ('choicenumber', models.IntegerField()),
                ('choicetext', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'choice',
                'managed': False,
            },
        ),
    ]
