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

from datetime import *
from django.db import models
from django.utils.safestring import mark_safe

class Cert(models.Model):
    c_d = models.CharField(db_column='C_D', max_length=1, blank=True, null=True)  
    certificate = models.CharField(db_column='C_KEY', primary_key=True, max_length=4)  
    c_full = models.CharField(db_column='C_Full', max_length=50, blank=True, null=True)  
    c_book = models.CharField(db_column='C_Book', max_length=1, blank=True, null=True)  
    c_main = models.CharField(db_column='C_Main', max_length=1, blank=True, null=True)  
    c_expires = models.CharField(db_column='C_Expires', max_length=1, blank=True, null=True)  
    c_interval_years = models.DecimalField(db_column='C_Interval_Years', max_digits=10, decimal_places=0, blank=True, null=True)  
    c_interval_months = models.DecimalField(db_column='C_Interval_Months', max_digits=10, decimal_places=0, blank=True, null=True)  
    c_time_last = models.TimeField(db_column='C_Time_Last', blank=True, null=True)  
    c_who_last = models.CharField(db_column='C_Who_Last', max_length=4, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'cert'

    def __str__(self):
        return self.certificate

class Contract(models.Model):
    con_d = models.CharField(db_column='CON_D', max_length=1, blank=True, null=True)  
    contract = models.IntegerField(primary_key=True, db_column='CON_REC')  
    con_unique = models.CharField(db_column='CON_UNIQUE', max_length=10)  
    con_unique_1 = models.CharField(db_column='CON_UNIQUE_1', max_length=29)  
    con_number = models.IntegerField(db_column='CON_Number', blank=True, null=True)  
    con_seq_no = models.IntegerField(db_column='CON_Seq_No', blank=True, null=True)  
    code = models.CharField(db_column='CON_B_ID', max_length=4, blank=True, null=True)  
    con_w_cs_key = models.CharField(db_column='CON_W_CS_KEY', max_length=2, blank=True, null=True)  
    con_t_cs_key = models.CharField(db_column='CON_T_CS_KEY', max_length=2, blank=True, null=True)  
    manning_agent = models.CharField(db_column='CON_MAN_KEY', max_length=4, blank=True, null=True)  
    principal = models.CharField(db_column='CON_Prin_P_KEY', max_length=6, blank=True, null=True)  
    con_master_p_key = models.CharField(db_column='CON_Master_P_KEY', max_length=6, blank=True, null=True)  
    wage = models.DecimalField(db_column='CON_Wage_W_REC', max_digits=10, decimal_places=0, blank=True, null=True)  
    vessel = models.CharField(db_column='CON_Vsl_V_KEY', max_length=4, blank=True, null=True)  
    rank = models.CharField(db_column='CON_Rank_R_KEY', max_length=4, blank=True, null=True)  
    crew_category = models.CharField(db_column='CON_Crew_Category', max_length=1, blank=True, null=True)  
    con_m_money = models.CharField(db_column='CON_M_Money', max_length=3, blank=True, null=True)  
    con_length = models.IntegerField(db_column='CON_Length', blank=True, null=True)  
    con_pdos = models.DateField(db_column='CON_PDOS', blank=True, null=True)  
    con_money_beg = models.DateField(db_column='CON_Money_Beg', blank=True, null=True)  
    con_embark = models.DateField(db_column='CON_Embark', blank=True, null=True)  
    con_embark_com = models.CharField(db_column='CON_Embark_Com', max_length=80, blank=True, null=True)  
    con_join = models.DateField(db_column='CON_Join', blank=True, null=True)  
    con_join_where = models.CharField(db_column='CON_Join_Where', max_length=16, blank=True, null=True)  
    con_left = models.DateField(db_column='CON_Left', blank=True, null=True)  
    con_left_where = models.CharField(db_column='CON_Left_Where', max_length=16, blank=True, null=True)  
    con_disembark = models.DateField(db_column='CON_Disembark', blank=True, null=True)  
    con_disembark_com = models.CharField(db_column='CON_Disembark_Com', max_length=80, blank=True, null=True)  
    con_money_end = models.DateField(db_column='CON_Money_End', blank=True, null=True)  
    con_reason_signoff = models.CharField(db_column='CON_Reason_Signoff', max_length=20, blank=True, null=True)  
    con_date_fitness = models.DateField(db_column='CON_Date_Fitness', blank=True, null=True)  
    con_contract_date = models.DateField(db_column='CON_Contract_Date', blank=True, null=True)  
    con_poea_date = models.DateField(db_column='CON_POEA_Date', blank=True, null=True)  
    con_oec = models.IntegerField(db_column='CON_OEC', blank=True, null=True)  
    con_last_eval_rcv = models.CharField(db_column='CON_Last_Eval_Rcv', max_length=1, blank=True, null=True)  
    con_seniority = models.IntegerField(db_column='CON_Seniority', blank=True, null=True)  
    con_senior_date = models.DateField(db_column='CON_Senior_Date', blank=True, null=True)  
    con_mth_basic = models.DecimalField(db_column='CON_Mth_Basic', max_digits=10, decimal_places=0, blank=True, null=True)  
    con_mth_extra1 = models.DecimalField(db_column='CON_Mth_Extra1', max_digits=10, decimal_places=0, blank=True, null=True)  
    con_mth_extra1_descr = models.CharField(db_column='CON_Mth_Extra1_Descr', max_length=32, blank=True, null=True)  
    con_mth_extra2 = models.DecimalField(db_column='CON_Mth_Extra2', max_digits=10, decimal_places=0, blank=True, null=True)  
    con_mth_extra2_descr = models.CharField(db_column='CON_Mth_Extra2_Descr', max_length=32, blank=True, null=True)  
    con_fix_mth_ot = models.DecimalField(db_column='CON_Fix_Mth_OT', max_digits=10, decimal_places=0, blank=True, null=True)  
    con_hourly_ot_rate = models.DecimalField(db_column='CON_Hourly_OT_Rate', max_digits=10, decimal_places=0, blank=True, null=True)  
    con_min_mth_ot_hours = models.IntegerField(db_column='CON_Min_Mth_OT_Hours', blank=True, null=True)  
    con_hours_week = models.IntegerField(db_column='CON_Hours_Week', blank=True, null=True)  
    con_comp_type_1 = models.CharField(db_column='CON_Comp_Type_1', max_length=3, blank=True, null=True)  
    con_comp_name_1 = models.CharField(db_column='CON_Comp_Name_1', max_length=16, blank=True, null=True)  
    con_comp_amnt_1 = models.DecimalField(db_column='CON_Comp_Amnt_1', max_digits=10, decimal_places=0, blank=True, null=True)  
    con_comp_type_2 = models.CharField(db_column='CON_Comp_Type_2', max_length=3, blank=True, null=True)  
    con_comp_name_2 = models.CharField(db_column='CON_Comp_Name_2', max_length=16, blank=True, null=True)  
    con_comp_amnt_2 = models.DecimalField(db_column='CON_Comp_Amnt_2', max_digits=10, decimal_places=0, blank=True, null=True)  
    con_comp_type_3 = models.CharField(db_column='CON_Comp_Type_3', max_length=3, blank=True, null=True)  
    con_comp_name_3 = models.CharField(db_column='CON_Comp_Name_3', max_length=16, blank=True, null=True)  
    con_comp_amnt_3 = models.DecimalField(db_column='CON_Comp_Amnt_3', max_digits=10, decimal_places=0, blank=True, null=True)  
    con_comp_type_4 = models.CharField(db_column='CON_Comp_Type_4', max_length=3, blank=True, null=True)  
    con_comp_name_4 = models.CharField(db_column='CON_Comp_Name_4', max_length=16, blank=True, null=True)  
    con_comp_amnt_4 = models.DecimalField(db_column='CON_Comp_Amnt_4', max_digits=10, decimal_places=0, blank=True, null=True)  
    con_comp_type_5 = models.CharField(db_column='CON_Comp_Type_5', max_length=3, blank=True, null=True)  
    con_comp_name_5 = models.CharField(db_column='CON_Comp_Name_5', max_length=16, blank=True, null=True)  
    con_comp_amnt_5 = models.DecimalField(db_column='CON_Comp_Amnt_5', max_digits=10, decimal_places=0, blank=True, null=True)  
    con_comp_type_6 = models.CharField(db_column='CON_Comp_Type_6', max_length=3, blank=True, null=True)  
    con_comp_name_6 = models.CharField(db_column='CON_Comp_Name_6', max_length=16, blank=True, null=True)  
    con_comp_amnt_6 = models.DecimalField(db_column='CON_Comp_Amnt_6', max_digits=10, decimal_places=0, blank=True, null=True)  
    con_comp_type_7 = models.CharField(db_column='CON_Comp_Type_7', max_length=3, blank=True, null=True)  
    con_comp_name_7 = models.CharField(db_column='CON_Comp_Name_7', max_length=16, blank=True, null=True)  
    con_comp_amnt_7 = models.DecimalField(db_column='CON_Comp_Amnt_7', max_digits=10, decimal_places=0, blank=True, null=True)  
    con_comp_type_8 = models.CharField(db_column='CON_Comp_Type_8', max_length=3, blank=True, null=True)  
    con_comp_name_8 = models.CharField(db_column='CON_Comp_Name_8', max_length=16, blank=True, null=True)  
    con_comp_amnt_8 = models.DecimalField(db_column='CON_Comp_Amnt_8', max_digits=10, decimal_places=0, blank=True, null=True)  
    con_comp_type_9 = models.CharField(db_column='CON_Comp_Type_9', max_length=3, blank=True, null=True)  
    con_comp_name_9 = models.CharField(db_column='CON_Comp_Name_9', max_length=16, blank=True, null=True)  
    con_comp_amnt_9 = models.DecimalField(db_column='CON_Comp_Amnt_9', max_digits=10, decimal_places=0, blank=True, null=True)  
    con_comp_type_10 = models.CharField(db_column='CON_Comp_Type_10', max_length=3, blank=True, null=True)  
    con_comp_name_10 = models.CharField(db_column='CON_Comp_Name_10', max_length=16, blank=True, null=True)  
    con_comp_amnt_10 = models.DecimalField(db_column='CON_Comp_Amnt_10', max_digits=10, decimal_places=0, blank=True, null=True)  
    con_comp_type_11 = models.CharField(db_column='CON_Comp_Type_11', max_length=3, blank=True, null=True)  
    con_comp_name_11 = models.CharField(db_column='CON_Comp_Name_11', max_length=16, blank=True, null=True)  
    con_comp_amnt_11 = models.DecimalField(db_column='CON_Comp_Amnt_11', max_digits=10, decimal_places=0, blank=True, null=True)  
    con_comp_type_12 = models.CharField(db_column='CON_Comp_Type_12', max_length=3, blank=True, null=True)  
    con_comp_name_12 = models.CharField(db_column='CON_Comp_Name_12', max_length=16, blank=True, null=True)  
    con_comp_amnt_12 = models.DecimalField(db_column='CON_Comp_Amnt_12', max_digits=10, decimal_places=0, blank=True, null=True)  
    con_comp_type_13 = models.CharField(db_column='CON_Comp_Type_13', max_length=3, blank=True, null=True)  
    con_comp_name_13 = models.CharField(db_column='CON_Comp_Name_13', max_length=16, blank=True, null=True)  
    con_comp_amnt_13 = models.DecimalField(db_column='CON_Comp_Amnt_13', max_digits=10, decimal_places=0, blank=True, null=True)  
    con_comp_type_14 = models.CharField(db_column='CON_Comp_Type_14', max_length=3, blank=True, null=True)  
    con_comp_name_14 = models.CharField(db_column='CON_Comp_Name_14', max_length=16, blank=True, null=True)  
    con_comp_amnt_14 = models.DecimalField(db_column='CON_Comp_Amnt_14', max_digits=10, decimal_places=0, blank=True, null=True)  
    con_comp_type_15 = models.CharField(db_column='CON_Comp_Type_15', max_length=3, blank=True, null=True)  
    con_comp_name_15 = models.CharField(db_column='CON_Comp_Name_15', max_length=16, blank=True, null=True)  
    con_comp_amnt_15 = models.DecimalField(db_column='CON_Comp_Amnt_15', max_digits=10, decimal_places=0, blank=True, null=True)  
    con_comp_type_16 = models.CharField(db_column='CON_Comp_Type_16', max_length=3, blank=True, null=True)  
    con_comp_name_16 = models.CharField(db_column='CON_Comp_Name_16', max_length=16, blank=True, null=True)  
    con_comp_amnt_16 = models.DecimalField(db_column='CON_Comp_Amnt_16', max_digits=10, decimal_places=0, blank=True, null=True)  
    con_comp_type_17 = models.CharField(db_column='CON_Comp_Type_17', max_length=3, blank=True, null=True)  
    con_comp_name_17 = models.CharField(db_column='CON_Comp_Name_17', max_length=16, blank=True, null=True)  
    con_comp_amnt_17 = models.DecimalField(db_column='CON_Comp_Amnt_17', max_digits=10, decimal_places=0, blank=True, null=True)  
    con_comp_type_18 = models.CharField(db_column='CON_Comp_Type_18', max_length=3, blank=True, null=True)  
    con_comp_name_18 = models.CharField(db_column='CON_Comp_Name_18', max_length=16, blank=True, null=True)  
    con_comp_amnt_18 = models.DecimalField(db_column='CON_Comp_Amnt_18', max_digits=10, decimal_places=0, blank=True, null=True)  
    con_comp_type_19 = models.CharField(db_column='CON_Comp_Type_19', max_length=3, blank=True, null=True)  
    con_comp_name_19 = models.CharField(db_column='CON_Comp_Name_19', max_length=16, blank=True, null=True)  
    con_comp_amnt_19 = models.DecimalField(db_column='CON_Comp_Amnt_19', max_digits=10, decimal_places=0, blank=True, null=True)  
    con_comp_type_20 = models.CharField(db_column='CON_Comp_Type_20', max_length=3, blank=True, null=True)  
    con_comp_name_20 = models.CharField(db_column='CON_Comp_Name_20', max_length=16, blank=True, null=True)  
    con_comp_amnt_20 = models.DecimalField(db_column='CON_Comp_Amnt_20', max_digits=10, decimal_places=0, blank=True, null=True)  
    con_comp_type_21 = models.CharField(db_column='CON_Comp_Type_21', max_length=3, blank=True, null=True)  
    con_comp_name_21 = models.CharField(db_column='CON_Comp_Name_21', max_length=16, blank=True, null=True)  
    con_comp_amnt_21 = models.DecimalField(db_column='CON_Comp_Amnt_21', max_digits=10, decimal_places=0, blank=True, null=True)  
    con_comp_type_22 = models.CharField(db_column='CON_Comp_Type_22', max_length=3, blank=True, null=True)  
    con_comp_name_22 = models.CharField(db_column='CON_Comp_Name_22', max_length=16, blank=True, null=True)  
    con_comp_amnt_22 = models.DecimalField(db_column='CON_Comp_Amnt_22', max_digits=10, decimal_places=0, blank=True, null=True)  
    con_comp_type_23 = models.CharField(db_column='CON_Comp_Type_23', max_length=3, blank=True, null=True)  
    con_comp_name_23 = models.CharField(db_column='CON_Comp_Name_23', max_length=16, blank=True, null=True)  
    con_comp_amnt_23 = models.DecimalField(db_column='CON_Comp_Amnt_23', max_digits=10, decimal_places=0, blank=True, null=True)  
    con_comp_type_24 = models.CharField(db_column='CON_Comp_Type_24', max_length=3, blank=True, null=True)  
    con_comp_name_24 = models.CharField(db_column='CON_Comp_Name_24', max_length=16, blank=True, null=True)  
    con_comp_amnt_24 = models.DecimalField(db_column='CON_Comp_Amnt_24', max_digits=10, decimal_places=0, blank=True, null=True)  
    con_pays_nat = models.CharField(db_column='CON_Pays_NAT', max_length=1, blank=True, null=True)  
    con_pays_seaman_home = models.CharField(db_column='CON_Pays_Seaman_Home', max_length=1, blank=True, null=True)  
    con_pays_fmy = models.CharField(db_column='CON_Pays_FMY', max_length=1, blank=True, null=True)  
    con_pays_tax = models.CharField(db_column='CON_Pays_TAX', max_length=1, blank=True, null=True)  
    con_pays_pno = models.CharField(db_column='CON_Pays_PNO', max_length=1, blank=True, null=True)  
    con_leave_onsignoff = models.CharField(db_column='CON_Leave_OnSignoff', max_length=1, blank=True, null=True)  
    con_seniority_rank = models.IntegerField(db_column='CON_Seniority_Rank', blank=True, null=True)  
    con_senior_rank_date = models.DateField(db_column='CON_Senior_Rank_Date', blank=True, null=True)  
    con_ereceipt = models.IntegerField(db_column='CON_EReceipt', blank=True, null=True)  
    con_cba = models.CharField(db_column='CON_CBA', max_length=12, blank=True, null=True)  
    con_bmi = models.DecimalField(db_column='CON_BMI', max_digits=10, decimal_places=0, blank=True, null=True)  
    con_cash_advance = models.DecimalField(db_column='CON_Cash_Advance', max_digits=10, decimal_places=0, blank=True, null=True)  
    con_tax_anal = models.DecimalField(db_column='CON_Tax_Anal', max_digits=10, decimal_places=0, blank=True, null=True)  
    con_p_alo = models.DecimalField(db_column='CON_P_ALO', max_digits=10, decimal_places=0, blank=True, null=True)  
    con_balance_total = models.DecimalField(db_column='CON_Balance_Total', max_digits=10, decimal_places=0, blank=True, null=True)  
    con_balance_amt_cur1 = models.DecimalField(db_column='CON_Balance_Amt_Cur1', max_digits=10, decimal_places=0, blank=True, null=True)  
    con_balance_cur1 = models.CharField(db_column='CON_Balance_Cur1', max_length=3, blank=True, null=True)  
    con_balance_amt_cur2 = models.DecimalField(db_column='CON_Balance_Amt_Cur2', max_digits=10, decimal_places=0, blank=True, null=True)  
    con_balance_cur2 = models.CharField(db_column='CON_Balance_Cur2', max_length=3, blank=True, null=True)  
    con_balance_amt_cur3 = models.DecimalField(db_column='CON_Balance_Amt_Cur3', max_digits=10, decimal_places=0, blank=True, null=True)  
    con_balance_cur3 = models.CharField(db_column='CON_Balance_Cur3', max_length=3, blank=True, null=True)  
    con_balance_comment = models.CharField(db_column='CON_Balance_Comment', max_length=32, blank=True, null=True)  
    con_balance_status = models.CharField(db_column='CON_Balance_Status', max_length=1, blank=True, null=True)  
    con_balance_payday = models.DateField(db_column='CON_Balance_Payday', blank=True, null=True)  
    con_retro1_from = models.DateField(db_column='CON_Retro1_From', blank=True, null=True)  
    con_retro1_to = models.DateField(db_column='CON_Retro1_To', blank=True, null=True)  
    con_retro1_total = models.DecimalField(db_column='CON_Retro1_Total', max_digits=10, decimal_places=0, blank=True, null=True)  
    con_retro1_amt_cur1 = models.DecimalField(db_column='CON_Retro1_Amt_Cur1', max_digits=10, decimal_places=0, blank=True, null=True)  
    con_retro1_cur1 = models.CharField(db_column='CON_Retro1_Cur1', max_length=3, blank=True, null=True)  
    con_retro1_amt_cur2 = models.DecimalField(db_column='CON_Retro1_Amt_Cur2', max_digits=10, decimal_places=0, blank=True, null=True)  
    con_retro1_cur2 = models.CharField(db_column='CON_Retro1_Cur2', max_length=3, blank=True, null=True)  
    con_retro1_amt_cur3 = models.DecimalField(db_column='CON_Retro1_Amt_Cur3', max_digits=10, decimal_places=0, blank=True, null=True)  
    con_retro1_cur3 = models.CharField(db_column='CON_Retro1_Cur3', max_length=3, blank=True, null=True)  
    con_retro1_status = models.CharField(db_column='CON_Retro1_Status', max_length=1, blank=True, null=True)  
    con_retro1_payday = models.DateField(db_column='CON_Retro1_Payday', blank=True, null=True)  
    con_retro1_comment = models.CharField(db_column='CON_Retro1_Comment', max_length=32, blank=True, null=True)  
    con_retro2_from = models.DateField(db_column='CON_Retro2_From', blank=True, null=True)  
    con_retro2_to = models.DateField(db_column='CON_Retro2_To', blank=True, null=True)  
    con_retro2_total = models.DecimalField(db_column='CON_Retro2_Total', max_digits=10, decimal_places=0, blank=True, null=True)  
    con_retro2_amt_cur1 = models.DecimalField(db_column='CON_Retro2_Amt_Cur1', max_digits=10, decimal_places=0, blank=True, null=True)  
    con_retro2_cur1 = models.CharField(db_column='CON_Retro2_Cur1', max_length=3, blank=True, null=True)  
    con_retro2_amt_cur2 = models.DecimalField(db_column='CON_Retro2_Amt_Cur2', max_digits=10, decimal_places=0, blank=True, null=True)  
    con_retro2_cur2 = models.CharField(db_column='CON_Retro2_Cur2', max_length=3, blank=True, null=True)  
    con_retro2_amt_cur3 = models.DecimalField(db_column='CON_Retro2_Amt_Cur3', max_digits=10, decimal_places=0, blank=True, null=True)  
    con_retro2_cur3 = models.CharField(db_column='CON_Retro2_Cur3', max_length=3, blank=True, null=True)  
    con_retro2_status = models.CharField(db_column='CON_Retro2_Status', max_length=1, blank=True, null=True)  
    con_retro2_payday = models.DateField(db_column='CON_Retro2_Payday', blank=True, null=True)  
    con_retro2_comment = models.CharField(db_column='CON_Retro2_Comment', max_length=32, blank=True, null=True)  
    con_retro3_from = models.DateField(db_column='CON_Retro3_From', blank=True, null=True)  
    con_retro3_to = models.DateField(db_column='CON_Retro3_To', blank=True, null=True)  
    con_retro3_total = models.DecimalField(db_column='CON_Retro3_Total', max_digits=10, decimal_places=0, blank=True, null=True)  
    con_retro3_amt_cur1 = models.DecimalField(db_column='CON_Retro3_Amt_Cur1', max_digits=10, decimal_places=0, blank=True, null=True)  
    con_retro3_cur1 = models.CharField(db_column='CON_Retro3_Cur1', max_length=3, blank=True, null=True)  
    con_retro3_amt_cur2 = models.DecimalField(db_column='CON_Retro3_Amt_Cur2', max_digits=10, decimal_places=0, blank=True, null=True)  
    con_retro3_cur2 = models.CharField(db_column='CON_Retro3_Cur2', max_length=3, blank=True, null=True)  
    con_retro3_amt_cur3 = models.DecimalField(db_column='CON_Retro3_Amt_Cur3', max_digits=10, decimal_places=0, blank=True, null=True)  
    con_retro3_cur3 = models.CharField(db_column='CON_Retro3_Cur3', max_length=3, blank=True, null=True)  
    con_retro3_status = models.CharField(db_column='CON_Retro3_Status', max_length=1, blank=True, null=True)  
    con_retro3_payday = models.DateField(db_column='CON_Retro3_Payday', blank=True, null=True)  
    con_retro3_comment = models.CharField(db_column='CON_Retro3_Comment', max_length=32, blank=True, null=True)  
    con_time_last = models.TimeField(db_column='CON_Time_Last', blank=True, null=True)  
    con_who_last = models.CharField(db_column='CON_Who_Last', max_length=4, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'contract'

    def __str__(self):
        return self.con_unique


class Country(models.Model):
    cn_d = models.CharField(db_column='CN_D', max_length=1, blank=True, null=True)  
    country = models.CharField(db_column='CN_KEY', primary_key=True, max_length=2)  
    cn_full = models.CharField(db_column='CN_Full', max_length=45, blank=True, null=True)  
    cn_nationality = models.CharField(db_column='CN_Nationality', max_length=20, blank=True, null=True)  
    cn_time_last = models.TimeField(db_column='CN_Time_Last', blank=True, null=True)  
    cn_who_last = models.CharField(db_column='CN_Who_Last', max_length=4, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'country'

    def __str__(self):
        return self.country

class Doc(models.Model):
    d_d = models.CharField(db_column='D_D', max_length=1, blank=True, null=True)  
    doc = models.IntegerField(db_column='D_REC', primary_key=True)  
    d_unique = models.CharField(db_column='D_UNIQUE', max_length=9, blank=True, null=True)  
    code = models.CharField(db_column='D_ID_B_ID', max_length=4, blank=True, null=True)  
    cert = models.ForeignKey('Cert', db_column='D_Cert_C_KEY', max_length=4, blank=True, null=True)  
    d_number = models.CharField(db_column='D_Number', max_length=32, blank=True, null=True)  
    d_rank_r_key = models.CharField(db_column='D_Rank_R_KEY', max_length=4, blank=True, null=True)  
    d_issue = models.DateField(db_column='D_Issue', blank=True, null=True)  
    d_expire = models.DateField(db_column='D_Expire', blank=True, null=True)  
    d_othercountry = models.CharField(db_column='D_OtherCountry', max_length=2, blank=True, null=True)  
    d_time_last = models.TimeField(db_column='D_Time_Last', blank=True, null=True)  
    d_who_last = models.CharField(db_column='D_Who_Last', max_length=4, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'doc'

    def __str__(self):
        return str(self.doc)

class Principal(models.Model):
    p_d = models.CharField(db_column='P_D', max_length=1, blank=True, null=True)  
    principal = models.CharField(db_column='P_KEY', primary_key=True, max_length=6)  
    p_master_p_key = models.CharField(db_column='P_Master_P_KEY', max_length=6, blank=True, null=True)  
    p_full = models.CharField(db_column='P_Full', max_length=40, blank=True, null=True)  
    p_sss = models.CharField(db_column='P_SSS', max_length=12, blank=True, null=True)  
    p_accredno = models.CharField(db_column='P_AccredNo', max_length=12, blank=True, null=True)  
    p_addr1 = models.CharField(db_column='P_Addr1', max_length=32, blank=True, null=True)  
    p_addr2 = models.CharField(db_column='P_Addr2', max_length=32, blank=True, null=True)  
    p_addr3 = models.CharField(db_column='P_Addr3', max_length=32, blank=True, null=True)  
    p_lawcountry = models.CharField(db_column='P_LawCountry', max_length=24, blank=True, null=True)  
    p_telephone = models.CharField(db_column='P_Telephone', max_length=32, blank=True, null=True)  
    p_email_address = models.CharField(db_column='P_Email_Address', max_length=36, blank=True, null=True)  
    p_acct_category_a = models.CharField(db_column='P_Acct_Category_A', max_length=16, blank=True, null=True)  
    p_acct_category_b = models.CharField(db_column='P_Acct_Category_B', max_length=16, blank=True, null=True)  
    p_acct_category_c = models.CharField(db_column='P_Acct_Category_C', max_length=16, blank=True, null=True)  
    p_acct_category_d = models.CharField(db_column='P_Acct_Category_D', max_length=16, blank=True, null=True)  
    p_acct_category_e = models.CharField(db_column='P_Acct_Category_E', max_length=16, blank=True, null=True)  
    p_acct_category_f = models.CharField(db_column='P_Acct_Category_F', max_length=16, blank=True, null=True)  
    p_acct_category_g = models.CharField(db_column='P_Acct_Category_G', max_length=16, blank=True, null=True)  
    p_acct_expenses = models.CharField(db_column='P_Acct_Expenses', max_length=16, blank=True, null=True)  
    p_time_last = models.TimeField(db_column='P_Time_Last', blank=True, null=True)  
    p_who_last = models.CharField(db_column='P_Who_Last', max_length=4, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'principal'

    def __str__(self):
        return self.principal

class Rank(models.Model):
    r_d = models.CharField(db_column='R_D', max_length=1, blank=True, null=True)  
    rank = models.CharField(db_column='R_KEY', primary_key=True, max_length=4)  
    r_full = models.CharField(db_column='R_Full', max_length=16, blank=True, null=True)  
    r_grk_desc = models.CharField(db_column='R_Grk_Desc', max_length=20, blank=True, null=True)  
    r_sort = models.CharField(db_column='R_Sort', max_length=2, blank=True, null=True)  
    r_tc_key = models.CharField(db_column='R_TC_KEY', max_length=1, blank=True, null=True)  
    r_officer = models.CharField(db_column='R_Officer', max_length=1, blank=True, null=True)  
    r_time_last = models.TimeField(db_column='R_Time_Last', blank=True, null=True)  
    r_who_last = models.CharField(db_column='R_Who_Last', max_length=4, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'rank'

    def __str__(self):
        return self.rank

class Service(models.Model):
    s_d = models.CharField(db_column='S_D', max_length=1, blank=True, null=True)  
    s_rec = models.IntegerField(primary_key=True, db_column='S_REC')  
    s_unique = models.CharField(db_column='S_UNIQUE', max_length=13)  
    contract = models.CharField(db_column='S_CON_UNIQUE', max_length=20, null=True)  
    # s_id_b_id = models.CharField(db_column='S_ID_B_ID', max_length=4, blank=True, null=True)  
    code = models.CharField(db_column='S_ID_B_ID', null=True, max_length=4)
    s_start = models.DateField(db_column='S_Start', blank=True, null=True)  
    s_end = models.DateField(db_column='S_End', blank=True, null=True)  
    s_why = models.CharField(db_column='S_Why', max_length=1, blank=True, null=True)  
    s_rank_r_key = models.CharField(db_column='S_Rank_R_KEY', max_length=4, blank=True, null=True)  
    s_vsl_v_key = models.CharField(db_column='S_Vsl_V_KEY', max_length=4, blank=True, null=True)  
    s_vsl_name = models.CharField(db_column='S_Vsl_Name', max_length=20, blank=True, null=True)  
    s_principal = models.CharField(db_column='S_Principal', max_length=20, blank=True, null=True)  
    s_cn_key = models.CharField(db_column='S_CN_KEY', max_length=2, blank=True, null=True)  
    s_grt = models.CharField(db_column='S_GRT', max_length=6, blank=True, null=True)  
    s_type_vt_key = models.CharField(db_column='S_Type_VT_KEY', max_length=4, blank=True, null=True)  
    s_engine = models.CharField(db_column='S_Engine', max_length=6, blank=True, null=True)  
    s_horsepower = models.CharField(db_column='S_HorsePower', max_length=8, blank=True, null=True)  
    s_time_last = models.TimeField(db_column='S_Time_Last', blank=True, null=True)  
    s_who_last = models.CharField(db_column='S_Who_Last', max_length=4, blank=True, null=True)  

    class Meta:
        managed = True
        db_table = 'service'

    def __str__(self):
        return str(self.s_rec)

    def days(self):
        start = str(self.s_start)
        end = str(self.s_end)

        if end == 'None':
            result = ''
        else:
            start = datetime.strptime(start, "%Y-%m-%d").date()
            end = datetime.strptime(end, "%Y-%m-%d").date()
            result = end - start
            result = (result.days)+1
        return result

        # start = datetime.strptime(start, "%Y-%m-%d").date()
        # end = datetime.strptime(end, "%Y-%m-%d").date()
        # result = end - start
        # return result.days

class Vessel(models.Model):
    v_d = models.CharField(db_column='V_D', max_length=1, blank=True, null=True)  
    vessel = models.CharField(db_column='V_KEY', primary_key=True, max_length=4)  
    vessel_type = models.ForeignKey('Vtype', db_column='V_Type', verbose_name='Vessel Type')  
    v_full = models.CharField(db_column='V_Full', max_length=32, blank=True, null=True)  
    principal = models.CharField(db_column='V_P_KEY', verbose_name='Principal', max_length=6, blank=True, null=True)  
    v_registry = models.CharField(db_column='V_Registry', max_length=12, blank=True, null=True)  
    v_cn_key = models.CharField(db_column='V_CN_KEY', max_length=2, blank=True, null=True)  
    v_regnumber = models.CharField(db_column='V_RegNumber', max_length=16, blank=True, null=True)  
    v_grt = models.IntegerField(db_column='V_GRT', blank=True, null=True)  
    v_nrt = models.IntegerField(db_column='V_NRT', blank=True, null=True)  
    v_dwt = models.CharField(db_column='V_DWT', max_length=8, blank=True, null=True)  
    v_engine = models.CharField(db_column='V_Engine', max_length=6, blank=True, null=True)  
    v_horsepower = models.CharField(db_column='V_HorsePower', max_length=8, blank=True, null=True)  
    v_class = models.CharField(db_column='V_Class', max_length=4, blank=True, null=True)  
    v_yard = models.CharField(db_column='V_Yard', max_length=12, blank=True, null=True)  
    v_yearbuilt = models.IntegerField(db_column='V_YearBuilt', blank=True, null=True)  
    v_trades = models.CharField(db_column='V_Trades', max_length=16, blank=True, null=True)  
    v_ums = models.CharField(db_column='V_UMS', max_length=1, blank=True, null=True)  
    v_callsign = models.CharField(db_column='V_CallSign', max_length=6, blank=True, null=True)  
    v_owner_ship = models.CharField(db_column='V_Owner_Ship', max_length=45, blank=True, null=True)  
    v_imo = models.CharField(db_column='V_IMO', max_length=12, blank=True, null=True)  
    v_status = models.CharField(db_column='V_Status', max_length=1, blank=True, null=True)  
    v_end = models.DateField(db_column='V_End', blank=True, null=True)  
    v_reason = models.CharField(db_column='V_Reason', max_length=18, blank=True, null=True)  
    v_main_cat = models.CharField(db_column='V_Main_Cat', max_length=1, blank=True, null=True)  
    v_equip_1 = models.CharField(db_column='V_Equip_1', max_length=4, blank=True, null=True)  
    v_equip_2 = models.CharField(db_column='V_Equip_2', max_length=4, blank=True, null=True)  
    v_equip_3 = models.CharField(db_column='V_Equip_3', max_length=4, blank=True, null=True)  
    v_equip_4 = models.CharField(db_column='V_Equip_4', max_length=4, blank=True, null=True)  
    v_pays_nat = models.CharField(db_column='V_Pays_NAT', max_length=1, blank=True, null=True)  
    v_pays_fmy = models.CharField(db_column='V_Pays_FMY', max_length=1, blank=True, null=True)  
    v_pays_pno = models.CharField(db_column='V_Pays_PNO', max_length=1, blank=True, null=True)  
    v_pays_tax = models.CharField(db_column='V_Pays_TAX', max_length=1, blank=True, null=True)  
    v_p_post_date = models.DateField(db_column='V_P_Post_Date', blank=True, null=True)  
    v_r_post_date = models.DateField(db_column='V_R_Post_Date', blank=True, null=True)  
    v_e_post_date = models.DateField(db_column='V_E_Post_Date', blank=True, null=True)  
    v_tfs_fleet = models.CharField(db_column='V_TFS_Fleet', max_length=1, blank=True, null=True)  
    v_tfs_ship = models.CharField(db_column='V_TFS_Ship', max_length=4, blank=True, null=True)  
    v_email_1 = models.CharField(db_column='V_Email_1', max_length=28, blank=True, null=True)  
    v_email_2 = models.CharField(db_column='V_Email_2', max_length=28, blank=True, null=True)  
    v_time_last = models.TimeField(db_column='V_Time_Last', blank=True, null=True)  
    v_who_last = models.CharField(db_column='V_Who_Last', max_length=4, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'vessel'

    def __str__(self):
        return self.vessel


class Vtype(models.Model):
    vt_d = models.CharField(db_column='VT_D', max_length=1, blank=True, null=True)  
    vessel_type = models.CharField(db_column='VT_KEY', primary_key=True, max_length=4)  
    vt_full = models.CharField(db_column='VT_Full', max_length=16, blank=True, null=True)  
    vt_time_last = models.TimeField(db_column='VT_Time_Last', blank=True, null=True)  
    vt_who_last = models.CharField(db_column='VT_Who_Last', max_length=4, blank=True, null=True)  

    class Meta:
        managed = False
        db_table = 'vtype'

    def __str__(self):
        return self.vessel_type

class Bio(models.Model):
    # id = models.IntegerField(primary_key=True)
    code = models.CharField(db_column='B_ID', max_length=4, primary_key=True)  
    b_d = models.CharField(db_column='B_D', max_length=1, blank=True, null=True)  
    b_uid = models.IntegerField(db_column='B_UID', blank=True, null=True)  
    last_name = models.CharField(db_column='B_Last_Name', max_length=18, blank=True, null=True)  
    b_last_name_grk = models.CharField(db_column='B_Last_Name_Grk', max_length=18, blank=True, null=True)  
    first_name = models.CharField(db_column='B_First_Name', max_length=28, blank=True, null=True)  
    b_first_name_grk = models.CharField(db_column='B_First_Name_Grk', max_length=18, blank=True, null=True)  
    middle_name = models.CharField(db_column='B_Middle_Name', max_length=18, blank=True, null=True)  
    b_suffix_name = models.CharField(db_column='B_Suffix_Name', max_length=5, blank=True, null=True)  
    b_middle_name_grk = models.CharField(db_column='B_Middle_Name_Grk', max_length=18, blank=True, null=True)  
    b_father_name = models.CharField(db_column='B_Father_Name', max_length=18, blank=True, null=True)  
    b_father_name_grk = models.CharField(db_column='B_Father_Name_Grk', max_length=18, blank=True, null=True)  
    b_mother_name = models.CharField(db_column='B_Mother_Name', max_length=18, blank=True, null=True)  
    b_mother_name_grk = models.CharField(db_column='B_Mother_Name_Grk', max_length=18, blank=True, null=True)  
    country = models.CharField(db_column='B_CN_KEY', max_length=2, blank=True, null=True)  
    status = models.CharField(db_column='B_Bio_Status', verbose_name='Status', max_length=1, blank=True, null=True)  
    b_available = models.DateField(db_column='B_Available', blank=True, null=True)  
    rank = models.CharField(db_column='B_Position_1st', verbose_name='Rank', max_length=4, blank=True, null=True)  
    b_ex_crew = models.CharField(db_column='B_Ex_Crew', max_length=1, blank=True, null=True)  
    last_vessel = models.ForeignKey('Vessel', verbose_name='Last Vessel', db_column='B_Last_V_KEY')  
    b_rank1_r_key = models.CharField(db_column='B_Rank1_R_KEY', max_length=4, blank=True, null=True)  
    b_type1_vt_key = models.CharField(db_column='B_Type1_VT_KEY', max_length=4, blank=True, null=True)  
    b_rank2_r_key = models.CharField(db_column='B_Rank2_R_KEY', max_length=4, blank=True, null=True)  
    b_type2_vt_key = models.CharField(db_column='B_Type2_VT_KEY', max_length=4, blank=True, null=True)  
    b_birth_date = models.DateField(db_column='B_Birth_Date', blank=True, null=True)  
    b_birth_place = models.CharField(db_column='B_Birth_Place', max_length=32, blank=True, null=True)  
    b_height = models.CharField(db_column='B_Height', max_length=5, blank=True, null=True)  
    b_weight = models.CharField(db_column='B_Weight', max_length=5, blank=True, null=True)  
    b_bmi = models.DecimalField(db_column='B_BMI', max_digits=10, decimal_places=0, blank=True, null=True)  
    b_phone_1 = models.CharField(db_column='B_Phone_1', max_length=16, blank=True, null=True)  
    b_phone_2 = models.CharField(db_column='B_Phone_2', max_length=16, blank=True, null=True)  
    b_metro_addr_1 = models.CharField(db_column='B_Metro_Addr_1', max_length=32, blank=True, null=True)  
    b_metro_addr_2 = models.CharField(db_column='B_Metro_Addr_2', max_length=32, blank=True, null=True)  
    b_metro_addr_3 = models.CharField(db_column='B_Metro_Addr_3', max_length=32, blank=True, null=True)  
    b_metro_addr_4 = models.CharField(db_column='B_Metro_Addr_4', max_length=32, blank=True, null=True)  
    b_prov_addr_1 = models.CharField(db_column='B_Prov_Addr_1', max_length=16, blank=True, null=True)  
    b_prov_addr_2 = models.CharField(db_column='B_Prov_Addr_2', max_length=16, blank=True, null=True)  
    b_prov_addr_3 = models.CharField(db_column='B_Prov_Addr_3', max_length=16, blank=True, null=True)  
    b_prov_addr_4 = models.CharField(db_column='B_Prov_Addr_4', max_length=16, blank=True, null=True)  
    b_addr_grk_1 = models.CharField(db_column='B_Addr_Grk_1', max_length=16, blank=True, null=True)  
    b_addr_grk_2 = models.CharField(db_column='B_Addr_Grk_2', max_length=16, blank=True, null=True)  
    b_addr_grk_3 = models.CharField(db_column='B_Addr_Grk_3', max_length=16, blank=True, null=True)  
    b_addr_grk_4 = models.CharField(db_column='B_Addr_Grk_4', max_length=16, blank=True, null=True)  
    b_marital_status = models.CharField(db_column='B_Marital_Status', max_length=1, blank=True, null=True)  
    b_number_dependents = models.IntegerField(db_column='B_Number_Dependents', blank=True, null=True)  
    b_emergency_name = models.CharField(db_column='B_Emergency_Name', max_length=24, blank=True, null=True)  
    b_emergency_relation = models.CharField(db_column='B_Emergency_Relation', max_length=4, blank=True, null=True)  
    b_emergency_phone = models.CharField(db_column='B_Emergency_Phone', max_length=16, blank=True, null=True)  
    b_emergency_addr_1 = models.CharField(db_column='B_Emergency_Addr_1', max_length=32, blank=True, null=True)  
    b_emergency_addr_2 = models.CharField(db_column='B_Emergency_Addr_2', max_length=32, blank=True, null=True)  
    b_emergency_addr_3 = models.CharField(db_column='B_Emergency_Addr_3', max_length=32, blank=True, null=True)  
    b_emergency_addr_4 = models.CharField(db_column='B_Emergency_Addr_4', max_length=32, blank=True, null=True)  
    b_educ_note_1 = models.CharField(db_column='B_Educ_Note_1', max_length=34, blank=True, null=True)  
    b_educ_note_2 = models.CharField(db_column='B_Educ_Note_2', max_length=34, blank=True, null=True)  
    b_mother_language = models.CharField(db_column='B_Mother_Language', max_length=8, blank=True, null=True)  
    b_english = models.CharField(db_column='B_English', max_length=1, blank=True, null=True)  
    b_comments = models.CharField(db_column='B_Comments', max_length=60, blank=True, null=True)  
    b_wife_name = models.CharField(db_column='B_Wife_Name', max_length=34, blank=True, null=True)  
    b_wife_birthdate = models.DateField(db_column='B_Wife_BirthDate', blank=True, null=True)  
    b_wife_job = models.CharField(db_column='B_Wife_Job', max_length=1, blank=True, null=True)  
    b_tax_status = models.CharField(db_column='B_Tax_Status', max_length=1, blank=True, null=True)  
    b_tax_acct = models.CharField(db_column='B_Tax_Acct', max_length=20, blank=True, null=True)  
    b_tax_office = models.CharField(db_column='B_Tax_Office', max_length=30, blank=True, null=True)  
    b_sss = models.CharField(db_column='B_SSS', max_length=16, blank=True, null=True)  
    b_phealth = models.CharField(db_column='B_PHealth', max_length=16, blank=True, null=True)  
    b_vocational = models.CharField(db_column='B_Vocational', max_length=16, blank=True, null=True)  
    b_hs_grad = models.CharField(db_column='B_HS_Grad', max_length=1, blank=True, null=True)  
    b_hs_date = models.DateField(db_column='B_HS_Date', blank=True, null=True)  
    b_nautical_school = models.CharField(db_column='B_Nautical_School', max_length=16, blank=True, null=True)  
    b_nautical_degree = models.CharField(db_column='B_Nautical_Degree', max_length=4, blank=True, null=True)  
    b_nautical_date = models.DateField(db_column='B_Nautical_Date', blank=True, null=True)  
    b_other_school = models.CharField(db_column='B_Other_School', max_length=16, blank=True, null=True)  
    b_other_degree = models.CharField(db_column='B_Other_Degree', max_length=8, blank=True, null=True)  
    b_other_date = models.DateField(db_column='B_Other_Date', blank=True, null=True)  
    b_union = models.CharField(db_column='B_Union', max_length=1, blank=True, null=True)  
    b_separation_type = models.CharField(db_column='B_Separation_Type', max_length=1, blank=True, null=True)  
    b_sea_months = models.IntegerField(db_column='B_Sea_Months', blank=True, null=True)  
    b_high_rank1_r_key = models.CharField(db_column='B_High_Rank1_R_KEY', max_length=4, blank=True, null=True)  
    b_vtype_rank1_vt_key = models.CharField(db_column='B_VType_Rank1_VT_KEY', max_length=4, blank=True, null=True)  
    b_high_rank2_r_key = models.CharField(db_column='B_High_Rank2_R_KEY', max_length=4, blank=True, null=True)  
    b_vtype_rank2_vt_key = models.CharField(db_column='B_VType_Rank2_VT_KEY', max_length=4, blank=True, null=True)  
    b_skills = models.CharField(db_column='B_Skills', max_length=32, blank=True, null=True)  
    b_nick_name = models.CharField(db_column='B_Nick_Name', max_length=12, blank=True, null=True)  
    b_email_address = models.CharField(db_column='B_Email_Address', max_length=45, blank=True, null=True)  
    b_ofw_id = models.CharField(db_column='B_OFW_ID', max_length=32, blank=True, null=True)  
    b_pagibig = models.CharField(db_column='B_Pagibig', max_length=16, blank=True, null=True)  
    b_freemail = models.CharField(db_column='B_Freemail', max_length=1, blank=True, null=True)  
    b_time_last = models.TimeField(db_column='B_Time_Last', blank=True, null=True)  
    b_who_last = models.CharField(db_column='B_Who_Last', max_length=4, blank=True, null=True)

    # first_name = models.CharField(max_length=70, null=True)
    class Meta:
        managed = False
        db_table = 'bio'

    def __str__(self):
        return self.code

    def clean(self):
        if self.b_d:
            return self.code

    def name(self):
        return "%s %s %s" % (self.first_name, self.middle_name, self.last_name)
    # full_name = property(get_full_name)

    def vessel_type(self):
        return self.last_vessel.vessel_type

    def principal(self):
        return self.last_vessel.principal

    def view_info(self):
        return mark_safe("<a href='/crew/view-info/%s' onclick='return showAddAnotherPopup(this, 0.9, 0.80);'><button type='button' class='btn btn-warning view-info'>View Full Info</button></a>" % self.code)
    view_info.short_description = ''

    def view_picture(self):
        return mark_safe("<a href='/crew/view-picture/%s' onclick='return picturePopup(this, .16, 0.22);'><button type='button' class='btn btn-warning view-pic'>View Picture</button></a>" % self.code)
    view_picture.short_description = ''

class Wage(models.Model):
    w_d = models.CharField(db_column='W_D', max_length=1, blank=True, null=True)  # Field name made lowercase.
    w_rec = models.IntegerField(primary_key=True, db_column='W_REC')  # Field name made lowercase.
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

    def __str__(self):
        return self.w_unique