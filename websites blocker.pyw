from tkinter import *
root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("GUI FORCED - Website Blocker@79")
Label(root, text ='GUI FORCED - Website Blocker@79' , font ='CASTELLER 16 bold').pack()
host_path ='C:\Windows\System32\drivers\etc\hosts'
ip_address = '127.0.0.1'
Label(root, text ='Enter the Website :' , font ='TimesNewRoman 11 bold').place(x=5 ,y=60)
Websites = Text(root,font = 'TimesNewRoman 10',height='2', width = '40')
Websites.place(x= 140,y = 60)

def Blocker():
    website_lists = Websites.get(1.0,END)
    Website = list(website_lists.split(","))
    with open (host_path , 'r+') as host_file:
        file_content = host_file.read()
        for web in Website:
            if web in file_content:
                Label(root, text = 'Already  Blocked  Site - sorry!' , font = 'contour 12 bold').place(x=173,y=200)
                pass
            else:
                host_file.write(ip_address + " " + web + '\n')
                Label(root, text = "Blocked! - Permission Denied", font = 'Constantia 10 bold').place(x=170,y =200)

block = Button(root, text = 'Block',font = 'ALGERIAN 10 ',pady = 5,command = Blocker ,width = 6, bg = 'red', activebackground = 'Yellow')
block.place(x = 230, y = 150)
root.mainloop()

