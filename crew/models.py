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
	R_Officer = models.CharField(max_length=1) # Officer/Crew
	R_Time_Last = models.DateTimeField() # Timestamp of last change
	R_Who_Last = models.CharField(max_length=4) # Who did the last change

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
	# CN_KEY as Foreign Key to D_OtherCountry
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
	# 45 rows
	# Foreign Keys = ['Manning Agent', 'Principal', 'Wage']
	CON_D = models.CharField(max_length=1, null=True) # Delete Status (if D this record is deleted)self.
	# 1-3
	CON_Number = models.IntegerField() # Contract Number
	CON_B_ID = models.CharField(max_length=4) # Seaman ID
	CON_W_CS_KEY = models.CharField(max_length=2) # Wages Scale
	CON_T_CS_KEY = models.CharField(max_length=2) # Taxes Scale
	# Prin_P_KEY as foreign key of CON_Prin_P_KEY
	CON_Prin_P_KEY = models.CharField(max_length=6) # Principals Code
	# Master_P_KEY as foreign key of CON_Master_P_KEY
	CON_Master_P_KEY = models.CharField(max_length=6) # Master Official POEA Principal
	# W_REC as foreign key of CON_Wage_W_REC
	CON_Wage_W_REC = models.DecimalField(max_digits=8, decimal_places=2)
	# V_KEY as foreign key of CON_Vsl_V_KEY
	CON_Vsl_V_KEY = models.CharField(max_length=4) # Vessel Code
	# R_KEY as foreign key of CON_Rank_R_KEY
	CON_Rank_R_KEY = models.CharField(max_length=4) # Rank
	CON_Crew_Category = models.CharField(max_length=1) #C(rew)/T(rainee)
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
	# CN_KEY as foreign key of V_CN_Key
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

class VESSEL_TYPE(models.Model):
	# 5 rows
	VT_D = models.CharField(max_length=1, null=True) # Delete Status (if D this record is deleted).
	VT_KEY = models.CharField(max_length=4) # Short Vessel Type Code
	VT_Full = models.CharField(max_length=16) # Description of Vessel Type Code
	VT_Time_Last = models.DateTimeField() # Timestamp of last change
	VT_Who_Last = models.DateTimeField() # Who did the last change