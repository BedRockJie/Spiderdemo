from tkinter import *
from tkinter import messagebox
import requests
import re
from PIL import Image,ImageTk
def sign():
    name = entry.get()
    name.strip()
    if name == '':
        messagebox.showinfo('提示',message='请输入姓名!!')
    else:
        date = {
            'id':name,
            'zhenbi':2019123,
            'id1': 901,
            'id2': 15,
            'id3':  '#000000',
            'id5':  '#FFFFFF',
        }
        url = 'http://www.jiqie.com/a/re14.php'
        response = requests.post(url,date).text
       # print(response)
        #img = response.xpath('//img/src/text()').extract()
        img = re.findall('(http.*?)"',response)[0]
       # print(img)
       #  return img
        picture = requests.get(img).content
        # print()
        with open('{}.jpg'.format(name),'wb') as f:
            f.write(picture)

        bm = ImageTk.PhotoImage(file='{}.jpg'.format(name))

        label2 = Label(root,image=bm)
        label2.bm = bm
        label2.grid(row=2,columnspan=2)
        #print(response)


#创建一个窗口
root = Tk()
#设置大小
root.geometry("789x681+643+245")
root.title("签名设计")
# root.iconphoto()
lable = Label(root,text = '签名',font=('华文行楷',20))
lable.grid()

entry = Entry(root,font=("微软雅黑",20))
entry.grid(row=0,column=1)

button = Button(root,text="设计签名",font=("微软雅黑",20),command=sign)
button.grid(row=1,column=1)

root.mainloop()