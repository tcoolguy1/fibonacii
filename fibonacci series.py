from tkinter import*
root = Tk()
root.title("Fibonacci")
root.geometry("500x500")
label_series = Label(root,text="fibonacci series")
label_flower = Label(root)
label_spiral = Label(root)
def Fibonacci():
    first_no = 0
    second_no = 1
    num = 11
    sum = 0
    counter = 1
    while(counter<=num):
        label_series["text"] += str(sum) +""
        counter = counter+1
        first_no = second_no
        second_no = sum
        sum = second_no + first_no
        label_flower["text"] = "flower is still blooming"
        label_spiral["text"] = "spirals in right direction are" + str(first_no) +"spiral in left direction are" +str(second_no) + "total spiral are" + str(sum)
btn = Button(root, text = "Show fibonacci series", command = Fibonacci) 
btn.pack()
label_flower.pack()
label_spiral.pack()
label_series.pack()

root.mainloop()


