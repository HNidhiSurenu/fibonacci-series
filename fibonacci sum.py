from tkinter import*
root=Tk()
root.title("fibonacci project")
root.geometry("400x400")
root.configure(background="light green")
enter_num=Entry(root)
enter_num.place(relx=0.5, rely=0.1, anchor=CENTER)
label_series=Label(root, text="fibonacci series:")
label_sum=Label(root, text="fibonacci sum:")
def fibonacci():
    first_no=0
    second_no=1
    sum=0
    sum2=0
    i=1
    n=enter_num.get()
    while(i<=int(n)):
        label_series["text"] += str(sum) + " "
        i=i+1
        first_no=second_no
        second_no=sum
        sum=first_no + second_no
        sum2=sum2+sum
        label_sum["text"]= str(sum2)
        
btn=Button(root, text="generate fibonacci series", command=fibonacci)
btn.place(relx=0.5, rely=0.2, anchor=CENTER)
label_series.place(relx=0.5, rely=0.3, anchor=CENTER)
label_sum.place(relx=0.5, rely=0.4, anchor=CENTER)
root.mainloop()