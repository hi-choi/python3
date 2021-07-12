class EMP:
    def __init__(self, empno, lname, fname, email, phone, hdate,
                 jobid='', sal='', comm='', mgr='', deptid=''):
        self.__empno = empno
        self.__lname = lname
        self.__fname = fname
        self.__email = email
        self.__phone = phone
        self.__hdate = hdate
        self.__jobid = jobid
        self.__sal = sal
        self.__comm = comm
        self.__mgr = mgr
        self.__deptid = deptid

    def __str__(self):
        result = f'{self.__empno} {self.__lname} {self.__fname} {self.__email} {self.__phone} {self.__hdate}' \
                 f'{self.__jobid} {self.__sal} {self.__comm} {self.__mgr} {self.__deptid}'
        return result

    @property
    def empno(self):
        return self.__empno

    @empno.setter
    def empno(self,empno):
        self.__empno

    @property
    def lname(self):
        return self.__lname

    @lname.setter
    def lname(self, lname):
        self.__lname

    @property
    def fname(self):
        return self.__fname

    @fname.setter
    def fname(self, fname):
        self.__fname

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone

    @property
    def hdate(self):
        return self.__hdate

    @hdate.setter
    def hdate(self, hdate):
        self.__hdate

    @property
    def jobid(self):
        return self.__jobid

    @jobid.setter
    def jobid(self, jobid):
        self.__jobid

    @property
    def sal(self):
        return self.__sal

    @sal.setter
    def sal(self, sal):
        self.__sal

    @property
    def comm(self):
        return self.__comm

    @comm.setter
    def comm(self, comm):
        self.__comm

    @property
    def mgr(self):
        return self.__mgr

    @mgr.setter
    def empno(self, mgr):
        self.__mgr


    @property
    def deptid(self,deptid):
        return self.__deptid

    @deptid.setter
    def deptid(self, deptid):
        self.__deptid