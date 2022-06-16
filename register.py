import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
import mysql.connector
main_window = tk.Tk()
gender =tk.StringVar()
read = tk.IntVar()
write = tk.IntVar()
singing = tk.IntVar()


label_username = ttk.Label(main_window,text="User Name:")
label_username.grid(row=0,column=0)
text_username =ttk.Entry(width=200)
text_username.grid(row=0,column=1)
label_age = ttk.Label(text="Age:")
label_age.grid(row=1,column=0)
text_age =ttk.Entry(width=200)
text_age.grid(row=1,column=1)
label_phone = ttk.Label(text="Phone:")
label_phone.grid(row=2,column=0)
text_phone =ttk.Entry(width=200)
text_phone.grid(row=2,column=1)
label_gender=ttk.Label(text="Gender")
label_gender.grid(row=3,column=0)
radio_gender_male=ttk.Radiobutton(main_window,text="Male",variable=gender,value="male")
radio_gender_female=ttk.Radiobutton(main_window,text="Female",variable=gender,value="female")
radio_gender_male.grid(row=4,column=0)
radio_gender_female.grid(row=4,column=1)
user_hobbies=""
label_hobbies = ttk.Label(main_window,text="Hobbies").grid(row=5,column=0)
checkbox_read = tk.Checkbutton(main_window, text="Read",variable=read).grid(row=6, column=0)
checkbox_write = tk.Checkbutton(main_window, text="Write",variable=write).grid(row=6, column=1)
checkbox_sing = tk.Checkbutton(main_window, text="Singe",variable=singing).grid(row=6, column=2,sticky="W")
def submit():
    user_name =text_username.get()
    user_age  =text_age.get()
    user_phone=text_phone.get()
    gender_status=gender.get()
    if(read.get()==1):
        user_hobbies="read,"
    if(write.get()==1):
        user_hobbies+="write,"
    if(singing.get()==1):
        user_hobbies+="singing"

    try:
            mysql_connection = mysql.connector.connect(host="localhost",user="hithinpythone",password="hithin",database="hithinpythone")
            mysql_cursor = mysql_connection.cursor()
            mysql_query="insert into employee (name,age,phone,gender,hobbies) values('{0}','{1}','{2}','{3}','{4}')".format(user_name,user_age,user_phone,gender_status,user_hobbies)
            mysql_cursor.execute(mysql_query)
            mysql_connection.commit()
            if(mysql_cursor.rowcount):
                tk.messagebox.showinfo(title="Status",message="Employee Added")
                main_window.option_clear()
                text_username.delete(0,tk.END)
                text_phone.delete(0,tk.END)
                text_age.delete(0,tk.END)
                
    except:
            print("Error")

submit_button=ttk.Button(main_window,name="save",text="SAVE",command=submit)
submit_button.grid(row=10,column=0)

main_window.mainloop()