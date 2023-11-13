import pandas as pd
data={'employee_ID':[102,101,101,201,114,122,200,176,176,200],
 'Start_date':['13-01-2001','21-09-1997','28-10-2001','17-02-2004',
 '24-03-2006','01-01-2007','17-09-1995','24-03-2006','01-01-2007','01-07-2002'],
 'End_date':['24-07-2006','27-10-2001','15-03-2005','19-12-2007','31-12-2007','31-12-2007','17-06-2001','31-12-2006','31-12-2007','31-12-2006'],
 'Job_ID':['IT_PROG','AC_ACCOUNT','AC_MGR','MK_REP','ST_CLER','ST_CLERK','AD_ASST','SA_REP','SA_MAN','AC_ACCOUNT'],
 'Department_ID':[60,110,110,20,50,50,90,80,80,90]
}
df=pd.DataFrame(data)
data2=df['employee_ID'].value_counts()
print(data2[data2>1])
