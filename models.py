# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Ac(models.Model):
    ac_d = models.CharField(db_column='AC_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ac_key = models.CharField(db_column='AC_KEY', primary_key=True, max_length=22)  # Field name made lowercase.
    ac_g_key = models.CharField(db_column='AC_G_KEY', max_length=4, blank=True, null=True)  # Field name made lowercase.
    ac_loginid = models.CharField(db_column='AC_LoginID', max_length=4, blank=True, null=True)  # Field name made lowercase.
    ac_program = models.CharField(db_column='AC_Program', max_length=12, blank=True, null=True)  # Field name made lowercase.
    ac_add = models.CharField(db_column='AC_Add', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ac_del = models.CharField(db_column='AC_Del', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ac_find = models.CharField(db_column='AC_Find', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ac_up = models.CharField(db_column='AC_Up', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ac_time_last = models.TimeField(db_column='AC_Time_Last', blank=True, null=True)  # Field name made lowercase.
    ac_who_last = models.CharField(db_column='AC_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ac'


class Address(models.Model):
    a_d = models.CharField(db_column='A_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    a_key = models.CharField(db_column='A_KEY', primary_key=True, max_length=4)  # Field name made lowercase.
    a_full = models.CharField(db_column='A_Full', max_length=32, blank=True, null=True)  # Field name made lowercase.
    a_addr1 = models.CharField(db_column='A_Addr1', max_length=32, blank=True, null=True)  # Field name made lowercase.
    a_addr2 = models.CharField(db_column='A_Addr2', max_length=32, blank=True, null=True)  # Field name made lowercase.
    a_addr3 = models.CharField(db_column='A_Addr3', max_length=32, blank=True, null=True)  # Field name made lowercase.
    a_addr4 = models.CharField(db_column='A_Addr4', max_length=32, blank=True, null=True)  # Field name made lowercase.
    a_time_last = models.TimeField(db_column='A_Time_Last', blank=True, null=True)  # Field name made lowercase.
    a_who_last = models.CharField(db_column='A_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'address'


class Adets(models.Model):
    adets_d = models.CharField(db_column='ADETS_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    adets_rec = models.IntegerField(db_column='ADETS_REC', primary_key=True)  # Field name made lowercase.
    adets_ahead_rec = models.IntegerField(db_column='ADETS_AHEAD_REC', blank=True, null=True)  # Field name made lowercase.
    adets_flag_ded_here = models.CharField(db_column='ADETS_FLAG_Ded_Here', max_length=1, blank=True, null=True)  # Field name made lowercase.
    adets_allot_usd = models.DecimalField(db_column='ADETS_Allot_USD', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    adets_before_peso = models.DecimalField(db_column='ADETS_Before_Peso', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    adets_dollar_acct = models.CharField(db_column='ADETS_Dollar_Acct', max_length=1, blank=True, null=True)  # Field name made lowercase.
    adets_name = models.CharField(db_column='ADETS_Name', max_length=24, blank=True, null=True)  # Field name made lowercase.
    adets_addr1 = models.CharField(db_column='ADETS_Addr1', max_length=16, blank=True, null=True)  # Field name made lowercase.
    adets_addr2 = models.CharField(db_column='ADETS_Addr2', max_length=16, blank=True, null=True)  # Field name made lowercase.
    adets_bank_bk_key = models.CharField(db_column='ADETS_Bank_BK_KEY', max_length=4, blank=True, null=True)  # Field name made lowercase.
    adets_b_type = models.CharField(db_column='ADETS_B_Type', max_length=1, blank=True, null=True)  # Field name made lowercase.
    adets_b_branch = models.CharField(db_column='ADETS_B_Branch', max_length=16, blank=True, null=True)  # Field name made lowercase.
    adets_b_acct = models.CharField(db_column='ADETS_B_Acct', max_length=16, blank=True, null=True)  # Field name made lowercase.
    adets_time_last = models.TimeField(db_column='ADETS_Time_Last', blank=True, null=True)  # Field name made lowercase.
    adets_who_last = models.CharField(db_column='ADETS_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adets'


class AdvProv(models.Model):
    adp_d = models.CharField(db_column='ADP_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    adp_key = models.CharField(db_column='ADP_KEY', primary_key=True, max_length=1)  # Field name made lowercase.
    adp_full = models.CharField(db_column='ADP_Full', max_length=30, blank=True, null=True)  # Field name made lowercase.
    adp_time_last = models.TimeField(db_column='ADP_Time_Last', blank=True, null=True)  # Field name made lowercase.
    adp_who_last = models.CharField(db_column='ADP_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'adv_prov'


class Agents(models.Model):
    agn_d = models.CharField(db_column='AGN_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    agn_key = models.CharField(db_column='AGN_KEY', primary_key=True, max_length=4)  # Field name made lowercase.
    agn_full = models.CharField(db_column='AGN_Full', max_length=40, blank=True, null=True)  # Field name made lowercase.
    agn_addr1 = models.CharField(db_column='AGN_Addr1', max_length=32, blank=True, null=True)  # Field name made lowercase.
    agn_addr2 = models.CharField(db_column='AGN_Addr2', max_length=32, blank=True, null=True)  # Field name made lowercase.
    agn_addr3 = models.CharField(db_column='AGN_Addr3', max_length=32, blank=True, null=True)  # Field name made lowercase.
    agn_addr4 = models.CharField(db_column='AGN_Addr4', max_length=32, blank=True, null=True)  # Field name made lowercase.
    agn_cn_key = models.CharField(db_column='AGN_CN_KEY', max_length=2, blank=True, null=True)  # Field name made lowercase.
    agn_phone = models.CharField(db_column='AGN_Phone', max_length=32, blank=True, null=True)  # Field name made lowercase.
    agn_telex = models.CharField(db_column='AGN_Telex', max_length=32, blank=True, null=True)  # Field name made lowercase.
    agn_fax = models.CharField(db_column='AGN_Fax', max_length=32, blank=True, null=True)  # Field name made lowercase.
    agn_aoh = models.CharField(db_column='AGN_AOH', max_length=32, blank=True, null=True)  # Field name made lowercase.
    agn_comment = models.CharField(db_column='AGN_Comment', max_length=70, blank=True, null=True)  # Field name made lowercase.
    agn_time_last = models.TimeField(db_column='AGN_Time_Last', blank=True, null=True)  # Field name made lowercase.
    agn_who_last = models.CharField(db_column='AGN_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'agents'


class Ahead(models.Model):
    ahead_d = models.CharField(db_column='AHEAD_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ahead_rec = models.IntegerField(db_column='AHEAD_REC')  # Field name made lowercase.
    ahead_unique = models.CharField(db_column='AHEAD_UNIQUE', max_length=13)  # Field name made lowercase.
    ahead_id_b_id = models.CharField(db_column='AHEAD_ID_B_ID', max_length=4, blank=True, null=True)  # Field name made lowercase.
    ahead_date = models.DateField(db_column='AHEAD_Date', blank=True, null=True)  # Field name made lowercase.
    ahead_extra = models.CharField(db_column='AHEAD_Extra', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ahead_frozen = models.CharField(db_column='AHEAD_Frozen', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ahead_contract_con_rec = models.IntegerField(db_column='AHEAD_Contract_CON_REC', blank=True, null=True)  # Field name made lowercase.
    ahead_entered = models.DateField(db_column='AHEAD_Entered', blank=True, null=True)  # Field name made lowercase.
    ahead_tax = models.DecimalField(db_column='AHEAD_Tax', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ahead_employee_sss_ded = models.DecimalField(db_column='AHEAD_Employee_SSS_Ded', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ahead_employer_sss_cont = models.DecimalField(db_column='AHEAD_Employer_SSS_Cont', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ahead_employee_med_ded = models.DecimalField(db_column='AHEAD_Employee_Med_Ded', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ahead_employer_med_cont = models.DecimalField(db_column='AHEAD_Employer_Med_Cont', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ahead_employer_ecc_cont = models.DecimalField(db_column='AHEAD_Employer_ECC_Cont', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ahead_advances_amnt = models.DecimalField(db_column='AHEAD_Advances_Amnt', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ahead_salary_loan = models.DecimalField(db_column='AHEAD_Salary_Loan', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ahead_stock_loan = models.DecimalField(db_column='AHEAD_Stock_Loan', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ahead_sundry = models.CharField(db_column='AHEAD_Sundry', max_length=24, blank=True, null=True)  # Field name made lowercase.
    ahead_sundry_amnt = models.DecimalField(db_column='AHEAD_Sundry_Amnt', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ahead_employee_pagibig_ded = models.DecimalField(db_column='AHEAD_Employee_Pagibig_Ded', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ahead_employer_pagibig_cont = models.DecimalField(db_column='AHEAD_Employer_Pagibig_Cont', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ahead_time_last = models.TimeField(db_column='AHEAD_Time_Last', blank=True, null=True)  # Field name made lowercase.
    ahead_who_last = models.CharField(db_column='AHEAD_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ahead'
        unique_together = (('AHEAD_REC', 'AHEAD_UNIQUE'),)


class Alist(models.Model):
    alist_d = models.CharField(db_column='ALIST_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    alist_rec = models.IntegerField(db_column='ALIST_REC', primary_key=True)  # Field name made lowercase.
    alist_id_ex_id_b_id = models.CharField(db_column='ALIST_ID_EX_ID_B_ID', max_length=4, blank=True, null=True)  # Field name made lowercase.
    alist_allot_usd = models.DecimalField(db_column='ALIST_Allot_USD', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    alist_allot_name = models.CharField(db_column='ALIST_Allot_Name', max_length=32, blank=True, null=True)  # Field name made lowercase.
    alist_allot_bank_branch = models.CharField(db_column='ALIST_Allot_Bank_Branch', max_length=16, blank=True, null=True)  # Field name made lowercase.
    alist_allot_addr1 = models.CharField(db_column='ALIST_Allot_Addr1', max_length=16, blank=True, null=True)  # Field name made lowercase.
    alist_allot_addr2 = models.CharField(db_column='ALIST_Allot_Addr2', max_length=16, blank=True, null=True)  # Field name made lowercase.
    alist_allot_relation = models.CharField(db_column='ALIST_Allot_Relation', max_length=8, blank=True, null=True)  # Field name made lowercase.
    alist_allot_phone = models.CharField(db_column='ALIST_Allot_Phone', max_length=16, blank=True, null=True)  # Field name made lowercase.
    alist_allot_bank_bk_key = models.CharField(db_column='ALIST_Allot_Bank_BK_KEY', max_length=4, blank=True, null=True)  # Field name made lowercase.
    alist_allot_bank_acct = models.CharField(db_column='ALIST_Allot_Bank_Acct', max_length=20, blank=True, null=True)  # Field name made lowercase.
    alist_allot_type = models.CharField(db_column='ALIST_Allot_Type', max_length=1, blank=True, null=True)  # Field name made lowercase.
    alist_allot_display = models.CharField(db_column='ALIST_Allot_Display', max_length=1, blank=True, null=True)  # Field name made lowercase.
    alist_time_last = models.TimeField(db_column='ALIST_Time_Last', blank=True, null=True)  # Field name made lowercase.
    alist_who_last = models.CharField(db_column='ALIST_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'alist'


class Bio(models.Model):
    b_d = models.CharField(db_column='B_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    b_id = models.CharField(db_column='B_ID', max_length=4)  # Field name made lowercase.
    b_uid = models.IntegerField(db_column='B_UID', blank=True, null=True)  # Field name made lowercase.
    b_last_name = models.CharField(db_column='B_Last_Name', max_length=18, blank=True, null=True)  # Field name made lowercase.
    b_last_name_grk = models.CharField(db_column='B_Last_Name_Grk', max_length=18, blank=True, null=True)  # Field name made lowercase.
    b_first_name = models.CharField(db_column='B_First_Name', max_length=28, blank=True, null=True)  # Field name made lowercase.
    b_first_name_grk = models.CharField(db_column='B_First_Name_Grk', max_length=18, blank=True, null=True)  # Field name made lowercase.
    b_middle_name = models.CharField(db_column='B_Middle_Name', max_length=18, blank=True, null=True)  # Field name made lowercase.
    b_suffix_name = models.CharField(db_column='B_Suffix_Name', max_length=5, blank=True, null=True)  # Field name made lowercase.
    b_middle_name_grk = models.CharField(db_column='B_Middle_Name_Grk', max_length=18, blank=True, null=True)  # Field name made lowercase.
    b_father_name = models.CharField(db_column='B_Father_Name', max_length=18, blank=True, null=True)  # Field name made lowercase.
    b_father_name_grk = models.CharField(db_column='B_Father_Name_Grk', max_length=18, blank=True, null=True)  # Field name made lowercase.
    b_mother_name = models.CharField(db_column='B_Mother_Name', max_length=18, blank=True, null=True)  # Field name made lowercase.
    b_mother_name_grk = models.CharField(db_column='B_Mother_Name_Grk', max_length=18, blank=True, null=True)  # Field name made lowercase.
    b_cn_key = models.CharField(db_column='B_CN_KEY', max_length=2, blank=True, null=True)  # Field name made lowercase.
    b_bio_status = models.CharField(db_column='B_Bio_Status', max_length=1, blank=True, null=True)  # Field name made lowercase.
    b_available = models.DateField(db_column='B_Available', blank=True, null=True)  # Field name made lowercase.
    b_position_1st = models.CharField(db_column='B_Position_1st', max_length=4, blank=True, null=True)  # Field name made lowercase.
    b_ex_crew = models.CharField(db_column='B_Ex_Crew', max_length=1, blank=True, null=True)  # Field name made lowercase.
    b_last_v_key = models.CharField(db_column='B_Last_V_KEY', max_length=4, blank=True, null=True)  # Field name made lowercase.
    b_rank1_r_key = models.CharField(db_column='B_Rank1_R_KEY', max_length=4, blank=True, null=True)  # Field name made lowercase.
    b_type1_vt_key = models.CharField(db_column='B_Type1_VT_KEY', max_length=4, blank=True, null=True)  # Field name made lowercase.
    b_rank2_r_key = models.CharField(db_column='B_Rank2_R_KEY', max_length=4, blank=True, null=True)  # Field name made lowercase.
    b_type2_vt_key = models.CharField(db_column='B_Type2_VT_KEY', max_length=4, blank=True, null=True)  # Field name made lowercase.
    b_birth_date = models.DateField(db_column='B_Birth_Date', blank=True, null=True)  # Field name made lowercase.
    b_birth_place = models.CharField(db_column='B_Birth_Place', max_length=32, blank=True, null=True)  # Field name made lowercase.
    b_height = models.CharField(db_column='B_Height', max_length=5, blank=True, null=True)  # Field name made lowercase.
    b_weight = models.CharField(db_column='B_Weight', max_length=5, blank=True, null=True)  # Field name made lowercase.
    b_bmi = models.DecimalField(db_column='B_BMI', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    b_phone_1 = models.CharField(db_column='B_Phone_1', max_length=16, blank=True, null=True)  # Field name made lowercase.
    b_phone_2 = models.CharField(db_column='B_Phone_2', max_length=16, blank=True, null=True)  # Field name made lowercase.
    b_metro_addr_1 = models.CharField(db_column='B_Metro_Addr_1', max_length=32, blank=True, null=True)  # Field name made lowercase.
    b_metro_addr_2 = models.CharField(db_column='B_Metro_Addr_2', max_length=32, blank=True, null=True)  # Field name made lowercase.
    b_metro_addr_3 = models.CharField(db_column='B_Metro_Addr_3', max_length=32, blank=True, null=True)  # Field name made lowercase.
    b_metro_addr_4 = models.CharField(db_column='B_Metro_Addr_4', max_length=32, blank=True, null=True)  # Field name made lowercase.
    b_prov_addr_1 = models.CharField(db_column='B_Prov_Addr_1', max_length=16, blank=True, null=True)  # Field name made lowercase.
    b_prov_addr_2 = models.CharField(db_column='B_Prov_Addr_2', max_length=16, blank=True, null=True)  # Field name made lowercase.
    b_prov_addr_3 = models.CharField(db_column='B_Prov_Addr_3', max_length=16, blank=True, null=True)  # Field name made lowercase.
    b_prov_addr_4 = models.CharField(db_column='B_Prov_Addr_4', max_length=16, blank=True, null=True)  # Field name made lowercase.
    b_addr_grk_1 = models.CharField(db_column='B_Addr_Grk_1', max_length=16, blank=True, null=True)  # Field name made lowercase.
    b_addr_grk_2 = models.CharField(db_column='B_Addr_Grk_2', max_length=16, blank=True, null=True)  # Field name made lowercase.
    b_addr_grk_3 = models.CharField(db_column='B_Addr_Grk_3', max_length=16, blank=True, null=True)  # Field name made lowercase.
    b_addr_grk_4 = models.CharField(db_column='B_Addr_Grk_4', max_length=16, blank=True, null=True)  # Field name made lowercase.
    b_marital_status = models.CharField(db_column='B_Marital_Status', max_length=1, blank=True, null=True)  # Field name made lowercase.
    b_number_dependents = models.IntegerField(db_column='B_Number_Dependents', blank=True, null=True)  # Field name made lowercase.
    b_emergency_name = models.CharField(db_column='B_Emergency_Name', max_length=24, blank=True, null=True)  # Field name made lowercase.
    b_emergency_relation = models.CharField(db_column='B_Emergency_Relation', max_length=4, blank=True, null=True)  # Field name made lowercase.
    b_emergency_phone = models.CharField(db_column='B_Emergency_Phone', max_length=16, blank=True, null=True)  # Field name made lowercase.
    b_emergency_addr_1 = models.CharField(db_column='B_Emergency_Addr_1', max_length=32, blank=True, null=True)  # Field name made lowercase.
    b_emergency_addr_2 = models.CharField(db_column='B_Emergency_Addr_2', max_length=32, blank=True, null=True)  # Field name made lowercase.
    b_emergency_addr_3 = models.CharField(db_column='B_Emergency_Addr_3', max_length=32, blank=True, null=True)  # Field name made lowercase.
    b_emergency_addr_4 = models.CharField(db_column='B_Emergency_Addr_4', max_length=32, blank=True, null=True)  # Field name made lowercase.
    b_educ_note_1 = models.CharField(db_column='B_Educ_Note_1', max_length=34, blank=True, null=True)  # Field name made lowercase.
    b_educ_note_2 = models.CharField(db_column='B_Educ_Note_2', max_length=34, blank=True, null=True)  # Field name made lowercase.
    b_mother_language = models.CharField(db_column='B_Mother_Language', max_length=8, blank=True, null=True)  # Field name made lowercase.
    b_english = models.CharField(db_column='B_English', max_length=1, blank=True, null=True)  # Field name made lowercase.
    b_comments = models.CharField(db_column='B_Comments', max_length=60, blank=True, null=True)  # Field name made lowercase.
    b_wife_name = models.CharField(db_column='B_Wife_Name', max_length=34, blank=True, null=True)  # Field name made lowercase.
    b_wife_birthdate = models.DateField(db_column='B_Wife_BirthDate', blank=True, null=True)  # Field name made lowercase.
    b_wife_job = models.CharField(db_column='B_Wife_Job', max_length=1, blank=True, null=True)  # Field name made lowercase.
    b_tax_status = models.CharField(db_column='B_Tax_Status', max_length=1, blank=True, null=True)  # Field name made lowercase.
    b_tax_acct = models.CharField(db_column='B_Tax_Acct', max_length=20, blank=True, null=True)  # Field name made lowercase.
    b_tax_office = models.CharField(db_column='B_Tax_Office', max_length=30, blank=True, null=True)  # Field name made lowercase.
    b_sss = models.CharField(db_column='B_SSS', max_length=16, blank=True, null=True)  # Field name made lowercase.
    b_phealth = models.CharField(db_column='B_PHealth', max_length=16, blank=True, null=True)  # Field name made lowercase.
    b_vocational = models.CharField(db_column='B_Vocational', max_length=16, blank=True, null=True)  # Field name made lowercase.
    b_hs_grad = models.CharField(db_column='B_HS_Grad', max_length=1, blank=True, null=True)  # Field name made lowercase.
    b_hs_date = models.DateField(db_column='B_HS_Date', blank=True, null=True)  # Field name made lowercase.
    b_nautical_school = models.CharField(db_column='B_Nautical_School', max_length=16, blank=True, null=True)  # Field name made lowercase.
    b_nautical_degree = models.CharField(db_column='B_Nautical_Degree', max_length=4, blank=True, null=True)  # Field name made lowercase.
    b_nautical_date = models.DateField(db_column='B_Nautical_Date', blank=True, null=True)  # Field name made lowercase.
    b_other_school = models.CharField(db_column='B_Other_School', max_length=16, blank=True, null=True)  # Field name made lowercase.
    b_other_degree = models.CharField(db_column='B_Other_Degree', max_length=8, blank=True, null=True)  # Field name made lowercase.
    b_other_date = models.DateField(db_column='B_Other_Date', blank=True, null=True)  # Field name made lowercase.
    b_union = models.CharField(db_column='B_Union', max_length=1, blank=True, null=True)  # Field name made lowercase.
    b_separation_type = models.CharField(db_column='B_Separation_Type', max_length=1, blank=True, null=True)  # Field name made lowercase.
    b_sea_months = models.IntegerField(db_column='B_Sea_Months', blank=True, null=True)  # Field name made lowercase.
    b_high_rank1_r_key = models.CharField(db_column='B_High_Rank1_R_KEY', max_length=4, blank=True, null=True)  # Field name made lowercase.
    b_vtype_rank1_vt_key = models.CharField(db_column='B_VType_Rank1_VT_KEY', max_length=4, blank=True, null=True)  # Field name made lowercase.
    b_high_rank2_r_key = models.CharField(db_column='B_High_Rank2_R_KEY', max_length=4, blank=True, null=True)  # Field name made lowercase.
    b_vtype_rank2_vt_key = models.CharField(db_column='B_VType_Rank2_VT_KEY', max_length=4, blank=True, null=True)  # Field name made lowercase.
    b_skills = models.CharField(db_column='B_Skills', max_length=32, blank=True, null=True)  # Field name made lowercase.
    b_nick_name = models.CharField(db_column='B_Nick_Name', max_length=12, blank=True, null=True)  # Field name made lowercase.
    b_email_address = models.CharField(db_column='B_Email_Address', max_length=45, blank=True, null=True)  # Field name made lowercase.
    b_ofw_id = models.CharField(db_column='B_OFW_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    b_pagibig = models.CharField(db_column='B_Pagibig', max_length=16, blank=True, null=True)  # Field name made lowercase.
    b_freemail = models.CharField(db_column='B_Freemail', max_length=1, blank=True, null=True)  # Field name made lowercase.
    b_time_last = models.TimeField(db_column='B_Time_Last', blank=True, null=True)  # Field name made lowercase.
    b_who_last = models.CharField(db_column='B_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bio'


class Biostat(models.Model):
    bs_d = models.CharField(db_column='BS_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    bs_key = models.CharField(db_column='BS_KEY', primary_key=True, max_length=1)  # Field name made lowercase.
    bs_full = models.CharField(db_column='BS_Full', max_length=16, blank=True, null=True)  # Field name made lowercase.
    bs_time_last = models.TimeField(db_column='BS_Time_Last', blank=True, null=True)  # Field name made lowercase.
    bs_who_last = models.CharField(db_column='BS_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'biostat'


class Bond(models.Model):
    bo_d = models.CharField(db_column='BO_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    bo_rec = models.IntegerField(db_column='BO_REC')  # Field name made lowercase.
    bo_unique = models.CharField(db_column='BO_UNIQUE', max_length=13)  # Field name made lowercase.
    bo_unique_1 = models.CharField(db_column='BO_UNIQUE_1', max_length=15)  # Field name made lowercase.
    bo_v_key = models.CharField(db_column='BO_V_KEY', max_length=4, blank=True, null=True)  # Field name made lowercase.
    bo_rob_date = models.DateField(db_column='BO_Rob_Date', blank=True, null=True)  # Field name made lowercase.
    bo_closed = models.CharField(db_column='BO_Closed', max_length=1, blank=True, null=True)  # Field name made lowercase.
    bo_cig_rob_quant = models.IntegerField(db_column='BO_Cig_Rob_Quant', blank=True, null=True)  # Field name made lowercase.
    bo_cig_rob_perit = models.DecimalField(db_column='BO_Cig_Rob_PerIt', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bo_cig_rob_amnt = models.DecimalField(db_column='BO_Cig_Rob_Amnt', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bo_cig_pur_date1 = models.DateField(db_column='BO_Cig_Pur_Date1', blank=True, null=True)  # Field name made lowercase.
    bo_cig_pur_quan1 = models.IntegerField(db_column='BO_Cig_Pur_Quan1', blank=True, null=True)  # Field name made lowercase.
    bo_cig_pur_peri1 = models.DecimalField(db_column='BO_Cig_Pur_PerI1', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bo_cig_pur_amnt1 = models.DecimalField(db_column='BO_Cig_Pur_Amnt1', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bo_cig_pur_desc1 = models.CharField(db_column='BO_Cig_Pur_Desc1', max_length=32, blank=True, null=True)  # Field name made lowercase.
    bo_cig_pur_date2 = models.DateField(db_column='BO_Cig_Pur_Date2', blank=True, null=True)  # Field name made lowercase.
    bo_cig_pur_quan2 = models.IntegerField(db_column='BO_Cig_Pur_Quan2', blank=True, null=True)  # Field name made lowercase.
    bo_cig_pur_peri2 = models.DecimalField(db_column='BO_Cig_Pur_PerI2', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bo_cig_pur_amnt2 = models.DecimalField(db_column='BO_Cig_Pur_Amnt2', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bo_cig_pur_desc2 = models.CharField(db_column='BO_Cig_Pur_Desc2', max_length=32, blank=True, null=True)  # Field name made lowercase.
    bo_cig_crew_quant = models.IntegerField(db_column='BO_Cig_Crew_Quant', blank=True, null=True)  # Field name made lowercase.
    bo_cig_crew_perit = models.DecimalField(db_column='BO_Cig_Crew_PerIt', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bo_cig_crew_amnt = models.DecimalField(db_column='BO_Cig_Crew_Amnt', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bo_cig_grat_date1 = models.DateField(db_column='BO_Cig_Grat_Date1', blank=True, null=True)  # Field name made lowercase.
    bo_cig_grat_quan1 = models.IntegerField(db_column='BO_Cig_Grat_Quan1', blank=True, null=True)  # Field name made lowercase.
    bo_cig_grat_peri1 = models.DecimalField(db_column='BO_Cig_Grat_PerI1', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bo_cig_grat_amnt1 = models.DecimalField(db_column='BO_Cig_Grat_Amnt1', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bo_cig_grat_desc1 = models.CharField(db_column='BO_Cig_Grat_Desc1', max_length=32, blank=True, null=True)  # Field name made lowercase.
    bo_cig_grat_date2 = models.DateField(db_column='BO_Cig_Grat_Date2', blank=True, null=True)  # Field name made lowercase.
    bo_cig_grat_quan2 = models.IntegerField(db_column='BO_Cig_Grat_Quan2', blank=True, null=True)  # Field name made lowercase.
    bo_cig_grat_peri2 = models.DecimalField(db_column='BO_Cig_Grat_PerI2', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bo_cig_grat_amnt2 = models.DecimalField(db_column='BO_Cig_Grat_Amnt2', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bo_cig_grat_desc2 = models.CharField(db_column='BO_Cig_Grat_Desc2', max_length=32, blank=True, null=True)  # Field name made lowercase.
    bo_cig_grat_date3 = models.DateField(db_column='BO_Cig_Grat_Date3', blank=True, null=True)  # Field name made lowercase.
    bo_cig_grat_quan3 = models.IntegerField(db_column='BO_Cig_Grat_Quan3', blank=True, null=True)  # Field name made lowercase.
    bo_cig_grat_peri3 = models.DecimalField(db_column='BO_Cig_Grat_PerI3', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bo_cig_grat_amnt3 = models.DecimalField(db_column='BO_Cig_Grat_Amnt3', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bo_cig_grat_desc3 = models.CharField(db_column='BO_Cig_Grat_Desc3', max_length=32, blank=True, null=True)  # Field name made lowercase.
    bo_cig_grat_date4 = models.DateField(db_column='BO_Cig_Grat_Date4', blank=True, null=True)  # Field name made lowercase.
    bo_cig_grat_quan4 = models.IntegerField(db_column='BO_Cig_Grat_Quan4', blank=True, null=True)  # Field name made lowercase.
    bo_cig_grat_peri4 = models.DecimalField(db_column='BO_Cig_Grat_PerI4', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bo_cig_grat_amnt4 = models.DecimalField(db_column='BO_Cig_Grat_Amnt4', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bo_cig_grat_desc4 = models.CharField(db_column='BO_Cig_Grat_Desc4', max_length=32, blank=True, null=True)  # Field name made lowercase.
    bo_cig_grat_date5 = models.DateField(db_column='BO_Cig_Grat_Date5', blank=True, null=True)  # Field name made lowercase.
    bo_cig_grat_quan5 = models.IntegerField(db_column='BO_Cig_Grat_Quan5', blank=True, null=True)  # Field name made lowercase.
    bo_cig_grat_peri5 = models.DecimalField(db_column='BO_Cig_Grat_PerI5', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bo_cig_grat_amnt5 = models.DecimalField(db_column='BO_Cig_Grat_Amnt5', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bo_cig_grat_desc5 = models.CharField(db_column='BO_Cig_Grat_Desc5', max_length=32, blank=True, null=True)  # Field name made lowercase.
    bo_cig_cur_quant = models.IntegerField(db_column='BO_Cig_Cur_Quant', blank=True, null=True)  # Field name made lowercase.
    bo_cig_cur_perit = models.DecimalField(db_column='BO_Cig_Cur_PerIt', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bo_cig_cur_amnt = models.DecimalField(db_column='BO_Cig_Cur_Amnt', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bo_spir_rob_quant = models.IntegerField(db_column='BO_Spir_Rob_Quant', blank=True, null=True)  # Field name made lowercase.
    bo_spir_rob_perit = models.DecimalField(db_column='BO_Spir_Rob_PerIt', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bo_spir_rob_amnt = models.DecimalField(db_column='BO_Spir_Rob_Amnt', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bo_spir_pur_date1 = models.DateField(db_column='BO_Spir_Pur_Date1', blank=True, null=True)  # Field name made lowercase.
    bo_spir_pur_quan1 = models.IntegerField(db_column='BO_Spir_Pur_Quan1', blank=True, null=True)  # Field name made lowercase.
    bo_spir_pur_peri1 = models.DecimalField(db_column='BO_Spir_Pur_PerI1', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bo_spir_pur_amnt1 = models.DecimalField(db_column='BO_Spir_Pur_Amnt1', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bo_spir_pur_desc1 = models.CharField(db_column='BO_Spir_Pur_Desc1', max_length=32, blank=True, null=True)  # Field name made lowercase.
    bo_spir_pur_date2 = models.DateField(db_column='BO_Spir_Pur_Date2', blank=True, null=True)  # Field name made lowercase.
    bo_spir_pur_quan2 = models.IntegerField(db_column='BO_Spir_Pur_Quan2', blank=True, null=True)  # Field name made lowercase.
    bo_spir_pur_peri2 = models.DecimalField(db_column='BO_Spir_Pur_PerI2', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bo_spir_pur_amnt2 = models.DecimalField(db_column='BO_Spir_Pur_Amnt2', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bo_spir_pur_desc2 = models.CharField(db_column='BO_Spir_Pur_Desc2', max_length=32, blank=True, null=True)  # Field name made lowercase.
    bo_spir_grat_date1 = models.DateField(db_column='BO_Spir_Grat_Date1', blank=True, null=True)  # Field name made lowercase.
    bo_spir_grat_quan1 = models.IntegerField(db_column='BO_Spir_Grat_Quan1', blank=True, null=True)  # Field name made lowercase.
    bo_spir_grat_peri1 = models.DecimalField(db_column='BO_Spir_Grat_PerI1', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bo_spir_grat_amnt1 = models.DecimalField(db_column='BO_Spir_Grat_Amnt1', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bo_spir_grat_desc1 = models.CharField(db_column='BO_Spir_Grat_Desc1', max_length=32, blank=True, null=True)  # Field name made lowercase.
    bo_spir_grat_date2 = models.DateField(db_column='BO_Spir_Grat_Date2', blank=True, null=True)  # Field name made lowercase.
    bo_spir_grat_quan2 = models.IntegerField(db_column='BO_Spir_Grat_Quan2', blank=True, null=True)  # Field name made lowercase.
    bo_spir_grat_peri2 = models.DecimalField(db_column='BO_Spir_Grat_PerI2', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bo_spir_grat_amnt2 = models.DecimalField(db_column='BO_Spir_Grat_Amnt2', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bo_spir_grat_desc2 = models.CharField(db_column='BO_Spir_Grat_Desc2', max_length=32, blank=True, null=True)  # Field name made lowercase.
    bo_spir_grat_date3 = models.DateField(db_column='BO_Spir_Grat_Date3', blank=True, null=True)  # Field name made lowercase.
    bo_spir_grat_quan3 = models.IntegerField(db_column='BO_Spir_Grat_Quan3', blank=True, null=True)  # Field name made lowercase.
    bo_spir_grat_peri3 = models.DecimalField(db_column='BO_Spir_Grat_PerI3', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bo_spir_grat_amnt3 = models.DecimalField(db_column='BO_Spir_Grat_Amnt3', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bo_spir_grat_desc3 = models.CharField(db_column='BO_Spir_Grat_Desc3', max_length=32, blank=True, null=True)  # Field name made lowercase.
    bo_spir_grat_date4 = models.DateField(db_column='BO_Spir_Grat_Date4', blank=True, null=True)  # Field name made lowercase.
    bo_spir_grat_quan4 = models.IntegerField(db_column='BO_Spir_Grat_Quan4', blank=True, null=True)  # Field name made lowercase.
    bo_spir_grat_peri4 = models.DecimalField(db_column='BO_Spir_Grat_PerI4', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bo_spir_grat_amnt4 = models.DecimalField(db_column='BO_Spir_Grat_Amnt4', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bo_spir_grat_desc4 = models.CharField(db_column='BO_Spir_Grat_Desc4', max_length=32, blank=True, null=True)  # Field name made lowercase.
    bo_spir_grat_date5 = models.DateField(db_column='BO_Spir_Grat_Date5', blank=True, null=True)  # Field name made lowercase.
    bo_spir_grat_quan5 = models.IntegerField(db_column='BO_Spir_Grat_Quan5', blank=True, null=True)  # Field name made lowercase.
    bo_spir_grat_peri5 = models.DecimalField(db_column='BO_Spir_Grat_PerI5', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bo_spir_grat_amnt5 = models.DecimalField(db_column='BO_Spir_Grat_Amnt5', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bo_spir_grat_desc5 = models.CharField(db_column='BO_Spir_Grat_Desc5', max_length=32, blank=True, null=True)  # Field name made lowercase.
    bo_spir_cur_quant = models.IntegerField(db_column='BO_Spir_Cur_Quant', blank=True, null=True)  # Field name made lowercase.
    bo_spir_cur_perit = models.DecimalField(db_column='BO_Spir_Cur_PerIt', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bo_spir_cur_amnt = models.DecimalField(db_column='BO_Spir_Cur_Amnt', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    bo_post_date = models.DateField(db_column='BO_Post_Date', blank=True, null=True)  # Field name made lowercase.
    bo_time_last = models.TimeField(db_column='BO_Time_Last', blank=True, null=True)  # Field name made lowercase.
    bo_who_last = models.CharField(db_column='BO_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bond'
        unique_together = (('BO_REC', 'BO_UNIQUE', 'BO_UNIQUE_1'),)


class Cash(models.Model):
    ca_d = models.CharField(db_column='CA_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ca_rec = models.IntegerField(db_column='CA_REC')  # Field name made lowercase.
    ca_unique = models.CharField(db_column='CA_UNIQUE', max_length=17)  # Field name made lowercase.
    ca_unique_1 = models.CharField(db_column='CA_UNIQUE_1', max_length=19)  # Field name made lowercase.
    ca_v_key = models.CharField(db_column='CA_V_KEY', max_length=4, blank=True, null=True)  # Field name made lowercase.
    ca_rob_date = models.DateField(db_column='CA_Rob_Date', blank=True, null=True)  # Field name made lowercase.
    ca_m_money = models.CharField(db_column='CA_M_Money', max_length=3, blank=True, null=True)  # Field name made lowercase.
    ca_closed = models.CharField(db_column='CA_Closed', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ca_post_date = models.DateField(db_column='CA_Post_Date', blank=True, null=True)  # Field name made lowercase.
    ca_rob_amount = models.DecimalField(db_column='CA_Rob_Amount', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ca_pur_date1 = models.DateField(db_column='CA_Pur_Date1', blank=True, null=True)  # Field name made lowercase.
    ca_pur_desc1 = models.CharField(db_column='CA_Pur_Desc1', max_length=32, blank=True, null=True)  # Field name made lowercase.
    ca_pur_amnt1 = models.DecimalField(db_column='CA_Pur_Amnt1', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ca_pur_date2 = models.DateField(db_column='CA_Pur_Date2', blank=True, null=True)  # Field name made lowercase.
    ca_pur_desc2 = models.CharField(db_column='CA_Pur_Desc2', max_length=32, blank=True, null=True)  # Field name made lowercase.
    ca_pur_amnt2 = models.DecimalField(db_column='CA_Pur_Amnt2', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ca_pur_date3 = models.DateField(db_column='CA_Pur_Date3', blank=True, null=True)  # Field name made lowercase.
    ca_pur_desc3 = models.CharField(db_column='CA_Pur_Desc3', max_length=32, blank=True, null=True)  # Field name made lowercase.
    ca_pur_amnt3 = models.DecimalField(db_column='CA_Pur_Amnt3', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ca_pur_date4 = models.DateField(db_column='CA_Pur_Date4', blank=True, null=True)  # Field name made lowercase.
    ca_pur_desc4 = models.CharField(db_column='CA_Pur_Desc4', max_length=32, blank=True, null=True)  # Field name made lowercase.
    ca_pur_amnt4 = models.DecimalField(db_column='CA_Pur_Amnt4', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ca_pur_date5 = models.DateField(db_column='CA_Pur_Date5', blank=True, null=True)  # Field name made lowercase.
    ca_pur_desc5 = models.CharField(db_column='CA_Pur_Desc5', max_length=32, blank=True, null=True)  # Field name made lowercase.
    ca_pur_amnt5 = models.DecimalField(db_column='CA_Pur_Amnt5', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ca_disb_date1 = models.DateField(db_column='CA_Disb_Date1', blank=True, null=True)  # Field name made lowercase.
    ca_disb_desc1 = models.CharField(db_column='CA_Disb_Desc1', max_length=32, blank=True, null=True)  # Field name made lowercase.
    ca_disb_amnt1 = models.DecimalField(db_column='CA_Disb_Amnt1', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ca_disb_date2 = models.DateField(db_column='CA_Disb_Date2', blank=True, null=True)  # Field name made lowercase.
    ca_disb_desc2 = models.CharField(db_column='CA_Disb_Desc2', max_length=32, blank=True, null=True)  # Field name made lowercase.
    ca_disb_amnt2 = models.DecimalField(db_column='CA_Disb_Amnt2', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ca_disb_date3 = models.DateField(db_column='CA_Disb_Date3', blank=True, null=True)  # Field name made lowercase.
    ca_disb_desc3 = models.CharField(db_column='CA_Disb_Desc3', max_length=32, blank=True, null=True)  # Field name made lowercase.
    ca_disb_amnt3 = models.DecimalField(db_column='CA_Disb_Amnt3', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ca_disb_date4 = models.DateField(db_column='CA_Disb_Date4', blank=True, null=True)  # Field name made lowercase.
    ca_disb_desc4 = models.CharField(db_column='CA_Disb_Desc4', max_length=32, blank=True, null=True)  # Field name made lowercase.
    ca_disb_amnt4 = models.DecimalField(db_column='CA_Disb_Amnt4', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ca_disb_date5 = models.DateField(db_column='CA_Disb_Date5', blank=True, null=True)  # Field name made lowercase.
    ca_disb_desc5 = models.CharField(db_column='CA_Disb_Desc5', max_length=32, blank=True, null=True)  # Field name made lowercase.
    ca_disb_amnt5 = models.DecimalField(db_column='CA_Disb_Amnt5', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ca_crew_amnt = models.DecimalField(db_column='CA_Crew_Amnt', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ca_curr_amnt = models.DecimalField(db_column='CA_Curr_Amnt', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ca_time_last = models.TimeField(db_column='CA_Time_Last', blank=True, null=True)  # Field name made lowercase.
    ca_who_last = models.CharField(db_column='CA_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cash'
        unique_together = (('CA_REC', 'CA_UNIQUE', 'CA_UNIQUE_1'),)


class Cba(models.Model):
    cba_d = models.CharField(db_column='CBA_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cba_key = models.CharField(db_column='CBA_KEY', primary_key=True, max_length=12)  # Field name made lowercase.
    cba_full = models.CharField(db_column='CBA_Full', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cba_time_last = models.TimeField(db_column='CBA_Time_Last', blank=True, null=True)  # Field name made lowercase.
    cba_who_last = models.CharField(db_column='CBA_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cba'


class Cert(models.Model):
    c_d = models.CharField(db_column='C_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    c_key = models.CharField(db_column='C_KEY', primary_key=True, max_length=4)  # Field name made lowercase.
    c_full = models.CharField(db_column='C_Full', max_length=50, blank=True, null=True)  # Field name made lowercase.
    c_book = models.CharField(db_column='C_Book', max_length=1, blank=True, null=True)  # Field name made lowercase.
    c_main = models.CharField(db_column='C_Main', max_length=1, blank=True, null=True)  # Field name made lowercase.
    c_expires = models.CharField(db_column='C_Expires', max_length=1, blank=True, null=True)  # Field name made lowercase.
    c_interval_years = models.DecimalField(db_column='C_Interval_Years', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    c_interval_months = models.DecimalField(db_column='C_Interval_Months', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    c_time_last = models.TimeField(db_column='C_Time_Last', blank=True, null=True)  # Field name made lowercase.
    c_who_last = models.CharField(db_column='C_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cert'


class Cgdets(models.Model):
    cgd_d = models.CharField(db_column='CGD_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cgd_rec = models.IntegerField(db_column='CGD_REC')  # Field name made lowercase.
    cgd_unique = models.CharField(db_column='CGD_UNIQUE', max_length=9)  # Field name made lowercase.
    cgd_cg_key = models.CharField(db_column='CGD_CG_KEY', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cgd_cert_c_key = models.CharField(db_column='CGD_Cert_C_Key', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cgd_weight = models.CharField(db_column='CGD_Weight', max_length=5, blank=True, null=True)  # Field name made lowercase.
    cgd_vc_key = models.CharField(db_column='CGD_VC_KEY', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cgd_tags = models.CharField(db_column='CGD_Tags', max_length=16, blank=True, null=True)  # Field name made lowercase.
    cgd_time_last = models.TimeField(db_column='CGD_Time_Last', blank=True, null=True)  # Field name made lowercase.
    cgd_who_last = models.CharField(db_column='CGD_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cgdets'
        unique_together = (('CGD_REC', 'CGD_UNIQUE'),)


class Cghead(models.Model):
    cg_d = models.CharField(db_column='CG_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cg_key = models.CharField(db_column='CG_KEY', primary_key=True, max_length=4)  # Field name made lowercase.
    cg_full = models.CharField(db_column='CG_Full', max_length=64, blank=True, null=True)  # Field name made lowercase.
    cg_time_last = models.TimeField(db_column='CG_Time_Last', blank=True, null=True)  # Field name made lowercase.
    cg_who_last = models.CharField(db_column='CG_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cghead'


class Comp(models.Model):
    co_d = models.CharField(db_column='CO_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    co_key = models.CharField(db_column='CO_KEY', primary_key=True, max_length=3)  # Field name made lowercase.
    co_full = models.CharField(db_column='CO_Full', max_length=40, blank=True, null=True)  # Field name made lowercase.
    co_full_grk = models.CharField(db_column='CO_Full_GRK', max_length=40, blank=True, null=True)  # Field name made lowercase.
    co_cs_key = models.CharField(db_column='CO_CS_KEY', max_length=2, blank=True, null=True)  # Field name made lowercase.
    co_sort = models.IntegerField(db_column='CO_Sort', blank=True, null=True)  # Field name made lowercase.
    co_table = models.CharField(db_column='CO_Table', max_length=1, blank=True, null=True)  # Field name made lowercase.
    co_skip = models.CharField(db_column='CO_Skip', max_length=1, blank=True, null=True)  # Field name made lowercase.
    co_taxable = models.CharField(db_column='CO_Taxable', max_length=1, blank=True, null=True)  # Field name made lowercase.
    co_who_pays = models.CharField(db_column='CO_Who_Pays', max_length=1, blank=True, null=True)  # Field name made lowercase.
    co_is_tax = models.CharField(db_column='CO_Is_Tax', max_length=1, blank=True, null=True)  # Field name made lowercase.
    co_prt_monthly = models.CharField(db_column='CO_Prt_Monthly', max_length=1, blank=True, null=True)  # Field name made lowercase.
    co_prt_contract_gca = models.CharField(db_column='CO_Prt_Contract_GCA', max_length=1, blank=True, null=True)  # Field name made lowercase.
    co_prt_payroll = models.CharField(db_column='CO_Prt_Payroll', max_length=1, blank=True, null=True)  # Field name made lowercase.
    co_prt_r_payroll = models.CharField(db_column='CO_Prt_R_Payroll', max_length=1, blank=True, null=True)  # Field name made lowercase.
    co_prt_retro = models.CharField(db_column='CO_Prt_Retro', max_length=1, blank=True, null=True)  # Field name made lowercase.
    co_prt_article = models.CharField(db_column='CO_Prt_Article', max_length=1, blank=True, null=True)  # Field name made lowercase.
    co_prt_clone = models.CharField(db_column='CO_Prt_Clone', max_length=1, blank=True, null=True)  # Field name made lowercase.
    co_prt_quest3 = models.CharField(db_column='CO_Prt_Quest3', max_length=1, blank=True, null=True)  # Field name made lowercase.
    co_prt_quest4 = models.CharField(db_column='CO_Prt_Quest4', max_length=1, blank=True, null=True)  # Field name made lowercase.
    co_prt_quest5 = models.CharField(db_column='CO_Prt_Quest5', max_length=1, blank=True, null=True)  # Field name made lowercase.
    co_mon_amnt = models.CharField(db_column='CO_Mon_Amnt', max_length=20, blank=True, null=True)  # Field name made lowercase.
    co_tot_amnt = models.CharField(db_column='CO_Tot_Amnt', max_length=20, blank=True, null=True)  # Field name made lowercase.
    co_fld_depend1 = models.CharField(db_column='CO_Fld_Depend1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    co_fld_depend2 = models.CharField(db_column='CO_Fld_Depend2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    co_fld_change1 = models.CharField(db_column='CO_Fld_Change1', max_length=20, blank=True, null=True)  # Field name made lowercase.
    co_fld_change2 = models.CharField(db_column='CO_Fld_Change2', max_length=20, blank=True, null=True)  # Field name made lowercase.
    co_fld_special = models.CharField(db_column='CO_Fld_Special', max_length=80, blank=True, null=True)  # Field name made lowercase.
    co_time_last = models.TimeField(db_column='CO_Time_Last', blank=True, null=True)  # Field name made lowercase.
    co_who_last = models.CharField(db_column='CO_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'comp'


class Contract(models.Model):
    con_d = models.CharField(db_column='CON_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    con_rec = models.IntegerField(db_column='CON_REC')  # Field name made lowercase.
    con_unique = models.CharField(db_column='CON_UNIQUE', max_length=10)  # Field name made lowercase.
    con_unique_1 = models.CharField(db_column='CON_UNIQUE_1', max_length=29)  # Field name made lowercase.
    con_number = models.IntegerField(db_column='CON_Number', blank=True, null=True)  # Field name made lowercase.
    con_seq_no = models.IntegerField(db_column='CON_Seq_No', blank=True, null=True)  # Field name made lowercase.
    con_b_id = models.CharField(db_column='CON_B_ID', max_length=4, blank=True, null=True)  # Field name made lowercase.
    con_w_cs_key = models.CharField(db_column='CON_W_CS_KEY', max_length=2, blank=True, null=True)  # Field name made lowercase.
    con_t_cs_key = models.CharField(db_column='CON_T_CS_KEY', max_length=2, blank=True, null=True)  # Field name made lowercase.
    con_man_key = models.CharField(db_column='CON_MAN_KEY', max_length=4, blank=True, null=True)  # Field name made lowercase.
    con_prin_p_key = models.CharField(db_column='CON_Prin_P_KEY', max_length=6, blank=True, null=True)  # Field name made lowercase.
    con_master_p_key = models.CharField(db_column='CON_Master_P_KEY', max_length=6, blank=True, null=True)  # Field name made lowercase.
    con_wage_w_rec = models.DecimalField(db_column='CON_Wage_W_REC', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_vsl_v_key = models.CharField(db_column='CON_Vsl_V_KEY', max_length=4, blank=True, null=True)  # Field name made lowercase.
    con_rank_r_key = models.CharField(db_column='CON_Rank_R_KEY', max_length=4, blank=True, null=True)  # Field name made lowercase.
    con_crew_category = models.CharField(db_column='CON_Crew_Category', max_length=1, blank=True, null=True)  # Field name made lowercase.
    con_m_money = models.CharField(db_column='CON_M_Money', max_length=3, blank=True, null=True)  # Field name made lowercase.
    con_length = models.IntegerField(db_column='CON_Length', blank=True, null=True)  # Field name made lowercase.
    con_pdos = models.DateField(db_column='CON_PDOS', blank=True, null=True)  # Field name made lowercase.
    con_money_beg = models.DateField(db_column='CON_Money_Beg', blank=True, null=True)  # Field name made lowercase.
    con_embark = models.DateField(db_column='CON_Embark', blank=True, null=True)  # Field name made lowercase.
    con_embark_com = models.CharField(db_column='CON_Embark_Com', max_length=80, blank=True, null=True)  # Field name made lowercase.
    con_join = models.DateField(db_column='CON_Join', blank=True, null=True)  # Field name made lowercase.
    con_join_where = models.CharField(db_column='CON_Join_Where', max_length=16, blank=True, null=True)  # Field name made lowercase.
    con_left = models.DateField(db_column='CON_Left', blank=True, null=True)  # Field name made lowercase.
    con_left_where = models.CharField(db_column='CON_Left_Where', max_length=16, blank=True, null=True)  # Field name made lowercase.
    con_disembark = models.DateField(db_column='CON_Disembark', blank=True, null=True)  # Field name made lowercase.
    con_disembark_com = models.CharField(db_column='CON_Disembark_Com', max_length=80, blank=True, null=True)  # Field name made lowercase.
    con_money_end = models.DateField(db_column='CON_Money_End', blank=True, null=True)  # Field name made lowercase.
    con_reason_signoff = models.CharField(db_column='CON_Reason_Signoff', max_length=20, blank=True, null=True)  # Field name made lowercase.
    con_date_fitness = models.DateField(db_column='CON_Date_Fitness', blank=True, null=True)  # Field name made lowercase.
    con_contract_date = models.DateField(db_column='CON_Contract_Date', blank=True, null=True)  # Field name made lowercase.
    con_poea_date = models.DateField(db_column='CON_POEA_Date', blank=True, null=True)  # Field name made lowercase.
    con_oec = models.IntegerField(db_column='CON_OEC', blank=True, null=True)  # Field name made lowercase.
    con_last_eval_rcv = models.CharField(db_column='CON_Last_Eval_Rcv', max_length=1, blank=True, null=True)  # Field name made lowercase.
    con_seniority = models.IntegerField(db_column='CON_Seniority', blank=True, null=True)  # Field name made lowercase.
    con_senior_date = models.DateField(db_column='CON_Senior_Date', blank=True, null=True)  # Field name made lowercase.
    con_mth_basic = models.DecimalField(db_column='CON_Mth_Basic', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_mth_extra1 = models.DecimalField(db_column='CON_Mth_Extra1', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_mth_extra1_descr = models.CharField(db_column='CON_Mth_Extra1_Descr', max_length=32, blank=True, null=True)  # Field name made lowercase.
    con_mth_extra2 = models.DecimalField(db_column='CON_Mth_Extra2', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_mth_extra2_descr = models.CharField(db_column='CON_Mth_Extra2_Descr', max_length=32, blank=True, null=True)  # Field name made lowercase.
    con_fix_mth_ot = models.DecimalField(db_column='CON_Fix_Mth_OT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_hourly_ot_rate = models.DecimalField(db_column='CON_Hourly_OT_Rate', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_min_mth_ot_hours = models.IntegerField(db_column='CON_Min_Mth_OT_Hours', blank=True, null=True)  # Field name made lowercase.
    con_hours_week = models.IntegerField(db_column='CON_Hours_Week', blank=True, null=True)  # Field name made lowercase.
    con_comp_type_1 = models.CharField(db_column='CON_Comp_Type_1', max_length=3, blank=True, null=True)  # Field name made lowercase.
    con_comp_name_1 = models.CharField(db_column='CON_Comp_Name_1', max_length=16, blank=True, null=True)  # Field name made lowercase.
    con_comp_amnt_1 = models.DecimalField(db_column='CON_Comp_Amnt_1', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_comp_type_2 = models.CharField(db_column='CON_Comp_Type_2', max_length=3, blank=True, null=True)  # Field name made lowercase.
    con_comp_name_2 = models.CharField(db_column='CON_Comp_Name_2', max_length=16, blank=True, null=True)  # Field name made lowercase.
    con_comp_amnt_2 = models.DecimalField(db_column='CON_Comp_Amnt_2', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_comp_type_3 = models.CharField(db_column='CON_Comp_Type_3', max_length=3, blank=True, null=True)  # Field name made lowercase.
    con_comp_name_3 = models.CharField(db_column='CON_Comp_Name_3', max_length=16, blank=True, null=True)  # Field name made lowercase.
    con_comp_amnt_3 = models.DecimalField(db_column='CON_Comp_Amnt_3', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_comp_type_4 = models.CharField(db_column='CON_Comp_Type_4', max_length=3, blank=True, null=True)  # Field name made lowercase.
    con_comp_name_4 = models.CharField(db_column='CON_Comp_Name_4', max_length=16, blank=True, null=True)  # Field name made lowercase.
    con_comp_amnt_4 = models.DecimalField(db_column='CON_Comp_Amnt_4', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_comp_type_5 = models.CharField(db_column='CON_Comp_Type_5', max_length=3, blank=True, null=True)  # Field name made lowercase.
    con_comp_name_5 = models.CharField(db_column='CON_Comp_Name_5', max_length=16, blank=True, null=True)  # Field name made lowercase.
    con_comp_amnt_5 = models.DecimalField(db_column='CON_Comp_Amnt_5', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_comp_type_6 = models.CharField(db_column='CON_Comp_Type_6', max_length=3, blank=True, null=True)  # Field name made lowercase.
    con_comp_name_6 = models.CharField(db_column='CON_Comp_Name_6', max_length=16, blank=True, null=True)  # Field name made lowercase.
    con_comp_amnt_6 = models.DecimalField(db_column='CON_Comp_Amnt_6', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_comp_type_7 = models.CharField(db_column='CON_Comp_Type_7', max_length=3, blank=True, null=True)  # Field name made lowercase.
    con_comp_name_7 = models.CharField(db_column='CON_Comp_Name_7', max_length=16, blank=True, null=True)  # Field name made lowercase.
    con_comp_amnt_7 = models.DecimalField(db_column='CON_Comp_Amnt_7', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_comp_type_8 = models.CharField(db_column='CON_Comp_Type_8', max_length=3, blank=True, null=True)  # Field name made lowercase.
    con_comp_name_8 = models.CharField(db_column='CON_Comp_Name_8', max_length=16, blank=True, null=True)  # Field name made lowercase.
    con_comp_amnt_8 = models.DecimalField(db_column='CON_Comp_Amnt_8', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_comp_type_9 = models.CharField(db_column='CON_Comp_Type_9', max_length=3, blank=True, null=True)  # Field name made lowercase.
    con_comp_name_9 = models.CharField(db_column='CON_Comp_Name_9', max_length=16, blank=True, null=True)  # Field name made lowercase.
    con_comp_amnt_9 = models.DecimalField(db_column='CON_Comp_Amnt_9', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_comp_type_10 = models.CharField(db_column='CON_Comp_Type_10', max_length=3, blank=True, null=True)  # Field name made lowercase.
    con_comp_name_10 = models.CharField(db_column='CON_Comp_Name_10', max_length=16, blank=True, null=True)  # Field name made lowercase.
    con_comp_amnt_10 = models.DecimalField(db_column='CON_Comp_Amnt_10', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_comp_type_11 = models.CharField(db_column='CON_Comp_Type_11', max_length=3, blank=True, null=True)  # Field name made lowercase.
    con_comp_name_11 = models.CharField(db_column='CON_Comp_Name_11', max_length=16, blank=True, null=True)  # Field name made lowercase.
    con_comp_amnt_11 = models.DecimalField(db_column='CON_Comp_Amnt_11', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_comp_type_12 = models.CharField(db_column='CON_Comp_Type_12', max_length=3, blank=True, null=True)  # Field name made lowercase.
    con_comp_name_12 = models.CharField(db_column='CON_Comp_Name_12', max_length=16, blank=True, null=True)  # Field name made lowercase.
    con_comp_amnt_12 = models.DecimalField(db_column='CON_Comp_Amnt_12', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_comp_type_13 = models.CharField(db_column='CON_Comp_Type_13', max_length=3, blank=True, null=True)  # Field name made lowercase.
    con_comp_name_13 = models.CharField(db_column='CON_Comp_Name_13', max_length=16, blank=True, null=True)  # Field name made lowercase.
    con_comp_amnt_13 = models.DecimalField(db_column='CON_Comp_Amnt_13', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_comp_type_14 = models.CharField(db_column='CON_Comp_Type_14', max_length=3, blank=True, null=True)  # Field name made lowercase.
    con_comp_name_14 = models.CharField(db_column='CON_Comp_Name_14', max_length=16, blank=True, null=True)  # Field name made lowercase.
    con_comp_amnt_14 = models.DecimalField(db_column='CON_Comp_Amnt_14', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_comp_type_15 = models.CharField(db_column='CON_Comp_Type_15', max_length=3, blank=True, null=True)  # Field name made lowercase.
    con_comp_name_15 = models.CharField(db_column='CON_Comp_Name_15', max_length=16, blank=True, null=True)  # Field name made lowercase.
    con_comp_amnt_15 = models.DecimalField(db_column='CON_Comp_Amnt_15', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_comp_type_16 = models.CharField(db_column='CON_Comp_Type_16', max_length=3, blank=True, null=True)  # Field name made lowercase.
    con_comp_name_16 = models.CharField(db_column='CON_Comp_Name_16', max_length=16, blank=True, null=True)  # Field name made lowercase.
    con_comp_amnt_16 = models.DecimalField(db_column='CON_Comp_Amnt_16', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_comp_type_17 = models.CharField(db_column='CON_Comp_Type_17', max_length=3, blank=True, null=True)  # Field name made lowercase.
    con_comp_name_17 = models.CharField(db_column='CON_Comp_Name_17', max_length=16, blank=True, null=True)  # Field name made lowercase.
    con_comp_amnt_17 = models.DecimalField(db_column='CON_Comp_Amnt_17', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_comp_type_18 = models.CharField(db_column='CON_Comp_Type_18', max_length=3, blank=True, null=True)  # Field name made lowercase.
    con_comp_name_18 = models.CharField(db_column='CON_Comp_Name_18', max_length=16, blank=True, null=True)  # Field name made lowercase.
    con_comp_amnt_18 = models.DecimalField(db_column='CON_Comp_Amnt_18', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_comp_type_19 = models.CharField(db_column='CON_Comp_Type_19', max_length=3, blank=True, null=True)  # Field name made lowercase.
    con_comp_name_19 = models.CharField(db_column='CON_Comp_Name_19', max_length=16, blank=True, null=True)  # Field name made lowercase.
    con_comp_amnt_19 = models.DecimalField(db_column='CON_Comp_Amnt_19', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_comp_type_20 = models.CharField(db_column='CON_Comp_Type_20', max_length=3, blank=True, null=True)  # Field name made lowercase.
    con_comp_name_20 = models.CharField(db_column='CON_Comp_Name_20', max_length=16, blank=True, null=True)  # Field name made lowercase.
    con_comp_amnt_20 = models.DecimalField(db_column='CON_Comp_Amnt_20', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_comp_type_21 = models.CharField(db_column='CON_Comp_Type_21', max_length=3, blank=True, null=True)  # Field name made lowercase.
    con_comp_name_21 = models.CharField(db_column='CON_Comp_Name_21', max_length=16, blank=True, null=True)  # Field name made lowercase.
    con_comp_amnt_21 = models.DecimalField(db_column='CON_Comp_Amnt_21', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_comp_type_22 = models.CharField(db_column='CON_Comp_Type_22', max_length=3, blank=True, null=True)  # Field name made lowercase.
    con_comp_name_22 = models.CharField(db_column='CON_Comp_Name_22', max_length=16, blank=True, null=True)  # Field name made lowercase.
    con_comp_amnt_22 = models.DecimalField(db_column='CON_Comp_Amnt_22', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_comp_type_23 = models.CharField(db_column='CON_Comp_Type_23', max_length=3, blank=True, null=True)  # Field name made lowercase.
    con_comp_name_23 = models.CharField(db_column='CON_Comp_Name_23', max_length=16, blank=True, null=True)  # Field name made lowercase.
    con_comp_amnt_23 = models.DecimalField(db_column='CON_Comp_Amnt_23', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_comp_type_24 = models.CharField(db_column='CON_Comp_Type_24', max_length=3, blank=True, null=True)  # Field name made lowercase.
    con_comp_name_24 = models.CharField(db_column='CON_Comp_Name_24', max_length=16, blank=True, null=True)  # Field name made lowercase.
    con_comp_amnt_24 = models.DecimalField(db_column='CON_Comp_Amnt_24', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_pays_nat = models.CharField(db_column='CON_Pays_NAT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    con_pays_seaman_home = models.CharField(db_column='CON_Pays_Seaman_Home', max_length=1, blank=True, null=True)  # Field name made lowercase.
    con_pays_fmy = models.CharField(db_column='CON_Pays_FMY', max_length=1, blank=True, null=True)  # Field name made lowercase.
    con_pays_tax = models.CharField(db_column='CON_Pays_TAX', max_length=1, blank=True, null=True)  # Field name made lowercase.
    con_pays_pno = models.CharField(db_column='CON_Pays_PNO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    con_leave_onsignoff = models.CharField(db_column='CON_Leave_OnSignoff', max_length=1, blank=True, null=True)  # Field name made lowercase.
    con_seniority_rank = models.IntegerField(db_column='CON_Seniority_Rank', blank=True, null=True)  # Field name made lowercase.
    con_senior_rank_date = models.DateField(db_column='CON_Senior_Rank_Date', blank=True, null=True)  # Field name made lowercase.
    con_ereceipt = models.IntegerField(db_column='CON_EReceipt', blank=True, null=True)  # Field name made lowercase.
    con_cba = models.CharField(db_column='CON_CBA', max_length=12, blank=True, null=True)  # Field name made lowercase.
    con_bmi = models.DecimalField(db_column='CON_BMI', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_cash_advance = models.DecimalField(db_column='CON_Cash_Advance', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_tax_anal = models.DecimalField(db_column='CON_Tax_Anal', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_p_alo = models.DecimalField(db_column='CON_P_ALO', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_balance_total = models.DecimalField(db_column='CON_Balance_Total', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_balance_amt_cur1 = models.DecimalField(db_column='CON_Balance_Amt_Cur1', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_balance_cur1 = models.CharField(db_column='CON_Balance_Cur1', max_length=3, blank=True, null=True)  # Field name made lowercase.
    con_balance_amt_cur2 = models.DecimalField(db_column='CON_Balance_Amt_Cur2', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_balance_cur2 = models.CharField(db_column='CON_Balance_Cur2', max_length=3, blank=True, null=True)  # Field name made lowercase.
    con_balance_amt_cur3 = models.DecimalField(db_column='CON_Balance_Amt_Cur3', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_balance_cur3 = models.CharField(db_column='CON_Balance_Cur3', max_length=3, blank=True, null=True)  # Field name made lowercase.
    con_balance_comment = models.CharField(db_column='CON_Balance_Comment', max_length=32, blank=True, null=True)  # Field name made lowercase.
    con_balance_status = models.CharField(db_column='CON_Balance_Status', max_length=1, blank=True, null=True)  # Field name made lowercase.
    con_balance_payday = models.DateField(db_column='CON_Balance_Payday', blank=True, null=True)  # Field name made lowercase.
    con_retro1_from = models.DateField(db_column='CON_Retro1_From', blank=True, null=True)  # Field name made lowercase.
    con_retro1_to = models.DateField(db_column='CON_Retro1_To', blank=True, null=True)  # Field name made lowercase.
    con_retro1_total = models.DecimalField(db_column='CON_Retro1_Total', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_retro1_amt_cur1 = models.DecimalField(db_column='CON_Retro1_Amt_Cur1', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_retro1_cur1 = models.CharField(db_column='CON_Retro1_Cur1', max_length=3, blank=True, null=True)  # Field name made lowercase.
    con_retro1_amt_cur2 = models.DecimalField(db_column='CON_Retro1_Amt_Cur2', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_retro1_cur2 = models.CharField(db_column='CON_Retro1_Cur2', max_length=3, blank=True, null=True)  # Field name made lowercase.
    con_retro1_amt_cur3 = models.DecimalField(db_column='CON_Retro1_Amt_Cur3', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_retro1_cur3 = models.CharField(db_column='CON_Retro1_Cur3', max_length=3, blank=True, null=True)  # Field name made lowercase.
    con_retro1_status = models.CharField(db_column='CON_Retro1_Status', max_length=1, blank=True, null=True)  # Field name made lowercase.
    con_retro1_payday = models.DateField(db_column='CON_Retro1_Payday', blank=True, null=True)  # Field name made lowercase.
    con_retro1_comment = models.CharField(db_column='CON_Retro1_Comment', max_length=32, blank=True, null=True)  # Field name made lowercase.
    con_retro2_from = models.DateField(db_column='CON_Retro2_From', blank=True, null=True)  # Field name made lowercase.
    con_retro2_to = models.DateField(db_column='CON_Retro2_To', blank=True, null=True)  # Field name made lowercase.
    con_retro2_total = models.DecimalField(db_column='CON_Retro2_Total', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_retro2_amt_cur1 = models.DecimalField(db_column='CON_Retro2_Amt_Cur1', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_retro2_cur1 = models.CharField(db_column='CON_Retro2_Cur1', max_length=3, blank=True, null=True)  # Field name made lowercase.
    con_retro2_amt_cur2 = models.DecimalField(db_column='CON_Retro2_Amt_Cur2', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_retro2_cur2 = models.CharField(db_column='CON_Retro2_Cur2', max_length=3, blank=True, null=True)  # Field name made lowercase.
    con_retro2_amt_cur3 = models.DecimalField(db_column='CON_Retro2_Amt_Cur3', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_retro2_cur3 = models.CharField(db_column='CON_Retro2_Cur3', max_length=3, blank=True, null=True)  # Field name made lowercase.
    con_retro2_status = models.CharField(db_column='CON_Retro2_Status', max_length=1, blank=True, null=True)  # Field name made lowercase.
    con_retro2_payday = models.DateField(db_column='CON_Retro2_Payday', blank=True, null=True)  # Field name made lowercase.
    con_retro2_comment = models.CharField(db_column='CON_Retro2_Comment', max_length=32, blank=True, null=True)  # Field name made lowercase.
    con_retro3_from = models.DateField(db_column='CON_Retro3_From', blank=True, null=True)  # Field name made lowercase.
    con_retro3_to = models.DateField(db_column='CON_Retro3_To', blank=True, null=True)  # Field name made lowercase.
    con_retro3_total = models.DecimalField(db_column='CON_Retro3_Total', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_retro3_amt_cur1 = models.DecimalField(db_column='CON_Retro3_Amt_Cur1', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_retro3_cur1 = models.CharField(db_column='CON_Retro3_Cur1', max_length=3, blank=True, null=True)  # Field name made lowercase.
    con_retro3_amt_cur2 = models.DecimalField(db_column='CON_Retro3_Amt_Cur2', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_retro3_cur2 = models.CharField(db_column='CON_Retro3_Cur2', max_length=3, blank=True, null=True)  # Field name made lowercase.
    con_retro3_amt_cur3 = models.DecimalField(db_column='CON_Retro3_Amt_Cur3', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    con_retro3_cur3 = models.CharField(db_column='CON_Retro3_Cur3', max_length=3, blank=True, null=True)  # Field name made lowercase.
    con_retro3_status = models.CharField(db_column='CON_Retro3_Status', max_length=1, blank=True, null=True)  # Field name made lowercase.
    con_retro3_payday = models.DateField(db_column='CON_Retro3_Payday', blank=True, null=True)  # Field name made lowercase.
    con_retro3_comment = models.CharField(db_column='CON_Retro3_Comment', max_length=32, blank=True, null=True)  # Field name made lowercase.
    con_time_last = models.TimeField(db_column='CON_Time_Last', blank=True, null=True)  # Field name made lowercase.
    con_who_last = models.CharField(db_column='CON_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'contract'
        unique_together = (('CON_REC', 'CON_UNIQUE', 'CON_UNIQUE_1'),)


class Country(models.Model):
    cn_d = models.CharField(db_column='CN_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cn_key = models.CharField(db_column='CN_KEY', primary_key=True, max_length=2)  # Field name made lowercase.
    cn_full = models.CharField(db_column='CN_Full', max_length=45, blank=True, null=True)  # Field name made lowercase.
    cn_nationality = models.CharField(db_column='CN_Nationality', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cn_time_last = models.TimeField(db_column='CN_Time_Last', blank=True, null=True)  # Field name made lowercase.
    cn_who_last = models.CharField(db_column='CN_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'country'


class Cscale(models.Model):
    cs_d = models.CharField(db_column='CS_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cs_key = models.CharField(db_column='CS_KEY', primary_key=True, max_length=2)  # Field name made lowercase.
    cs_full = models.CharField(db_column='CS_Full', max_length=40, blank=True, null=True)  # Field name made lowercase.
    cs_time_last = models.TimeField(db_column='CS_Time_Last', blank=True, null=True)  # Field name made lowercase.
    cs_who_last = models.CharField(db_column='CS_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cscale'


class Depend(models.Model):
    dep_d = models.CharField(db_column='DEP_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    dep_rec = models.IntegerField(db_column='DEP_REC', primary_key=True)  # Field name made lowercase.
    dep_id_b_id = models.CharField(db_column='DEP_ID_B_ID', max_length=4, blank=True, null=True)  # Field name made lowercase.
    dep_rel_key = models.CharField(db_column='DEP_REL_KEY', max_length=4, blank=True, null=True)  # Field name made lowercase.
    dep_birth_date = models.DateField(db_column='DEP_Birth_Date', blank=True, null=True)  # Field name made lowercase.
    dep_firstnm = models.CharField(db_column='DEP_FirstNm', max_length=28, blank=True, null=True)  # Field name made lowercase.
    dep_lastnm = models.CharField(db_column='DEP_LastNm', max_length=20, blank=True, null=True)  # Field name made lowercase.
    dep_fathernm = models.CharField(db_column='DEP_FatherNm', max_length=18, blank=True, null=True)  # Field name made lowercase.
    dep_time_last = models.TimeField(db_column='DEP_Time_Last', blank=True, null=True)  # Field name made lowercase.
    dep_who_last = models.CharField(db_column='DEP_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'depend'



class Doc(models.Model):
    d_d = models.CharField(db_column='D_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    d_rec = models.IntegerField(db_column='D_REC', primary_key=True)  # Field name made lowercase.
    d_unique = models.CharField(db_column='D_UNIQUE', max_length=9, blank=True, null=True)  # Field name made lowercase.
    d_id_b_id = models.CharField(db_column='D_ID_B_ID', max_length=4, blank=True, null=True)  # Field name made lowercase.
    d_cert_c_key = models.CharField(db_column='D_Cert_C_KEY', max_length=4, blank=True, null=True)  # Field name made lowercase.
    d_number = models.CharField(db_column='D_Number', max_length=32, blank=True, null=True)  # Field name made lowercase.
    d_rank_r_key = models.CharField(db_column='D_Rank_R_KEY', max_length=4, blank=True, null=True)  # Field name made lowercase.
    d_issue = models.DateField(db_column='D_Issue', blank=True, null=True)  # Field name made lowercase.
    d_expire = models.DateField(db_column='D_Expire', blank=True, null=True)  # Field name made lowercase.
    d_othercountry = models.CharField(db_column='D_OtherCountry', max_length=2, blank=True, null=True)  # Field name made lowercase.
    d_time_last = models.TimeField(db_column='D_Time_Last', blank=True, null=True)  # Field name made lowercase.
    d_who_last = models.CharField(db_column='D_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'doc'


class Eval(models.Model):
    e_d = models.CharField(db_column='E_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    e_rec = models.IntegerField(db_column='E_REC')  # Field name made lowercase.
    e_unique = models.CharField(db_column='E_UNIQUE', max_length=13)  # Field name made lowercase.
    e_b_id = models.CharField(db_column='E_B_ID', max_length=4, blank=True, null=True)  # Field name made lowercase.
    e_date = models.DateField(db_column='E_Date', blank=True, null=True)  # Field name made lowercase.
    e_rep_key1 = models.CharField(db_column='E_REP_KEY1', max_length=4, blank=True, null=True)  # Field name made lowercase.
    e_rep_key2 = models.CharField(db_column='E_REP_KEY2', max_length=4, blank=True, null=True)  # Field name made lowercase.
    e_v_key = models.CharField(db_column='E_V_KEY', max_length=4, blank=True, null=True)  # Field name made lowercase.
    e_r_key = models.CharField(db_column='E_R_KEY', max_length=4, blank=True, null=True)  # Field name made lowercase.
    e_version = models.IntegerField(db_column='E_Version', blank=True, null=True)  # Field name made lowercase.
    e_which = models.CharField(db_column='E_Which', max_length=1, blank=True, null=True)  # Field name made lowercase.
    e_begin = models.DateField(db_column='E_Begin', blank=True, null=True)  # Field name made lowercase.
    e_end = models.DateField(db_column='E_End', blank=True, null=True)  # Field name made lowercase.
    e_general_remark1 = models.CharField(db_column='E_General_Remark1', max_length=126, blank=True, null=True)  # Field name made lowercase.
    e_general_remark2 = models.CharField(db_column='E_General_Remark2', max_length=126, blank=True, null=True)  # Field name made lowercase.
    e_component1 = models.CharField(db_column='E_Component1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    e_grade1 = models.CharField(db_column='E_Grade1', max_length=1, blank=True, null=True)  # Field name made lowercase.
    e_choices1 = models.CharField(db_column='E_Choices1', max_length=6, blank=True, null=True)  # Field name made lowercase.
    e_component2 = models.CharField(db_column='E_Component2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    e_grade2 = models.CharField(db_column='E_Grade2', max_length=1, blank=True, null=True)  # Field name made lowercase.
    e_choices2 = models.CharField(db_column='E_Choices2', max_length=6, blank=True, null=True)  # Field name made lowercase.
    e_component3 = models.CharField(db_column='E_Component3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    e_grade3 = models.CharField(db_column='E_Grade3', max_length=1, blank=True, null=True)  # Field name made lowercase.
    e_choices3 = models.CharField(db_column='E_Choices3', max_length=6, blank=True, null=True)  # Field name made lowercase.
    e_component4 = models.CharField(db_column='E_Component4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    e_grade4 = models.CharField(db_column='E_Grade4', max_length=1, blank=True, null=True)  # Field name made lowercase.
    e_choices4 = models.CharField(db_column='E_Choices4', max_length=6, blank=True, null=True)  # Field name made lowercase.
    e_component5 = models.CharField(db_column='E_Component5', max_length=40, blank=True, null=True)  # Field name made lowercase.
    e_grade5 = models.CharField(db_column='E_Grade5', max_length=1, blank=True, null=True)  # Field name made lowercase.
    e_choices5 = models.CharField(db_column='E_Choices5', max_length=6, blank=True, null=True)  # Field name made lowercase.
    e_component6 = models.CharField(db_column='E_Component6', max_length=40, blank=True, null=True)  # Field name made lowercase.
    e_grade6 = models.CharField(db_column='E_Grade6', max_length=1, blank=True, null=True)  # Field name made lowercase.
    e_choices6 = models.CharField(db_column='E_Choices6', max_length=6, blank=True, null=True)  # Field name made lowercase.
    e_component7 = models.CharField(db_column='E_Component7', max_length=40, blank=True, null=True)  # Field name made lowercase.
    e_grade7 = models.CharField(db_column='E_Grade7', max_length=1, blank=True, null=True)  # Field name made lowercase.
    e_choices7 = models.CharField(db_column='E_Choices7', max_length=6, blank=True, null=True)  # Field name made lowercase.
    e_component8 = models.CharField(db_column='E_Component8', max_length=40, blank=True, null=True)  # Field name made lowercase.
    e_grade8 = models.CharField(db_column='E_Grade8', max_length=1, blank=True, null=True)  # Field name made lowercase.
    e_choices8 = models.CharField(db_column='E_Choices8', max_length=6, blank=True, null=True)  # Field name made lowercase.
    e_component9 = models.CharField(db_column='E_Component9', max_length=40, blank=True, null=True)  # Field name made lowercase.
    e_grade9 = models.CharField(db_column='E_Grade9', max_length=1, blank=True, null=True)  # Field name made lowercase.
    e_choices9 = models.CharField(db_column='E_Choices9', max_length=6, blank=True, null=True)  # Field name made lowercase.
    e_component10 = models.CharField(db_column='E_Component10', max_length=40, blank=True, null=True)  # Field name made lowercase.
    e_grade10 = models.CharField(db_column='E_Grade10', max_length=1, blank=True, null=True)  # Field name made lowercase.
    e_choices10 = models.CharField(db_column='E_Choices10', max_length=6, blank=True, null=True)  # Field name made lowercase.
    e_component11 = models.CharField(db_column='E_Component11', max_length=40, blank=True, null=True)  # Field name made lowercase.
    e_grade11 = models.CharField(db_column='E_Grade11', max_length=1, blank=True, null=True)  # Field name made lowercase.
    e_choices11 = models.CharField(db_column='E_Choices11', max_length=6, blank=True, null=True)  # Field name made lowercase.
    e_component12 = models.CharField(db_column='E_Component12', max_length=40, blank=True, null=True)  # Field name made lowercase.
    e_grade12 = models.CharField(db_column='E_Grade12', max_length=1, blank=True, null=True)  # Field name made lowercase.
    e_choices12 = models.CharField(db_column='E_Choices12', max_length=6, blank=True, null=True)  # Field name made lowercase.
    e_component13 = models.CharField(db_column='E_Component13', max_length=40, blank=True, null=True)  # Field name made lowercase.
    e_grade13 = models.CharField(db_column='E_Grade13', max_length=1, blank=True, null=True)  # Field name made lowercase.
    e_choices13 = models.CharField(db_column='E_Choices13', max_length=6, blank=True, null=True)  # Field name made lowercase.
    e_component14 = models.CharField(db_column='E_Component14', max_length=40, blank=True, null=True)  # Field name made lowercase.
    e_grade14 = models.CharField(db_column='E_Grade14', max_length=1, blank=True, null=True)  # Field name made lowercase.
    e_choices14 = models.CharField(db_column='E_Choices14', max_length=6, blank=True, null=True)  # Field name made lowercase.
    e_component15 = models.CharField(db_column='E_Component15', max_length=40, blank=True, null=True)  # Field name made lowercase.
    e_grade15 = models.CharField(db_column='E_Grade15', max_length=1, blank=True, null=True)  # Field name made lowercase.
    e_choices15 = models.CharField(db_column='E_Choices15', max_length=6, blank=True, null=True)  # Field name made lowercase.
    e_component16 = models.CharField(db_column='E_Component16', max_length=40, blank=True, null=True)  # Field name made lowercase.
    e_grade16 = models.CharField(db_column='E_Grade16', max_length=1, blank=True, null=True)  # Field name made lowercase.
    e_choices16 = models.CharField(db_column='E_Choices16', max_length=6, blank=True, null=True)  # Field name made lowercase.
    e_component17 = models.CharField(db_column='E_Component17', max_length=40, blank=True, null=True)  # Field name made lowercase.
    e_grade17 = models.CharField(db_column='E_Grade17', max_length=1, blank=True, null=True)  # Field name made lowercase.
    e_choices17 = models.CharField(db_column='E_Choices17', max_length=6, blank=True, null=True)  # Field name made lowercase.
    e_component18 = models.CharField(db_column='E_Component18', max_length=40, blank=True, null=True)  # Field name made lowercase.
    e_grade18 = models.CharField(db_column='E_Grade18', max_length=1, blank=True, null=True)  # Field name made lowercase.
    e_choices18 = models.CharField(db_column='E_Choices18', max_length=6, blank=True, null=True)  # Field name made lowercase.
    e_component19 = models.CharField(db_column='E_Component19', max_length=40, blank=True, null=True)  # Field name made lowercase.
    e_grade19 = models.CharField(db_column='E_Grade19', max_length=1, blank=True, null=True)  # Field name made lowercase.
    e_choices19 = models.CharField(db_column='E_Choices19', max_length=6, blank=True, null=True)  # Field name made lowercase.
    e_component20 = models.CharField(db_column='E_Component20', max_length=40, blank=True, null=True)  # Field name made lowercase.
    e_grade20 = models.CharField(db_column='E_Grade20', max_length=1, blank=True, null=True)  # Field name made lowercase.
    e_choices20 = models.CharField(db_column='E_Choices20', max_length=6, blank=True, null=True)  # Field name made lowercase.
    e_component21 = models.CharField(db_column='E_Component21', max_length=40, blank=True, null=True)  # Field name made lowercase.
    e_grade21 = models.CharField(db_column='E_Grade21', max_length=1, blank=True, null=True)  # Field name made lowercase.
    e_choices21 = models.CharField(db_column='E_Choices21', max_length=6, blank=True, null=True)  # Field name made lowercase.
    e_component22 = models.CharField(db_column='E_Component22', max_length=40, blank=True, null=True)  # Field name made lowercase.
    e_grade22 = models.CharField(db_column='E_Grade22', max_length=1, blank=True, null=True)  # Field name made lowercase.
    e_choices22 = models.CharField(db_column='E_Choices22', max_length=6, blank=True, null=True)  # Field name made lowercase.
    e_component23 = models.CharField(db_column='E_Component23', max_length=40, blank=True, null=True)  # Field name made lowercase.
    e_grade23 = models.CharField(db_column='E_Grade23', max_length=1, blank=True, null=True)  # Field name made lowercase.
    e_choices23 = models.CharField(db_column='E_Choices23', max_length=6, blank=True, null=True)  # Field name made lowercase.
    e_component24 = models.CharField(db_column='E_Component24', max_length=40, blank=True, null=True)  # Field name made lowercase.
    e_grade24 = models.CharField(db_column='E_Grade24', max_length=1, blank=True, null=True)  # Field name made lowercase.
    e_choices24 = models.CharField(db_column='E_Choices24', max_length=6, blank=True, null=True)  # Field name made lowercase.
    e_comp1 = models.CharField(db_column='E_Comp1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    e_comments1 = models.CharField(db_column='E_Comments1', max_length=95, blank=True, null=True)  # Field name made lowercase.
    e_comp2 = models.CharField(db_column='E_Comp2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    e_comments2 = models.CharField(db_column='E_Comments2', max_length=95, blank=True, null=True)  # Field name made lowercase.
    e_comp3 = models.CharField(db_column='E_Comp3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    e_comments3 = models.CharField(db_column='E_Comments3', max_length=95, blank=True, null=True)  # Field name made lowercase.
    e_comp4 = models.CharField(db_column='E_Comp4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    e_comments4 = models.CharField(db_column='E_Comments4', max_length=95, blank=True, null=True)  # Field name made lowercase.
    e_comp5 = models.CharField(db_column='E_Comp5', max_length=40, blank=True, null=True)  # Field name made lowercase.
    e_comments5 = models.CharField(db_column='E_Comments5', max_length=95, blank=True, null=True)  # Field name made lowercase.
    e_comp6 = models.CharField(db_column='E_Comp6', max_length=40, blank=True, null=True)  # Field name made lowercase.
    e_comments6 = models.CharField(db_column='E_Comments6', max_length=95, blank=True, null=True)  # Field name made lowercase.
    e_age = models.IntegerField(db_column='E_Age', blank=True, null=True)  # Field name made lowercase.
    e_comp_years = models.IntegerField(db_column='E_Comp_Years', blank=True, null=True)  # Field name made lowercase.
    e_exempted = models.CharField(db_column='E_Exempted', max_length=1, blank=True, null=True)  # Field name made lowercase.
    e_att_id = models.CharField(db_column='E_Att_ID', max_length=4, blank=True, null=True)  # Field name made lowercase.
    e_att_date = models.DateField(db_column='E_Att_Date', blank=True, null=True)  # Field name made lowercase.
    e_att = models.CharField(db_column='E_Att', max_length=100, blank=True, null=True)  # Field name made lowercase.
    e_act = models.CharField(db_column='E_Act', max_length=100, blank=True, null=True)  # Field name made lowercase.
    e_act_date = models.DateField(db_column='E_Act_Date', blank=True, null=True)  # Field name made lowercase.
    e_recommendation = models.CharField(db_column='E_Recommendation', max_length=1, blank=True, null=True)  # Field name made lowercase.
    e_time_last = models.TimeField(db_column='E_Time_Last', blank=True, null=True)  # Field name made lowercase.
    e_who_last = models.CharField(db_column='E_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'eval'
        unique_together = (('E_REC', 'E_UNIQUE'),)


class Evalform(models.Model):
    ef_d = models.CharField(db_column='EF_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ef_rec = models.IntegerField(db_column='EF_REC')  # Field name made lowercase.
    ef_unique = models.CharField(db_column='EF_UNIQUE', max_length=10)  # Field name made lowercase.
    ef_prin_p_key = models.CharField(db_column='EF_Prin_P_KEY', max_length=6, blank=True, null=True)  # Field name made lowercase.
    ef_version = models.IntegerField(db_column='EF_Version', blank=True, null=True)  # Field name made lowercase.
    ef_which = models.CharField(db_column='EF_Which', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ef_component1 = models.CharField(db_column='EF_Component1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ef_choices1 = models.CharField(db_column='EF_Choices1', max_length=6, blank=True, null=True)  # Field name made lowercase.
    ef_component2 = models.CharField(db_column='EF_Component2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ef_choices2 = models.CharField(db_column='EF_Choices2', max_length=6, blank=True, null=True)  # Field name made lowercase.
    ef_component3 = models.CharField(db_column='EF_Component3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ef_choices3 = models.CharField(db_column='EF_Choices3', max_length=6, blank=True, null=True)  # Field name made lowercase.
    ef_component4 = models.CharField(db_column='EF_Component4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ef_choices4 = models.CharField(db_column='EF_Choices4', max_length=6, blank=True, null=True)  # Field name made lowercase.
    ef_component5 = models.CharField(db_column='EF_Component5', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ef_choices5 = models.CharField(db_column='EF_Choices5', max_length=6, blank=True, null=True)  # Field name made lowercase.
    ef_component6 = models.CharField(db_column='EF_Component6', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ef_choices6 = models.CharField(db_column='EF_Choices6', max_length=6, blank=True, null=True)  # Field name made lowercase.
    ef_component7 = models.CharField(db_column='EF_Component7', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ef_choices7 = models.CharField(db_column='EF_Choices7', max_length=6, blank=True, null=True)  # Field name made lowercase.
    ef_component8 = models.CharField(db_column='EF_Component8', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ef_choices8 = models.CharField(db_column='EF_Choices8', max_length=6, blank=True, null=True)  # Field name made lowercase.
    ef_component9 = models.CharField(db_column='EF_Component9', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ef_choices9 = models.CharField(db_column='EF_Choices9', max_length=6, blank=True, null=True)  # Field name made lowercase.
    ef_component10 = models.CharField(db_column='EF_Component10', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ef_choices10 = models.CharField(db_column='EF_Choices10', max_length=6, blank=True, null=True)  # Field name made lowercase.
    ef_component11 = models.CharField(db_column='EF_Component11', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ef_choices11 = models.CharField(db_column='EF_Choices11', max_length=6, blank=True, null=True)  # Field name made lowercase.
    ef_component12 = models.CharField(db_column='EF_Component12', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ef_choices12 = models.CharField(db_column='EF_Choices12', max_length=6, blank=True, null=True)  # Field name made lowercase.
    ef_component13 = models.CharField(db_column='EF_Component13', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ef_choices13 = models.CharField(db_column='EF_Choices13', max_length=6, blank=True, null=True)  # Field name made lowercase.
    ef_component14 = models.CharField(db_column='EF_Component14', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ef_choices14 = models.CharField(db_column='EF_Choices14', max_length=6, blank=True, null=True)  # Field name made lowercase.
    ef_component15 = models.CharField(db_column='EF_Component15', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ef_choices15 = models.CharField(db_column='EF_Choices15', max_length=6, blank=True, null=True)  # Field name made lowercase.
    ef_component16 = models.CharField(db_column='EF_Component16', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ef_choices16 = models.CharField(db_column='EF_Choices16', max_length=6, blank=True, null=True)  # Field name made lowercase.
    ef_component17 = models.CharField(db_column='EF_Component17', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ef_choices17 = models.CharField(db_column='EF_Choices17', max_length=6, blank=True, null=True)  # Field name made lowercase.
    ef_component18 = models.CharField(db_column='EF_Component18', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ef_choices18 = models.CharField(db_column='EF_Choices18', max_length=6, blank=True, null=True)  # Field name made lowercase.
    ef_component19 = models.CharField(db_column='EF_Component19', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ef_choices19 = models.CharField(db_column='EF_Choices19', max_length=6, blank=True, null=True)  # Field name made lowercase.
    ef_component20 = models.CharField(db_column='EF_Component20', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ef_choices20 = models.CharField(db_column='EF_Choices20', max_length=6, blank=True, null=True)  # Field name made lowercase.
    ef_component21 = models.CharField(db_column='EF_Component21', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ef_choices21 = models.CharField(db_column='EF_Choices21', max_length=6, blank=True, null=True)  # Field name made lowercase.
    ef_component22 = models.CharField(db_column='EF_Component22', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ef_choices22 = models.CharField(db_column='EF_Choices22', max_length=6, blank=True, null=True)  # Field name made lowercase.
    ef_component23 = models.CharField(db_column='EF_Component23', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ef_choices23 = models.CharField(db_column='EF_Choices23', max_length=6, blank=True, null=True)  # Field name made lowercase.
    ef_component24 = models.CharField(db_column='EF_Component24', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ef_choices24 = models.CharField(db_column='EF_Choices24', max_length=6, blank=True, null=True)  # Field name made lowercase.
    ef_comments1 = models.CharField(db_column='EF_Comments1', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ef_comments2 = models.CharField(db_column='EF_Comments2', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ef_comments3 = models.CharField(db_column='EF_Comments3', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ef_comments4 = models.CharField(db_column='EF_Comments4', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ef_comments5 = models.CharField(db_column='EF_Comments5', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ef_comments6 = models.CharField(db_column='EF_Comments6', max_length=40, blank=True, null=True)  # Field name made lowercase.
    ef_time_last = models.TimeField(db_column='EF_Time_Last', blank=True, null=True)  # Field name made lowercase.
    ef_who_last = models.CharField(db_column='EF_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'evalform'
        unique_together = (('EF_REC', 'EF_UNIQUE'),)


class Exit(models.Model):
    ex_d = models.CharField(db_column='EX_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ex_id_b_id = models.CharField(db_column='EX_ID_B_ID', primary_key=True, max_length=4)  # Field name made lowercase.
    ex_months_employ_shore = models.IntegerField(db_column='EX_Months_Employ_Shore', blank=True, null=True)  # Field name made lowercase.
    ex_last_employer_shore = models.CharField(db_column='EX_Last_Employer_Shore', max_length=16, blank=True, null=True)  # Field name made lowercase.
    ex_last_position_shore = models.CharField(db_column='EX_Last_Position_Shore', max_length=8, blank=True, null=True)  # Field name made lowercase.
    ex_months_employ_abroad = models.IntegerField(db_column='EX_Months_Employ_Abroad', blank=True, null=True)  # Field name made lowercase.
    ex_last_employer_abroad = models.CharField(db_column='EX_Last_Employer_Abroad', max_length=16, blank=True, null=True)  # Field name made lowercase.
    ex_last_position_abroad = models.CharField(db_column='EX_Last_Position_Abroad', max_length=8, blank=True, null=True)  # Field name made lowercase.
    ex_last_employer_addr_abroad = models.CharField(db_column='EX_Last_Employer_Addr_Abroad', max_length=16, blank=True, null=True)  # Field name made lowercase.
    ex_beneficiary_name1 = models.CharField(db_column='EX_Beneficiary_Name1', max_length=48, blank=True, null=True)  # Field name made lowercase.
    ex_beneficiary_birthdate1 = models.DateField(db_column='EX_Beneficiary_Birthdate1', blank=True, null=True)  # Field name made lowercase.
    ex_beneficiary_address1 = models.CharField(db_column='EX_Beneficiary_Address1', max_length=32, blank=True, null=True)  # Field name made lowercase.
    ex_beneficiary_relation1 = models.CharField(db_column='EX_Beneficiary_Relation1', max_length=8, blank=True, null=True)  # Field name made lowercase.
    ex_beneficiary_name2 = models.CharField(db_column='EX_Beneficiary_Name2', max_length=48, blank=True, null=True)  # Field name made lowercase.
    ex_beneficiary_birthdate2 = models.DateField(db_column='EX_Beneficiary_Birthdate2', blank=True, null=True)  # Field name made lowercase.
    ex_beneficiary_address2 = models.CharField(db_column='EX_Beneficiary_Address2', max_length=32, blank=True, null=True)  # Field name made lowercase.
    ex_beneficiary_relation2 = models.CharField(db_column='EX_Beneficiary_Relation2', max_length=8, blank=True, null=True)  # Field name made lowercase.
    ex_beneficiary_name3 = models.CharField(db_column='EX_Beneficiary_Name3', max_length=48, blank=True, null=True)  # Field name made lowercase.
    ex_beneficiary_birthdate3 = models.DateField(db_column='EX_Beneficiary_Birthdate3', blank=True, null=True)  # Field name made lowercase.
    ex_beneficiary_address3 = models.CharField(db_column='EX_Beneficiary_Address3', max_length=32, blank=True, null=True)  # Field name made lowercase.
    ex_beneficiary_relation3 = models.CharField(db_column='EX_Beneficiary_Relation3', max_length=8, blank=True, null=True)  # Field name made lowercase.
    ex_beneficiary_name4 = models.CharField(db_column='EX_Beneficiary_Name4', max_length=48, blank=True, null=True)  # Field name made lowercase.
    ex_beneficiary_birthdate4 = models.DateField(db_column='EX_Beneficiary_Birthdate4', blank=True, null=True)  # Field name made lowercase.
    ex_beneficiary_address4 = models.CharField(db_column='EX_Beneficiary_Address4', max_length=32, blank=True, null=True)  # Field name made lowercase.
    ex_beneficiary_relation4 = models.CharField(db_column='EX_Beneficiary_Relation4', max_length=8, blank=True, null=True)  # Field name made lowercase.
    ex_beneficiary_name5 = models.CharField(db_column='EX_Beneficiary_Name5', max_length=48, blank=True, null=True)  # Field name made lowercase.
    ex_beneficiary_birthdate5 = models.DateField(db_column='EX_Beneficiary_Birthdate5', blank=True, null=True)  # Field name made lowercase.
    ex_beneficiary_address5 = models.CharField(db_column='EX_Beneficiary_Address5', max_length=32, blank=True, null=True)  # Field name made lowercase.
    ex_beneficiary_relation5 = models.CharField(db_column='EX_Beneficiary_Relation5', max_length=8, blank=True, null=True)  # Field name made lowercase.
    ex_beneficiary_name6 = models.CharField(db_column='EX_Beneficiary_Name6', max_length=48, blank=True, null=True)  # Field name made lowercase.
    ex_beneficiary_birthdate6 = models.DateField(db_column='EX_Beneficiary_Birthdate6', blank=True, null=True)  # Field name made lowercase.
    ex_beneficiary_address6 = models.CharField(db_column='EX_Beneficiary_Address6', max_length=32, blank=True, null=True)  # Field name made lowercase.
    ex_beneficiary_relation6 = models.CharField(db_column='EX_Beneficiary_Relation6', max_length=8, blank=True, null=True)  # Field name made lowercase.
    ex_beneficiary_name7 = models.CharField(db_column='EX_Beneficiary_Name7', max_length=48, blank=True, null=True)  # Field name made lowercase.
    ex_beneficiary_birthdate7 = models.DateField(db_column='EX_Beneficiary_Birthdate7', blank=True, null=True)  # Field name made lowercase.
    ex_beneficiary_address7 = models.CharField(db_column='EX_Beneficiary_Address7', max_length=32, blank=True, null=True)  # Field name made lowercase.
    ex_beneficiary_relation7 = models.CharField(db_column='EX_Beneficiary_Relation7', max_length=8, blank=True, null=True)  # Field name made lowercase.
    ex_beneficiary_name8 = models.CharField(db_column='EX_Beneficiary_Name8', max_length=48, blank=True, null=True)  # Field name made lowercase.
    ex_beneficiary_birthdate8 = models.DateField(db_column='EX_Beneficiary_Birthdate8', blank=True, null=True)  # Field name made lowercase.
    ex_beneficiary_address8 = models.CharField(db_column='EX_Beneficiary_Address8', max_length=32, blank=True, null=True)  # Field name made lowercase.
    ex_beneficiary_relation8 = models.CharField(db_column='EX_Beneficiary_Relation8', max_length=8, blank=True, null=True)  # Field name made lowercase.
    ex_beneficiary_name9 = models.CharField(db_column='EX_Beneficiary_Name9', max_length=48, blank=True, null=True)  # Field name made lowercase.
    ex_beneficiary_birthdate9 = models.DateField(db_column='EX_Beneficiary_Birthdate9', blank=True, null=True)  # Field name made lowercase.
    ex_beneficiary_address9 = models.CharField(db_column='EX_Beneficiary_Address9', max_length=32, blank=True, null=True)  # Field name made lowercase.
    ex_beneficiary_relation9 = models.CharField(db_column='EX_Beneficiary_Relation9', max_length=8, blank=True, null=True)  # Field name made lowercase.
    ex_beneficiary_name10 = models.CharField(db_column='EX_Beneficiary_Name10', max_length=48, blank=True, null=True)  # Field name made lowercase.
    ex_beneficiary_birthdate10 = models.DateField(db_column='EX_Beneficiary_Birthdate10', blank=True, null=True)  # Field name made lowercase.
    ex_beneficiary_address10 = models.CharField(db_column='EX_Beneficiary_Address10', max_length=32, blank=True, null=True)  # Field name made lowercase.
    ex_beneficiary_relation10 = models.CharField(db_column='EX_Beneficiary_Relation10', max_length=8, blank=True, null=True)  # Field name made lowercase.
    ex_allot_percent = models.IntegerField(db_column='EX_Allot_Percent', blank=True, null=True)  # Field name made lowercase.
    ex_time_last = models.TimeField(db_column='EX_Time_Last', blank=True, null=True)  # Field name made lowercase.
    ex_who_last = models.CharField(db_column='EX_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'exit'


class Extra(models.Model):
    ext_d = models.CharField(db_column='EXT_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ext_rec = models.IntegerField(db_column='EXT_REC', primary_key=True)  # Field name made lowercase.
    ext_date = models.DateField(db_column='EXT_Date', blank=True, null=True)  # Field name made lowercase.
    ext_con_rec = models.IntegerField(db_column='EXT_CON_REC', blank=True, null=True)  # Field name made lowercase.
    ext_tax_rec = models.DecimalField(db_column='EXT_TAX_REC', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ext_tax_date = models.DateField(db_column='EXT_Tax_Date', blank=True, null=True)  # Field name made lowercase.
    ext_paid = models.CharField(db_column='EXT_Paid', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ext_paid_date = models.DateField(db_column='EXT_Paid_Date', blank=True, null=True)  # Field name made lowercase.
    ext_description = models.CharField(db_column='EXT_Description', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ext_m_money = models.CharField(db_column='EXT_M_Money', max_length=3, blank=True, null=True)  # Field name made lowercase.
    ext_taxable_amnt = models.DecimalField(db_column='EXT_Taxable_Amnt', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ext_net = models.DecimalField(db_column='EXT_Net', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ext_net_paid = models.DecimalField(db_column='EXT_Net_Paid', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ext_d_comp_type_1 = models.CharField(db_column='EXT_D_Comp_Type_1', max_length=3, blank=True, null=True)  # Field name made lowercase.
    ext_d_comp_name_1 = models.CharField(db_column='EXT_D_Comp_Name_1', max_length=16, blank=True, null=True)  # Field name made lowercase.
    ext_d_comp_amnt_1 = models.DecimalField(db_column='EXT_D_Comp_Amnt_1', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ext_d_comp_type_2 = models.CharField(db_column='EXT_D_Comp_Type_2', max_length=3, blank=True, null=True)  # Field name made lowercase.
    ext_d_comp_name_2 = models.CharField(db_column='EXT_D_Comp_Name_2', max_length=16, blank=True, null=True)  # Field name made lowercase.
    ext_d_comp_amnt_2 = models.DecimalField(db_column='EXT_D_Comp_Amnt_2', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ext_d_comp_type_3 = models.CharField(db_column='EXT_D_Comp_Type_3', max_length=3, blank=True, null=True)  # Field name made lowercase.
    ext_d_comp_name_3 = models.CharField(db_column='EXT_D_Comp_Name_3', max_length=16, blank=True, null=True)  # Field name made lowercase.
    ext_d_comp_amnt_3 = models.DecimalField(db_column='EXT_D_Comp_Amnt_3', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ext_d_comp_type_4 = models.CharField(db_column='EXT_D_Comp_Type_4', max_length=3, blank=True, null=True)  # Field name made lowercase.
    ext_d_comp_name_4 = models.CharField(db_column='EXT_D_Comp_Name_4', max_length=16, blank=True, null=True)  # Field name made lowercase.
    ext_d_comp_amnt_4 = models.DecimalField(db_column='EXT_D_Comp_Amnt_4', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ext_d_comp_type_5 = models.CharField(db_column='EXT_D_Comp_Type_5', max_length=3, blank=True, null=True)  # Field name made lowercase.
    ext_d_comp_name_5 = models.CharField(db_column='EXT_D_Comp_Name_5', max_length=16, blank=True, null=True)  # Field name made lowercase.
    ext_d_comp_amnt_5 = models.DecimalField(db_column='EXT_D_Comp_Amnt_5', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ext_d_comp_type_6 = models.CharField(db_column='EXT_D_Comp_Type_6', max_length=3, blank=True, null=True)  # Field name made lowercase.
    ext_d_comp_name_6 = models.CharField(db_column='EXT_D_Comp_Name_6', max_length=16, blank=True, null=True)  # Field name made lowercase.
    ext_d_comp_amnt_6 = models.DecimalField(db_column='EXT_D_Comp_Amnt_6', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ext_seaman_dstamp = models.DecimalField(db_column='EXT_Seaman_Dstamp', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ext_seaman_doga = models.DecimalField(db_column='EXT_Seaman_Doga', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ext_seaman_dtax = models.DecimalField(db_column='EXT_Seaman_Dtax', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ext_seaman_dtax_oga = models.DecimalField(db_column='EXT_Seaman_Dtax_Oga', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ext_seaman_dtax_anal = models.DecimalField(db_column='EXT_Seaman_Dtax_Anal', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ext_seaman_dtax_oga_anal = models.DecimalField(db_column='EXT_Seaman_Dtax_Oga_Anal', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ext_time_last = models.TimeField(db_column='EXT_Time_Last', blank=True, null=True)  # Field name made lowercase.
    ext_who_last = models.CharField(db_column='EXT_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'extra'


class Freemailw(models.Model):
    fmw_d = models.CharField(db_column='FMW_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fmw_rec = models.IntegerField(db_column='FMW_REC', primary_key=True)  # Field name made lowercase.
    fmw_unique = models.CharField(db_column='FMW_UNIQUE', max_length=65, blank=True, null=True)  # Field name made lowercase.
    fmw_b_id = models.CharField(db_column='FMW_B_ID', max_length=4, blank=True, null=True)  # Field name made lowercase.
    fmw_address = models.CharField(db_column='FMW_Address', max_length=60, blank=True, null=True)  # Field name made lowercase.
    fmw_time_last = models.TimeField(db_column='FMW_Time_Last', blank=True, null=True)  # Field name made lowercase.
    fmw_who_last = models.CharField(db_column='FMW_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'freemailw'


class Fx(models.Model):
    fx_d = models.CharField(db_column='FX_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fx_key = models.CharField(db_column='FX_Key', primary_key=True, max_length=12)  # Field name made lowercase.
    fx_code = models.CharField(db_column='FX_Code', max_length=3, blank=True, null=True)  # Field name made lowercase.
    fx_date = models.DateField(db_column='FX_Date', blank=True, null=True)  # Field name made lowercase.
    fx_rate = models.DecimalField(db_column='FX_Rate', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    fx_dorm = models.CharField(db_column='FX_dORm', max_length=1, blank=True, null=True)  # Field name made lowercase.
    fx_decpt = models.IntegerField(db_column='FX_Decpt', blank=True, null=True)  # Field name made lowercase.
    fx_time_last = models.TimeField(db_column='FX_Time_Last', blank=True, null=True)  # Field name made lowercase.
    fx_who_last = models.CharField(db_column='FX_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fx'


class Gl(models.Model):
    gl_d = models.CharField(db_column='GL_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    gl_rec = models.IntegerField(db_column='GL_REC')  # Field name made lowercase.
    gl_unique = models.CharField(db_column='GL_UNIQUE', max_length=14)  # Field name made lowercase.
    gl_unique_1 = models.CharField(db_column='GL_UNIQUE_1', max_length=14)  # Field name made lowercase.
    gl_date = models.DateField(db_column='GL_Date', blank=True, null=True)  # Field name made lowercase.
    gl_w_scale = models.CharField(db_column='GL_W_Scale', max_length=2, blank=True, null=True)  # Field name made lowercase.
    gl_t_scale = models.CharField(db_column='GL_T_Scale', max_length=2, blank=True, null=True)  # Field name made lowercase.
    gl_ec_invoice = models.CharField(db_column='GL_EC_Invoice', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_et_invoice = models.CharField(db_column='GL_ET_Invoice', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_em_invoice = models.CharField(db_column='GL_EM_Invoice', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_c_basic = models.CharField(db_column='GL_C_Basic', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_basic = models.CharField(db_column='GL_T_Basic', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_m_basic = models.CharField(db_column='GL_M_Basic', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_w_type_1 = models.CharField(db_column='GL_W_Type_1', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_w_type_2 = models.CharField(db_column='GL_W_Type_2', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_w_type_3 = models.CharField(db_column='GL_W_Type_3', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_w_type_4 = models.CharField(db_column='GL_W_Type_4', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_w_type_5 = models.CharField(db_column='GL_W_Type_5', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_w_type_6 = models.CharField(db_column='GL_W_Type_6', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_w_type_7 = models.CharField(db_column='GL_W_Type_7', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_w_type_8 = models.CharField(db_column='GL_W_Type_8', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_w_type_9 = models.CharField(db_column='GL_W_Type_9', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_w_type_10 = models.CharField(db_column='GL_W_Type_10', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_w_type_11 = models.CharField(db_column='GL_W_Type_11', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_w_type_12 = models.CharField(db_column='GL_W_Type_12', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_w_type_13 = models.CharField(db_column='GL_W_Type_13', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_w_type_14 = models.CharField(db_column='GL_W_Type_14', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_w_type_15 = models.CharField(db_column='GL_W_Type_15', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_w_type_16 = models.CharField(db_column='GL_W_Type_16', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_w_type_17 = models.CharField(db_column='GL_W_Type_17', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_w_type_18 = models.CharField(db_column='GL_W_Type_18', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_w_type_19 = models.CharField(db_column='GL_W_Type_19', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_w_type_20 = models.CharField(db_column='GL_W_Type_20', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_w_type_21 = models.CharField(db_column='GL_W_Type_21', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_w_type_22 = models.CharField(db_column='GL_W_Type_22', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_w_type_23 = models.CharField(db_column='GL_W_Type_23', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_w_type_24 = models.CharField(db_column='GL_W_Type_24', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_w_type_25 = models.CharField(db_column='GL_W_Type_25', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_w_type_26 = models.CharField(db_column='GL_W_Type_26', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_w_type_27 = models.CharField(db_column='GL_W_Type_27', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_w_type_28 = models.CharField(db_column='GL_W_Type_28', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_w_type_29 = models.CharField(db_column='GL_W_Type_29', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_w_type_30 = models.CharField(db_column='GL_W_Type_30', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_w_type_31 = models.CharField(db_column='GL_W_Type_31', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_w_type_32 = models.CharField(db_column='GL_W_Type_32', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_w_type_33 = models.CharField(db_column='GL_W_Type_33', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_w_type_34 = models.CharField(db_column='GL_W_Type_34', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_w_type_35 = models.CharField(db_column='GL_W_Type_35', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_w_type_36 = models.CharField(db_column='GL_W_Type_36', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_w_type_37 = models.CharField(db_column='GL_W_Type_37', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_wc_book_1 = models.CharField(db_column='GL_WC_Book_1', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wc_book_2 = models.CharField(db_column='GL_WC_Book_2', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wc_book_3 = models.CharField(db_column='GL_WC_Book_3', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wc_book_4 = models.CharField(db_column='GL_WC_Book_4', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wc_book_5 = models.CharField(db_column='GL_WC_Book_5', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wc_book_6 = models.CharField(db_column='GL_WC_Book_6', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wc_book_7 = models.CharField(db_column='GL_WC_Book_7', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wc_book_8 = models.CharField(db_column='GL_WC_Book_8', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wc_book_9 = models.CharField(db_column='GL_WC_Book_9', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wc_book_10 = models.CharField(db_column='GL_WC_Book_10', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wc_book_11 = models.CharField(db_column='GL_WC_Book_11', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wc_book_12 = models.CharField(db_column='GL_WC_Book_12', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wc_book_13 = models.CharField(db_column='GL_WC_Book_13', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wc_book_14 = models.CharField(db_column='GL_WC_Book_14', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wc_book_15 = models.CharField(db_column='GL_WC_Book_15', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wc_book_16 = models.CharField(db_column='GL_WC_Book_16', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wc_book_17 = models.CharField(db_column='GL_WC_Book_17', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wc_book_18 = models.CharField(db_column='GL_WC_Book_18', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wc_book_19 = models.CharField(db_column='GL_WC_Book_19', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wc_book_20 = models.CharField(db_column='GL_WC_Book_20', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wc_book_21 = models.CharField(db_column='GL_WC_Book_21', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wc_book_22 = models.CharField(db_column='GL_WC_Book_22', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wc_book_23 = models.CharField(db_column='GL_WC_Book_23', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wc_book_24 = models.CharField(db_column='GL_WC_Book_24', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wc_book_25 = models.CharField(db_column='GL_WC_Book_25', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wc_book_26 = models.CharField(db_column='GL_WC_Book_26', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wc_book_27 = models.CharField(db_column='GL_WC_Book_27', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wc_book_28 = models.CharField(db_column='GL_WC_Book_28', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wc_book_29 = models.CharField(db_column='GL_WC_Book_29', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wc_book_30 = models.CharField(db_column='GL_WC_Book_30', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wc_book_31 = models.CharField(db_column='GL_WC_Book_31', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wc_book_32 = models.CharField(db_column='GL_WC_Book_32', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wc_book_33 = models.CharField(db_column='GL_WC_Book_33', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wc_book_34 = models.CharField(db_column='GL_WC_Book_34', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wc_book_35 = models.CharField(db_column='GL_WC_Book_35', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wc_book_36 = models.CharField(db_column='GL_WC_Book_36', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wc_book_37 = models.CharField(db_column='GL_WC_Book_37', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wt_book_1 = models.CharField(db_column='GL_WT_Book_1', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wt_book_2 = models.CharField(db_column='GL_WT_Book_2', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wt_book_3 = models.CharField(db_column='GL_WT_Book_3', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wt_book_4 = models.CharField(db_column='GL_WT_Book_4', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wt_book_5 = models.CharField(db_column='GL_WT_Book_5', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wt_book_6 = models.CharField(db_column='GL_WT_Book_6', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wt_book_7 = models.CharField(db_column='GL_WT_Book_7', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wt_book_8 = models.CharField(db_column='GL_WT_Book_8', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wt_book_9 = models.CharField(db_column='GL_WT_Book_9', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wt_book_10 = models.CharField(db_column='GL_WT_Book_10', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wt_book_11 = models.CharField(db_column='GL_WT_Book_11', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wt_book_12 = models.CharField(db_column='GL_WT_Book_12', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wt_book_13 = models.CharField(db_column='GL_WT_Book_13', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wt_book_14 = models.CharField(db_column='GL_WT_Book_14', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wt_book_15 = models.CharField(db_column='GL_WT_Book_15', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wt_book_16 = models.CharField(db_column='GL_WT_Book_16', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wt_book_17 = models.CharField(db_column='GL_WT_Book_17', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wt_book_18 = models.CharField(db_column='GL_WT_Book_18', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wt_book_19 = models.CharField(db_column='GL_WT_Book_19', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wt_book_20 = models.CharField(db_column='GL_WT_Book_20', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wt_book_21 = models.CharField(db_column='GL_WT_Book_21', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wt_book_22 = models.CharField(db_column='GL_WT_Book_22', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wt_book_23 = models.CharField(db_column='GL_WT_Book_23', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wt_book_24 = models.CharField(db_column='GL_WT_Book_24', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wt_book_25 = models.CharField(db_column='GL_WT_Book_25', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wt_book_26 = models.CharField(db_column='GL_WT_Book_26', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wt_book_27 = models.CharField(db_column='GL_WT_Book_27', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wt_book_28 = models.CharField(db_column='GL_WT_Book_28', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wt_book_29 = models.CharField(db_column='GL_WT_Book_29', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wt_book_30 = models.CharField(db_column='GL_WT_Book_30', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wt_book_31 = models.CharField(db_column='GL_WT_Book_31', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wt_book_32 = models.CharField(db_column='GL_WT_Book_32', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wt_book_33 = models.CharField(db_column='GL_WT_Book_33', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wt_book_34 = models.CharField(db_column='GL_WT_Book_34', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wt_book_35 = models.CharField(db_column='GL_WT_Book_35', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wt_book_36 = models.CharField(db_column='GL_WT_Book_36', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wt_book_37 = models.CharField(db_column='GL_WT_Book_37', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wm_book_1 = models.CharField(db_column='GL_WM_Book_1', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wm_book_2 = models.CharField(db_column='GL_WM_Book_2', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wm_book_3 = models.CharField(db_column='GL_WM_Book_3', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wm_book_4 = models.CharField(db_column='GL_WM_Book_4', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wm_book_5 = models.CharField(db_column='GL_WM_Book_5', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wm_book_6 = models.CharField(db_column='GL_WM_Book_6', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wm_book_7 = models.CharField(db_column='GL_WM_Book_7', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wm_book_8 = models.CharField(db_column='GL_WM_Book_8', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wm_book_9 = models.CharField(db_column='GL_WM_Book_9', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wm_book_10 = models.CharField(db_column='GL_WM_Book_10', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wm_book_11 = models.CharField(db_column='GL_WM_Book_11', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wm_book_12 = models.CharField(db_column='GL_WM_Book_12', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wm_book_13 = models.CharField(db_column='GL_WM_Book_13', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wm_book_14 = models.CharField(db_column='GL_WM_Book_14', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wm_book_15 = models.CharField(db_column='GL_WM_Book_15', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wm_book_16 = models.CharField(db_column='GL_WM_Book_16', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wm_book_17 = models.CharField(db_column='GL_WM_Book_17', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wm_book_18 = models.CharField(db_column='GL_WM_Book_18', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wm_book_19 = models.CharField(db_column='GL_WM_Book_19', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wm_book_20 = models.CharField(db_column='GL_WM_Book_20', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wm_book_21 = models.CharField(db_column='GL_WM_Book_21', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wm_book_22 = models.CharField(db_column='GL_WM_Book_22', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wm_book_23 = models.CharField(db_column='GL_WM_Book_23', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wm_book_24 = models.CharField(db_column='GL_WM_Book_24', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wm_book_25 = models.CharField(db_column='GL_WM_Book_25', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wm_book_26 = models.CharField(db_column='GL_WM_Book_26', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wm_book_27 = models.CharField(db_column='GL_WM_Book_27', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wm_book_28 = models.CharField(db_column='GL_WM_Book_28', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wm_book_29 = models.CharField(db_column='GL_WM_Book_29', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wm_book_30 = models.CharField(db_column='GL_WM_Book_30', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wm_book_31 = models.CharField(db_column='GL_WM_Book_31', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wm_book_32 = models.CharField(db_column='GL_WM_Book_32', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wm_book_33 = models.CharField(db_column='GL_WM_Book_33', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wm_book_34 = models.CharField(db_column='GL_WM_Book_34', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wm_book_35 = models.CharField(db_column='GL_WM_Book_35', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wm_book_36 = models.CharField(db_column='GL_WM_Book_36', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_wm_book_37 = models.CharField(db_column='GL_WM_Book_37', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_cc_extra = models.CharField(db_column='GL_CC_Extra', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_ct_extra = models.CharField(db_column='GL_CT_Extra', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_cm_extra = models.CharField(db_column='GL_CM_Extra', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_mc_extra = models.CharField(db_column='GL_MC_Extra', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_mt_extra = models.CharField(db_column='GL_MT_Extra', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_mm_extra = models.CharField(db_column='GL_MM_Extra', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_c_hrb = models.CharField(db_column='GL_C_HRB', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_hrb = models.CharField(db_column='GL_T_HRB', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_m_hrb = models.CharField(db_column='GL_M_HRB', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_c_senior = models.CharField(db_column='GL_C_Senior', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_senior = models.CharField(db_column='GL_T_Senior', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_m_senior = models.CharField(db_column='GL_M_Senior', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_c_senior_rank = models.CharField(db_column='GL_C_Senior_Rank', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_senior_rank = models.CharField(db_column='GL_T_Senior_Rank', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_m_senior_rank = models.CharField(db_column='GL_M_Senior_Rank', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_rc_balance = models.CharField(db_column='GL_RC_Balance', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_rt_balance = models.CharField(db_column='GL_RT_Balance', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_rm_balance = models.CharField(db_column='GL_RM_Balance', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_d_cnote = models.CharField(db_column='GL_D_CNote', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_type_1 = models.CharField(db_column='GL_T_Type_1', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_t_book_1 = models.CharField(db_column='GL_T_Book_1', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_inva_1 = models.CharField(db_column='GL_T_InvA_1', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_acca_1 = models.CharField(db_column='GL_T_AccA_1', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_type_2 = models.CharField(db_column='GL_T_Type_2', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_t_book_2 = models.CharField(db_column='GL_T_Book_2', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_inva_2 = models.CharField(db_column='GL_T_InvA_2', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_acca_2 = models.CharField(db_column='GL_T_AccA_2', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_type_3 = models.CharField(db_column='GL_T_Type_3', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_t_book_3 = models.CharField(db_column='GL_T_Book_3', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_inva_3 = models.CharField(db_column='GL_T_InvA_3', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_acca_3 = models.CharField(db_column='GL_T_AccA_3', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_type_4 = models.CharField(db_column='GL_T_Type_4', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_t_book_4 = models.CharField(db_column='GL_T_Book_4', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_inva_4 = models.CharField(db_column='GL_T_InvA_4', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_acca_4 = models.CharField(db_column='GL_T_AccA_4', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_type_5 = models.CharField(db_column='GL_T_Type_5', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_t_book_5 = models.CharField(db_column='GL_T_Book_5', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_inva_5 = models.CharField(db_column='GL_T_InvA_5', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_acca_5 = models.CharField(db_column='GL_T_AccA_5', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_type_6 = models.CharField(db_column='GL_T_Type_6', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_t_book_6 = models.CharField(db_column='GL_T_Book_6', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_inva_6 = models.CharField(db_column='GL_T_InvA_6', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_acca_6 = models.CharField(db_column='GL_T_AccA_6', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_type_7 = models.CharField(db_column='GL_T_Type_7', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_t_book_7 = models.CharField(db_column='GL_T_Book_7', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_inva_7 = models.CharField(db_column='GL_T_InvA_7', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_acca_7 = models.CharField(db_column='GL_T_AccA_7', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_type_8 = models.CharField(db_column='GL_T_Type_8', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_t_book_8 = models.CharField(db_column='GL_T_Book_8', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_inva_8 = models.CharField(db_column='GL_T_InvA_8', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_acca_8 = models.CharField(db_column='GL_T_AccA_8', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_type_9 = models.CharField(db_column='GL_T_Type_9', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_t_book_9 = models.CharField(db_column='GL_T_Book_9', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_inva_9 = models.CharField(db_column='GL_T_InvA_9', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_acca_9 = models.CharField(db_column='GL_T_AccA_9', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_type_10 = models.CharField(db_column='GL_T_Type_10', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_t_book_10 = models.CharField(db_column='GL_T_Book_10', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_inva_10 = models.CharField(db_column='GL_T_InvA_10', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_acca_10 = models.CharField(db_column='GL_T_AccA_10', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_type_11 = models.CharField(db_column='GL_T_Type_11', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_t_book_11 = models.CharField(db_column='GL_T_Book_11', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_inva_11 = models.CharField(db_column='GL_T_InvA_11', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_acca_11 = models.CharField(db_column='GL_T_AccA_11', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_type_12 = models.CharField(db_column='GL_T_Type_12', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_t_book_12 = models.CharField(db_column='GL_T_Book_12', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_inva_12 = models.CharField(db_column='GL_T_InvA_12', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_acca_12 = models.CharField(db_column='GL_T_AccA_12', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_type_13 = models.CharField(db_column='GL_T_Type_13', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_t_book_13 = models.CharField(db_column='GL_T_Book_13', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_inva_13 = models.CharField(db_column='GL_T_InvA_13', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_acca_13 = models.CharField(db_column='GL_T_AccA_13', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_type_14 = models.CharField(db_column='GL_T_Type_14', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_t_book_14 = models.CharField(db_column='GL_T_Book_14', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_inva_14 = models.CharField(db_column='GL_T_InvA_14', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_acca_14 = models.CharField(db_column='GL_T_AccA_14', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_type_15 = models.CharField(db_column='GL_T_Type_15', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_t_book_15 = models.CharField(db_column='GL_T_Book_15', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_inva_15 = models.CharField(db_column='GL_T_InvA_15', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_acca_15 = models.CharField(db_column='GL_T_AccA_15', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_type_16 = models.CharField(db_column='GL_T_Type_16', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_t_book_16 = models.CharField(db_column='GL_T_Book_16', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_inva_16 = models.CharField(db_column='GL_T_InvA_16', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_acca_16 = models.CharField(db_column='GL_T_AccA_16', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_type_17 = models.CharField(db_column='GL_T_Type_17', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_t_book_17 = models.CharField(db_column='GL_T_Book_17', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_inva_17 = models.CharField(db_column='GL_T_InvA_17', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_acca_17 = models.CharField(db_column='GL_T_AccA_17', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_type_18 = models.CharField(db_column='GL_T_Type_18', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_t_book_18 = models.CharField(db_column='GL_T_Book_18', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_inva_18 = models.CharField(db_column='GL_T_InvA_18', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_acca_18 = models.CharField(db_column='GL_T_AccA_18', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_type_19 = models.CharField(db_column='GL_T_Type_19', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_t_book_19 = models.CharField(db_column='GL_T_Book_19', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_inva_19 = models.CharField(db_column='GL_T_InvA_19', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_acca_19 = models.CharField(db_column='GL_T_AccA_19', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_type_20 = models.CharField(db_column='GL_T_Type_20', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_t_book_20 = models.CharField(db_column='GL_T_Book_20', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_inva_20 = models.CharField(db_column='GL_T_InvA_20', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_acca_20 = models.CharField(db_column='GL_T_AccA_20', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_type_21 = models.CharField(db_column='GL_T_Type_21', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_t_book_21 = models.CharField(db_column='GL_T_Book_21', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_inva_21 = models.CharField(db_column='GL_T_InvA_21', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_acca_21 = models.CharField(db_column='GL_T_AccA_21', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_type_22 = models.CharField(db_column='GL_T_Type_22', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_t_book_22 = models.CharField(db_column='GL_T_Book_22', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_inva_22 = models.CharField(db_column='GL_T_InvA_22', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_acca_22 = models.CharField(db_column='GL_T_AccA_22', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_type_23 = models.CharField(db_column='GL_T_Type_23', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_t_book_23 = models.CharField(db_column='GL_T_Book_23', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_inva_23 = models.CharField(db_column='GL_T_InvA_23', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_acca_23 = models.CharField(db_column='GL_T_AccA_23', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_type_24 = models.CharField(db_column='GL_T_Type_24', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_t_book_24 = models.CharField(db_column='GL_T_Book_24', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_inva_24 = models.CharField(db_column='GL_T_InvA_24', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_acca_24 = models.CharField(db_column='GL_T_AccA_24', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_type_25 = models.CharField(db_column='GL_T_Type_25', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_t_book_25 = models.CharField(db_column='GL_T_Book_25', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_inva_25 = models.CharField(db_column='GL_T_InvA_25', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_acca_25 = models.CharField(db_column='GL_T_AccA_25', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_type_26 = models.CharField(db_column='GL_T_Type_26', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_t_book_26 = models.CharField(db_column='GL_T_Book_26', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_inva_26 = models.CharField(db_column='GL_T_InvA_26', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_acca_26 = models.CharField(db_column='GL_T_AccA_26', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_type_27 = models.CharField(db_column='GL_T_Type_27', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_t_book_27 = models.CharField(db_column='GL_T_Book_27', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_inva_27 = models.CharField(db_column='GL_T_InvA_27', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_acca_27 = models.CharField(db_column='GL_T_AccA_27', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_type_28 = models.CharField(db_column='GL_T_Type_28', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_t_book_28 = models.CharField(db_column='GL_T_Book_28', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_inva_28 = models.CharField(db_column='GL_T_InvA_28', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_acca_28 = models.CharField(db_column='GL_T_AccA_28', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_type_29 = models.CharField(db_column='GL_T_Type_29', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_t_book_29 = models.CharField(db_column='GL_T_Book_29', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_inva_29 = models.CharField(db_column='GL_T_InvA_29', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_acca_29 = models.CharField(db_column='GL_T_AccA_29', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_type_30 = models.CharField(db_column='GL_T_Type_30', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_t_book_30 = models.CharField(db_column='GL_T_Book_30', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_inva_30 = models.CharField(db_column='GL_T_InvA_30', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_acca_30 = models.CharField(db_column='GL_T_AccA_30', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_type_31 = models.CharField(db_column='GL_T_Type_31', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_t_book_31 = models.CharField(db_column='GL_T_Book_31', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_inva_31 = models.CharField(db_column='GL_T_InvA_31', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_acca_31 = models.CharField(db_column='GL_T_AccA_31', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_type_32 = models.CharField(db_column='GL_T_Type_32', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_t_book_32 = models.CharField(db_column='GL_T_Book_32', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_inva_32 = models.CharField(db_column='GL_T_InvA_32', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_acca_32 = models.CharField(db_column='GL_T_AccA_32', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_type_33 = models.CharField(db_column='GL_T_Type_33', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_t_book_33 = models.CharField(db_column='GL_T_Book_33', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_inva_33 = models.CharField(db_column='GL_T_InvA_33', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_acca_33 = models.CharField(db_column='GL_T_AccA_33', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_type_34 = models.CharField(db_column='GL_T_Type_34', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_t_book_34 = models.CharField(db_column='GL_T_Book_34', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_inva_34 = models.CharField(db_column='GL_T_InvA_34', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_acca_34 = models.CharField(db_column='GL_T_AccA_34', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_type_35 = models.CharField(db_column='GL_T_Type_35', max_length=3, blank=True, null=True)  # Field name made lowercase.
    gl_t_book_35 = models.CharField(db_column='GL_T_Book_35', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_inva_35 = models.CharField(db_column='GL_T_InvA_35', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_t_acca_35 = models.CharField(db_column='GL_T_AccA_35', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_d_jrnl = models.CharField(db_column='GL_D_Jrnl', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_d_master = models.CharField(db_column='GL_D_Master', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_d_master_jrnl = models.CharField(db_column='GL_D_Master_Jrnl', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_d_advance = models.CharField(db_column='GL_D_Advance', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_d_advance_jrnl = models.CharField(db_column='GL_D_Advance_Jrnl', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_d_allot = models.CharField(db_column='GL_D_Allot', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_d_bond = models.CharField(db_column='GL_D_Bond', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_d_phone = models.CharField(db_column='GL_D_Phone', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_d_repatriate = models.CharField(db_column='GL_D_Repatriate', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_d_extra = models.CharField(db_column='GL_D_Extra', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_nc_balance = models.CharField(db_column='GL_NC_Balance', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_nt_balance = models.CharField(db_column='GL_NT_Balance', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_nm_balance = models.CharField(db_column='GL_NM_Balance', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_pf_balance = models.CharField(db_column='GL_PF_Balance', max_length=15, blank=True, null=True)  # Field name made lowercase.
    gl_skip_bid_1 = models.CharField(db_column='GL_Skip_BID_1', max_length=4, blank=True, null=True)  # Field name made lowercase.
    gl_skip_bid_2 = models.CharField(db_column='GL_Skip_BID_2', max_length=4, blank=True, null=True)  # Field name made lowercase.
    gl_skip_bid_3 = models.CharField(db_column='GL_Skip_BID_3', max_length=4, blank=True, null=True)  # Field name made lowercase.
    gl_skip_bid_4 = models.CharField(db_column='GL_Skip_BID_4', max_length=4, blank=True, null=True)  # Field name made lowercase.
    gl_skip_bid_5 = models.CharField(db_column='GL_Skip_BID_5', max_length=4, blank=True, null=True)  # Field name made lowercase.
    gl_skip_bid_6 = models.CharField(db_column='GL_Skip_BID_6', max_length=4, blank=True, null=True)  # Field name made lowercase.
    gl_skip_bid_7 = models.CharField(db_column='GL_Skip_BID_7', max_length=4, blank=True, null=True)  # Field name made lowercase.
    gl_skip_bid_8 = models.CharField(db_column='GL_Skip_BID_8', max_length=4, blank=True, null=True)  # Field name made lowercase.
    gl_skip_bid_9 = models.CharField(db_column='GL_Skip_BID_9', max_length=4, blank=True, null=True)  # Field name made lowercase.
    gl_skip_bid_10 = models.CharField(db_column='GL_Skip_BID_10', max_length=4, blank=True, null=True)  # Field name made lowercase.
    gl_skip_bid_11 = models.CharField(db_column='GL_Skip_BID_11', max_length=4, blank=True, null=True)  # Field name made lowercase.
    gl_skip_bid_12 = models.CharField(db_column='GL_Skip_BID_12', max_length=4, blank=True, null=True)  # Field name made lowercase.
    gl_skip_bid_13 = models.CharField(db_column='GL_Skip_BID_13', max_length=4, blank=True, null=True)  # Field name made lowercase.
    gl_skip_bid_14 = models.CharField(db_column='GL_Skip_BID_14', max_length=4, blank=True, null=True)  # Field name made lowercase.
    gl_skip_bid_15 = models.CharField(db_column='GL_Skip_BID_15', max_length=4, blank=True, null=True)  # Field name made lowercase.
    gl_skip_bid_16 = models.CharField(db_column='GL_Skip_BID_16', max_length=4, blank=True, null=True)  # Field name made lowercase.
    gl_skip_bid_17 = models.CharField(db_column='GL_Skip_BID_17', max_length=4, blank=True, null=True)  # Field name made lowercase.
    gl_skip_bid_18 = models.CharField(db_column='GL_Skip_BID_18', max_length=4, blank=True, null=True)  # Field name made lowercase.
    gl_skip_bid_19 = models.CharField(db_column='GL_Skip_BID_19', max_length=4, blank=True, null=True)  # Field name made lowercase.
    gl_skip_bid_20 = models.CharField(db_column='GL_Skip_BID_20', max_length=4, blank=True, null=True)  # Field name made lowercase.
    gl_time_last = models.TimeField(db_column='GL_Time_Last', blank=True, null=True)  # Field name made lowercase.
    gl_who_last = models.CharField(db_column='GL_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gl'
        unique_together = (('GL_REC', 'GL_UNIQUE', 'GL_UNIQUE_1'),)


class Group(models.Model):
    g_d = models.CharField(db_column='G_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    g_key = models.CharField(db_column='G_KEY', primary_key=True, max_length=4)  # Field name made lowercase.
    g_time_last = models.TimeField(db_column='G_Time_Last', blank=True, null=True)  # Field name made lowercase.
    g_who_last = models.CharField(db_column='G_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'group'


class Licdets(models.Model):
    ld_d = models.CharField(db_column='LD_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ld_rec = models.IntegerField(db_column='LD_REC')  # Field name made lowercase.
    ld_unique = models.CharField(db_column='LD_UNIQUE', max_length=9)  # Field name made lowercase.
    ld_id_lh_b_id = models.CharField(db_column='LD_ID_LH_B_ID', max_length=4, blank=True, null=True)  # Field name made lowercase.
    ld_other_country = models.CharField(db_column='LD_Other_Country', max_length=2, blank=True, null=True)  # Field name made lowercase.
    ld_book_number = models.CharField(db_column='LD_Book_Number', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ld_book_rank_r_key = models.CharField(db_column='LD_Book_Rank_R_KEY', max_length=4, blank=True, null=True)  # Field name made lowercase.
    ld_book_issue = models.DateField(db_column='LD_Book_Issue', blank=True, null=True)  # Field name made lowercase.
    ld_book_expire = models.DateField(db_column='LD_Book_Expire', blank=True, null=True)  # Field name made lowercase.
    ld_license = models.CharField(db_column='LD_License', max_length=10, blank=True, null=True)  # Field name made lowercase.
    ld_rank_r_key = models.CharField(db_column='LD_Rank_R_KEY', max_length=4, blank=True, null=True)  # Field name made lowercase.
    ld_issue = models.DateField(db_column='LD_Issue', blank=True, null=True)  # Field name made lowercase.
    ld_expire = models.DateField(db_column='LD_Expire', blank=True, null=True)  # Field name made lowercase.
    ld_time_last = models.TimeField(db_column='LD_Time_Last', blank=True, null=True)  # Field name made lowercase.
    ld_who_last = models.CharField(db_column='LD_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'licdets'
        unique_together = (('LD_REC', 'LD_UNIQUE'),)


class Lichead(models.Model):
    lh_d = models.CharField(db_column='LH_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    lh_b_id = models.CharField(db_column='LH_B_ID', primary_key=True, max_length=4)  # Field name made lowercase.
    lh_rp_book_number = models.CharField(db_column='LH_RP_Book_Number', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lh_rp_book_issue = models.DateField(db_column='LH_RP_Book_Issue', blank=True, null=True)  # Field name made lowercase.
    lh_rp_book_expire = models.DateField(db_column='LH_RP_Book_Expire', blank=True, null=True)  # Field name made lowercase.
    lh_rp_book_place = models.CharField(db_column='LH_RP_Book_Place', max_length=12, blank=True, null=True)  # Field name made lowercase.
    lh_rp_license = models.CharField(db_column='LH_RP_License', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lh_rp_rank_r_key = models.CharField(db_column='LH_RP_Rank_R_KEY', max_length=4, blank=True, null=True)  # Field name made lowercase.
    lh_rp_issue = models.DateField(db_column='LH_RP_Issue', blank=True, null=True)  # Field name made lowercase.
    lh_rp_expire = models.DateField(db_column='LH_RP_Expire', blank=True, null=True)  # Field name made lowercase.
    lh_reg_card = models.CharField(db_column='LH_Reg_Card', max_length=14, blank=True, null=True)  # Field name made lowercase.
    lh_reg_issue = models.DateField(db_column='LH_Reg_Issue', blank=True, null=True)  # Field name made lowercase.
    lh_reg_expire = models.DateField(db_column='LH_Reg_Expire', blank=True, null=True)  # Field name made lowercase.
    lh_reg_rank_r_key = models.CharField(db_column='LH_Reg_Rank_R_KEY', max_length=4, blank=True, null=True)  # Field name made lowercase.
    lh_passport = models.CharField(db_column='LH_Passport', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lh_passport_issue = models.DateField(db_column='LH_Passport_Issue', blank=True, null=True)  # Field name made lowercase.
    lh_passport_expire = models.DateField(db_column='LH_Passport_Expire', blank=True, null=True)  # Field name made lowercase.
    lh_passport_place = models.CharField(db_column='LH_Passport_Place', max_length=8, blank=True, null=True)  # Field name made lowercase.
    lh_usa_visa = models.CharField(db_column='LH_USA_Visa', max_length=1, blank=True, null=True)  # Field name made lowercase.
    lh_usa_expire = models.DateField(db_column='LH_USA_Expire', blank=True, null=True)  # Field name made lowercase.
    lh_pending_legal = models.CharField(db_column='LH_Pending_Legal', max_length=24, blank=True, null=True)  # Field name made lowercase.
    lh_yellow_card = models.CharField(db_column='LH_Yellow_Card', max_length=1, blank=True, null=True)  # Field name made lowercase.
    lh_yellow_card_expire = models.DateField(db_column='LH_Yellow_Card_Expire', blank=True, null=True)  # Field name made lowercase.
    lh_dutch_visa = models.CharField(db_column='LH_Dutch_Visa', max_length=1, blank=True, null=True)  # Field name made lowercase.
    lh_dutch_expire = models.DateField(db_column='LH_Dutch_Expire', blank=True, null=True)  # Field name made lowercase.
    lh_time_last = models.TimeField(db_column='LH_Time_Last', blank=True, null=True)  # Field name made lowercase.
    lh_who_last = models.CharField(db_column='LH_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'lichead'


class M(models.Model):
    m_d = models.CharField(db_column='M_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    m_money = models.CharField(db_column='M_Money', primary_key=True, max_length=3)  # Field name made lowercase.
    m_desc = models.CharField(db_column='M_Desc', max_length=24, blank=True, null=True)  # Field name made lowercase.
    m_decpt = models.IntegerField(db_column='M_Decpt', blank=True, null=True)  # Field name made lowercase.
    m_time_last = models.TimeField(db_column='M_Time_Last', blank=True, null=True)  # Field name made lowercase.
    m_who_last = models.CharField(db_column='M_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'm'


class Managent(models.Model):
    man_d = models.CharField(db_column='MAN_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    man_key = models.CharField(db_column='MAN_KEY', primary_key=True, max_length=4)  # Field name made lowercase.
    man_full = models.CharField(db_column='MAN_Full', max_length=40, blank=True, null=True)  # Field name made lowercase.
    man_addr1 = models.CharField(db_column='MAN_Addr1', max_length=32, blank=True, null=True)  # Field name made lowercase.
    man_addr2 = models.CharField(db_column='MAN_Addr2', max_length=32, blank=True, null=True)  # Field name made lowercase.
    man_addr3 = models.CharField(db_column='MAN_Addr3', max_length=32, blank=True, null=True)  # Field name made lowercase.
    man_addr4 = models.CharField(db_column='MAN_Addr4', max_length=32, blank=True, null=True)  # Field name made lowercase.
    man_lawcountry = models.CharField(db_column='MAN_LawCountry', max_length=32, blank=True, null=True)  # Field name made lowercase.
    man_phonetelex = models.CharField(db_column='MAN_PhoneTelex', max_length=32, blank=True, null=True)  # Field name made lowercase.
    man_w_tax_agnt = models.CharField(db_column='MAN_W_Tax_Agnt', max_length=18, blank=True, null=True)  # Field name made lowercase.
    man_taxacct = models.CharField(db_column='MAN_TaxAcct', max_length=20, blank=True, null=True)  # Field name made lowercase.
    man_sss = models.CharField(db_column='MAN_SSS', max_length=16, blank=True, null=True)  # Field name made lowercase.
    man_aoh = models.CharField(db_column='MAN_AOH', max_length=32, blank=True, null=True)  # Field name made lowercase.
    man_of_key = models.CharField(db_column='MAN_OF_KEY', max_length=4, blank=True, null=True)  # Field name made lowercase.
    man_time_last = models.TimeField(db_column='MAN_Time_Last', blank=True, null=True)  # Field name made lowercase.
    man_who_last = models.CharField(db_column='MAN_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'managent'


class Monthly(models.Model):
    mon_d = models.CharField(db_column='MON_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    mon_rec = models.IntegerField(db_column='MON_REC')  # Field name made lowercase.
    mon_unique = models.CharField(db_column='MON_UNIQUE', max_length=21)  # Field name made lowercase.
    mon_unique_1 = models.CharField(db_column='MON_UNIQUE_1', max_length=23)  # Field name made lowercase.
    mon_type = models.CharField(db_column='MON_Type', max_length=1, blank=True, null=True)  # Field name made lowercase.
    mon_con_rec = models.IntegerField(db_column='MON_CON_REC', blank=True, null=True)  # Field name made lowercase.
    mon_w_rec = models.DecimalField(db_column='MON_W_REC', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_tax_rec = models.DecimalField(db_column='MON_TAX_REC', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_date_from = models.DateField(db_column='MON_Date_From', blank=True, null=True)  # Field name made lowercase.
    mon_date_to = models.DateField(db_column='MON_Date_To', blank=True, null=True)  # Field name made lowercase.
    mon_locked = models.CharField(db_column='MON_Locked', max_length=1, blank=True, null=True)  # Field name made lowercase.
    mon_closed = models.CharField(db_column='MON_Closed', max_length=1, blank=True, null=True)  # Field name made lowercase.
    mon_closed_date = models.DateField(db_column='MON_Closed_Date', blank=True, null=True)  # Field name made lowercase.
    mon_crew_category = models.CharField(db_column='MON_Crew_Category', max_length=1, blank=True, null=True)  # Field name made lowercase.
    mon_signoff = models.CharField(db_column='MON_Signoff', max_length=1, blank=True, null=True)  # Field name made lowercase.
    mon_wages_date = models.DateField(db_column='MON_Wages_Date', blank=True, null=True)  # Field name made lowercase.
    mon_no_of_months = models.IntegerField(db_column='MON_No_Of_Months', blank=True, null=True)  # Field name made lowercase.
    mon_no_of_days = models.IntegerField(db_column='MON_No_Of_Days', blank=True, null=True)  # Field name made lowercase.
    mon_nat_months = models.IntegerField(db_column='MON_Nat_Months', blank=True, null=True)  # Field name made lowercase.
    mon_nat_days = models.IntegerField(db_column='MON_Nat_Days', blank=True, null=True)  # Field name made lowercase.
    mon_hsingle = models.IntegerField(db_column='MON_Hsingle', blank=True, null=True)  # Field name made lowercase.
    mon_hdouble = models.IntegerField(db_column='MON_Hdouble', blank=True, null=True)  # Field name made lowercase.
    mon_hholiday = models.IntegerField(db_column='MON_Hholiday', blank=True, null=True)  # Field name made lowercase.
    mon_seniority = models.IntegerField(db_column='MON_Seniority', blank=True, null=True)  # Field name made lowercase.
    mon_seniority_rank = models.IntegerField(db_column='MON_Seniority_Rank', blank=True, null=True)  # Field name made lowercase.
    mon_port_days = models.IntegerField(db_column='MON_Port_Days', blank=True, null=True)  # Field name made lowercase.
    mon_leave_from = models.DateField(db_column='MON_Leave_From', blank=True, null=True)  # Field name made lowercase.
    mon_leave_to = models.DateField(db_column='MON_Leave_To', blank=True, null=True)  # Field name made lowercase.
    mon_months_of_leave = models.IntegerField(db_column='MON_Months_Of_Leave', blank=True, null=True)  # Field name made lowercase.
    mon_days_of_leave = models.IntegerField(db_column='MON_Days_Of_Leave', blank=True, null=True)  # Field name made lowercase.
    mon_earn_total = models.DecimalField(db_column='MON_Earn_Total', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_e_basic_salary = models.DecimalField(db_column='MON_E_Basic_Salary', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_e_increased_salary = models.DecimalField(db_column='MON_E_Increased_Salary', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_e_extra_descr = models.CharField(db_column='MON_E_Extra_Descr', max_length=32, blank=True, null=True)  # Field name made lowercase.
    mon_e_extra_amnt = models.DecimalField(db_column='MON_E_Extra_Amnt', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_e_cextra1 = models.DecimalField(db_column='MON_E_CExtra1', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_e_cextra2 = models.DecimalField(db_column='MON_E_CExtra2', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_hrb_descr = models.CharField(db_column='MON_HRB_Descr', max_length=32, blank=True, null=True)  # Field name made lowercase.
    mon_hrb_pay = models.DecimalField(db_column='MON_HRB_Pay', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_e_seniority = models.DecimalField(db_column='MON_E_Seniority', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_e_seniority_rank = models.DecimalField(db_column='MON_E_Seniority_Rank', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_e_comp_amnt_1 = models.DecimalField(db_column='MON_E_Comp_Amnt_1', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_e_comp_amnt_2 = models.DecimalField(db_column='MON_E_Comp_Amnt_2', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_e_comp_amnt_3 = models.DecimalField(db_column='MON_E_Comp_Amnt_3', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_e_comp_amnt_4 = models.DecimalField(db_column='MON_E_Comp_Amnt_4', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_e_comp_amnt_5 = models.DecimalField(db_column='MON_E_Comp_Amnt_5', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_e_comp_amnt_6 = models.DecimalField(db_column='MON_E_Comp_Amnt_6', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_e_comp_amnt_7 = models.DecimalField(db_column='MON_E_Comp_Amnt_7', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_e_comp_amnt_8 = models.DecimalField(db_column='MON_E_Comp_Amnt_8', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_e_comp_amnt_9 = models.DecimalField(db_column='MON_E_Comp_Amnt_9', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_e_comp_amnt_10 = models.DecimalField(db_column='MON_E_Comp_Amnt_10', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_e_comp_amnt_11 = models.DecimalField(db_column='MON_E_Comp_Amnt_11', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_e_comp_amnt_12 = models.DecimalField(db_column='MON_E_Comp_Amnt_12', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_e_comp_amnt_13 = models.DecimalField(db_column='MON_E_Comp_Amnt_13', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_e_comp_amnt_14 = models.DecimalField(db_column='MON_E_Comp_Amnt_14', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_e_comp_amnt_15 = models.DecimalField(db_column='MON_E_Comp_Amnt_15', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_e_comp_amnt_16 = models.DecimalField(db_column='MON_E_Comp_Amnt_16', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_e_comp_amnt_17 = models.DecimalField(db_column='MON_E_Comp_Amnt_17', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_e_comp_amnt_18 = models.DecimalField(db_column='MON_E_Comp_Amnt_18', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_e_comp_amnt_19 = models.DecimalField(db_column='MON_E_Comp_Amnt_19', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_e_comp_amnt_20 = models.DecimalField(db_column='MON_E_Comp_Amnt_20', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_e_comp_amnt_21 = models.DecimalField(db_column='MON_E_Comp_Amnt_21', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_e_comp_amnt_22 = models.DecimalField(db_column='MON_E_Comp_Amnt_22', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_e_comp_amnt_23 = models.DecimalField(db_column='MON_E_Comp_Amnt_23', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_e_comp_amnt_24 = models.DecimalField(db_column='MON_E_Comp_Amnt_24', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_comp_amnt_1 = models.DecimalField(db_column='MON_D_Comp_Amnt_1', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_comp_amnt_2 = models.DecimalField(db_column='MON_D_Comp_Amnt_2', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_comp_amnt_3 = models.DecimalField(db_column='MON_D_Comp_Amnt_3', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_comp_amnt_4 = models.DecimalField(db_column='MON_D_Comp_Amnt_4', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_comp_amnt_5 = models.DecimalField(db_column='MON_D_Comp_Amnt_5', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_comp_amnt_6 = models.DecimalField(db_column='MON_D_Comp_Amnt_6', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_comp_amnt_7 = models.DecimalField(db_column='MON_D_Comp_Amnt_7', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_comp_amnt_8 = models.DecimalField(db_column='MON_D_Comp_Amnt_8', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_comp_amnt_9 = models.DecimalField(db_column='MON_D_Comp_Amnt_9', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_comp_amnt_10 = models.DecimalField(db_column='MON_D_Comp_Amnt_10', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_comp_amnt_11 = models.DecimalField(db_column='MON_D_Comp_Amnt_11', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_comp_amnt_12 = models.DecimalField(db_column='MON_D_Comp_Amnt_12', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_comp_amnt_13 = models.DecimalField(db_column='MON_D_Comp_Amnt_13', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_comp_amnt_14 = models.DecimalField(db_column='MON_D_Comp_Amnt_14', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_comp_amnt_15 = models.DecimalField(db_column='MON_D_Comp_Amnt_15', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_comp_amnt_16 = models.DecimalField(db_column='MON_D_Comp_Amnt_16', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_comp_amnt_17 = models.DecimalField(db_column='MON_D_Comp_Amnt_17', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_comp_amnt_18 = models.DecimalField(db_column='MON_D_Comp_Amnt_18', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_comp_amnt_19 = models.DecimalField(db_column='MON_D_Comp_Amnt_19', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_comp_amnt_20 = models.DecimalField(db_column='MON_D_Comp_Amnt_20', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_comp_amnt_21 = models.DecimalField(db_column='MON_D_Comp_Amnt_21', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_comp_amnt_22 = models.DecimalField(db_column='MON_D_Comp_Amnt_22', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_comp_amnt_23 = models.DecimalField(db_column='MON_D_Comp_Amnt_23', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_comp_amnt_24 = models.DecimalField(db_column='MON_D_Comp_Amnt_24', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_comp_amnt_25 = models.DecimalField(db_column='MON_D_Comp_Amnt_25', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_comp_amnt_26 = models.DecimalField(db_column='MON_D_Comp_Amnt_26', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_comp_amnt_27 = models.DecimalField(db_column='MON_D_Comp_Amnt_27', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_comp_amnt_28 = models.DecimalField(db_column='MON_D_Comp_Amnt_28', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_comp_amnt_29 = models.DecimalField(db_column='MON_D_Comp_Amnt_29', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_comp_amnt_30 = models.DecimalField(db_column='MON_D_Comp_Amnt_30', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_comp_amnt_31 = models.DecimalField(db_column='MON_D_Comp_Amnt_31', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_comp_amnt_32 = models.DecimalField(db_column='MON_D_Comp_Amnt_32', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_comp_amnt_33 = models.DecimalField(db_column='MON_D_Comp_Amnt_33', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_comp_amnt_34 = models.DecimalField(db_column='MON_D_Comp_Amnt_34', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_comp_amnt_35 = models.DecimalField(db_column='MON_D_Comp_Amnt_35', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_comp_amnt_36 = models.DecimalField(db_column='MON_D_Comp_Amnt_36', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_allot_date1 = models.DateField(db_column='MON_D_Allot_Date1', blank=True, null=True)  # Field name made lowercase.
    mon_d_allot_curr1 = models.CharField(db_column='MON_D_Allot_Curr1', max_length=3, blank=True, null=True)  # Field name made lowercase.
    mon_d_allot_comm1 = models.CharField(db_column='MON_D_Allot_Comm1', max_length=32, blank=True, null=True)  # Field name made lowercase.
    mon_d_allot_amnt1_usd = models.DecimalField(db_column='MON_D_Allot_Amnt1_USD', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_allot_amnt1 = models.DecimalField(db_column='MON_D_Allot_Amnt1', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_allot_date2 = models.DateField(db_column='MON_D_Allot_Date2', blank=True, null=True)  # Field name made lowercase.
    mon_d_allot_curr2 = models.CharField(db_column='MON_D_Allot_Curr2', max_length=3, blank=True, null=True)  # Field name made lowercase.
    mon_d_allot_comm2 = models.CharField(db_column='MON_D_Allot_Comm2', max_length=32, blank=True, null=True)  # Field name made lowercase.
    mon_d_allot_amnt2_usd = models.DecimalField(db_column='MON_D_Allot_Amnt2_USD', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_allot_amnt2 = models.DecimalField(db_column='MON_D_Allot_Amnt2', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_allot_date3 = models.DateField(db_column='MON_D_Allot_Date3', blank=True, null=True)  # Field name made lowercase.
    mon_d_allot_curr3 = models.CharField(db_column='MON_D_Allot_Curr3', max_length=3, blank=True, null=True)  # Field name made lowercase.
    mon_d_allot_comm3 = models.CharField(db_column='MON_D_Allot_Comm3', max_length=32, blank=True, null=True)  # Field name made lowercase.
    mon_d_allot_amnt3_usd = models.DecimalField(db_column='MON_D_Allot_Amnt3_USD', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_allot_amnt3 = models.DecimalField(db_column='MON_D_Allot_Amnt3', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_allot_date4 = models.DateField(db_column='MON_D_Allot_Date4', blank=True, null=True)  # Field name made lowercase.
    mon_d_allot_curr4 = models.CharField(db_column='MON_D_Allot_Curr4', max_length=3, blank=True, null=True)  # Field name made lowercase.
    mon_d_allot_comm4 = models.CharField(db_column='MON_D_Allot_Comm4', max_length=32, blank=True, null=True)  # Field name made lowercase.
    mon_d_allot_amnt4_usd = models.DecimalField(db_column='MON_D_Allot_Amnt4_USD', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_allot_amnt4 = models.DecimalField(db_column='MON_D_Allot_Amnt4', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_allot_total_usd = models.DecimalField(db_column='MON_D_Allot_Total_USD', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_allot_total = models.DecimalField(db_column='MON_D_Allot_Total', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_advance_date1 = models.DateField(db_column='MON_D_Advance_Date1', blank=True, null=True)  # Field name made lowercase.
    mon_d_advance_adp_key1 = models.CharField(db_column='MON_D_Advance_ADP_KEY1', max_length=1, blank=True, null=True)  # Field name made lowercase.
    mon_d_advance_curr1_local = models.CharField(db_column='MON_D_Advance_Curr1_Local', max_length=3, blank=True, null=True)  # Field name made lowercase.
    mon_d_advance_rate1_local = models.DecimalField(db_column='MON_D_Advance_Rate1_Local', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_advance_amnt1_local = models.DecimalField(db_column='MON_D_Advance_Amnt1_Local', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_advance_amnt1_usd = models.DecimalField(db_column='MON_D_Advance_Amnt1_USD', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_advance_amnt1 = models.DecimalField(db_column='MON_D_Advance_Amnt1', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_advance_date2 = models.DateField(db_column='MON_D_Advance_Date2', blank=True, null=True)  # Field name made lowercase.
    mon_d_advance_adp_key2 = models.CharField(db_column='MON_D_Advance_ADP_KEY2', max_length=1, blank=True, null=True)  # Field name made lowercase.
    mon_d_advance_curr2_local = models.CharField(db_column='MON_D_Advance_Curr2_Local', max_length=3, blank=True, null=True)  # Field name made lowercase.
    mon_d_advance_rate2_local = models.DecimalField(db_column='MON_D_Advance_Rate2_Local', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_advance_amnt2_local = models.DecimalField(db_column='MON_D_Advance_Amnt2_Local', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_advance_amnt2_usd = models.DecimalField(db_column='MON_D_Advance_Amnt2_USD', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_advance_amnt2 = models.DecimalField(db_column='MON_D_Advance_Amnt2', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_advance_date3 = models.DateField(db_column='MON_D_Advance_Date3', blank=True, null=True)  # Field name made lowercase.
    mon_d_advance_adp_key3 = models.CharField(db_column='MON_D_Advance_ADP_KEY3', max_length=1, blank=True, null=True)  # Field name made lowercase.
    mon_d_advance_curr3_local = models.CharField(db_column='MON_D_Advance_Curr3_Local', max_length=3, blank=True, null=True)  # Field name made lowercase.
    mon_d_advance_rate3_local = models.DecimalField(db_column='MON_D_Advance_Rate3_Local', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_advance_amnt3_local = models.DecimalField(db_column='MON_D_Advance_Amnt3_Local', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_advance_amnt3_usd = models.DecimalField(db_column='MON_D_Advance_Amnt3_USD', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_advance_amnt3 = models.DecimalField(db_column='MON_D_Advance_Amnt3', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_advance_date4 = models.DateField(db_column='MON_D_Advance_Date4', blank=True, null=True)  # Field name made lowercase.
    mon_d_advance_adp_key4 = models.CharField(db_column='MON_D_Advance_ADP_KEY4', max_length=1, blank=True, null=True)  # Field name made lowercase.
    mon_d_advance_curr4_local = models.CharField(db_column='MON_D_Advance_Curr4_Local', max_length=3, blank=True, null=True)  # Field name made lowercase.
    mon_d_advance_rate4_local = models.DecimalField(db_column='MON_D_Advance_Rate4_Local', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_advance_amnt4_local = models.DecimalField(db_column='MON_D_Advance_Amnt4_Local', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_advance_amnt4_usd = models.DecimalField(db_column='MON_D_Advance_Amnt4_USD', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_advance_amnt4 = models.DecimalField(db_column='MON_D_Advance_Amnt4', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_advance_total_usd = models.DecimalField(db_column='MON_D_Advance_Total_USD', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_advance_total = models.DecimalField(db_column='MON_D_Advance_Total', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_phone_comm1 = models.CharField(db_column='MON_D_Phone_Comm1', max_length=32, blank=True, null=True)  # Field name made lowercase.
    mon_d_phone_amnt1_usd = models.DecimalField(db_column='MON_D_Phone_Amnt1_USD', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_phone_amnt1 = models.DecimalField(db_column='MON_D_Phone_Amnt1', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_bond_quan1 = models.IntegerField(db_column='MON_D_Bond_Quan1', blank=True, null=True)  # Field name made lowercase.
    mon_d_bond_peri1 = models.DecimalField(db_column='MON_D_Bond_PerI1', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_bond_rate1 = models.DecimalField(db_column='MON_D_Bond_Rate1', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_bond_amnt1_usd = models.DecimalField(db_column='MON_D_Bond_Amnt1_USD', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_bond_amnt1 = models.DecimalField(db_column='MON_D_Bond_Amnt1', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_bond_comm1 = models.CharField(db_column='MON_D_Bond_Comm1', max_length=32, blank=True, null=True)  # Field name made lowercase.
    mon_d_bond_quan2 = models.IntegerField(db_column='MON_D_Bond_Quan2', blank=True, null=True)  # Field name made lowercase.
    mon_d_bond_peri2 = models.DecimalField(db_column='MON_D_Bond_PerI2', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_bond_rate2 = models.DecimalField(db_column='MON_D_Bond_Rate2', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_bond_amnt2_usd = models.DecimalField(db_column='MON_D_Bond_Amnt2_USD', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_bond_amnt2 = models.DecimalField(db_column='MON_D_Bond_Amnt2', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_bond_comm2 = models.CharField(db_column='MON_D_Bond_Comm2', max_length=32, blank=True, null=True)  # Field name made lowercase.
    mon_d_bond_quan3 = models.IntegerField(db_column='MON_D_Bond_Quan3', blank=True, null=True)  # Field name made lowercase.
    mon_d_bond_peri3 = models.DecimalField(db_column='MON_D_Bond_PerI3', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_bond_rate3 = models.DecimalField(db_column='MON_D_Bond_Rate3', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_bond_amnt3_usd = models.DecimalField(db_column='MON_D_Bond_Amnt3_USD', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_bond_amnt3 = models.DecimalField(db_column='MON_D_Bond_Amnt3', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_bond_comm3 = models.CharField(db_column='MON_D_Bond_Comm3', max_length=32, blank=True, null=True)  # Field name made lowercase.
    mon_d_bond_quan4 = models.IntegerField(db_column='MON_D_Bond_Quan4', blank=True, null=True)  # Field name made lowercase.
    mon_d_bond_peri4 = models.DecimalField(db_column='MON_D_Bond_PerI4', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_bond_rate4 = models.DecimalField(db_column='MON_D_Bond_Rate4', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_bond_amnt4_usd = models.DecimalField(db_column='MON_D_Bond_Amnt4_USD', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_bond_amnt4 = models.DecimalField(db_column='MON_D_Bond_Amnt4', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_bond_comm4 = models.CharField(db_column='MON_D_Bond_Comm4', max_length=32, blank=True, null=True)  # Field name made lowercase.
    mon_d_bond_quan5 = models.IntegerField(db_column='MON_D_Bond_Quan5', blank=True, null=True)  # Field name made lowercase.
    mon_d_bond_peri5 = models.DecimalField(db_column='MON_D_Bond_PerI5', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_bond_rate5 = models.DecimalField(db_column='MON_D_Bond_Rate5', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_bond_amnt5_usd = models.DecimalField(db_column='MON_D_Bond_Amnt5_USD', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_bond_amnt5 = models.DecimalField(db_column='MON_D_Bond_Amnt5', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_bond_comm5 = models.CharField(db_column='MON_D_Bond_Comm5', max_length=32, blank=True, null=True)  # Field name made lowercase.
    mon_d_bond_total_usd = models.DecimalField(db_column='MON_D_Bond_Total_USD', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_bond_total = models.DecimalField(db_column='MON_D_Bond_Total', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_repatriate_com = models.CharField(db_column='MON_D_Repatriate_Com', max_length=32, blank=True, null=True)  # Field name made lowercase.
    mon_d_repatriate_usd = models.DecimalField(db_column='MON_D_Repatriate_USD', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_repatriate = models.DecimalField(db_column='MON_D_Repatriate', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_extra1_descr = models.CharField(db_column='MON_D_Extra1_Descr', max_length=32, blank=True, null=True)  # Field name made lowercase.
    mon_d_extra1_usd = models.DecimalField(db_column='MON_D_Extra1_USD', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_extra1 = models.DecimalField(db_column='MON_D_Extra1', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_extra2_descr = models.CharField(db_column='MON_D_Extra2_Descr', max_length=32, blank=True, null=True)  # Field name made lowercase.
    mon_d_extra2_usd = models.DecimalField(db_column='MON_D_Extra2_USD', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_extra2 = models.DecimalField(db_column='MON_D_Extra2', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_total = models.DecimalField(db_column='MON_D_Total', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_fmy_comm = models.CharField(db_column='MON_D_Fmy_Comm', max_length=32, blank=True, null=True)  # Field name made lowercase.
    mon_d_tax_comm = models.CharField(db_column='MON_D_TAX_Comm', max_length=32, blank=True, null=True)  # Field name made lowercase.
    mon_e_taxable = models.DecimalField(db_column='MON_E_Taxable', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_taxable_amnt = models.DecimalField(db_column='MON_Taxable_Amnt', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_nat_total = models.DecimalField(db_column='MON_D_Nat_Total', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_d_seaman_taxes = models.DecimalField(db_column='MON_D_Seaman_Taxes', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_seaman_dstamp = models.DecimalField(db_column='MON_Seaman_Dstamp', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_seaman_doga = models.DecimalField(db_column='MON_Seaman_Doga', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_seaman_dtax = models.DecimalField(db_column='MON_Seaman_Dtax', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_seaman_dtax_oga = models.DecimalField(db_column='MON_Seaman_Dtax_Oga', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_seaman_dtax_anal = models.DecimalField(db_column='MON_Seaman_Dtax_Anal', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_seaman_dtax_oga_anal = models.DecimalField(db_column='MON_Seaman_Dtax_Oga_Anal', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_prev_balance = models.DecimalField(db_column='MON_Prev_Balance', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_curr_balance = models.DecimalField(db_column='MON_Curr_Balance', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_forw_balance = models.DecimalField(db_column='MON_Forw_Balance', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_retro_balance = models.DecimalField(db_column='MON_Retro_Balance', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    mon_time_last = models.TimeField(db_column='MON_Time_Last', blank=True, null=True)  # Field name made lowercase.
    mon_who_last = models.CharField(db_column='MON_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'monthly'
        unique_together = (('MON_REC', 'MON_UNIQUE', 'MON_UNIQUE_1'),)


class Official(models.Model):
    of_d = models.CharField(db_column='OF_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    of_key = models.CharField(db_column='OF_KEY', primary_key=True, max_length=4)  # Field name made lowercase.
    of_full = models.CharField(db_column='OF_Full', max_length=24, blank=True, null=True)  # Field name made lowercase.
    of_position = models.CharField(db_column='OF_Position', max_length=16, blank=True, null=True)  # Field name made lowercase.
    of_taxacct = models.CharField(db_column='OF_TaxAcct', max_length=20, blank=True, null=True)  # Field name made lowercase.
    of_time_last = models.TimeField(db_column='OF_Time_Last', blank=True, null=True)  # Field name made lowercase.
    of_who_last = models.CharField(db_column='OF_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'official'


class Pbio(models.Model):
    pb_d = models.CharField(db_column='PB_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    pb_rec = models.IntegerField(db_column='PB_REC', primary_key=True)  # Field name made lowercase.
    pb_unique = models.CharField(db_column='PB_UNIQUE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    pb_b_id = models.CharField(db_column='PB_B_ID', max_length=4, blank=True, null=True)  # Field name made lowercase.
    pb_p_key = models.CharField(db_column='PB_P_KEY', max_length=6, blank=True, null=True)  # Field name made lowercase.
    pb_start = models.DateField(db_column='PB_Start', blank=True, null=True)  # Field name made lowercase.
    pb_end = models.DateField(db_column='PB_End', blank=True, null=True)  # Field name made lowercase.
    pb_time_last = models.TimeField(db_column='PB_Time_Last', blank=True, null=True)  # Field name made lowercase.
    pb_who_last = models.CharField(db_column='PB_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pbio'


class Principal(models.Model):
    p_d = models.CharField(db_column='P_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    p_key = models.CharField(db_column='P_KEY', primary_key=True, max_length=6)  # Field name made lowercase.
    p_master_p_key = models.CharField(db_column='P_Master_P_KEY', max_length=6, blank=True, null=True)  # Field name made lowercase.
    p_full = models.CharField(db_column='P_Full', max_length=40, blank=True, null=True)  # Field name made lowercase.
    p_sss = models.CharField(db_column='P_SSS', max_length=12, blank=True, null=True)  # Field name made lowercase.
    p_accredno = models.CharField(db_column='P_AccredNo', max_length=12, blank=True, null=True)  # Field name made lowercase.
    p_addr1 = models.CharField(db_column='P_Addr1', max_length=32, blank=True, null=True)  # Field name made lowercase.
    p_addr2 = models.CharField(db_column='P_Addr2', max_length=32, blank=True, null=True)  # Field name made lowercase.
    p_addr3 = models.CharField(db_column='P_Addr3', max_length=32, blank=True, null=True)  # Field name made lowercase.
    p_lawcountry = models.CharField(db_column='P_LawCountry', max_length=24, blank=True, null=True)  # Field name made lowercase.
    p_telephone = models.CharField(db_column='P_Telephone', max_length=32, blank=True, null=True)  # Field name made lowercase.
    p_email_address = models.CharField(db_column='P_Email_Address', max_length=36, blank=True, null=True)  # Field name made lowercase.
    p_acct_category_a = models.CharField(db_column='P_Acct_Category_A', max_length=16, blank=True, null=True)  # Field name made lowercase.
    p_acct_category_b = models.CharField(db_column='P_Acct_Category_B', max_length=16, blank=True, null=True)  # Field name made lowercase.
    p_acct_category_c = models.CharField(db_column='P_Acct_Category_C', max_length=16, blank=True, null=True)  # Field name made lowercase.
    p_acct_category_d = models.CharField(db_column='P_Acct_Category_D', max_length=16, blank=True, null=True)  # Field name made lowercase.
    p_acct_category_e = models.CharField(db_column='P_Acct_Category_E', max_length=16, blank=True, null=True)  # Field name made lowercase.
    p_acct_category_f = models.CharField(db_column='P_Acct_Category_F', max_length=16, blank=True, null=True)  # Field name made lowercase.
    p_acct_category_g = models.CharField(db_column='P_Acct_Category_G', max_length=16, blank=True, null=True)  # Field name made lowercase.
    p_acct_expenses = models.CharField(db_column='P_Acct_Expenses', max_length=16, blank=True, null=True)  # Field name made lowercase.
    p_time_last = models.TimeField(db_column='P_Time_Last', blank=True, null=True)  # Field name made lowercase.
    p_who_last = models.CharField(db_column='P_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'principal'


class Rank(models.Model):
    r_d = models.CharField(db_column='R_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    r_key = models.CharField(db_column='R_KEY', primary_key=True, max_length=4)  # Field name made lowercase.
    r_full = models.CharField(db_column='R_Full', max_length=16, blank=True, null=True)  # Field name made lowercase.
    r_grk_desc = models.CharField(db_column='R_Grk_Desc', max_length=20, blank=True, null=True)  # Field name made lowercase.
    r_sort = models.CharField(db_column='R_Sort', max_length=2, blank=True, null=True)  # Field name made lowercase.
    r_tc_key = models.CharField(db_column='R_TC_KEY', max_length=1, blank=True, null=True)  # Field name made lowercase.
    r_officer = models.CharField(db_column='R_Officer', max_length=1, blank=True, null=True)  # Field name made lowercase.
    r_time_last = models.TimeField(db_column='R_Time_Last', blank=True, null=True)  # Field name made lowercase.
    r_who_last = models.CharField(db_column='R_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rank'


class Receipt(models.Model):
    rcv_d = models.CharField(db_column='RCV_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rcv_rec = models.IntegerField(db_column='RCV_REC')  # Field name made lowercase.
    rcv_unique = models.CharField(db_column='RCV_UNIQUE', max_length=15)  # Field name made lowercase.
    rcv_prin_p_key = models.CharField(db_column='RCV_Prin_P_KEY', max_length=6, blank=True, null=True)  # Field name made lowercase.
    rcv_date = models.DateField(db_column='RCV_Date', blank=True, null=True)  # Field name made lowercase.
    rcv_bank_bk_key = models.CharField(db_column='RCV_Bank_BK_KEY', max_length=4, blank=True, null=True)  # Field name made lowercase.
    rcv_fund_date = models.DateField(db_column='RCV_Fund_Date', blank=True, null=True)  # Field name made lowercase.
    rcv_fx_rate = models.DecimalField(db_column='RCV_FX_Rate', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    rcv_usd = models.DecimalField(db_column='RCV_USD', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    rcv_peso = models.DecimalField(db_column='RCV_Peso', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    rcv_allot_std = models.DecimalField(db_column='RCV_Allot_Std', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    rcv_allot_add = models.DecimalField(db_column='RCV_Allot_Add', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    rcv_category_amnt_a = models.DecimalField(db_column='RCV_Category_Amnt_A', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    rcv_category_amnt_b = models.DecimalField(db_column='RCV_Category_Amnt_B', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    rcv_category_amnt_c = models.DecimalField(db_column='RCV_Category_Amnt_C', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    rcv_category_amnt_d = models.DecimalField(db_column='RCV_Category_Amnt_D', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    rcv_category_amnt_e = models.DecimalField(db_column='RCV_Category_Amnt_E', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    rcv_category_amnt_f = models.DecimalField(db_column='RCV_Category_Amnt_F', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    rcv_category_amnt_g = models.DecimalField(db_column='RCV_Category_Amnt_G', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    rcv_expenses = models.DecimalField(db_column='RCV_Expenses', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    rcv_time_last = models.TimeField(db_column='RCV_Time_Last', blank=True, null=True)  # Field name made lowercase.
    rcv_who_last = models.CharField(db_column='RCV_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'receipt'
        unique_together = (('RCV_REC', 'RCV_UNIQUE'),)


class Relations(models.Model):
    rel_d = models.CharField(db_column='REL_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rel_key = models.CharField(db_column='REL_KEY', primary_key=True, max_length=4)  # Field name made lowercase.
    rel_full = models.CharField(db_column='REL_FULL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    rel_time_last = models.TimeField(db_column='REL_Time_Last', blank=True, null=True)  # Field name made lowercase.
    rel_who_last = models.CharField(db_column='REL_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'relations'


class Reporter(models.Model):
    rep_d = models.CharField(db_column='REP_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rep_key = models.CharField(db_column='REP_KEY', primary_key=True, max_length=4)  # Field name made lowercase.
    rep_full = models.CharField(db_column='REP_Full', max_length=24, blank=True, null=True)  # Field name made lowercase.
    rep_rank_r_key = models.CharField(db_column='REP_Rank_R_KEY', max_length=4, blank=True, null=True)  # Field name made lowercase.
    rep_time_last = models.TimeField(db_column='REP_Time_Last', blank=True, null=True)  # Field name made lowercase.
    rep_who_last = models.CharField(db_column='REP_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'reporter'


class ReqCert(models.Model):
    rc_d = models.CharField(db_column='RC_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rc_rec = models.IntegerField(db_column='RC_REC')  # Field name made lowercase.
    rc_unique = models.CharField(db_column='RC_UNIQUE', max_length=18)  # Field name made lowercase.
    rc_p_key = models.CharField(db_column='RC_P_KEY', max_length=6, blank=True, null=True)  # Field name made lowercase.
    rc_vc_key = models.CharField(db_column='RC_VC_KEY', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rc_r_key = models.CharField(db_column='RC_R_KEY', max_length=4, blank=True, null=True)  # Field name made lowercase.
    rc_cg_key = models.CharField(db_column='RC_CG_KEY', max_length=4, blank=True, null=True)  # Field name made lowercase.
    rc_source = models.CharField(db_column='RC_Source', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rc_interval = models.DecimalField(db_column='RC_Interval', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    rc_time_last = models.TimeField(db_column='RC_Time_Last', blank=True, null=True)  # Field name made lowercase.
    rc_who_last = models.CharField(db_column='RC_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'req_cert'
        unique_together = (('RC_REC', 'RC_UNIQUE'),)


class Rgdets(models.Model):
    rgd_d = models.CharField(db_column='RGD_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rgd_rec = models.IntegerField(db_column='RGD_REC')  # Field name made lowercase.
    rgd_unique = models.CharField(db_column='RGD_UNIQUE', max_length=13)  # Field name made lowercase.
    rgd_rg_key = models.CharField(db_column='RGD_RG_KEY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    rgd_r_key = models.CharField(db_column='RGD_R_KEY', max_length=4, blank=True, null=True)  # Field name made lowercase.
    rgd_status = models.CharField(db_column='RGD_Status', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rgd_tags = models.CharField(db_column='RGD_Tags', max_length=16, blank=True, null=True)  # Field name made lowercase.
    rgd_time_last = models.TimeField(db_column='RGD_Time_Last', blank=True, null=True)  # Field name made lowercase.
    rgd_who_last = models.CharField(db_column='RGD_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rgdets'
        unique_together = (('RGD_REC', 'RGD_UNIQUE'),)


class Rghead(models.Model):
    rg_d = models.CharField(db_column='RG_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rg_key = models.CharField(db_column='RG_KEY', primary_key=True, max_length=8)  # Field name made lowercase.
    rg_full = models.CharField(db_column='RG_Full', max_length=32, blank=True, null=True)  # Field name made lowercase.
    rg_group_by = models.CharField(db_column='RG_Group_By', max_length=12, blank=True, null=True)  # Field name made lowercase.
    rg_p_key = models.CharField(db_column='RG_P_Key', max_length=6, blank=True, null=True)  # Field name made lowercase.
    rg_status = models.CharField(db_column='RG_Status', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rg_time_last = models.TimeField(db_column='RG_Time_Last', blank=True, null=True)  # Field name made lowercase.
    rg_who_last = models.CharField(db_column='RG_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rghead'


class Roster(models.Model):
    cr_d = models.CharField(db_column='CR_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cr_rec = models.IntegerField(db_column='CR_REC', primary_key=True)  # Field name made lowercase.
    cr_unique = models.CharField(db_column='CR_UNIQUE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    cr_b_id = models.CharField(db_column='CR_B_ID', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cr_p_key = models.CharField(db_column='CR_P_KEY', max_length=6, blank=True, null=True)  # Field name made lowercase.
    cr_start = models.DateField(db_column='CR_Start', blank=True, null=True)  # Field name made lowercase.
    cr_end = models.DateField(db_column='CR_End', blank=True, null=True)  # Field name made lowercase.
    cr_rank_1 = models.CharField(db_column='CR_Rank_1', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cr_rank_2 = models.CharField(db_column='CR_Rank_2', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cr_rank_3 = models.CharField(db_column='CR_Rank_3', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cr_vg_key = models.CharField(db_column='CR_VG_Key', max_length=8, blank=True, null=True)  # Field name made lowercase.
    cr_next_ship = models.CharField(db_column='CR_Next_Ship', max_length=4, blank=True, null=True)  # Field name made lowercase.
    cr_general_comments_1 = models.CharField(db_column='CR_General_Comments_1', max_length=70, blank=True, null=True)  # Field name made lowercase.
    cr_general_comments_2 = models.CharField(db_column='CR_General_Comments_2', max_length=70, blank=True, null=True)  # Field name made lowercase.
    cr_availability_comments = models.CharField(db_column='CR_Availability_Comments', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cr_availability_date = models.DateField(db_column='CR_Availability_Date', blank=True, null=True)  # Field name made lowercase.
    cr_status = models.CharField(db_column='CR_Status', max_length=1, blank=True, null=True)  # Field name made lowercase.
    cr_time_last = models.TimeField(db_column='CR_Time_Last', blank=True, null=True)  # Field name made lowercase.
    cr_who_last = models.CharField(db_column='CR_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'roster'


class Rosterd(models.Model):
    rd_d = models.CharField(db_column='RD_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rd_rec = models.IntegerField(db_column='RD_REC', primary_key=True)  # Field name made lowercase.
    rd_rh_rec = models.IntegerField(db_column='RD_RH_REC', blank=True, null=True)  # Field name made lowercase.
    rd_b_id = models.CharField(db_column='RD_B_ID', max_length=4, blank=True, null=True)  # Field name made lowercase.
    rd_status = models.CharField(db_column='RD_Status', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rd_current_rank = models.CharField(db_column='RD_Current_Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    rd_next_rank = models.CharField(db_column='RD_Next_Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    rd_current_ship = models.CharField(db_column='RD_Current_Ship', max_length=4, blank=True, null=True)  # Field name made lowercase.
    rd_next_ship = models.CharField(db_column='RD_Next_Ship', max_length=4, blank=True, null=True)  # Field name made lowercase.
    rd_general_comments = models.CharField(db_column='RD_General_Comments', max_length=100, blank=True, null=True)  # Field name made lowercase.
    rd_availability_comments = models.CharField(db_column='RD_Availability_Comments', max_length=50, blank=True, null=True)  # Field name made lowercase.
    rd_availability_date = models.DateField(db_column='RD_Availability_Date', blank=True, null=True)  # Field name made lowercase.
    rd_time_last = models.TimeField(db_column='RD_Time_Last', blank=True, null=True)  # Field name made lowercase.
    rd_who_last = models.CharField(db_column='RD_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rosterd'


class Rosterh(models.Model):
    rh_d = models.CharField(db_column='RH_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rh_rec = models.IntegerField(db_column='RH_REC', primary_key=True)  # Field name made lowercase.
    rh_unique = models.CharField(db_column='RH_UNIQUE', max_length=14, blank=True, null=True)  # Field name made lowercase.
    rh_vg_key = models.CharField(db_column='RH_VG_Key', max_length=8, blank=True, null=True)  # Field name made lowercase.
    rh_department = models.CharField(db_column='RH_Department', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rh_rank = models.CharField(db_column='RH_Rank', max_length=3, blank=True, null=True)  # Field name made lowercase.
    rh_general_comments_1 = models.CharField(db_column='RH_General_Comments_1', max_length=100, blank=True, null=True)  # Field name made lowercase.
    rh_general_comments_2 = models.CharField(db_column='RH_General_Comments_2', max_length=100, blank=True, null=True)  # Field name made lowercase.
    rh_general_comments_3 = models.CharField(db_column='RH_General_Comments_3', max_length=100, blank=True, null=True)  # Field name made lowercase.
    rh_time_last = models.TimeField(db_column='RH_Time_Last', blank=True, null=True)  # Field name made lowercase.
    rh_who_last = models.CharField(db_column='RH_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rosterh'


class Rostervg(models.Model):
    rv_d = models.CharField(db_column='RV_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    rv_vg_key = models.CharField(db_column='RV_VG_Key', primary_key=True, max_length=8)  # Field name made lowercase.
    rv_time_last = models.TimeField(db_column='RV_Time_Last', blank=True, null=True)  # Field name made lowercase.
    rv_who_last = models.CharField(db_column='RV_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rostervg'


class Secret(models.Model):
    se_d = models.CharField(db_column='SE_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    se_rec = models.IntegerField(db_column='SE_REC')  # Field name made lowercase.
    se_unique = models.CharField(db_column='SE_UNIQUE', max_length=18)  # Field name made lowercase.
    se_id_b_id = models.CharField(db_column='SE_ID_B_ID', max_length=4, blank=True, null=True)  # Field name made lowercase.
    se_id_b2_id = models.CharField(db_column='SE_ID_B2_ID', max_length=4, blank=True, null=True)  # Field name made lowercase.
    se_date = models.DateField(db_column='SE_Date', blank=True, null=True)  # Field name made lowercase.
    se_grade = models.IntegerField(db_column='SE_Grade', blank=True, null=True)  # Field name made lowercase.
    se_comments_1 = models.CharField(db_column='SE_Comments_1', max_length=75, blank=True, null=True)  # Field name made lowercase.
    se_comments_2 = models.CharField(db_column='SE_Comments_2', max_length=75, blank=True, null=True)  # Field name made lowercase.
    se_comments_3 = models.CharField(db_column='SE_Comments_3', max_length=75, blank=True, null=True)  # Field name made lowercase.
    se_comments_4 = models.CharField(db_column='SE_Comments_4', max_length=75, blank=True, null=True)  # Field name made lowercase.
    se_comments_5 = models.CharField(db_column='SE_Comments_5', max_length=75, blank=True, null=True)  # Field name made lowercase.
    se_comments_6 = models.CharField(db_column='SE_Comments_6', max_length=75, blank=True, null=True)  # Field name made lowercase.
    se_comments_7 = models.CharField(db_column='SE_Comments_7', max_length=75, blank=True, null=True)  # Field name made lowercase.
    se_comments_8 = models.CharField(db_column='SE_Comments_8', max_length=75, blank=True, null=True)  # Field name made lowercase.
    se_time_last = models.TimeField(db_column='SE_Time_Last', blank=True, null=True)  # Field name made lowercase.
    se_who_last = models.CharField(db_column='SE_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'secret'
        unique_together = (('SE_REC', 'SE_UNIQUE'),)


class Seq(models.Model):
    seq_d = models.CharField(db_column='SEQ_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    seq_rec = models.IntegerField(db_column='SEQ_REC')  # Field name made lowercase.
    seq_unique = models.IntegerField(db_column='SEQ_UNIQUE')  # Field name made lowercase.
    seq_con_number = models.IntegerField(db_column='SEQ_CON_Number', blank=True, null=True)  # Field name made lowercase.
    seq_con_seq_no = models.IntegerField(db_column='SEQ_CON_Seq_No', blank=True, null=True)  # Field name made lowercase.
    seq_date = models.DateField(db_column='SEQ_Date', blank=True, null=True)  # Field name made lowercase.
    seq_verify = models.CharField(db_column='SEQ_Verify', max_length=1, blank=True, null=True)  # Field name made lowercase.
    seq_comment = models.CharField(db_column='SEQ_Comment', max_length=60, blank=True, null=True)  # Field name made lowercase.
    seq_time_last = models.TimeField(db_column='SEQ_Time_Last', blank=True, null=True)  # Field name made lowercase.
    seq_who_last = models.CharField(db_column='SEQ_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'seq'
        unique_together = (('SEQ_REC', 'SEQ_UNIQUE'),)


class Service(models.Model):
    s_d = models.CharField(db_column='S_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    s_rec = models.IntegerField(db_column='S_REC')  # Field name made lowercase.
    s_unique = models.CharField(db_column='S_UNIQUE', max_length=13)  # Field name made lowercase.
    s_con_unique = models.CharField(db_column='S_CON_UNIQUE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    s_id_b_id = models.CharField(db_column='S_ID_B_ID', max_length=4, blank=True, null=True)  # Field name made lowercase.
    s_start = models.DateField(db_column='S_Start', blank=True, null=True)  # Field name made lowercase.
    s_end = models.DateField(db_column='S_End', blank=True, null=True)  # Field name made lowercase.
    s_why = models.CharField(db_column='S_Why', max_length=1, blank=True, null=True)  # Field name made lowercase.
    s_rank_r_key = models.CharField(db_column='S_Rank_R_KEY', max_length=4, blank=True, null=True)  # Field name made lowercase.
    s_vsl_v_key = models.CharField(db_column='S_Vsl_V_KEY', max_length=4, blank=True, null=True)  # Field name made lowercase.
    s_vsl_name = models.CharField(db_column='S_Vsl_Name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s_principal = models.CharField(db_column='S_Principal', max_length=20, blank=True, null=True)  # Field name made lowercase.
    s_cn_key = models.CharField(db_column='S_CN_KEY', max_length=2, blank=True, null=True)  # Field name made lowercase.
    s_grt = models.CharField(db_column='S_GRT', max_length=6, blank=True, null=True)  # Field name made lowercase.
    s_type_vt_key = models.CharField(db_column='S_Type_VT_KEY', max_length=4, blank=True, null=True)  # Field name made lowercase.
    s_engine = models.CharField(db_column='S_Engine', max_length=6, blank=True, null=True)  # Field name made lowercase.
    s_horsepower = models.CharField(db_column='S_HorsePower', max_length=8, blank=True, null=True)  # Field name made lowercase.
    s_time_last = models.TimeField(db_column='S_Time_Last', blank=True, null=True)  # Field name made lowercase.
    s_who_last = models.CharField(db_column='S_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'service'
        unique_together = (('S_REC', 'S_UNIQUE'),)


class Sssbir(models.Model):
    sss_d = models.CharField(db_column='SSS_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    sss_rec = models.IntegerField(db_column='SSS_REC')  # Field name made lowercase.
    sss_unique = models.CharField(db_column='SSS_UNIQUE', max_length=15)  # Field name made lowercase.
    sss_prin_p_key = models.CharField(db_column='SSS_Prin_P_KEY', max_length=6, blank=True, null=True)  # Field name made lowercase.
    sss_date = models.DateField(db_column='SSS_Date', blank=True, null=True)  # Field name made lowercase.
    sss_bir_paydate = models.DateField(db_column='SSS_BIR_Paydate', blank=True, null=True)  # Field name made lowercase.
    sss_bir_bank = models.CharField(db_column='SSS_BIR_Bank', max_length=4, blank=True, null=True)  # Field name made lowercase.
    sss_sss_paydate = models.DateField(db_column='SSS_SSS_Paydate', blank=True, null=True)  # Field name made lowercase.
    sss_sss_receipt = models.CharField(db_column='SSS_SSS_Receipt', max_length=14, blank=True, null=True)  # Field name made lowercase.
    sss_medicare_paydate = models.DateField(db_column='SSS_Medicare_Paydate', blank=True, null=True)  # Field name made lowercase.
    sss_medicare_receipt = models.CharField(db_column='SSS_Medicare_Receipt', max_length=14, blank=True, null=True)  # Field name made lowercase.
    sss_housing_paydate = models.DateField(db_column='SSS_Housing_Paydate', blank=True, null=True)  # Field name made lowercase.
    sss_housing_receipt = models.CharField(db_column='SSS_Housing_Receipt', max_length=14, blank=True, null=True)  # Field name made lowercase.
    sss_time_last = models.TimeField(db_column='SSS_Time_Last', blank=True, null=True)  # Field name made lowercase.
    sss_who_last = models.CharField(db_column='SSS_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sssbir'
        unique_together = (('SSS_REC', 'SSS_UNIQUE'),)


class Tax(models.Model):
    tax_d = models.CharField(db_column='TAX_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tax_rec = models.IntegerField(db_column='TAX_REC')  # Field name made lowercase.
    tax_unique = models.CharField(db_column='TAX_UNIQUE', max_length=13)  # Field name made lowercase.
    tax_unique_1 = models.CharField(db_column='TAX_UNIQUE_1', max_length=13)  # Field name made lowercase.
    tax_date = models.DateField(db_column='TAX_Date', blank=True, null=True)  # Field name made lowercase.
    tax_tc_key = models.CharField(db_column='TAX_TC_KEY', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tax_cs_key = models.CharField(db_column='TAX_CS_KEY', max_length=2, blank=True, null=True)  # Field name made lowercase.
    tax_m_money = models.CharField(db_column='TAX_M_Money', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tax_basic_increment = models.DecimalField(db_column='TAX_Basic_Increment', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tax_comp_type_1 = models.CharField(db_column='TAX_Comp_Type_1', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tax_comp_name_1 = models.CharField(db_column='TAX_Comp_Name_1', max_length=16, blank=True, null=True)  # Field name made lowercase.
    tax_comp_amnt_1 = models.DecimalField(db_column='TAX_Comp_Amnt_1', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tax_comp_type_2 = models.CharField(db_column='TAX_Comp_Type_2', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tax_comp_name_2 = models.CharField(db_column='TAX_Comp_Name_2', max_length=16, blank=True, null=True)  # Field name made lowercase.
    tax_comp_amnt_2 = models.DecimalField(db_column='TAX_Comp_Amnt_2', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tax_comp_type_3 = models.CharField(db_column='TAX_Comp_Type_3', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tax_comp_name_3 = models.CharField(db_column='TAX_Comp_Name_3', max_length=16, blank=True, null=True)  # Field name made lowercase.
    tax_comp_amnt_3 = models.DecimalField(db_column='TAX_Comp_Amnt_3', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tax_comp_type_4 = models.CharField(db_column='TAX_Comp_Type_4', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tax_comp_name_4 = models.CharField(db_column='TAX_Comp_Name_4', max_length=16, blank=True, null=True)  # Field name made lowercase.
    tax_comp_amnt_4 = models.DecimalField(db_column='TAX_Comp_Amnt_4', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tax_comp_type_5 = models.CharField(db_column='TAX_Comp_Type_5', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tax_comp_name_5 = models.CharField(db_column='TAX_Comp_Name_5', max_length=16, blank=True, null=True)  # Field name made lowercase.
    tax_comp_amnt_5 = models.DecimalField(db_column='TAX_Comp_Amnt_5', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tax_comp_type_6 = models.CharField(db_column='TAX_Comp_Type_6', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tax_comp_name_6 = models.CharField(db_column='TAX_Comp_Name_6', max_length=16, blank=True, null=True)  # Field name made lowercase.
    tax_comp_amnt_6 = models.DecimalField(db_column='TAX_Comp_Amnt_6', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tax_comp_type_7 = models.CharField(db_column='TAX_Comp_Type_7', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tax_comp_name_7 = models.CharField(db_column='TAX_Comp_Name_7', max_length=16, blank=True, null=True)  # Field name made lowercase.
    tax_comp_amnt_7 = models.DecimalField(db_column='TAX_Comp_Amnt_7', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tax_comp_type_8 = models.CharField(db_column='TAX_Comp_Type_8', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tax_comp_name_8 = models.CharField(db_column='TAX_Comp_Name_8', max_length=16, blank=True, null=True)  # Field name made lowercase.
    tax_comp_amnt_8 = models.DecimalField(db_column='TAX_Comp_Amnt_8', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tax_comp_type_9 = models.CharField(db_column='TAX_Comp_Type_9', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tax_comp_name_9 = models.CharField(db_column='TAX_Comp_Name_9', max_length=16, blank=True, null=True)  # Field name made lowercase.
    tax_comp_amnt_9 = models.DecimalField(db_column='TAX_Comp_Amnt_9', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tax_comp_type_10 = models.CharField(db_column='TAX_Comp_Type_10', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tax_comp_name_10 = models.CharField(db_column='TAX_Comp_Name_10', max_length=16, blank=True, null=True)  # Field name made lowercase.
    tax_comp_amnt_10 = models.DecimalField(db_column='TAX_Comp_Amnt_10', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tax_comp_type_11 = models.CharField(db_column='TAX_Comp_Type_11', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tax_comp_name_11 = models.CharField(db_column='TAX_Comp_Name_11', max_length=16, blank=True, null=True)  # Field name made lowercase.
    tax_comp_amnt_11 = models.DecimalField(db_column='TAX_Comp_Amnt_11', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tax_comp_type_12 = models.CharField(db_column='TAX_Comp_Type_12', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tax_comp_name_12 = models.CharField(db_column='TAX_Comp_Name_12', max_length=16, blank=True, null=True)  # Field name made lowercase.
    tax_comp_amnt_12 = models.DecimalField(db_column='TAX_Comp_Amnt_12', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tax_comp_type_13 = models.CharField(db_column='TAX_Comp_Type_13', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tax_comp_name_13 = models.CharField(db_column='TAX_Comp_Name_13', max_length=16, blank=True, null=True)  # Field name made lowercase.
    tax_comp_amnt_13 = models.DecimalField(db_column='TAX_Comp_Amnt_13', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tax_comp_type_14 = models.CharField(db_column='TAX_Comp_Type_14', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tax_comp_name_14 = models.CharField(db_column='TAX_Comp_Name_14', max_length=16, blank=True, null=True)  # Field name made lowercase.
    tax_comp_amnt_14 = models.DecimalField(db_column='TAX_Comp_Amnt_14', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tax_comp_type_15 = models.CharField(db_column='TAX_Comp_Type_15', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tax_comp_name_15 = models.CharField(db_column='TAX_Comp_Name_15', max_length=16, blank=True, null=True)  # Field name made lowercase.
    tax_comp_amnt_15 = models.DecimalField(db_column='TAX_Comp_Amnt_15', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tax_comp_type_16 = models.CharField(db_column='TAX_Comp_Type_16', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tax_comp_name_16 = models.CharField(db_column='TAX_Comp_Name_16', max_length=16, blank=True, null=True)  # Field name made lowercase.
    tax_comp_amnt_16 = models.DecimalField(db_column='TAX_Comp_Amnt_16', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tax_comp_type_17 = models.CharField(db_column='TAX_Comp_Type_17', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tax_comp_name_17 = models.CharField(db_column='TAX_Comp_Name_17', max_length=16, blank=True, null=True)  # Field name made lowercase.
    tax_comp_amnt_17 = models.DecimalField(db_column='TAX_Comp_Amnt_17', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tax_comp_type_18 = models.CharField(db_column='TAX_Comp_Type_18', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tax_comp_name_18 = models.CharField(db_column='TAX_Comp_Name_18', max_length=16, blank=True, null=True)  # Field name made lowercase.
    tax_comp_amnt_18 = models.DecimalField(db_column='TAX_Comp_Amnt_18', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tax_comp_type_19 = models.CharField(db_column='TAX_Comp_Type_19', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tax_comp_name_19 = models.CharField(db_column='TAX_Comp_Name_19', max_length=16, blank=True, null=True)  # Field name made lowercase.
    tax_comp_amnt_19 = models.DecimalField(db_column='TAX_Comp_Amnt_19', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tax_comp_type_20 = models.CharField(db_column='TAX_Comp_Type_20', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tax_comp_name_20 = models.CharField(db_column='TAX_Comp_Name_20', max_length=16, blank=True, null=True)  # Field name made lowercase.
    tax_comp_amnt_20 = models.DecimalField(db_column='TAX_Comp_Amnt_20', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tax_comp_type_21 = models.CharField(db_column='TAX_Comp_Type_21', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tax_comp_name_21 = models.CharField(db_column='TAX_Comp_Name_21', max_length=16, blank=True, null=True)  # Field name made lowercase.
    tax_comp_amnt_21 = models.DecimalField(db_column='TAX_Comp_Amnt_21', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tax_comp_type_22 = models.CharField(db_column='TAX_Comp_Type_22', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tax_comp_name_22 = models.CharField(db_column='TAX_Comp_Name_22', max_length=16, blank=True, null=True)  # Field name made lowercase.
    tax_comp_amnt_22 = models.DecimalField(db_column='TAX_Comp_Amnt_22', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tax_comp_type_23 = models.CharField(db_column='TAX_Comp_Type_23', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tax_comp_name_23 = models.CharField(db_column='TAX_Comp_Name_23', max_length=16, blank=True, null=True)  # Field name made lowercase.
    tax_comp_amnt_23 = models.DecimalField(db_column='TAX_Comp_Amnt_23', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tax_comp_type_24 = models.CharField(db_column='TAX_Comp_Type_24', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tax_comp_name_24 = models.CharField(db_column='TAX_Comp_Name_24', max_length=16, blank=True, null=True)  # Field name made lowercase.
    tax_comp_amnt_24 = models.DecimalField(db_column='TAX_Comp_Amnt_24', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tax_comp_type_25 = models.CharField(db_column='TAX_Comp_Type_25', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tax_comp_name_25 = models.CharField(db_column='TAX_Comp_Name_25', max_length=16, blank=True, null=True)  # Field name made lowercase.
    tax_comp_amnt_25 = models.DecimalField(db_column='TAX_Comp_Amnt_25', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tax_comp_type_26 = models.CharField(db_column='TAX_Comp_Type_26', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tax_comp_name_26 = models.CharField(db_column='TAX_Comp_Name_26', max_length=16, blank=True, null=True)  # Field name made lowercase.
    tax_comp_amnt_26 = models.DecimalField(db_column='TAX_Comp_Amnt_26', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tax_comp_type_27 = models.CharField(db_column='TAX_Comp_Type_27', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tax_comp_name_27 = models.CharField(db_column='TAX_Comp_Name_27', max_length=16, blank=True, null=True)  # Field name made lowercase.
    tax_comp_amnt_27 = models.DecimalField(db_column='TAX_Comp_Amnt_27', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tax_comp_type_28 = models.CharField(db_column='TAX_Comp_Type_28', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tax_comp_name_28 = models.CharField(db_column='TAX_Comp_Name_28', max_length=16, blank=True, null=True)  # Field name made lowercase.
    tax_comp_amnt_28 = models.DecimalField(db_column='TAX_Comp_Amnt_28', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tax_comp_type_29 = models.CharField(db_column='TAX_Comp_Type_29', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tax_comp_name_29 = models.CharField(db_column='TAX_Comp_Name_29', max_length=16, blank=True, null=True)  # Field name made lowercase.
    tax_comp_amnt_29 = models.DecimalField(db_column='TAX_Comp_Amnt_29', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tax_comp_type_30 = models.CharField(db_column='TAX_Comp_Type_30', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tax_comp_name_30 = models.CharField(db_column='TAX_Comp_Name_30', max_length=16, blank=True, null=True)  # Field name made lowercase.
    tax_comp_amnt_30 = models.DecimalField(db_column='TAX_Comp_Amnt_30', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tax_comp_type_31 = models.CharField(db_column='TAX_Comp_Type_31', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tax_comp_name_31 = models.CharField(db_column='TAX_Comp_Name_31', max_length=16, blank=True, null=True)  # Field name made lowercase.
    tax_comp_amnt_31 = models.DecimalField(db_column='TAX_Comp_Amnt_31', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tax_comp_type_32 = models.CharField(db_column='TAX_Comp_Type_32', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tax_comp_name_32 = models.CharField(db_column='TAX_Comp_Name_32', max_length=16, blank=True, null=True)  # Field name made lowercase.
    tax_comp_amnt_32 = models.DecimalField(db_column='TAX_Comp_Amnt_32', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tax_comp_type_33 = models.CharField(db_column='TAX_Comp_Type_33', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tax_comp_name_33 = models.CharField(db_column='TAX_Comp_Name_33', max_length=16, blank=True, null=True)  # Field name made lowercase.
    tax_comp_amnt_33 = models.DecimalField(db_column='TAX_Comp_Amnt_33', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tax_comp_type_34 = models.CharField(db_column='TAX_Comp_Type_34', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tax_comp_name_34 = models.CharField(db_column='TAX_Comp_Name_34', max_length=16, blank=True, null=True)  # Field name made lowercase.
    tax_comp_amnt_34 = models.DecimalField(db_column='TAX_Comp_Amnt_34', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tax_comp_type_35 = models.CharField(db_column='TAX_Comp_Type_35', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tax_comp_name_35 = models.CharField(db_column='TAX_Comp_Name_35', max_length=16, blank=True, null=True)  # Field name made lowercase.
    tax_comp_amnt_35 = models.DecimalField(db_column='TAX_Comp_Amnt_35', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tax_comp_type_36 = models.CharField(db_column='TAX_Comp_Type_36', max_length=3, blank=True, null=True)  # Field name made lowercase.
    tax_comp_name_36 = models.CharField(db_column='TAX_Comp_Name_36', max_length=16, blank=True, null=True)  # Field name made lowercase.
    tax_comp_amnt_36 = models.DecimalField(db_column='TAX_Comp_Amnt_36', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    tax_time_last = models.TimeField(db_column='TAX_Time_Last', blank=True, null=True)  # Field name made lowercase.
    tax_who_last = models.CharField(db_column='TAX_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tax'
        unique_together = (('TAX_REC', 'TAX_UNIQUE', 'TAX_UNIQUE_1'),)


class Taxcat(models.Model):
    tc_d = models.CharField(db_column='TC_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    tc_key = models.CharField(db_column='TC_KEY', primary_key=True, max_length=1)  # Field name made lowercase.
    tc_full = models.CharField(db_column='TC_Full', max_length=40, blank=True, null=True)  # Field name made lowercase.
    tc_time_last = models.TimeField(db_column='TC_Time_Last', blank=True, null=True)  # Field name made lowercase.
    tc_who_last = models.CharField(db_column='TC_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'taxcat'


class Taxsssfact(models.Model):
    t_d = models.CharField(db_column='T_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    t_key = models.CharField(db_column='T_KEY', primary_key=True, max_length=1)  # Field name made lowercase.
    t_lastupdate = models.DateField(db_column='T_LastUpdate', blank=True, null=True)  # Field name made lowercase.
    t_employee_sss_ded = models.DecimalField(db_column='T_Employee_SSS_Ded', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    t_employer_sss_cont = models.DecimalField(db_column='T_Employer_SSS_Cont', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    t_employee_med_ded = models.DecimalField(db_column='T_Employee_Med_Ded', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    t_employer_med_cont = models.DecimalField(db_column='T_Employer_Med_Cont', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    t_employer_ecc_cont = models.DecimalField(db_column='T_Employer_ECC_Cont', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    t_sss_ec = models.DecimalField(db_column='T_SSS_EC', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    t_employee_pagibig_ded = models.DecimalField(db_column='T_Employee_Pagibig_Ded', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    t_employer_pagibig_cont = models.DecimalField(db_column='T_Employer_Pagibig_Cont', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    t_time_last = models.TimeField(db_column='T_Time_Last', blank=True, null=True)  # Field name made lowercase.
    t_who_last = models.CharField(db_column='T_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'taxsssfact'


class Vcat(models.Model):
    vc_d = models.CharField(db_column='VC_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    vc_key = models.CharField(db_column='VC_KEY', primary_key=True, max_length=1)  # Field name made lowercase.
    vc_full = models.CharField(db_column='VC_Full', max_length=26, blank=True, null=True)  # Field name made lowercase.
    vc_time_last = models.TimeField(db_column='VC_Time_Last', blank=True, null=True)  # Field name made lowercase.
    vc_who_last = models.CharField(db_column='VC_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vcat'


class Vequip(models.Model):
    ve_d = models.CharField(db_column='VE_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    ve_key = models.CharField(db_column='VE_KEY', primary_key=True, max_length=4)  # Field name made lowercase.
    ve_full = models.CharField(db_column='VE_Full', max_length=28, blank=True, null=True)  # Field name made lowercase.
    ve_time_last = models.TimeField(db_column='VE_Time_Last', blank=True, null=True)  # Field name made lowercase.
    ve_who_last = models.CharField(db_column='VE_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vequip'


class Vessel(models.Model):
    v_d = models.CharField(db_column='V_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    v_key = models.CharField(db_column='V_KEY', primary_key=True, max_length=4)  # Field name made lowercase.
    v_type = models.CharField(db_column='V_Type', max_length=4, blank=True, null=True)  # Field name made lowercase.
    v_full = models.CharField(db_column='V_Full', max_length=32, blank=True, null=True)  # Field name made lowercase.
    v_p_key = models.CharField(db_column='V_P_KEY', max_length=6, blank=True, null=True)  # Field name made lowercase.
    v_registry = models.CharField(db_column='V_Registry', max_length=12, blank=True, null=True)  # Field name made lowercase.
    v_cn_key = models.CharField(db_column='V_CN_KEY', max_length=2, blank=True, null=True)  # Field name made lowercase.
    v_regnumber = models.CharField(db_column='V_RegNumber', max_length=16, blank=True, null=True)  # Field name made lowercase.
    v_grt = models.IntegerField(db_column='V_GRT', blank=True, null=True)  # Field name made lowercase.
    v_nrt = models.IntegerField(db_column='V_NRT', blank=True, null=True)  # Field name made lowercase.
    v_dwt = models.CharField(db_column='V_DWT', max_length=8, blank=True, null=True)  # Field name made lowercase.
    v_engine = models.CharField(db_column='V_Engine', max_length=6, blank=True, null=True)  # Field name made lowercase.
    v_horsepower = models.CharField(db_column='V_HorsePower', max_length=8, blank=True, null=True)  # Field name made lowercase.
    v_class = models.CharField(db_column='V_Class', max_length=4, blank=True, null=True)  # Field name made lowercase.
    v_yard = models.CharField(db_column='V_Yard', max_length=12, blank=True, null=True)  # Field name made lowercase.
    v_yearbuilt = models.IntegerField(db_column='V_YearBuilt', blank=True, null=True)  # Field name made lowercase.
    v_trades = models.CharField(db_column='V_Trades', max_length=16, blank=True, null=True)  # Field name made lowercase.
    v_ums = models.CharField(db_column='V_UMS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    v_callsign = models.CharField(db_column='V_CallSign', max_length=6, blank=True, null=True)  # Field name made lowercase.
    v_owner_ship = models.CharField(db_column='V_Owner_Ship', max_length=45, blank=True, null=True)  # Field name made lowercase.
    v_imo = models.CharField(db_column='V_IMO', max_length=12, blank=True, null=True)  # Field name made lowercase.
    v_status = models.CharField(db_column='V_Status', max_length=1, blank=True, null=True)  # Field name made lowercase.
    v_end = models.DateField(db_column='V_End', blank=True, null=True)  # Field name made lowercase.
    v_reason = models.CharField(db_column='V_Reason', max_length=18, blank=True, null=True)  # Field name made lowercase.
    v_main_cat = models.CharField(db_column='V_Main_Cat', max_length=1, blank=True, null=True)  # Field name made lowercase.
    v_equip_1 = models.CharField(db_column='V_Equip_1', max_length=4, blank=True, null=True)  # Field name made lowercase.
    v_equip_2 = models.CharField(db_column='V_Equip_2', max_length=4, blank=True, null=True)  # Field name made lowercase.
    v_equip_3 = models.CharField(db_column='V_Equip_3', max_length=4, blank=True, null=True)  # Field name made lowercase.
    v_equip_4 = models.CharField(db_column='V_Equip_4', max_length=4, blank=True, null=True)  # Field name made lowercase.
    v_pays_nat = models.CharField(db_column='V_Pays_NAT', max_length=1, blank=True, null=True)  # Field name made lowercase.
    v_pays_fmy = models.CharField(db_column='V_Pays_FMY', max_length=1, blank=True, null=True)  # Field name made lowercase.
    v_pays_pno = models.CharField(db_column='V_Pays_PNO', max_length=1, blank=True, null=True)  # Field name made lowercase.
    v_pays_tax = models.CharField(db_column='V_Pays_TAX', max_length=1, blank=True, null=True)  # Field name made lowercase.
    v_p_post_date = models.DateField(db_column='V_P_Post_Date', blank=True, null=True)  # Field name made lowercase.
    v_r_post_date = models.DateField(db_column='V_R_Post_Date', blank=True, null=True)  # Field name made lowercase.
    v_e_post_date = models.DateField(db_column='V_E_Post_Date', blank=True, null=True)  # Field name made lowercase.
    v_tfs_fleet = models.CharField(db_column='V_TFS_Fleet', max_length=1, blank=True, null=True)  # Field name made lowercase.
    v_tfs_ship = models.CharField(db_column='V_TFS_Ship', max_length=4, blank=True, null=True)  # Field name made lowercase.
    v_email_1 = models.CharField(db_column='V_Email_1', max_length=28, blank=True, null=True)  # Field name made lowercase.
    v_email_2 = models.CharField(db_column='V_Email_2', max_length=28, blank=True, null=True)  # Field name made lowercase.
    v_time_last = models.TimeField(db_column='V_Time_Last', blank=True, null=True)  # Field name made lowercase.
    v_who_last = models.CharField(db_column='V_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vessel'


class Vgdets(models.Model):
    vgd_d = models.CharField(db_column='VGD_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    vgd_rec = models.IntegerField(db_column='VGD_REC')  # Field name made lowercase.
    vgd_unique = models.CharField(db_column='VGD_UNIQUE', max_length=13)  # Field name made lowercase.
    vgd_vg_key = models.CharField(db_column='VGD_VG_KEY', max_length=8, blank=True, null=True)  # Field name made lowercase.
    vgd_v_key = models.CharField(db_column='VGD_V_KEY', max_length=4, blank=True, null=True)  # Field name made lowercase.
    vgd_status = models.CharField(db_column='VGD_Status', max_length=1, blank=True, null=True)  # Field name made lowercase.
    vgd_tags = models.CharField(db_column='VGD_Tags', max_length=16, blank=True, null=True)  # Field name made lowercase.
    vgd_time_last = models.TimeField(db_column='VGD_Time_Last', blank=True, null=True)  # Field name made lowercase.
    vgd_who_last = models.CharField(db_column='VGD_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vgdets'
        unique_together = (('VGD_REC', 'VGD_UNIQUE'),)


class Vghead(models.Model):
    vg_d = models.CharField(db_column='VG_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    vg_key = models.CharField(db_column='VG_KEY', primary_key=True, max_length=8)  # Field name made lowercase.
    vg_full = models.CharField(db_column='VG_Full', max_length=32, blank=True, null=True)  # Field name made lowercase.
    vg_group_by = models.CharField(db_column='VG_Group_By', max_length=12, blank=True, null=True)  # Field name made lowercase.
    vg_p_key = models.CharField(db_column='VG_P_Key', max_length=6, blank=True, null=True)  # Field name made lowercase.
    vg_status = models.CharField(db_column='VG_Status', max_length=1, blank=True, null=True)  # Field name made lowercase.
    vg_time_last = models.TimeField(db_column='VG_Time_Last', blank=True, null=True)  # Field name made lowercase.
    vg_who_last = models.CharField(db_column='VG_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vghead'


class Vtype(models.Model):
    vt_d = models.CharField(db_column='VT_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    vt_key = models.CharField(db_column='VT_KEY', primary_key=True, max_length=4)  # Field name made lowercase.
    vt_full = models.CharField(db_column='VT_Full', max_length=16, blank=True, null=True)  # Field name made lowercase.
    vt_time_last = models.TimeField(db_column='VT_Time_Last', blank=True, null=True)  # Field name made lowercase.
    vt_who_last = models.CharField(db_column='VT_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vtype'


class Wage(models.Model):
    w_d = models.CharField(db_column='W_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    w_rec = models.IntegerField(db_column='W_REC')  # Field name made lowercase.
    w_unique = models.CharField(db_column='W_UNIQUE', max_length=23)  # Field name made lowercase.
    w_unique_1 = models.CharField(db_column='W_UNIQUE_1', max_length=23)  # Field name made lowercase.
    w_p_key = models.CharField(db_column='W_P_KEY', max_length=6, blank=True, null=True)  # Field name made lowercase.
    w_date = models.DateField(db_column='W_Date', blank=True, null=True)  # Field name made lowercase.
    w_rank_r_key = models.CharField(db_column='W_Rank_R_KEY', max_length=4, blank=True, null=True)  # Field name made lowercase.
    w_cs_key = models.CharField(db_column='W_CS_KEY', max_length=2, blank=True, null=True)  # Field name made lowercase.
    w_m_money = models.CharField(db_column='W_M_Money', max_length=3, blank=True, null=True)  # Field name made lowercase.
    w_mth_basic = models.DecimalField(db_column='W_Mth_Basic', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    w_fix_mth_ot = models.DecimalField(db_column='W_Fix_Mth_OT', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    w_hourly_ot_rate = models.DecimalField(db_column='W_Hourly_OT_Rate', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    w_min_mth_ot_hours = models.IntegerField(db_column='W_Min_Mth_OT_Hours', blank=True, null=True)  # Field name made lowercase.
    w_hours_week = models.IntegerField(db_column='W_Hours_Week', blank=True, null=True)  # Field name made lowercase.
    w_comp_type_1 = models.CharField(db_column='W_Comp_Type_1', max_length=3, blank=True, null=True)  # Field name made lowercase.
    w_comp_name_1 = models.CharField(db_column='W_Comp_Name_1', max_length=16, blank=True, null=True)  # Field name made lowercase.
    w_comp_amnt_1 = models.DecimalField(db_column='W_Comp_Amnt_1', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    w_comp_type_2 = models.CharField(db_column='W_Comp_Type_2', max_length=3, blank=True, null=True)  # Field name made lowercase.
    w_comp_name_2 = models.CharField(db_column='W_Comp_Name_2', max_length=16, blank=True, null=True)  # Field name made lowercase.
    w_comp_amnt_2 = models.DecimalField(db_column='W_Comp_Amnt_2', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    w_comp_type_3 = models.CharField(db_column='W_Comp_Type_3', max_length=3, blank=True, null=True)  # Field name made lowercase.
    w_comp_name_3 = models.CharField(db_column='W_Comp_Name_3', max_length=16, blank=True, null=True)  # Field name made lowercase.
    w_comp_amnt_3 = models.DecimalField(db_column='W_Comp_Amnt_3', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    w_comp_type_4 = models.CharField(db_column='W_Comp_Type_4', max_length=3, blank=True, null=True)  # Field name made lowercase.
    w_comp_name_4 = models.CharField(db_column='W_Comp_Name_4', max_length=16, blank=True, null=True)  # Field name made lowercase.
    w_comp_amnt_4 = models.DecimalField(db_column='W_Comp_Amnt_4', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    w_comp_type_5 = models.CharField(db_column='W_Comp_Type_5', max_length=3, blank=True, null=True)  # Field name made lowercase.
    w_comp_name_5 = models.CharField(db_column='W_Comp_Name_5', max_length=16, blank=True, null=True)  # Field name made lowercase.
    w_comp_amnt_5 = models.DecimalField(db_column='W_Comp_Amnt_5', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    w_comp_type_6 = models.CharField(db_column='W_Comp_Type_6', max_length=3, blank=True, null=True)  # Field name made lowercase.
    w_comp_name_6 = models.CharField(db_column='W_Comp_Name_6', max_length=16, blank=True, null=True)  # Field name made lowercase.
    w_comp_amnt_6 = models.DecimalField(db_column='W_Comp_Amnt_6', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    w_comp_type_7 = models.CharField(db_column='W_Comp_Type_7', max_length=3, blank=True, null=True)  # Field name made lowercase.
    w_comp_name_7 = models.CharField(db_column='W_Comp_Name_7', max_length=16, blank=True, null=True)  # Field name made lowercase.
    w_comp_amnt_7 = models.DecimalField(db_column='W_Comp_Amnt_7', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    w_comp_type_8 = models.CharField(db_column='W_Comp_Type_8', max_length=3, blank=True, null=True)  # Field name made lowercase.
    w_comp_name_8 = models.CharField(db_column='W_Comp_Name_8', max_length=16, blank=True, null=True)  # Field name made lowercase.
    w_comp_amnt_8 = models.DecimalField(db_column='W_Comp_Amnt_8', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    w_comp_type_9 = models.CharField(db_column='W_Comp_Type_9', max_length=3, blank=True, null=True)  # Field name made lowercase.
    w_comp_name_9 = models.CharField(db_column='W_Comp_Name_9', max_length=16, blank=True, null=True)  # Field name made lowercase.
    w_comp_amnt_9 = models.DecimalField(db_column='W_Comp_Amnt_9', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    w_comp_type_10 = models.CharField(db_column='W_Comp_Type_10', max_length=3, blank=True, null=True)  # Field name made lowercase.
    w_comp_name_10 = models.CharField(db_column='W_Comp_Name_10', max_length=16, blank=True, null=True)  # Field name made lowercase.
    w_comp_amnt_10 = models.DecimalField(db_column='W_Comp_Amnt_10', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    w_comp_type_11 = models.CharField(db_column='W_Comp_Type_11', max_length=3, blank=True, null=True)  # Field name made lowercase.
    w_comp_name_11 = models.CharField(db_column='W_Comp_Name_11', max_length=16, blank=True, null=True)  # Field name made lowercase.
    w_comp_amnt_11 = models.DecimalField(db_column='W_Comp_Amnt_11', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    w_comp_type_12 = models.CharField(db_column='W_Comp_Type_12', max_length=3, blank=True, null=True)  # Field name made lowercase.
    w_comp_name_12 = models.CharField(db_column='W_Comp_Name_12', max_length=16, blank=True, null=True)  # Field name made lowercase.
    w_comp_amnt_12 = models.DecimalField(db_column='W_Comp_Amnt_12', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    w_comp_type_13 = models.CharField(db_column='W_Comp_Type_13', max_length=3, blank=True, null=True)  # Field name made lowercase.
    w_comp_name_13 = models.CharField(db_column='W_Comp_Name_13', max_length=16, blank=True, null=True)  # Field name made lowercase.
    w_comp_amnt_13 = models.DecimalField(db_column='W_Comp_Amnt_13', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    w_comp_type_14 = models.CharField(db_column='W_Comp_Type_14', max_length=3, blank=True, null=True)  # Field name made lowercase.
    w_comp_name_14 = models.CharField(db_column='W_Comp_Name_14', max_length=16, blank=True, null=True)  # Field name made lowercase.
    w_comp_amnt_14 = models.DecimalField(db_column='W_Comp_Amnt_14', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    w_comp_type_15 = models.CharField(db_column='W_Comp_Type_15', max_length=3, blank=True, null=True)  # Field name made lowercase.
    w_comp_name_15 = models.CharField(db_column='W_Comp_Name_15', max_length=16, blank=True, null=True)  # Field name made lowercase.
    w_comp_amnt_15 = models.DecimalField(db_column='W_Comp_Amnt_15', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    w_comp_type_16 = models.CharField(db_column='W_Comp_Type_16', max_length=3, blank=True, null=True)  # Field name made lowercase.
    w_comp_name_16 = models.CharField(db_column='W_Comp_Name_16', max_length=16, blank=True, null=True)  # Field name made lowercase.
    w_comp_amnt_16 = models.DecimalField(db_column='W_Comp_Amnt_16', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    w_comp_type_17 = models.CharField(db_column='W_Comp_Type_17', max_length=3, blank=True, null=True)  # Field name made lowercase.
    w_comp_name_17 = models.CharField(db_column='W_Comp_Name_17', max_length=16, blank=True, null=True)  # Field name made lowercase.
    w_comp_amnt_17 = models.DecimalField(db_column='W_Comp_Amnt_17', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    w_comp_type_18 = models.CharField(db_column='W_Comp_Type_18', max_length=3, blank=True, null=True)  # Field name made lowercase.
    w_comp_name_18 = models.CharField(db_column='W_Comp_Name_18', max_length=16, blank=True, null=True)  # Field name made lowercase.
    w_comp_amnt_18 = models.DecimalField(db_column='W_Comp_Amnt_18', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    w_comp_type_19 = models.CharField(db_column='W_Comp_Type_19', max_length=3, blank=True, null=True)  # Field name made lowercase.
    w_comp_name_19 = models.CharField(db_column='W_Comp_Name_19', max_length=16, blank=True, null=True)  # Field name made lowercase.
    w_comp_amnt_19 = models.DecimalField(db_column='W_Comp_Amnt_19', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    w_comp_type_20 = models.CharField(db_column='W_Comp_Type_20', max_length=3, blank=True, null=True)  # Field name made lowercase.
    w_comp_name_20 = models.CharField(db_column='W_Comp_Name_20', max_length=16, blank=True, null=True)  # Field name made lowercase.
    w_comp_amnt_20 = models.DecimalField(db_column='W_Comp_Amnt_20', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    w_comp_type_21 = models.CharField(db_column='W_Comp_Type_21', max_length=3, blank=True, null=True)  # Field name made lowercase.
    w_comp_name_21 = models.CharField(db_column='W_Comp_Name_21', max_length=16, blank=True, null=True)  # Field name made lowercase.
    w_comp_amnt_21 = models.DecimalField(db_column='W_Comp_Amnt_21', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    w_comp_type_22 = models.CharField(db_column='W_Comp_Type_22', max_length=3, blank=True, null=True)  # Field name made lowercase.
    w_comp_name_22 = models.CharField(db_column='W_Comp_Name_22', max_length=16, blank=True, null=True)  # Field name made lowercase.
    w_comp_amnt_22 = models.DecimalField(db_column='W_Comp_Amnt_22', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    w_comp_type_23 = models.CharField(db_column='W_Comp_Type_23', max_length=3, blank=True, null=True)  # Field name made lowercase.
    w_comp_name_23 = models.CharField(db_column='W_Comp_Name_23', max_length=16, blank=True, null=True)  # Field name made lowercase.
    w_comp_amnt_23 = models.DecimalField(db_column='W_Comp_Amnt_23', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    w_comp_type_24 = models.CharField(db_column='W_Comp_Type_24', max_length=3, blank=True, null=True)  # Field name made lowercase.
    w_comp_name_24 = models.CharField(db_column='W_Comp_Name_24', max_length=16, blank=True, null=True)  # Field name made lowercase.
    w_comp_amnt_24 = models.DecimalField(db_column='W_Comp_Amnt_24', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    w_sen_1 = models.DecimalField(db_column='W_Sen_1', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    w_sen_2 = models.DecimalField(db_column='W_Sen_2', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    w_sen_3 = models.DecimalField(db_column='W_Sen_3', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    w_sen_4 = models.DecimalField(db_column='W_Sen_4', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    w_sen_5 = models.DecimalField(db_column='W_Sen_5', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    w_sen_6 = models.DecimalField(db_column='W_Sen_6', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    w_sen_7 = models.DecimalField(db_column='W_Sen_7', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    w_sen_8 = models.DecimalField(db_column='W_Sen_8', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    w_sen_9 = models.DecimalField(db_column='W_Sen_9', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    w_sen_10 = models.DecimalField(db_column='W_Sen_10', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    w_sen_11 = models.DecimalField(db_column='W_Sen_11', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    w_sen_rank_1 = models.DecimalField(db_column='W_Sen_Rank_1', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    w_sen_rank_2 = models.DecimalField(db_column='W_Sen_Rank_2', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    w_sen_rank_3 = models.DecimalField(db_column='W_Sen_Rank_3', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    w_sen_rank_4 = models.DecimalField(db_column='W_Sen_Rank_4', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    w_sen_rank_5 = models.DecimalField(db_column='W_Sen_Rank_5', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    w_sen_rank_6 = models.DecimalField(db_column='W_Sen_Rank_6', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    w_sen_rank_7 = models.DecimalField(db_column='W_Sen_Rank_7', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    w_sen_rank_8 = models.DecimalField(db_column='W_Sen_Rank_8', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    w_sen_rank_9 = models.DecimalField(db_column='W_Sen_Rank_9', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    w_sen_rank_10 = models.DecimalField(db_column='W_Sen_Rank_10', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    w_sen_rank_11 = models.DecimalField(db_column='W_Sen_Rank_11', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    w_time_last = models.TimeField(db_column='W_Time_Last', blank=True, null=True)  # Field name made lowercase.
    w_who_last = models.CharField(db_column='W_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wage'
        unique_together = (('W_REC', 'W_UNIQUE', 'W_UNIQUE_1'),)


class Wives(models.Model):
    wob_d = models.CharField(db_column='WOB_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    wob_rec = models.IntegerField(db_column='WOB_REC')  # Field name made lowercase.
    wob_unique = models.CharField(db_column='WOB_UNIQUE', max_length=13)  # Field name made lowercase.
    wob_id_b_id = models.CharField(db_column='WOB_ID_B_ID', max_length=4, blank=True, null=True)  # Field name made lowercase.
    wob_embark_date = models.DateField(db_column='WOB_Embark_Date', blank=True, null=True)  # Field name made lowercase.
    wob_shp_code = models.CharField(db_column='WOB_Shp_Code', max_length=4, blank=True, null=True)  # Field name made lowercase.
    wob_name = models.CharField(db_column='WOB_Name', max_length=34, blank=True, null=True)  # Field name made lowercase.
    wob_embark_comments = models.CharField(db_column='WOB_Embark_Comments', max_length=80, blank=True, null=True)  # Field name made lowercase.
    wob_disembark_date = models.DateField(db_column='WOB_Disembark_Date', blank=True, null=True)  # Field name made lowercase.
    wob_disembark_comments = models.CharField(db_column='WOB_Disembark_Comments', max_length=80, blank=True, null=True)  # Field name made lowercase.
    wob_time_last = models.TimeField(db_column='WOB_Time_Last', blank=True, null=True)  # Field name made lowercase.
    wob_who_last = models.CharField(db_column='WOB_Who_Last', max_length=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wives'
        unique_together = (('WOB_REC', 'WOB_UNIQUE'),)