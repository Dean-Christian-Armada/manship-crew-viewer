from django.db import models

# Create your models here.
# Relational Keys must be a link

# FK = 'Vessel Category', 'Certificate Group', 'Tax Category', 'Country', 'Vessel Type', 'vequip', 'Contract'

class Certificates(models.Model):
	# 10 rows
	C_D = models.CharField(max_length=1, null=True) # Delete Status (if D this record is deleted).
	C_KEY = models.CharField(max_length=5) # certificate code e.g. SOLA solas
	C_Full = models.CharField(max_length=50) # certificate code e.g. SOLA solas
	C_Book = models.CharField(max_length=1) # Is this certificate the main certificate Y/N (Greek seaman's book)
	C_Main = models.CharField(max_length=1) # Is this certificate on the main form Y/N (FOR MSMI)
	C_Expires = models.CharField(max_length=1) # Is this certificate on the main form Y/N (FOR MSMI)
	C_Interval_Years = models.IntegerField() # Interval Years
	C_Interval_Months = models.IntegerField() # Interval Months
	C_Time_Last = models.DateTimeField() # Timestamp of last change
	C_Who_Last = models.CharField(max_length=100) # Who did the last change

class RequiredCertificates(models.Model):
	# 11 rows
	# Foreign Keys = ['Principals', 'Rank', 'Vessel Category', 'Certificate Group']
	RC_D = models.CharField(max_length=1, null=True) # Delete Status (if D this record is deleted).
	RC_REC = models.IntegerField() # Req Cert REC
	RC_UNIQUE = models.CharField(max_length=18) # Principal + Vessel Main Cat + Rank + Master Cert Key must be UNIQUE
	# P_KEY = Principal as Foreign Key
	RC_P_KEY = models.CharField(max_length=6, unique=True) # Principal Code
	# VC_KEY = Vessel Category as Foreign Key
	RC_VC_KEY = models.CharField(max_length=1) # Vessel Main Category
	# R_KEY = Rank as Foreign Key
	RC_R_KEY = models.CharField(max_length=4) # Rank Code
	# RG_KEY = Certificate Group as Foreign Key
	RC_CG_KEY = models.CharField(max_length=4) # Certificate Group Code
	RC_Source = models.CharField(max_length=1) # Source (I)nhouse or (O)utside
	RC_Interval = models.IntegerField() # Interval
	RC_Time_Last = models.DateTimeField() # Timestamp of last change
	RC_Who_Last = models.CharField(max_length=4) # Who did the last change

class CERT_GROUPS(models.Model):
	# 5 rows
	CG_D = models.CharField(max_length=1, null=True) # Delete Status (if D this record is deleted).
	CG_KEY = models.CharField(max_length=4) # Cert Group (Master) Key
	CG_Full = models.CharField(max_length=64) # Cert Group Full Name
	CG_Time_Last = models.DateTimeField() # Timestamp of last change
	CG_Who_Last = models.CharField(max_length=4) # Who did the last change

class BIO_DATA(models.Model):
	# 67 rows
	B_D = models.CharField(max_length=1, null=True) # Delete Status (if D this record is deleted).
	B_ID = models.CharField(max_length=4, unique=True) # Seaman Code ID e.g. KMB1
	B_UID = models.IntegerField() # UserID No
	B_Last_Name = models.CharField(max_length=18)
	B_First_Name = models.CharField(max_length=28)
	B_Middle_Name = models.CharField(max_length=18)
	B_Suffix_Name = models.CharField(max_length=5)
	B_Father_Name = models.CharField(max_length=18)
	B_Mother_Name = models.CharField(max_length=18)
	B_CN_KEY = models.CharField(max_length=2) # Nationality
	B_Bio_Status = models.CharField(max_length=1) # Overall Status
	B_Available = models.CharField(max_length=8) # When finished contract or available ??????????????????
	B_Position_1st = models.CharField(max_length=4) # Rank
	B_Ex_Crew = models.CharField(max_length=1) # Ex-Crew Y/N?
	B_Last_V_KEY = models.CharField(max_length=4) # Last Ship of Ours
	B_Birth_Date = models.DateTimeField() # Birth Date
	B_Birth_Place = models.CharField(max_length=32) # Birth Place
	B_Height = models.CharField(max_length=5) # Height (in feet) (FOR MSMI)
	B_Weight = models.CharField(max_length=5) # Weight (in pounds) (FOR MSMI)
	B_BMI = models.CharField(max_length=5) # Mass Index (BMI)
	B_Phone_1 = models.CharField(max_length=16) # Phone contact 1
	B_Phone_2 = models.CharField(max_length=16) # Phone contact 2
	B_Metro_Addr_1 = models.CharField(max_length=32) # Metro Manila Address Line 1
	B_Metro_Addr_2 = models.CharField(max_length=32) # Metro Manila Address Line 2
	B_Metro_Addr_3 = models.CharField(max_length=32) # Metro Manila Address Line 3
	B_Metro_Addr_4 = models.CharField(max_length=32) # Metro Manila Address Line 4
	# 35-38
	B_Prov_Addr_1 = models.CharField(max_length=16) # Province Address Line 1 (For MSMI)
	B_Prov_Addr_2 = models.CharField(max_length=16) # Province Address Line 2 (For MSMI)
	B_Prov_Addr_3 = models.CharField(max_length=16) # Province Address Line 3 (For MSMI)
	B_Marital_Status = models.CharField(max_length=1) # (S)ingle (M)arried (L)egalSeparate (W)idow ...
	B_Number_Dependents = models.IntegerField() # Number of Dependents
	B_Emergency_Name = models.CharField(max_length=24) # Emergency Name Contact
	B_Emergency_Relation = models.CharField(max_length=4) # Relationship of Emergency Contact
	B_Emergency_Phone = models.CharField(max_length=16) # Emergency Contact Phone
	B_Emergency_Addr_1 = models.CharField(max_length=32) # Emergency Contact Address 1
	B_Emergency_Addr_2 = models.CharField(max_length=32) # Emergency Contact Address 2
	B_Emergency_Addr_3 = models.CharField(max_length=32) # Emergency Contact Address 3
	B_Emergency_Addr_4 = models.CharField(max_length=32) # Emergency Contact Address 4
	B_Educ_Note_1 = models.CharField(max_length=34) # Educational Note 1
	B_Educ_Note_2 = models.CharField(max_length=34) # Educational Note 2
	B_Mother_Language = models.CharField(max_length=8) # Mother Language/Dialect
	B_English = models.CharField(max_length=1) # English (V)good (G)ood (S)at (P)oor (B)ad
	B_Comments = models.CharField(max_length=60) # Comments on the seaman
	B_Wife_Name = models.CharField(max_length=34) # Wifes Name
	B_Wife_BirthDate = models.IntegerField() # Wifes Birth Date
	B_Wife_Job = models.CharField(max_length=1) # Works or Not
	B_Tax_Status = models.CharField(max_length=1) # How Taxes are filed. (S)ingle (M)arried ...
	B_Tax_Acct = models.CharField(max_length=20) # Tax Acct Number.
	B_Tax_Office = models.CharField(max_length=30) # Tax Office
	B_SSS = models.CharField(max_length=16) # Social Security Number
	B_PHealth = models.CharField(max_length=16) # Philippine Health Number (FOR MSMI)
	B_Vocational = models.CharField(max_length=16) # Vocational Training  (FOR MSMI)
	B_HS_Grad = models.CharField(max_length=1) # High School Graduate Y/N?  (FOR MSMI)
	B_HS_Date = models.DateTimeField() # Date Graduated or Last Attended  (FOR MSMI)
	B_Nautical_School = models.CharField(max_length=16) # Nautical College Name  (FOR MSMI)
	B_Nautical_Degree = models.CharField(max_length=4) # Nautical Degree  (FOR MSMI)
	B_Nautical_Date = models.DateTimeField() # Date Graduated or Last Attended  (FOR MSMI)
	B_Other_School = models.CharField(max_length=8) # Other School Name  (FOR MSMI)
	B_Other_Degree = models.CharField(max_length=8) # Other Degrees  (FOR MSMI)
	B_Other_Date = models.DateTimeField() # Date Graduated or Last Attended  (FOR MSMI)
	B_Union = models.CharField(max_length=1) # Union Member Y/N?  (FOR MSMI)
	B_Separation_Type = models.CharField(max_length=1) # Separation Type B=Beneficial, U=Unavoidable, N=Normal
	B_Sea_Months = models.IntegerField(3) # Months at Sea  (FOR MSMI)
	# 77 - 81
	B_Nick_Name = models.CharField(max_length=12) # Nick Name of ID
	B_Email_Address = models.CharField(max_length=45) # Personal Email Address
	B_OFW_ID = models.CharField(max_length=32)
	B_Pagibig = models.CharField(max_length=16)
	# 86
	B_Time_Last = models.DateTimeField() # Timestamp of last change
	B_Who_Last = models.CharField(max_length=4) # Who did the last change

class RANKS(models.Model):
	# 8 rows
	# Foreign Keys = ['Tax Category']
	R_D = models.CharField(max_length=1, null=True) # Delete Status (if D this record is deleted).
	R_KEY = models.CharField(max_length=4) # Short rank code. e.g. CA captain
	R_Full = models.CharField(max_length=16) # Full rank description
	R_Sort = models.CharField(max_length=2) # Rank sorting seq. e.g.  CA=01 captain first
	# TC_KEY = Tax Category as Foreign Key of R_TC_KEY
	R_TC_KEY = models.CharField(max_length=1) # Category for taxes (C)rew / (O)fficer
	R_Officer = models.CharField(max_length=1) # Officer/Crew
	R_Time_Last = models.DateTimeField() # Timestamp of last change
	R_Who_Last = models.CharField(max_length=4) # Who did the last change

class TAX_CATEGORIES(models.Model):
	# 5 rows
	TC_D = models.CharField(max_length=1, null=True) # Delete Status (if D this record is deleted).
	TC_KEY = models.CharField(max_length=1) # Tax category eg (C)rew / (O)fficer
	TC_Full = models.CharField(max_length=40) # Full Category Name
	TC_Time_Last = models.DateTimeField() # Timestamp of last change
	TC_Who_Last = models.CharField(max_length=4) # Who did the last change

class DOCUMENTS(models.Model):
	# 12 rows
	# Foreign Keys = ['Bio', 'Certificates', 'Ranks', 'Country']
	# Many to Many Keys = ['Bio & Certificate']
	D_D = models.CharField(max_length=1, null=True) # Delete Status (if D this record is deleted).
	D_REC = models.IntegerField() # Documents RECORD NUMBER
	# B_ID.C_KEY as many-to-many of D_UNIQUE
	D_UNIQUE = models.CharField(max_length=9) # 4+1+4 UNIQUE (NOT REALLY UNIQUE !!)
	# B_ID as Foreign Key of D_ID_B_ID
	D_ID_B_ID = models.CharField(max_length=4) # Seaman Code ID e.g. KMB1
	# C_KEY as Foreign Key of D_Cert_C_Key
	D_Cert_C_KEY = models.CharField(max_length=4) # Cert. Code eg. SOLA
	D_Number = models.CharField(max_length=32) # Certificate Number
	# R_KEY as Foreign Key of D_Rank_R_KEY
	D_Rank_R_KEY = models.CharField(max_length=4) # Rank on Certificate
	D_Issue = models.DateTimeField() # Issue Date
	D_Expire = models.DateTimeField() # Expiry Date
	# CN_KEY as Foreign Key to CN_KEY
	D_OtherCountry = models.CharField(max_length=2) # Other Country for Book/License (FOR MSMI)
	D_Time_Last = models.DateTimeField() # Timestamp of last change
	D_Who_Last = models.CharField(max_length=4) # Who did the last change

class COUNTRY(models.Model):
	# 6 rows
	CN_D = models.CharField(max_length=1, null=True) # Delete Status (if D this record is deleted).
	CN_KEY = models.CharField(max_length=2) # ISO-3166 Short Country Code.  GR, TR, US etc
	CN_Full = models.CharField(max_length=45) # Full Country Name. Liberian Panamania Marshall Islands
	CN_Nationality = models.CharField(max_length=20) # Nationality Full Descr. (eg. Greek, Philipino etc).
	CN_Time_Last = models.DateTimeField() # Timestamp of last change
	CN_Who_Last = models.CharField(max_length=4) # Who did the last change

class PRINCIPALS(models.Model):
	# 23 rows
	P_D = models.CharField(max_length=1, null=True) # Delete Status (if D this record is deleted).
	P_KEY = models.CharField(max_length=6) # Principal Code
	# P_KEY as Foreign Key of P_Master_P_Key
	P_Master_P_KEY = models.CharField(max_length=6) # Ref to Master(POEA) principal
	P_Full = models.CharField(max_length=40) # Principals Full Name
	P_SSS = models.CharField(max_length=12) # Princials SSS number
	P_AccredNo = models.CharField(max_length=12) # Principals Accreditation Number
	P_Addr1 = models.CharField(max_length=32) # Address Line 1 for Principal
	P_Addr2 = models.CharField(max_length=32) # Address Line 2 for Principal
	P_Addr3 = models.CharField(max_length=32) # Address Line 3 for Principal
	P_LawCountry = models.CharField(max_length=24) # Law, City, Country of Principal| lawscity_country
	P_Telephone = models.CharField(max_length=32) # Telephone Number of Principal
	P_Email_Address = models.CharField(max_length=36) # Email Address of Principal
	P_Acct_Category_A = models.CharField(max_length=16) # Recipient Allocation Control A
	P_Acct_Category_B = models.CharField(max_length=16) # Recipient Allocation Control B
	P_Acct_Category_C = models.CharField(max_length=16) # Recipient Allocation Control C
	P_Acct_Category_D = models.CharField(max_length=16) # Recipient Allocation Control D
	P_Acct_Category_E = models.CharField(max_length=16) # Recipient Allocation Control E
	P_Acct_Category_F = models.CharField(max_length=16) # Recipient Allocation Control F
	P_Acct_Category_G = models.CharField(max_length=16) # Recipient Allocation Control G
	P_Acct_Expenses = models.CharField(max_length=16) # Recipient Expenses - eg Postage
	P_Time_Last = models.DateTimeField() # Timestamp of last change
	P_Who_Last = models.DateTimeField() # Who did the last change

class SERVICE_RECORDS(models.Model):
	# 19 rows
	# Foreign Keys = ['Contract', 'Bio', 'Rank', 'Vessels', 'Country', 'Vessel Type']
	S_D = models.CharField(max_length=1, null=True) # Delete Status (if D this record is deleted).
	S_REC = models.IntegerField() # Service Records RECORD NUMBER
	S_UNIQUE = models.CharField(max_length=13) # SeamanID.Start_Date UNIQUE
	# CON_UNIQUE as Foreign Key of S_CON_UNIQUE
	S_CON_UNIQUE = models.CharField(max_length=10) # Soft link to Contract that created this entry
	# B_ID as Foreign Key of S_ID_B_ID
	S_ID_B_ID = models.CharField(max_length=4) # Seaman Code ID e.g. KMB1
	S_Start = models.DateTimeField() # Start of Service
	S_End = models.DateTimeField() # End of Service
	S_Why = models.CharField(max_length=1) # Reason for leaving
	# R_KEY as foreign key of S_Rank_R_KEY
	S_Rank_R_KEY = models.CharField(max_length=4) # Rank
	# V_KEY as foreign key of S_Vsl_V_KEY
	S_Vsl_V_KEY = models.CharField(max_length=4) # Vessel ID Code
	S_Vsl_Name = models.CharField(max_length=20) # Vessel Name (Other maybe)
	S_Principal = models.CharField(max_length=20) # Principal/Owner
	# CN_KEY as foreign key of S_CN_KEY
	S_CN_KEY = models.CharField(max_length=2) # Flag
	S_GRT = models.CharField(max_length=6) # GRT
	# VT_KEYS as foreign key of S_Type_VT_KEY
	S_Type_VT_KEY = models.CharField(max_length=4) # Vessel Type
	S_Engine = models.CharField(max_length=6) # Engine Type
	S_HorsePower = models.CharField(max_length=8) # Engine HorsePower
	S_Time_Last = models.DateTimeField() # Timestamp of last change
	S_Who_Last = models.DateTimeField() # Who did the last change
	S_Engine = models.CharField(max_length=6) # Engine Type

class CONTRACTS(models.Model):
	# 44 rows
	# Foreign Keys = ['Manning Agent', 'Principal', 'Wage']
	CON_D = models.CharField(max_length=1, null=True) # Delete Status (if D this record is deleted)self.
	# 1-3
	CON_Number = models.IntegerField() # Contract Number
	CON_B_ID = models.CharField(max_length=4) # Seaman ID
	CON_W_CS_KEY = models.CharField(max_length=2) # Wages Scale
	CON_T_CS_KEY = models.CharField(max_length=2) # Taxes Scale
	# MAN_KEYS as foreign key of CON_MAN_KEY
	CON_MAN_KEY = models.CharField(max_length=4) # Manning Agent Code
	# Prin_P_KEY as foreign key of CON_Prin_P_KEY
	CON_Prin_P_KEY = models.CharField(max_length=6) # Principals Code
	# Master_P_KEY as foreign key of CON_Master_P_KEY
	CON_Master_P_KEY = models.CharField(max_length=6) # Master Official POEA Principal
	# Wage_W_REC as foreign key of CON_Wage_W_REC
	CON_Wage_W_REC = models.CharField(max_length=8) # Wage Table for this contract
	CON_Vsl_V_KEY = models.CharField(max_length=4) # Vessel Code
	CON_Rank_R_KEY = models.CharField(max_length=4) # Rank
	CON_Crew_Category = models.CharField(max_length=1) # models.CharField(max_length=rew)/T(rainee)
	# 16
	CON_Length = models.IntegerField() # Contract Duration
	CON_PDOS = models.DateTimeField() # Pre Depart Orient Sem. Date (FOR MSMI)
	CON_Money_Beg = models.DateTimeField() # When Principal Starts Paying
	CON_Embark = models.DateTimeField() # Embarkation Date
	CON_Embark_Com = models.CharField(max_length=80) # Embarkation Comment
	CON_Join = models.DateTimeField() # Date Joined Vessel
	CON_Join_Where = models.CharField(max_length=16) # Where Joined Vessel
	CON_Left = models.DateTimeField() # Date Joined Vessel
	CON_Left_Where = models.CharField(max_length=16) # Where Joined Vessel
	CON_Disembark = models.DateTimeField() # Disembark Date (arrived back)
	CON_Disembark_Com = models.CharField(max_length=80) # Disembark Comment
	CON_Money_End = models.DateTimeField() # When Principal STOPS Paying - signoff
	CON_Reason_Signoff = models.CharField(max_length=20) # Signoff Comment
	CON_Date_Fitness = models.DateTimeField() # Date of last Medical Fit (FOR MSMI)
	CON_Contract_Date = models.DateTimeField() # Contract Date
	CON_POEA_Date = models.DateTimeField() # POEA Date (FOR MSMI)
	CON_OEC = models.IntegerField() # OEC Number (FOR MSMI)
	CON_Last_Eval_Rcv = models.CharField(max_length=1) # Last Evaluation Received ? (Y/N)
	CON_Seniority = models.IntegerField() # Seniority (in years)
	CON_Senior_Date = models.DateTimeField() # Date for Seniority Change
	CON_Mth_Basic = models.DecimalField(max_digits=16, decimal_places=2) # Basic Monthly
	CON_Mth_Extra1 = models.DecimalField(max_digits=16, decimal_places=2) # Monthly Extra 1 outside wages
	CON_Mth_Extra1_Descr = models.CharField(max_length=32) # Description of extra1
	CON_Mth_Extra2 = models.DecimalField(max_digits=16, decimal_places=2) # Monthly Extra 1 outside wages
	CON_Mth_Extra2_Descr = models.CharField(max_length=32) # Description of extra1
	CON_Fix_Mth_OT = models.DecimalField(max_digits=16, decimal_places=2) # Fixed Mthly OT in USD
	CON_Hourly_OT_Rate = models.DecimalField(max_digits=16, decimal_places=2) # Hourly Overtime Rate
	CON_Min_Mth_OT_Hours = models.IntegerField() # Monthly Min. Overtime Hours
	CON_Hours_week = models.IntegerField() # Weekly Standard Hours
	# 46 -177
	CON_Time_Last = models.DateTimeField() # Timestamp of last change
	CON_Who_Last = models.DateTimeField() # Who did the last change

class WAGES(models.Model):
	# 107 rows
	# Foreign Keys = ['Principal', 'Rank', 'Component Scales', 'Components']
	W_D = models.CharField(max_length=1, null=True) # Delete Status (if D this record is deleted).
	# 1-3
	# P_KEY as foreign key of W_P_KEY
	W_P_KEY = models.CharField(max_length=6) # Principals Code | principal_code
	W_Date = models.DateTimeField() # Date Wage Scale becomes effective | effectivity_date
	# R_KEY as foreign key of W_Rank_R_KEY
	W_Rank_R_KEY = models.CharField(max_length=4) # Rank | rank_code
	# CS_Key as Foreign Key os W_CS_Key
	W_CS_KEY = models.CharField(max_length=2) # Wage Scale
	W_M_Money = models.CharField(max_length=3) # Currency for this Wage Scale
	W_Mth_Basic = models.DecimalField(max_digits=16, decimal_places=2) # Monthly Basic
	W_Fix_Mth_OT = models.DecimalField(max_digits=16, decimal_places=2) # Fixed Monthly Overtime USD
	W_Hourly_OT_Rate = models.DecimalField(max_digits=16, decimal_places=2) # Hourly Rate for OverTime USD/Hour
	W_Min_Mth_OT_Hours = models.IntegerField() # Monthly Min. Overtime Hours
	W_Hours_Week = models.IntegerField() # Weekly Standard Hours
	# CO_Key as Foreign Key of W_Comp_Type_*
	W_Comp_Type_1 = models.CharField(max_length=3) # Type of Salary Comp. 1 |"F"
	W_Comp_Name_1 = models.CharField(max_length=16) # Name of Salary Comp. 1 | "fix_mthly_overtime"
	W_Comp_Amnt_1 = models.DecimalField(max_digits=16, decimal_places=2) # Amnt of Salary Comp. 1 | fix_mthly_overtime
	# CO_Key as Foreign Key of W_Comp_Type_*
	W_Comp_Type_2 = models.CharField(max_length=3) # Type of Salary Comp. 2 |"H"
	W_Comp_Name_2 = models.CharField(max_length=16) # Name of Salary Comp. 2 | "hourly_rate_OT_usd"
	W_Comp_Amnt_2 = models.DecimalField(max_digits=16, decimal_places=2) # Amnt of Salary Comp. 2 | hourly_rate_OT_usd
	# CO_Key as Foreign Key of W_Comp_Type_*
	W_Comp_Type_3 = models.CharField(max_length=3) # Type of Salary Comp. 3 |"M"
	W_Comp_Name_3 = models.CharField(max_length=16) # Name of Salary Comp. 3 | "owners_bonus"
	W_Comp_Amnt_3 = models.DecimalField(max_digits=16, decimal_places=2) # Amnt of Salary Comp. 3 | owners_bonus
	# CO_Key as Foreign Key of W_Comp_Type_*
	W_Comp_Type_4 = models.CharField(max_length=3) # Type of Salary Comp. 4 |"M"
	W_Comp_Name_4 = models.CharField(max_length=16) # Name of Salary Comp. 4 | "owners_nat"
	W_Comp_Amnt_4 = models.DecimalField(max_digits=16, decimal_places=2) # Amnt of Salary Comp. 4 | owners_nat
	# CO_Key as Foreign Key of W_Comp_Type_*
	W_Comp_Type_5 = models.CharField(max_length=3) # Type of Salary Comp. 5 |"M"
	W_Comp_Name_5 = models.CharField(max_length=16) # Name of Salary Comp. 5 | "increased_salary"
	W_Comp_Amnt_5 = models.DecimalField(max_digits=16, decimal_places=2) # Amnt of Salary Comp. 5 | increased_salary
	# CO_Key as Foreign Key of W_Comp_Type_*
	W_Comp_Type_6 = models.CharField(max_length=3) # Type of Salary Comp. 6 |"M"
	W_Comp_Name_6 = models.CharField(max_length=16) # Name of Salary Comp. 6 | "mthly_seniority_bonus"
	W_Comp_Amnt_6 = models.DecimalField(max_digits=16, decimal_places=2) # Amnt of Salary Comp. 6 | mthly_seniority_bonus
	# CO_Key as Foreign Key of W_Comp_Type_*
	W_Comp_Type_7 = models.CharField(max_length=3) # Type of Salary Comp. 7 |"D"
	W_Comp_Name_7 = models.CharField(max_length=16) # Name of Salary Comp. 7 | "cpt_port_daily"
	W_Comp_Amnt_7 = models.DecimalField(max_digits=16, decimal_places=2) # Amnt of Salary Comp. 7 | cpt_port_daily
	# CO_Key as Foreign Key of W_Comp_Type_*
	W_Comp_Type_8 = models.CharField(max_length=3) # Type of Salary Comp. 8 |"M" 
	W_Comp_Name_8 = models.CharField(max_length=16) # Name of Salary Comp. 8 | "mthly_extras_outside_contract"
	W_Comp_Amnt_8 = models.DecimalField(max_digits=16, decimal_places=2) # Amnt of Salary Comp. 8 | mthly_extras_outside_contract
	# CO_Key as Foreign Key of W_Comp_Type_*
	W_Comp_Type_9 = models.CharField(max_length=3) # Type of Salary Comp. 9 |"M"
	W_Comp_Name_9 = models.CharField(max_length=16) # Name of Salary Comp. 9 | "provident_fund"
	W_Comp_Amnt_9 = models.DecimalField(max_digits=16, decimal_places=2) # Amnt of Salary Comp. 9 | provident_fund
	# CO_Key as Foreign Key of W_Comp_Type_* 
	W_Comp_Type_10 = models.CharField(max_length=3) # Type of Salary Comp. 10 |"M"
	W_Comp_Name_10 = models.CharField(max_length=16) # Name of Salary Comp. 10 | "monthly_Sunday_allow"
	W_Comp_Amnt_10 = models.DecimalField(max_digits=16, decimal_places=2) # Amnt of Salary Comp. 10 | monthly_Sunday_allow
	# CO_Key as Foreign Key of W_Comp_Type_*
	W_Comp_Type_11 = models.CharField(max_length=3) # Type of Salary Comp. 11 |"M"
	W_Comp_Name_11 = models.CharField(max_length=16) # Name of Salary Comp. 11 | "monthly_supplementary_salary"
	W_Comp_Amnt_11 = models.DecimalField(max_digits=16, decimal_places=2) # Amnt of Salary Comp. 11 | monthly_supplementary_salary
	# CO_Key as Foreign Key of W_Comp_Type_*
	W_Comp_Type_12 = models.CharField(max_length=3) # Type of Salary Comp. 12 |"M"
	W_Comp_Name_12 = models.CharField(max_length=16) # Name of Salary Comp. 12 | "monthly_tanker_allow"
	W_Comp_Amnt_12 = models.DecimalField(max_digits=16, decimal_places=2) # Amnt of Salary Comp. 12 | monthly_tanker_allow
	# CO_Key as Foreign Key of W_Comp_Type_*
	W_Comp_Type_13 = models.CharField(max_length=3) # Type of Salary Comp. 13 |"M"
	W_Comp_Name_13 = models.CharField(max_length=16) # Name of Salary Comp. 13 | "monthly_gca_allow"
	W_Comp_Amnt_13 = models.DecimalField(max_digits=16, decimal_places=2) # Amnt of Salary Comp. 13 | monthly_gca_allow
	# CO_Key as Foreign Key of W_Comp_Type_*
	W_Comp_Type_14 = models.CharField(max_length=3) # Type of Salary Comp. 14 |"M"
	W_Comp_Name_14 = models.CharField(max_length=16) # Name of Salary Comp. 14 | "monthly_accum_leave_day"
	W_Comp_Amnt_14 = models.DecimalField(max_digits=16, decimal_places=2) # Amnt of Salary Comp. 14 | monthly_accum_leave_day
	# CO_Key as Foreign Key of W_Comp_Type_*	
	W_Comp_Type_15 = models.CharField(max_length=3) # Type of Salary Comp. 15 |"M"	
	W_Comp_Name_15 = models.CharField(max_length=16) # Name of Salary Comp. 15 | "monthly_leave_pay"
	W_Comp_Amnt_15 = models.DecimalField(max_digits=16, decimal_places=2) # Amnt of Salary Comp. 15 | monthly_leave_pay
	# CO_Key as Foreign Key of W_Comp_Type_*
	W_Comp_Type_16 = models.CharField(max_length=3) # Type of Salary Comp. 16 |"R"
	W_Comp_Name_16 = models.CharField(max_length=16) # Name of Salary Comp. 16 | "overtime_rate_1"
	W_Comp_Amnt_16 = models.DecimalField(max_digits=16, decimal_places=2) # Amnt of Salary Comp. 16 | overtime_rate_1
	# CO_Key as Foreign Key of W_Comp_Type_*
	W_Comp_Type_17 = models.CharField(max_length=3) # Type of Salary Comp. 17 |"R"
	W_Comp_Name_17 = models.CharField(max_length=16) # Name of Salary Comp. 17 | "overtime_rate_2"
	W_Comp_Amnt_17 = models.DecimalField(max_digits=16, decimal_places=2) # Amnt of Salary Comp. 17 | overtime_rate_2
	# CO_Key as Foreign Key of W_Comp_Type_*
	W_Comp_Type_18 = models.CharField(max_length=3) # Type of Salary Comp. 18 |"R"
	W_Comp_Name_18 = models.CharField(max_length=16) # Name of Salary Comp. 18 | "overtime_rate_holy"
	W_Comp_Amnt_18 = models.DecimalField(max_digits=16, decimal_places=2) # Amnt of Salary Comp. 18 | overtime_rate_holy
	# CO_Key as Foreign Key of W_Comp_Type_*
	W_Comp_Type_19 = models.CharField(max_length=3) # Type of Salary Comp. 19 |"M"
	W_Comp_Name_19 = models.CharField(max_length=16) # Name of Salary Comp. 19 | "bake_port_allow"
	W_Comp_Amnt_19 = models.DecimalField(max_digits=16, decimal_places=2) # Amnt of Salary Comp. 19 | bake_port_allow
	# CO_Key as Foreign Key of W_Comp_Type_*
	W_Comp_Type_20 = models.CharField(max_length=3) # Type of Salary Comp. 20 |"M"
	W_Comp_Name_20 = models.CharField(max_length=16) # Name of Salary Comp. 20 | "laundry_allow"
	W_Comp_Amnt_20 = models.DecimalField(max_digits=16, decimal_places=2) # Amnt of Salary Comp. 20 | laundry_allow
	# CO_Key as Foreign Key of W_Comp_Type_*
	W_Comp_Type_21 = models.CharField(max_length=3) # Type of Salary Comp. 21 |"M"
	W_Comp_Name_21 = models.CharField(max_length=16) # Name of Salary Comp. 21 | "cook_duties"
	W_Comp_Amnt_21 = models.DecimalField(max_digits=16, decimal_places=2) # Amnt of Salary Comp. 21 | cook_duties
	# CO_Key as Foreign Key of W_Comp_Type_*
	W_Comp_Type_22 = models.CharField(max_length=3) # Type of Salary Comp. 22 |"M"
	W_Comp_Name_22 = models.CharField(max_length=16) # Name of Salary Comp. 22 | "clean_defrost"
	W_Comp_Amnt_22 = models.DecimalField(max_digits=16, decimal_places=2) # Amnt of Salary Comp. 22 | clean_defrost
	# CO_Key as Foreign Key of W_Comp_Type_*
	W_Comp_Type_23 = models.CharField(max_length=3) # Type of Salary Comp. 23 |"M"
	W_Comp_Name_23 = models.CharField(max_length=16) # Name of Salary Comp. 23 | "Cpt_Port_Fixed"
	W_Comp_Amnt_23 = models.DecimalField(max_digits=16, decimal_places=2) # Amnt of Salary Comp. 23 | Cpt_Port_Fixed
	# CO_Key as Foreign Key of W_Comp_Type_*
	W_Comp_Type_24 = models.CharField(max_length=3) # Type of Salary Comp. 24 |"M"
	W_Comp_Name_24 = models.CharField(max_length=16) # Name of Salary Comp. 24
	W_Comp_Amnt_24 = models.DecimalField(max_digits=16, decimal_places=2) # Amnt of Salary Comp. 24
	W_Sen_1 = models.DecimalField(max_digits=8, decimal_places=2) # Amnt of Seniority bonus 1st year
	W_Sen_2 = models.DecimalField(max_digits=8, decimal_places=2) # Amnt of Seniority bonus 2nd year
	W_Sen_3 = models.DecimalField(max_digits=8, decimal_places=2) # Amnt of Seniority bonus 3rd year
	W_Sen_4 = models.DecimalField(max_digits=8, decimal_places=2) # Amnt of Seniority bonus 4th year
	W_Sen_5 = models.DecimalField(max_digits=8, decimal_places=2) # Amnt of Seniority bonus 5th year
	W_Sen_6 = models.DecimalField(max_digits=8, decimal_places=2) # Amnt of Seniority bonus 6th year
	W_Sen_7 = models.DecimalField(max_digits=8, decimal_places=2) # Amnt of Seniority bonus 7th year
	W_Sen_8 = models.DecimalField(max_digits=8, decimal_places=2) # Amnt of Seniority bonus 8th year
	W_Sen_9 = models.DecimalField(max_digits=8, decimal_places=2) # Amnt of Seniority bonus 9th year
	W_Sen_10 = models.DecimalField(max_digits=8, decimal_places=2) # Amnt of Seniority bonus 10th year
	W_Sen_11 = models.DecimalField(max_digits=8, decimal_places=2) # Amnt of Seniority bonus 11th year
	W_Sen_Rank_1 = models.DecimalField(max_digits=8, decimal_places=2) # Amnt of Seniority on rank 1st year
	W_Sen_Rank_2 = models.DecimalField(max_digits=8, decimal_places=2) # Amnt of Seniority on rank 2nd year
	W_Sen_Rank_3 = models.DecimalField(max_digits=8, decimal_places=2) # Amnt of Seniority on rank 3rd year
	W_Sen_Rank_4 = models.DecimalField(max_digits=8, decimal_places=2) # Amnt of Seniority on rank 4th year
	W_Sen_Rank_5 = models.DecimalField(max_digits=8, decimal_places=2) # Amnt of Seniority on rank 5th year
	W_Sen_Rank_6 = models.DecimalField(max_digits=8, decimal_places=2) # Amnt of Seniority on rank 6th year
	W_Sen_Rank_7 = models.DecimalField(max_digits=8, decimal_places=2) # Amnt of Seniority on rank 7th year
	W_Sen_Rank_8 = models.DecimalField(max_digits=8, decimal_places=2) # Amnt of Seniority on rank 8th year
	W_Sen_Rank_9 = models.DecimalField(max_digits=8, decimal_places=2) # Amnt of Seniority on rank 9th year
	W_Sen_Rank_10 = models.DecimalField(max_digits=8, decimal_places=2) # Amnt of Seniority on rank 10th year
	W_Sen_Rank_11 = models.DecimalField(max_digits=8, decimal_places=2) # Amnt of Seniority on rank 11th year
	W_Time_Last = models.DateTimeField() # Timestamp of last change
	W_Who_Last = models.DateTimeField() # Who did the last change

class COMPONENTS(models.Model):
	# 30 Rows
	# Foreign Keys = 'Component Scales'
	CO_D = models.CharField(max_length=1, null=True) # Delete Status (if D this record is deleted).
	CO_KEY = models.CharField(max_length=4) # ;Component Code (e.g. H for Hourly, or GOF for Greek Owner's Family)
	CO_Full = models.CharField(max_length=40) # Component Name (e.g. Monthly GCA Allow, or Greek Seaman's Home)
	CO_Full_GRK = models.CharField(max_length=40) # Component Name in Greek (for printouts)
	CO_CS_KEY = models.CharField(max_length=2) # Where should we use this component (XX for all scales)
	CO_Sort = models.IntegerField() # Sort Number
	CO_Table = models.CharField(max_length=1) # W(ages)/T(axes)
	CO_Skip = models.CharField(max_length=1) # Skip input Y/N - if yes only display
	CO_Taxable = models.CharField(max_length=1) # Y=taxable for earn. or non-taxable for contributions
	CO_Who_Pays = models.CharField(max_length=1) # (S)eaman's or (O)wner's for contributions
	CO_Is_Tax = models.CharField(max_length=1) # Is this comp. taxes only ?
	CO_Prt_Monthly = models.CharField(max_length=1) # Print in monthly form (N)o,(W)ages only,(E)arnings only,(D)eductions only
	CO_Prt_Contract_GCA = models.CharField(max_length=1) # (G)CA,(E)xtra or (N)one for printing in contracts
	CO_Prt_Payroll = models.CharField(max_length=1) # (N)o,(Y)es alone,(O)vertime sum,(P)ort sum
	CO_Prt_R_Payroll = models.CharField(max_length=1) # (N)o,(Y)es as it is,(O)vertime,(P)ort,N(A)T-PNO,(T)axes/stamp
	CO_Prt_Retro = models.CharField(max_length=1) # Print in retro form ? (N)o,(E)arnings,(D)eductions
	CO_Prt_Article = models.CharField(max_length=1) # Print in ship's article ? (Y/N)
	CO_Prt_Clone = models.CharField(max_length=1) # Print in clone report ? (Y/N)
	CO_Prt_Quest3 = models.CharField(max_length=1) # For future use
	CO_Prt_Quest4 = models.CharField(max_length=1) # For future use
	CO_Prt_Quest5 = models.CharField(max_length=1) # For future use
	CO_Mon_Amnt = models.CharField(max_length=20) # Monthly amount - number, AMNT which means the assoc. amnt, or subroutine name
	CO_Tot_Amnt = models.CharField(max_length=20) # Subtotal amount - number, AMNT which means the assoc. amnt, or subroutine name
	CO_Fld_Depend1 = models.CharField(max_length=20) # Name of the screen field component is depending (eg multiplier, months etc)
	CO_Fld_Depend2 = models.CharField(max_length=20) # Name of the screen field component is depending (days etc)
	CO_Fld_Change1 = models.CharField(max_length=20) # Name of the screen field the component must change
	CO_Fld_Change2 = models.CharField(max_length=20) # Name of the screen field the component must change
	CO_Fld_Special = models.CharField(max_length=80) # General propose field with special meaning for each component
	CO_Time_Last = models.DateTimeField() # Timestamp of last change
	CO_Who_Last = models.DateTimeField() # Who did the last change

class COMPONENT_SCALES(models.Model):
	# 5 Rows
	CS_D = models.CharField(max_length=1, null=True) # Delete Status (if D this record is deleted).
	CS_KEY = models.CharField(max_length=2) # Component Scale (e.g. F for Philippine)
	CS_Full = models.CharField(max_length=40) # Wage Scale Full Description (e.g. Philippine)
	CS_Time_Last = models.DateTimeField() # Timestamp of last change
	CS_Who_Last = models.DateTimeField() # Who did the last change

class MANNING_AGENT(models.Model):
	# 16 rows
	# Foreign Key = 'Officials'
	MAN_D = models.CharField(max_length=1, null=True) # Delete Status (if D this record is deleted).
	MAN_KEY = models.CharField(max_length=4) # Short Manning Agent Code
	MAN_Full = models.CharField(max_length=40) # Full Manning Agent Code
	MAN_Addr1 = models.CharField(max_length=32) # Address Line 1 of Manning Agent
	MAN_Addr2 = models.CharField(max_length=32) # Address Line 2 of Manning Agent
	MAN_Addr3 = models.CharField(max_length=32) # Address Line 3 of Manning Agent
	MAN_Addr4 = models.CharField(max_length=32) # Address Line 4 of Manning Agent
	MAN_LawCountry = models.CharField(max_length=32) # Law, City, Country of Manning Agent
	MAN_PhoneTelex = models.CharField(max_length=32) # Phone or Telex Number of Manning Agent
	MAN_W_Tax_Agnt = models.CharField(max_length=18) # Tax Agent
	MAN_TaxAccnt = models.CharField(max_length=20) # Tax Acct Number of Manning Agent
	MAN_SSS = models.CharField(max_length=16) # Social Security Number of Manning Agent
	MAN_AOH = models.CharField(max_length=32) # After Office Hours of Manning Agent
	# OF_KEY as foreign key of MAN_OF_KEY
	MAN_OF_KEY = models.CharField(max_length=4) # Current Signer for Manning Agent
	MAN_Time_Last = models.DateTimeField() # Timestamp of last change
	MAN_Who_Last = models.DateTimeField() # Who did the last change

class OFFICIAL_SIGNERS(models.Model):
	# 7 rows
	OF_D = models.CharField(max_length=1, null=True) # Delete Status (if D this record is deleted).
	OF_KEY = models.CharField(max_length=4) # Signers Code e.g. DACB
	OF_Full = models.CharField(max_length=24) # Signers Full Name
	OF_Position = models.CharField(max_length=16) # Signers Official Position/Title
	OF_TaxAcct = models.CharField(max_length=20) # Signers Tax Acct Number
	OF_Time_Last = models.DateTimeField() # Timestamp of last change
	OF_Who_Last = models.DateTimeField() # Who did the last change

class VESSELS(models.Model):
	# 34 rows
	# Foreign Keys = ['Vessel Type', 'Principal', 'vequip']
	V_D = models.CharField(max_length=1, null=True) # Delete Status (if D this record is deleted).
	V_KEY = models.CharField(max_length=4) # Short Vessel Code
	# VT_KEYS as foreign key of V_Type
	V_Type = models.CharField(max_length=4) # Vessel Type Code. OIL CHEM BULK
	V_Full = models.CharField(max_length=32) # Full Vessel Name
	# P_KEY as foreign key of V_P_Key
	V_P_KEY = models.CharField(max_length=6) # Principals of the Vessel
	V_Registry = models.CharField(max_length=12) # Country of Registry
	V_CN_KEY = models.CharField(max_length=2) # Flag
	V_RegNumber = models.CharField(max_length=16) # Official Registry Number
	V_GRT = models.IntegerField() # Vessels GRT | grt
	V_NRT = models.IntegerField() # Vessels NRT
	V_DWT = models.CharField(max_length=8) # Vessels DWT
	V_Engine = models.CharField(max_length=6) # Vessels Engine Type - Motor Steam
	V_HorsePower = models.CharField(max_length=8) # Vessels HorsePower
	V_Class = models.CharField(max_length=4) # Vessels Class Society e.g. ABS
	V_Yard = models.CharField(max_length=12) # Vessels Yard where built
	V_YearBuilt = models.IntegerField() # Vessels Year Built
	V_Trades = models.CharField(max_length=16) # Vessels Trading Route: WorldWide
	V_UMS = models.CharField(max_length=1) # Vessel works as UMS or not Y/N
	V_CallSign = models.CharField(max_length=6) # Call Sign
	V_Owner_Ship = models.CharField(max_length=45) # Owner Ship
	V_IMO = models.CharField(max_length=12) # IMO Number
	V_Status = models.CharField(max_length=1) # Vessel Status (M)anaged (N)ot
	V_End = models.DateTimeField() # Date Management Ended
	V_Main_Cat = models.CharField(max_length=1) # Main Category (T)anker (B)ulk etc
	# VE_KEYS as foreign key of V_Equip_1
	V_Equip_1 = models.CharField(max_length=1) # Main Category (T)anker (B)ulk etc
	# VE_KEYS as foreign key of V_Equip_2
	V_Equip_2 = models.CharField(max_length=1) # Main Category (T)anker (B)ulk etc
	# VE_KEYS as foreign key of V_Equip_3
	V_Equip_3 = models.CharField(max_length=1) # Main Category (T)anker (B)ulk etc
	# VE_KEYS as foreign key of V_Equip_4
	V_Equip_4 = models.CharField(max_length=1) # Main Category (T)anker (B)ulk etc
	#29 -32
	V_TFS_Fleet = models.CharField(max_length=1) # The File System Fleet Code
	V_TFS_Ship = models.CharField(max_length=4) # The File System Ship Code
	V_Email_1 = models.CharField(max_length=28) # Email Address 1
	V_Email_2 = models.CharField(max_length=28) # Email Address 2
	V_Time_Last = models.DateTimeField() # Timestamp of last change
	V_Who_Last = models.DateTimeField() # Who did the last change

class VESSEL_CATEGORIES(models.Model):
	# 5 rows
	VC_D = models.CharField(max_length=1, null=True) # Delete Status (if D this record is deleted).
	VC_KEY = models.CharField(max_length=4) # Vessel Category Code
	VC_Full = models.CharField(max_length=26) # Description of Vessel Category
	VC_Time_Last = models.DateTimeField() # Timestamp of last change
	VC_Who_Last = models.DateTimeField() # Who did the last change

class VESSEL_TYPE(models.Model):
	# 5 rows
	VT_D = models.CharField(max_length=1, null=True) # Delete Status (if D this record is deleted).
	VT_KEY = models.CharField(max_length=4) # Short Vessel Type Code
	VT_Full = models.CharField(max_length=16) # Description of Vessel Type Code
	VT_Time_Last = models.DateTimeField() # Timestamp of last change
	VT_Who_Last = models.DateTimeField() # Who did the last change