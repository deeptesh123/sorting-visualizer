import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import copy
import styling as s
class Sorting_algorithms:
    def __init__(self,n):
        self.size=n
        self.lst=self.create_list()
        self.x=self.create_x()
        self.color_list=self.create_color_list()
    def create_color_list(self):
        return ["white"]*self.size
    def create_x(self):
        return [i+1 for i in range(self.size)]
    def create_list(self):
        l=[]
        for i in range(self.size): l.append(random.randint(5,30))
        return l
    def plot_design(self,ax):
            ax.set_facecolor("#213644")
            ax.spines["top"].set_visible(False)
            ax.spines["right"].set_visible(False)
            ax.spines["left"].set_visible(False)
            ax.spines["bottom"].set_visible(False)
            ax.set_xticks([])
            ax.set_yticks([])
    def final(self,l):
        for i in range(self.size):
            new_color_list=copy.deepcopy(self.color_list)
            if i==self.size-1:
                for j in range(self.size): new_color_list[j]="green"
            else:new_color_list[i]="green"
            ax=plt.axes()
            self.plot_design(ax)
            plt.bar(self.x,l,color=new_color_list)
            plt.pause(0.1)
            plt.clf()
        ax=plt.axes()
        self.plot_design(ax)
        plt.bar(self.x,l,color=self.color_list)
        plt.show(block=False)
    def bubble_sort(self):
        l=copy.deepcopy(self.lst)
        for i in range(len(l)):
            for j in range(0,len(l)-i-1):
                new_color_list=copy.deepcopy(self.color_list)
                new_color_list[j],new_color_list[j+1]='red','red'
                ax=plt.axes()
                self.plot_design(ax)
                plt.bar(self.x,l,color=new_color_list)
                plt.pause(0.0001)
                plt.clf()
                if l[j]>l[j+1]: l[j],l[j+1]=l[j+1],l[j]
        self.final(l)
    def insertion_sort(self):
        l=copy.deepcopy(self.lst)
        for i in range(self.size):
            temp=l[i]
            j=i-1
            while(j>=0 and l[j]>temp):
                new_color_list=copy.deepcopy(self.color_list)
                new_color_list[j],new_color_list[i]='red','red'
                ax=plt.axes()
                self.plot_design(ax)
                plt.bar(self.x,l,color=new_color_list)
                plt.pause(0.1)
                plt.clf()
                l[j+1]=l[j]
                j-=1
            l[j+1]=temp
        self.final(l)
    def selection_sort(self):
        l=copy.deepcopy(self.lst)
        for i in range(self.size-1):
            idx=i
            for j in range(i+1,self.size):
                new_color_list=copy.deepcopy(self.color_list)
                new_color_list[j],new_color_list[i]='red','red'
                ax=plt.axes()
                self.plot_design(ax)
                plt.bar(self.x,l,color=new_color_list)
                plt.pause(0.1)
                plt.clf()
                if l[j]<l[idx]:
                    idx=j
            if idx!=i: l[idx],l[i]=l[i],l[idx]
        self.final(l)
    def partition(self,l,low,high):
        left,right=low,high
        temp=copy.deepcopy(self.color_list)
        temp[left],temp[right]="blue","blue"
        while(left<right):
            while(l[left]<=l[low] and left<high):
                new_color_list=copy.deepcopy(temp)
                left+=1
                new_color_list[left]="red"
                ax=plt.axes()
                self.plot_design(ax)
                plt.bar(self.x,l,color=new_color_list)
                plt.pause(0.1)
                plt.clf()
            while(l[right]>l[low] and right>low):
                new_color_list=copy.deepcopy(temp )
                right-=1
                new_color_list[right]="red"
                ax=plt.axes()
                self.plot_design(ax)
                plt.bar(self.x,l,color=new_color_list)
                plt.pause(0.1)
                plt.clf()
            if left<right: l[left],l[right]=l[right],l[left]
        l[low],l[right]=l[right],l[low]
        return right
    def quick_sort(self):
        l=copy.deepcopy(self.lst)
        self.qs(l,0,self.size-1)
        self.final(l)
    def qs(self,l,low,high):
        if(low<high):
            pivot=self.partition(l,low,high)
            self.qs(l,low,pivot-1)
            self.qs(l,pivot+1,high)
    def merge_sort(self):
        pass
    def radix_sort(self):
        pass
class GUI:
    def __init__(self,SA):
        self.root=tk.Tk()
        self.root.title("Algorithm Visualizer")
        self.root.configure(background="#213644")
        self.sa=SA
    def randomz(self):
        self.sa.size=slider.get()
        self.sa.lst=self.sa.create_list()
        self.sa.x=self.sa.create_x()
        self.sa.color_list=self.sa.create_color_list()
        self.plot()
    def plot(self):
        l=copy.deepcopy(self.sa.lst)
        ax1.clear()
        self.canvas.flush_events()
        ax1.bar(self.sa.x,l,color=self.sa.color_list,width=0.8,edgecolor="white")
        ax1.set_facecolor("#213644")
        for i in range(len(l)):
            ax1.text(i+1,l[i],l[i],ha="center",va="bottom",size=10)
        self.canvas.draw_idle()
    def initialize(self):
    # initilaize plot
        title_frame=tk.Frame(self.root,bg="#213644",highlightbackground="green",highlightthickness=1)
        body_frame=tk.Frame(self.root,bg="#213644",highlightbackground="white",highlightthickness=1)
        button_frame=tk.Frame(body_frame,bg="#213644",highlightbackground="red",highlightthickness=1)
        graph_frame=tk.Frame(body_frame,bg="#213644",highlightbackground="red",highlightthickness=1)
        graph_setting_frame=tk.Frame(graph_frame,bg="#213644")
        global ax1
        fig,ax1=plt.subplots()
        fig.set_facecolor("#213644")
        fig.set_figheight(5)
        fig.set_figwidth(16)
        self.sa.plot_design(ax1)
        self.canvas=FigureCanvasTkAgg(fig,graph_frame)
        self.canvas.get_tk_widget().grid(row=1,column=0)
        self.plot()
    #initialize GUI
        title=tk.PhotoImage(name="TITLE",file="title.png")
        head=tk.Label(title_frame,image=title,borderwidth=0)
        head.grid(row=0,column=0)
        bs=tk.PhotoImage(name="but1",file="bubble_sort.png")
        bubble=tk.Button(button_frame,image=bs,command=self.sa.bubble_sort,borderwidth=0)
        ins=tk.PhotoImage(name="but2",file="ins1.png")
        insertion=tk.Button(button_frame,image=ins,command=self.sa.insertion_sort,borderwidth=0)
        qs=tk.PhotoImage(name="but3",file="quick_sort.png")
        quick=tk.Button(button_frame,image=qs,command=self.sa.quick_sort,borderwidth=0)
        ms=tk.PhotoImage(name="but4",file="merge_sort.png")
        merge=tk.Button(button_frame,image=ms,command=self.sa.merge_sort,borderwidth=0)
        ss=tk.PhotoImage(name="but5",file="selection_sort.png")
        selection=tk.Button(button_frame,image=ss,command=self.sa.selection_sort,borderwidth=0)
        rs=tk.PhotoImage(name="but6",file="radix_sort.png")
        radix=tk.Button(button_frame,image=rs,command=self.sa.radix_sort,borderwidth=0)
        rndm=tk.PhotoImage(name="but7",file="randomize.png")
        rr=tk.Button(graph_setting_frame,image=rndm,command=self.randomz,borderwidth=0)
        global slider
        slider=tk.Scale(graph_setting_frame,from_=5,to=30,orient="horizontal",width=50,length=500)
        slider.set(20)
        button_frame.grid(row=0,column=0)
        graph_frame.grid(row=0,column=1)
        title_frame.grid(row=0,column=0)
        body_frame.grid(row=1,column=0)
        graph_setting_frame.grid(row=0,column=0)
        bubble.grid(row=0,column=0,pady=10)
        insertion.grid(row=1,column=0,pady=20)
        quick.grid(row=2,column=0,pady=20)
        merge.grid(row=3,column=0,pady=20)
        selection.grid(row=4,column=0,pady=20)
        radix.grid(row=5,column=0,pady=20)
        rr.grid(row=0,column=0,padx=50)
        slider.grid(row=0,column=1,padx=50)
        self.root.mainloop()
sorting=Sorting_algorithms(10)
gui=GUI(sorting)
gui.initialize()

