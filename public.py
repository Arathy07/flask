from flask import *
from database import *
public=Blueprint('public',__name__)

@public.route('/')
def home():
    return render_template("home.html")


@public.route('/login')
def login():
    return render_template("login.html")

@public.route('/registration',methods=['get','post'])
def registration():
    data={}
    qry5="select * from registration"
    data['user']=select(qry5)
    if 'reg' in request.form:
        fn=request.form['fname']
        ln=request.form['lname']
        add=request.form['address']
        phnum=request.form['phone']
        mail=request.form['email']
        un=request.form['uname']
        passw=request.form['pw']    

        qry="insert into login values(null,'%s','%s','user')"%(un,passw)
        loginid=insert(qry)

        qry1="insert into registration values(null,'%s','%s','%s','%s','%s','%s')"%(loginid,fn,ln,add,phnum,mail)
        insert(qry1)
        # return '''<script>alert("Registartion successfull");window.locatioin="/login"</script>'''
        return redirect(url_for('public.registration'))
    
    if 'action'in request.args:
        action=request.args['action']
        id=request.args['id']


        if action=='delete':
            qry2="delete from registration where regid='%s'"%(id)
            delete(qry2)
            # return '''<script>alert("Delection successfull");window.locatioin="/registration"</script>'''
        
        if action=='update':
            qry4="select * from registration where regid='%s'"%(id)
            data['up']=select(qry4)

            if 'update' in request.form:
                fn=request.form['fname']
                ln=request.form['lname']
                add=request.form['address']
                phnum=request.form['phone']
                mail=request.form['email']


                q="update registration set firstname='%s',lastname='%s',address='%s',phone_no='%s',email='%s' where regid='%s'"%(fn,ln,add,phnum,mail,id)
                update(q)
        


    





    return render_template("registration.html",data=data)