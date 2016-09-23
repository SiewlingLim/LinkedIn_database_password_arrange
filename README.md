# Linkedin_database_password_arrange-

##What's this?
linkdedIn database combine password with mails    
look like:  
```
update idemail set idemail.password = mails.password where idemail.mail = mails.mail;
```
My MySQL was boom，so just use it. 

#table mails:
```
mysql> select * from mails where flag = 1 limit 0,7;
+---------------------------------+------------------------------------------+------+
| mail                            | password                                 | flag |
+---------------------------------+------------------------------------------+------+
| mnaderi@gmail.com               | 043bab64ffa7cba2dfeddc20a376ba1cab279225 |    1 |
| edgar@casarealtyinvestments.com | a22d86b4ca2e489f67bf083e623a2558f1eb2a31 |    1 |
| blkankh@gmail.com               | 0be150f6e0b05e5e8135130bbef021c46ce3d089 |    1 |
| scporfirio@hotmail.com          | b4b99d86e27d43e3740f7167a5c5b59cda044d73 |    1 |
| charlesmfeldman@aol.com         | 15acb58ea5737e06a1a40953575d0b6fbdbd78ba |    1 |
| wzrdofgz@gmail.com              | 47d4d399df36393755181d1095b548461a3e3096 |    1 |
| awaneeshpande@yahoo.com         | 0644bf09114451f6d11026728442ebbdcdb015f3 |    1 |
+---------------------------------+------------------------------------------+------+
```
#table idemail 
##Before
```
mysql> select * from idemail  limit 0,7;
+-----------+-------------------------------+----------+
| MEMBER_ID | mail                          | password |
+-----------+-------------------------------+----------+
| 59305718  | shownuff00@yahoo.com          | NULL     |
| 59287478  | francescoseccia@hotmail.com   | NULL     |
| 97148     | paulcohenlaw@gmail.com        | NULL     |
| 35238529  | david.martinez_01@hotmail.com | NULL     |
| 12878445  | sodanoa@libero.it             | NULL     |
| 59321231  | boyhoxiy@hotmail.com          | NULL     |
| 59447600  | talp105@soton.ac.uk           | NULL     |
+-----------+-------------------------------+----------+
```
##After
```
mysql> SELECT MEMBER_ID,mail,`password` FROM idemail WHERE mail in (select mail from (SELECT * from mails limit 0,7 ) as t );
+-----------+---------------------------------+------------------------------------------+
| MEMBER_ID | mail                            | password                                 |
+-----------+---------------------------------+------------------------------------------+
| 10864015  | mnaderi@gmail.com               | 043bab64ffa7cba2dfeddc20a376ba1cab279225 |
| 16160033  | edgar@casarealtyinvestments.com | a22d86b4ca2e489f67bf083e623a2558f1eb2a31 |
| 13378048  | blkankh@gmail.com               | 0be150f6e0b05e5e8135130bbef021c46ce3d089 |
| 10400583  | scporfirio@hotmail.com          | b4b99d86e27d43e3740f7167a5c5b59cda044d73 |
| 17601286  | charlesmfeldman@aol.com         | 15acb58ea5737e06a1a40953575d0b6fbdbd78ba |
| 12500353  | wzrdofgz@gmail.com              | 47d4d399df36393755181d1095b548461a3e3096 |
| 10811079  | awaneeshpande@yahoo.com         | 0644bf09114451f6d11026728442ebbdcdb015f3 |
+-----------+---------------------------------+------------------------------------------+
```
#About author

```javascript
  var about = {
    nickName  : "DragonEgg",
    site : "I forget"
  }
```
