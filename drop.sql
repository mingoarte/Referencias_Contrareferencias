drop table paciente_citas cascade;
drop table paciente_historia cascade;
drop table pacientetriaje cascade;
drop table paciente_paciente cascade;
drop table medico_medico_experiencias cascade;
drop table medico_medico_eventos cascade;
drop table medico_medico_logros cascade;
drop table medico_medico_publicaciones cascade;
drop table medico_medico_habilidades cascade;
drop table medico_medico_especialidad cascade;
drop table medico_medico_estudios cascade;
drop table medico_medico cascade;
drop table medico_institucion cascade;
drop table medico_especialidad cascade;
drop table django_migrations cascade;
drop table django_content_type cascade;
drop table auth_permission cascade;
drop table auth_group cascade;
drop table auth_group_permissions cascade;
drop table auth_user_groups cascade;
drop table auth_user_user_permissions cascade;
drop table django_admin_log  cascade;
drop table django_session cascade;
drop table administrador_inbox cascade;
drop table administrador_usuario cascade;
drop table auth_user cascade;
drop table auth_user_groups cascade;
drop table auth_user_user_permissions cascade;
drop table django_admin_log cascade;
drop table medico_medico_citas cascade;
drop table medico_medico_diagnostico cascade;
drop table medico_medico_informe cascade;
drop table medico_medico_revision cascade;
drop table medico_referencia cascade;
drop table medico_institucion cascade;
drop table medico_medico cascade;
drop table paciente_historiadetriaje;



-- alter table django_content_type ADD column name varchar(30);
-- create table administrador_usuario(id varchar(30) primary key, user_id varchar(30), ci varchar(30) unique);