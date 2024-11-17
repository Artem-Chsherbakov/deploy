from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Country(models.Model):
    c_cname = models.CharField(primary_key=True, max_length=50)
    c_population = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country'


class Discover(models.Model):
    dr_cname = models.OneToOneField(Country, models.DO_NOTHING, db_column='dr_cname', primary_key=True)  # The composite primary key (dr_cname, dr_disease_code) found, that is not supported. The first column is selected.
    dr_disease_code = models.ForeignKey('Disease', models.DO_NOTHING, db_column='dr_disease_code')
    dr_first_enc_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discover'
        unique_together = (('dr_cname', 'dr_disease_code'),)


class Disease(models.Model):
    ds_disease_code = models.CharField(primary_key=True, max_length=50)
    ds_pathogen = models.CharField(max_length=20, blank=True, null=True)
    ds_description = models.CharField(max_length=140, blank=True, null=True)
    ds = models.ForeignKey('DiseaseType', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disease'


class DiseaseType(models.Model):
    dt_id = models.IntegerField(primary_key=True)
    dt_description = models.CharField(max_length=140, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disease_type'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Doctor(models.Model):
    dc_email = models.OneToOneField('Users', models.DO_NOTHING, db_column='dc_email', primary_key=True)
    dc_degree = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'doctor'


class PatientDisease(models.Model):
    pd_email = models.OneToOneField('Users', models.DO_NOTHING, db_column='pd_email', primary_key=True)
    pd_disease_code = models.ForeignKey(Disease, models.DO_NOTHING, db_column='pd_disease_code', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_disease'


class Patients(models.Model):
    p_email = models.OneToOneField('Users', models.DO_NOTHING, db_column='p_email', primary_key=True)

    class Meta:
        managed = False
        db_table = 'patients'


class PublicServant(models.Model):
    ps_email = models.OneToOneField('Users', models.DO_NOTHING, db_column='ps_email', primary_key=True)
    ps_department = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'public_servant'


class Record(models.Model):
    r_email = models.OneToOneField(PublicServant, models.DO_NOTHING, db_column='r_email', primary_key=True)  # The composite primary key (r_email, r_cname, r_disease_code) found, that is not supported. The first column is selected.
    r_cname = models.ForeignKey(Country, models.DO_NOTHING, db_column='r_cname')
    r_disease_code = models.ForeignKey(Disease, models.DO_NOTHING, db_column='r_disease_code')
    r_total_deaths = models.IntegerField(blank=True, null=True)
    r_total_patients = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'record'
        unique_together = (('r_email', 'r_cname', 'r_disease_code'),)


class Specialize(models.Model):
    s = models.OneToOneField(DiseaseType, models.DO_NOTHING, primary_key=True)  # The composite primary key (s_id, s_email) found, that is not supported. The first column is selected.
    s_email = models.ForeignKey(Doctor, models.DO_NOTHING, db_column='s_email')

    class Meta:
        managed = False
        db_table = 'specialize'
        unique_together = (('s', 's_email'),)


class Users(models.Model):
    u_email = models.CharField(primary_key=True, max_length=60)
    u_name = models.CharField(max_length=30, blank=True, null=True)
    u_surname = models.CharField(max_length=40, blank=True, null=True)
    u_salary = models.IntegerField(blank=True, null=True)
    u_phone = models.CharField(max_length=20, blank=True, null=True)
    u_cname = models.ForeignKey(Country, models.DO_NOTHING, db_column='u_cname', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
