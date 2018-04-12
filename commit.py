import cx_Oracle
Connect= 'SCMSVN/coo1r3p0$@(DESCRIPTION=(ADDRESS_LIST=(LOAD_BALANCE=ON)(FAILOVER=ON)(ADDRESS=(PROTOCOL=TCP)(HOST=dbgen-prd1-12-vip.cisco.com)(PORT=1522))(ADDRESS=(PROTOCOL=TCP)(HOST=dbgen-prd1-13-vip.cisco.com)(PORT=1522)))(CONNECT_DATA=(SERVICE_NAME=MIGPRD.cisco.com)(SERVER=DEDICATED)))'
db = cx_Oracle.connect(Connect)
print("connected")
print(db.version)
gid=str(input("please give the group id\n"))
aid=str(input("please give the artifact id\n"))
#gid = 'it.cvc.ciscocommerce.b2bcatalog.b2bcatalog'
#aid = 'b2bcatalog/jbosseap-6'
cur=db.cursor()
#def fun(gid):
query = "select * from artifact_request where upper(TEAM_NAME) LIKE upper(:gid) or upper(PROJECT_NAME) like upper (:aid) "
cur.execute(query, {'gid':gid, 'aid' :aid })
data= cur.fetchall()
print(data)
  
#fun(gid)

db.close()







