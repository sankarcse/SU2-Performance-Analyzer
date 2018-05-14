###importing
import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg
from tkinter import Spinbox
from time import  sleep
from tkinter import Menu
from tkinter import filedialog
import os
import subprocess
import os,sys
win=tk.Tk()#creating main window

win.title("simple addition")

win.minsize(700,700)

win.resizable(False,False)



#creating menubar
menu_bar=Menu(win)
win.config(menu=menu_bar)
def Openfile():
	filename =filedialog.askopenfilename()
	#print("path"+filename)
	str1=str(filename)
	"""#print(str1)
	lst=list(filename)
	print(type(lst))
	l=len(lst)
	for i in range(0,l-1):
		if lst[i]==" ":
			lst.insert(i,'\')
	str2=str(lst)
	print(str2)"""
	os.system("gedit "+str1)


file_menu=Menu(menu_bar,tearoff=0)
file_menu.add_command(label="Openfile",command=Openfile)
menu_bar.add_cascade(label="File",menu=file_menu,activebackground="orange")


"""solve_file MENU ITEM"""

#creating menu and menu items RUNNING SU2_CFD 
def Solvefile():
	""" What to do when the Browse button is pressed """
	filename =filedialog.askopenfilename()
	#os.system()
	#print(filename)
	filename=str(filename)
	string = "".join(reversed(filename))
	l=len(string)
	str1=""
	for i in range(0,l-1):
		if string[i]=="/":
			break
		else:
			str1=string[i]+str1
			
	print(str1)
	#print(string)
	fi="./SU2_CFD "+str1
	os.system(fi)
		
#adding solve menu in menubar
solver_menu=Menu(menu_bar,tearoff=0)
solver_menu.add_command(label="solve parallelly",command=Solvefile)
def Solvefilep():
	""" What to do when the Browse button is pressed """
	filename =filedialog.askopenfilename()
	#os.system()
	#print(filename)
	filename=str(filename)
	string = "".join(reversed(filename))
	l=len(string)
	str1=""
	for i in range(0,l-1):
		if string[i]=="/":
			break
		else:
			str1=string[i]+str1
			
	print(str1)
	#print(string)
	fi="mpirun -np 3 ./SU2_CFD "+str1
	os.system(fi)

solver_menu.add_command(label="solve serially",command=Solvefilep)
menu_bar.add_cascade(label="run_tool",menu=solver_menu,activebackground="white")
		
def plotting_fun():
	#os.system("export ETS_TOOLKIT=wx")
	os.system("python pavani.py")#export ETS_TOOLKIT=wx &&

#adding plot menu in menubar
ploter_menu=Menu(menu_bar,tearoff=0)
ploter_menu.add_command(label="plot_File",command=plotting_fun)
menu_bar.add_cascade(label="plot_tool",menu=ploter_menu,activebackground="green")

##adding functionalities



#Creating tabs
tabControl = ttk.Notebook(win)

tab0 = ttk.Frame(tabControl)
tabControl.add(tab0,text='SU2 build options')
tabControl.pack(expand=1, fill="both")

tab1 = ttk.Frame(tabControl)
tabControl.add(tab1,text='Tab1')
tabControl.pack(expand=1, fill="both")

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2,text='Tab2')
tabControl.pack(expand=1, fill="both")

tab3 =ttk.Frame(tabControl)
tabControl.add(tab3,text='Tab3')
tabControl.pack(expand=1,fill="both")

###TAB0
###cleaning previous build
frame1000=ttk.LabelFrame(tab0,text='CLEANING PREVIOUS SU2 SOURCE CODE BUILDS')
frame1000.grid(column=0,row=10,sticky=tk.W)

def cleaning():
	out=subprocess.getoutput("cd locate SU2-6.0.0 | grep /SU2-6.0.0$")
	
	os.system("make clean")

button10001 = tk.Button(frame1000, text='CLEAN BUILD', command=cleaning)
button10001.grid(column=2, row=2, sticky=tk.W)

###building su2 source code serially
frame2000=ttk.LabelFrame(tab0,text='BUILDING SU2 SOURCE CODE SERIALLY')
frame2000.grid(column=0,row=20,sticky=tk.W)

def simplebuild():
	out=subprocess.getoutput("locate SU2-6.0.0 | grep /SU2-6.0.0$")
	print(out)
	os.system("./configre --prefix=locate SU2-6.0.0 | grep /SU2-6.0.0$")
	os.system("make")
	os.system("make install")
	os.system("make -j 4 install")


button20001 = tk.Button(frame2000, text='BUILD SERIALLY', command=simplebuild)
button20001.grid(column=2, row=2, sticky=tk.W)


###building su2 source code paralelly
frame3000=ttk.LabelFrame(tab0,text='BUILDING SU2 SOURCE CODE PARALLELY')
frame3000.grid(column=0,row=30,sticky=tk.W)

def parallelbuild():
	out=subprocess.getoutput("cd locate SU2-6.0.0 | grep /SU2-6.0.0$")
	#os.system("cd locate SU2-6.0.0 | grep /SU2-6.0.0$")
	os.system("./configure --prefix="+out+" CXXFLAGS=\"-03\" --enable-mpi --with-cc=/usr/local/etc/alternatives/mpicc --with-cxx=/usr/local/etc/alternatives/mpicxx")
	os.system("make")
	os.system("make install")
	os.system("make -j 4 install")
	os.system("CXXFLAGS=\"-03\"")
	os.system("--enable-mpi --with-cc=/usr/local/etc/alternatives/mpicc --with-cxx=/usr/local/etc/alternatives/mpicxx")
button30001 = tk.Button(frame3000, text='BUILD PARALLELY', command=parallelbuild)
button30001.grid(column=2, row=2, sticky=tk.W)




###TAB1
####1
frame15=ttk.LabelFrame(tab1,text='DIRECT, ADJOINT, AND LINEARIZED PROBLEM DEFINITION')
frame15.grid(column=0,row=10,sticky=tk.W)
#scrollbar.config( command = frame15.yview )

ttk.Label(frame15, text="PHYSICAL PROBLEM:").grid(column=0, row=0)
name5 = tk.StringVar(frame15,'EULER')
name5_chosen = ttk.Combobox(frame15, width=12, textvariable=name5)
name5_chosen['values'] = ("EULER","NAVIER")
name5_chosen.grid(column=2, row=0)
name5_chosen.current(0)

ttk.Label(frame15, text="MATHEMATICAL PROBLEM:").grid(column=0, row=1)
name6 = tk.StringVar(frame15,'DIRECT')
name6_chosen = ttk.Combobox(frame15, width=12, textvariable=name6)
name6_chosen['values'] = ("DIRECT","CONTINUOUS_ADJOINT")
name6_chosen.grid(column=2,row=1)
name6_chosen.current(0)

ttk.Label(frame15, text="RESTART_SOL:").grid(column=0, row=2)
name7 = tk.StringVar(frame15,'YES')
name7_chosen = ttk.Combobox(frame15, width=12, textvariable=name7)
name7_chosen['values'] = ("YES","NO")
name7_chosen.grid(column=2, row=2)
name7_chosen.current(0)




####2
frame1=ttk.LabelFrame(tab1,text='Compressible free-stream definition')
frame1.grid(column=0,row=11,sticky=tk.W)
#scrollbar.config( command = frame1.yview )

#place labels into the container element
ttk.Label(frame1,text="MACH_NUMBER").grid(column=0,row=0,sticky=tk.W)
ttk.Label(frame1,text="AOA").grid(column=0,row=1,sticky=tk.W)
ttk.Label(frame1,text="FREESTREAM_PRESSURE").grid(column=0,row=2,sticky=tk.W)
ttk.Label(frame1,text="FREESTREAM_TEMPERATURE").grid(column=0,row=3,sticky=tk.W)

spin_boxf11=tk.Spinbox(frame1,from_=0.8,to=107897827,width=5,bd=2,increment=0.1)
spin_boxf11.grid(column=2,row=0)
spin_boxf12=tk.Spinbox(frame1,from_=1.25,to=107897827,width=5,bd=2,increment=0.01)
spin_boxf12.grid(column=2,row=1)
spin_boxf13=tk.Spinbox(frame1,from_=101325.0,to=107897827,width=5,bd=2,increment=0.1)
spin_boxf13.grid(column=2,row=2)
spin_boxf14=tk.Spinbox(frame1,from_=273.15,to=107897827,width=5,bd=2,increment=0.01)
spin_boxf14.grid(column=2,row=3)

ttk.Label(frame1,text="Mach number(non-dimensional)").grid(column=4,row=0,sticky=tk.W)
ttk.Label(frame1,text="Angle of attack(in degrees)").grid(column=4,row=1,sticky=tk.W)
ttk.Label(frame1,text="Free-stream pressure(in pascal)").grid(column=4,row=2,sticky=tk.W)
ttk.Label(frame1,text="Free-stream temperature(in degrees kelvin)").grid(column=4,row=3,sticky=tk.W)



####3
frame2=ttk.LabelFrame(tab1,text='COMPRESSIBLE AND INCOMPRESSIBLE FLUID CONSTANTS')
frame2.grid(column=0,row=21,padx=2,pady=2)
#scrollbar.config( command = frame2.yview )

#place labels into the container element
ttk.Label(frame2,text="GAMMA_VALUE                    ").grid(column=0,row=0,sticky=tk.W)
ttk.Label(frame2,text="GAS_CONSTANT                   ").grid(column=0,row=1,sticky=tk.W)

spin_boxf21=tk.Spinbox(frame2,from_=1.4,to=107897827,width=5,bd=2,increment=0.1)
spin_boxf21.grid(column=10,row=0)
spin_boxf22=tk.Spinbox(frame2,from_=287.87,to=107897827,width=5,bd=2,increment=0.01)
spin_boxf22.grid(column=10,row=1)

ttk.Label(frame2,text="Ration of specific heats(for compressible fluids)").grid(column=12,row=0,sticky=tk.W)
ttk.Label(frame2,text="Specific gas constant(for compressible fluids)").grid(column=12,row=1,sticky=tk.W)


####4
frame3=ttk.LabelFrame(tab1,text='REFERENCE VALUE DEFINITION')
frame3.grid(column=0,row=31,sticky=tk.W)
#scrollbar.config( command = frame3.yview )

ttk.Label(frame3,text="REF_ORIGIN_MOMENT_X ").grid(column=0,row=0,sticky=tk.W)
ttk.Label(frame3,text="REF_ORIGIN_MOMENT_Y").grid(column=0,row=1,sticky=tk.W)
ttk.Label(frame3,text="REF_ORIGIN_MOMENT_Z").grid(column=0,row=2,sticky=tk.W)
ttk.Label(frame3,text="REF_LENGTH").grid(column=0,row=3,sticky=tk.W)
ttk.Label(frame3,text="REF_AREA").grid(column=0,row=4,sticky=tk.W)
ttk.Label(frame3,text="REF_DIMENSIONALIZATION").grid(column=0,row=5,sticky=tk.W)

name1 = tk.StringVar(win,'0.25')
name_entered1 = ttk.Entry(frame3,width=24,textvariable=name1)
name_entered1.grid(column=10,row=0)

name2 = tk.StringVar(win,'0.00')
name_entered2 = ttk.Entry(frame3,width=24,textvariable=name2)
name_entered2.grid(column=10,row=1)

name3 = tk.StringVar(win,'0.00')
name_entered3 = ttk.Entry(frame3,width=24,textvariable=name3)
name_entered3.grid(column=10,row=2)

name4 = tk.StringVar(win,'1.0')
name_entered4 = ttk.Entry(frame3,width=24,textvariable=name4)
name_entered4.grid(column=10,row=3)

name5 = tk.StringVar(win,'1.00')
name_entered5 = ttk.Entry(frame3,width=24,textvariable=name5)
name_entered5.grid(column=10,row=4)


name4 = tk.StringVar()
name_chosen4 = ttk.Combobox(frame3, width=22, textvariable=name4)
name_chosen4['values'] = ("DIMENSIONAL", "FREESTREAM_PRESS_EQ_ONE","FREESTREAM_VEL_EQ_MACH", "FREESTREAM_VEL_EQ_ONE")
name_chosen4.grid(column=10, row=5)
name_chosen4.current(0)



####5
frame16=ttk.LabelFrame(tab1,text='BOUNDARY CONDITION DEFINITION')
frame16.grid(column=0,row=41,sticky=tk.W)
#scrollbar.config( command = frame16.yview )

ttk.Label(frame16, text="MARKER_EULER").grid(column=0,row=0)
name3 = tk.StringVar(win,'(airfoil)')
name3_entered = ttk.Entry(frame16,textvariable=name3)
name3_entered.grid(column=2,row=0)

ttk.Label(frame16, text="MARKER_FAR").grid(column=0,row=1)
name4 = tk.StringVar(win,'(farfield)')
name4_entered = ttk.Entry(frame16,textvariable=name4)
name4_entered.grid(column=2,row=1)


####6
frame17=ttk.LabelFrame(tab1,text='SURFACES IDENTIFICATION')
frame17.grid(column=0,row=51,sticky=tk.W)
#scrollbar.config( command = frame17.yview )

ttk.Label(frame17, text="MARKER_PLOTTING").grid(column=0,row=0)
name5 = tk.StringVar(win,'(airfoil)')
name5_entered = ttk.Entry(frame17,textvariable=name5)
name5_entered.grid(column=2,row=0)

ttk.Label(frame17, text="MARKER_MONITORING").grid(column=0,row=1)
name6 = tk.StringVar(win,'(airfoil)')
name6_entered = ttk.Entry(frame17,textvariable=name6)
name6_entered.grid(column=2,row=1)

ttk.Label(frame17, text="MARKER_DESIGNING").grid(column=0,row=2)
name7 = tk.StringVar(win,'(airfoil)')
name7_entered = ttk.Entry(frame17,textvariable=name7)
name7_entered.grid(column=2,row=2)



####TAB2
####7
frame19=ttk.LabelFrame(tab2,text='COMMON PARAMETERS TO DEFINE THE NUMERICAL METHOD')
frame19.grid(column=0,row=61,sticky=tk.W)

ttk.Label(frame19, text="NUM_METHOD_GRAD").grid(column=0,row=0,sticky=tk.W)
name22 = tk.StringVar()
name22_chosen = ttk.Combobox(frame19, width=12, textvariable=name22)
name22_chosen['values'] = ("GREEN_GAUSS", "WEIGHTED_LEAST_SQUARES")
name22_chosen.grid(column=2, row=0)
name22_chosen.current(0)

ttk.Label(frame19, text="OBJECTIVE_FUNCTION").grid(column=0, row=1,sticky=tk.W)
name21 = tk.StringVar()
name21_chosen = ttk.Combobox(frame19, width=12, textvariable=name21)
name21_chosen['values'] = ("DRAG", "LIFT", "SIDEFORCE", "MOMENT_X","MOMENT_Y", "MOMENT_Z", "EFFICIENCY",
                                             "EQUIVALENT_AREA", "NEARFIELD_PRESSURE",
                                             "FORCE_X", "FORCE_Y", "FORCE_Z", "THRUST",
                                             "TORQUE", "FREE_SURFACE", "TOTAL_HEATFLUX",
                                            "MAXIMUM_HEATFLUX", "INVERSE_DESIGN_PRESSURE",
                                           "INVERSE_DESIGN_HEATFLUX")
name21_chosen.grid(column=2, row=1)
name21_chosen.current(0)

#Courant-Friedrichs-Lewy condition of the finest grid
ttk.Label(frame19,text="CFL_NUMBER").grid(column=0,row=2,sticky=tk.W)

spin_boxf71=tk.Spinbox(frame19,from_=4.0,to=107897827,width=5,bd=2,increment=0.1)
spin_boxf71.grid(column=2,row=2)

#Courant-Friedrichs-Lewy condition of the finest grid
ttk.Label(frame19,text="EXT_ITER").grid(column=0,row=3,sticky=tk.W)

spin_boxf72=tk.Spinbox(frame19,from_=250,to=107897827,width=5,bd=2,increment=1)
spin_boxf72.grid(column=2,row=3)




####8

frame20=ttk.LabelFrame(tab2,text='LINEAR SOLVER DEFINITION')
frame20.grid(column=0,row=71,sticky=tk.W)
ttk.Label(frame20,text="LINEAR_SOLVER").grid(column=0,row=0)

name23 = tk.StringVar()
name23_chosen = ttk.Combobox(frame20, width=12, textvariable=name23)
name23_chosen['values'] = ("BCGSTAB", "FGMRES")
name23_chosen.grid(column=2, row=0)
name23_chosen.current(0)


ttk.Label(frame20, text="LINEAR_SOLVER_PREC").grid(column=0,row=1)

name24 = tk.StringVar()
name24_chosen = ttk.Combobox(frame20, width=12, textvariable=name24)
name24_chosen['values'] = ("JACOBI", "LINELET","LU_SGS")
name24_chosen.grid(column=2, row=1)
name24_chosen.current(0)

ttk.Label(frame20,text="LINEAR_SOLVER_ERROR").grid(column=0,row=2)
name25 = tk.StringVar(frame20,'1E-6')
name25_entered = ttk.Entry(frame20,textvariable=name25)
name25_entered.grid(column=2,row=2)

ttk.Label(frame20,text="GAMMA_VALUE").grid(column=0,row=3,sticky=tk.W)
spin_boxf81=tk.Spinbox(frame20,from_=5,to=107897827,width=12,bd=2,increment=1)
spin_boxf81.grid(column=2,row=3)

####9

frame21=ttk.LabelFrame(tab2,text='MULTIGRID PARAMETERS')
frame21.grid(column=0,row=91,sticky=tk.W)

ttk.Label(frame21,text="MGLEVEL").grid(column=0,row=0,sticky=tk.W)
spin_boxf91=tk.Spinbox(frame21,from_=3,to=107897827,width=12,bd=2,increment=1)
spin_boxf91.grid(column=2,row=0)

ttk.Label(frame21, text="MGCYCLE").grid(column=0,row=1,sticky=tk.W)
name30 = tk.StringVar()
name30_chosen = ttk.Combobox(frame21, width=12, textvariable=name30)
name30_chosen['values'] = ("V_CYCLE","W_CYCLE","FULLMG_CYCLE")
name30_chosen.grid(column=2, row=1)
name30_chosen.current(0)

ttk.Label(frame21,text="MG_PRE_SMOOTH").grid(column=0,row=2,sticky=tk.W)
def add_item1():
    """
    add the text in the Entry widget to the end of the listbox
    """
    listbox91.delete(0,1000)
    listbox91.insert(tk.END, enterlist91.get())
    #print(listbox1.get(0))
#win = tk.Tk()
win.title("Listbox Operations")
# create the listbox (note that size is in characters)
listbox91 = tk.Listbox(frame21, width=12, height=1)
#listbox1.grid(row=0, column=3)

# use entry widget to display/edit selection
enterlist91 = tk.Entry(frame21, width=10, bg='yellow')
enterlist91.insert(0,'(1,2,3,3)')
enterlist91.grid(column=2, row=2)
# button to add a line to the listbox
button91 = tk.Button(frame21, text='press to add values', command=add_item1)
button91.grid(column=4, row=2, sticky=tk.W)



ttk.Label(frame21,text="MG_POST_SMOOTH").grid(column=0,row=3,sticky=tk.W)
def add_item2():
    """
    add the text in the Entry widget to the end of the listbox
    """
    listbox92.delete(0,1000)
    listbox92.insert(tk.END, enterlist92.get())
    #print(listbox2.get(0))
#win = tk.Tk()
#win.title("Listbox Operations")
# create the listbox (note that size is in characters)
listbox92 = tk.Listbox(frame21, width=12, height=1)
#listbox1.grid(row=0, column=3)

# use entry widget to display/edit selection
enterlist92 = tk.Entry(frame21, width=10, bg='yellow')
enterlist92.insert(0,'(0,0,0,0)')
enterlist92.grid(column=2, row=3)
# button to add a line to the listbox
button92 = tk.Button(frame21, text='Press to add values', command=add_item2)
button92.grid(column=4,row=3, sticky=tk.W)




ttk.Label(frame21,text="MG_CORRECTION_SMOOTH").grid(column=0,row=4,sticky=tk.W)
def add_item3():
    """
    add the text in the Entry widget to the end of the listbox
    """
    listbox93.delete(0,1000)
    listbox93.insert(tk.END, enterlist93.get())
    #print(listbox3.get(0))
#win = tk.Tk()
#win.title("Listbox Operations")
# create the listbox (note that size is in characters)
listbox93 = tk.Listbox(frame21, width=12, height=1)
#listbox1.grid(row=0, column=3)

# use entry widget to display/edit selection
enterlist93 = tk.Entry(frame21, width=10, bg='yellow')
enterlist93.insert(0,'(0,0,0,0)')
enterlist93.grid(column=2,row=4)
# button to add a line to the listbox
button93 = tk.Button(frame21, text='Press to add values', command=add_item3)
button93.grid(column=4,row=4,sticky=tk.W)



ttk.Label(frame21,text="MG_DAMP_RESTRICTION").grid(column=0,row=6,sticky=tk.W)
spin_boxf92=tk.Spinbox(frame21,from_=1.0,to=107897827,width=12,bd=2,increment=0.1)
spin_boxf92.grid(column=2,row=6)

ttk.Label(frame21,text="MG_DAMP_PROLONGATION").grid(column=0,row=7,sticky=tk.W)
spin_boxf93=tk.Spinbox(frame21,from_=1.0,to=107897827,width=12,bd=2,increment=0.1)
spin_boxf93.grid(column=2,row=7)



####10

frame22=ttk.LabelFrame(tab2,text='FLOW NUMERICAL METHOD DEFINITION')
frame22.grid(column=0,row=101,sticky=tk.W)


ttk.Label(frame22, text="CONV_NUM_METHOD_FLOW").grid(column=0, row=0)
name31 = tk.StringVar()
name31_chosen = ttk.Combobox(frame22, width=12, textvariable=name31)
name31_chosen['values'] = ("JST", "LAX-FRIEDRICH", "CUSP", "ROE", "AUSM", "HLLC","TURKEL_PREC", "MSW")
name31_chosen.grid(column=2, row=0)
name31_chosen.current(0)


ttk.Label(frame22, text="MUSCL_FLOW").grid(column=0, row=1)
name32 = tk.StringVar()
name32_chosen = ttk.Combobox(frame22, width=12, textvariable=name32)
name32_chosen['values'] = ("YES","NO")
name32_chosen.grid(column=2, row=1)
name32_chosen.current(0)

ttk.Label(frame22, text="SLOPE_LIMITER_FLOW").grid(column=0, row=2)
name33 = tk.StringVar()
name33_chosen = ttk.Combobox(frame22, width=12, textvariable=name33)
name33_chosen['values'] = ("NONE", "VENKATAKRISHNAN", "VENKATAKRISHNAN_WANG","BARTH_JESPERSEN", "VAN_ALBADA_EDGE")
name33_chosen.grid(column=2, row=2)
name33_chosen.current(0)
###pending here
ttk.Label(frame22,text="JST_SENSOR_COEFF").grid(column=0,row=3,sticky=tk.W)
def add_item():
    """
    add the text in the Entry widget to the end of the listbox
    """
    listbox101.delete(0,1000)
    listbox101.insert(tk.END, enterlist101.get())
    #print(listbox1.get(0))
#win = tk.Tk()
win.title("Listbox Operations")
# create the listbox (note that size is in characters)
listbox101 = tk.Listbox(frame22, width=12, height=1)
#listbox1.grid(row=0, column=3)

# use entry widget to display/edit selection
enterlist101 = tk.Entry(frame22, width=10, bg='yellow')
enterlist101.insert(0,'(0.5,0.02)')
enterlist101.grid(column=2,row=3)
# button to add a line to the listbox
button3= tk.Button(frame22, text='press to add values',width=10,height=1,bg="green",command=add_item)
button3.grid(column=4,row=3,sticky=tk.E)


ttk.Label(frame22,text="TIME_DESCRE_FLOW").grid(column=0, row=4)
name34 = tk.StringVar()
name34_chosen = ttk.Combobox(frame22, width=12, textvariable=name34)
name34_chosen['values'] = ("RUNGE-KUTTA_EXPLICIT", "EULER_IMPLICIT", "EULER_EXPLICIT")
name34_chosen.grid(column=2, row=5)
name34_chosen.current(0)
####11

frame23=ttk.LabelFrame(tab3,text='CONVERGENCE PARAMETERS')
frame23.grid(column=0,row=211,sticky=tk.W)

ttk.Label(frame23, text="CONV_CRITERIA").grid(column=0, row=1)
name35 = tk.StringVar()
name35_chosen = ttk.Combobox(frame23, width=12, textvariable=name35)
name35_chosen['values'] = ("CAUCHY","RESIDUAL")
name35_chosen.grid(column=2, row=0)
name35_chosen.current(0)

ttk.Label(frame23,text="RESEDUAL_REDUCTION").grid(column=0,row=2,sticky=tk.W)
spin_box111=tk.Spinbox(frame23,from_=6,to=107897827,width=12,bd=2,increment=1)
spin_box111.grid(column=2,row=1)

ttk.Label(frame23,text="RESEDUAL_MINVAL").grid(column=0,row=3,sticky=tk.W)
spin_box112=tk.Spinbox(frame23,from_=-8,to=107897827,width=12,bd=2,increment=1)
spin_box112.grid(column=2,row=2)

ttk.Label(frame23,text="STARTCONV_ITER").grid(column=0,row=4,sticky=tk.W)
spin_box113=tk.Spinbox(frame23,from_=10,to=107897827,width=12,bd=2,increment=1)
spin_box113.grid(column=2,row=3)

ttk.Label(frame23,text="CAUCHY_ELEMS").grid(column=0,row=5,sticky=tk.W)
spin_box114=tk.Spinbox(frame23,from_=100,to=107897827,width=12,bd=2,increment=1)
spin_box114.grid(column=2,row=4)

ttk.Label(frame23, text="CAUCHY_EPS   ").grid(column=0,row=6)
name36 = tk.StringVar(win,'1E-6')
name36_entered = ttk.Entry(frame23,textvariable=name36)
name36_entered.grid(column=2,row=5)

ttk.Label(frame23, text="CAUCHY_FUNC_FLOW").grid(column=0, row=7)
name37 = tk.StringVar()
name37_chosen = ttk.Combobox(frame23, width=12, textvariable=name37)
name37_chosen['values'] = ("LIFT", "DRAG", "SENS_GEOMETRY", "SENS_MACH","DELTA_LIFT", "DELTA_DRAG")
name37_chosen.grid(column=2, row=6)
name37_chosen.current(0)

####12
frame18=ttk.LabelFrame(tab3,text='INPUT/OUTPUT INFORMATION')
frame18.grid(column=0,row=221,sticky=tk.W)

ttk.Label(frame18, text="MESH_FILENAME").grid(column=0, row=0)      
filentry1=tk.StringVar()
entry_file1 = Entry(frame18, width=50,textvariable=filentry1)
entry_file1.grid(column=2,row=0)
#path=filentry1.get()

ttk.Label(frame18, text="MESH_FROMAT").grid(column=0, row=1)
name19 = tk.StringVar()
name19_chosen = ttk.Combobox(frame18, width=12, textvariable=name19)
name19_chosen['values'] = ("SU2","CGNS","NETCDF_ASCII")
name19_chosen.grid(column=2, row=1)
name19_chosen.current(0)

ttk.Label(frame18, text="MESH_OUPUT_FILENAME").grid(column=0,row=2)
name16 = tk.StringVar(frame18,'mesh_out.su2')
name16_entered = ttk.Entry(frame18,width=24,textvariable=name16)
name16_entered.grid(column=2,row=2)

ttk.Label(frame18, text="SOLUTION_FLOW_FILENAME").grid(column=0,row=3)
name8 = tk.StringVar(win,'solution_flow.dat')
name8_entered = ttk.Entry(frame18,textvariable=name8)
name8_entered.grid(column=2,row=3)

ttk.Label(frame18, text="SOLUTION_ADJ_FILENAME").grid(column=0,row=4)
name9 = tk.StringVar(win,'solution_adj.dat')
name9_entered = ttk.Entry(frame18,textvariable=name9)
name9_entered.grid(column=2,row=4)

##output format
ttk.Label(frame18, text="OUTPUT_FROMAT").grid(column=0,row=5)
name38 = tk.StringVar()
name38_chosen = ttk.Combobox(frame18, width=12, textvariable=name38)
name38_chosen['values'] = ("TECPLOT", "PARAVIEW", "TECPLOT_BINARY")
name38_chosen.grid(column=2, row=5)
name38_chosen.current(0)


ttk.Label(frame18, text="CONV_FILENAME").grid(column=0,row=6)
name12 = tk.StringVar(win,'history')
name12_entered = ttk.Entry(frame18,textvariable=name12)
name12_entered.grid(column=2,row=6)

ttk.Label(frame18, text="RESTART_FLOW_FILENAME").grid(column=0,row=7)
name13 = tk.StringVar(win,'restart_flow.dat')
name13_entered = ttk.Entry(frame18,textvariable=name13)
name13_entered.grid(column=2,row=7)

ttk.Label(frame18,text="RESTART_ADJ_FILENAME").grid(column=0,row=8)
name14 = tk.StringVar(win,'restart_adj.dat')
name14_entered = ttk.Entry(frame18,textvariable=name14)
name14_entered.grid(column=2,row=8)

ttk.Label(frame18, text="VOLUME_FLOW_FILENAME").grid(column=0,row=9)
name15 = tk.StringVar(win,'flow')
name15_entered = ttk.Entry(frame18,textvariable=name15)
name15_entered.grid(column=2,row=9)

ttk.Label(frame18, text="VOLUME_ADJ_FILENAME").grid(column=0,row=10)
name17 = tk.StringVar(win,'adjoint')
name17_entered = ttk.Entry(frame18,textvariable=name17)
name17_entered.grid(column=2,row=10)

ttk.Label(frame18, text="GRAD_OBJFUNC_FILENAME").grid(column=0,row=11)
name18 = tk.StringVar(win,'of_grad.dat')
name18_entered = ttk.Entry(frame18,textvariable=name18)
name18_entered.grid(column=2,row=11)

ttk.Label(frame18, text="SURFACE_FLOW_FILENAME").grid(column=0,row=12)
name19 = tk.StringVar(win,'surface_flow')
name19_entered = ttk.Entry(frame18,textvariable=name19)
name19_entered.grid(column=2,row=12)

ttk.Label(frame18, text="SURFACE_ADJ_FILENAME").grid(column=0,row=13)
name20 = tk.StringVar(win,'surface_adjoint')
name20_entered = ttk.Entry(frame18,textvariable=name20)
name20_entered.grid(column=2,row=13)

ttk.Label(frame18,text="WRT_SOL_FREQ").grid(column=0,row=14,sticky=tk.W)
spin_box121=tk.Spinbox(frame18,from_=200,to=107897827,width=12,bd=2,increment=1)
spin_box121.grid(column=2,row=14)

ttk.Label(frame18,text="WRT_CON_FREQ").grid(column=0,row=15,sticky=tk.W)
spin_box122=tk.Spinbox(frame18,from_=1,to=107897827,width=12,bd=2,increment=1)
spin_box122.grid(column=2,row=15)


def upload_file():
	file1=open("hello.cfg","w")
	file1.write("% SU2 configuration file %\n")
	file1.write("% Case description: Transonic inviscid flow around a NACA0012 airfoil%\n")
	file1.write("% Author: Thomas D. Economon%\n")
	file1.write("% Institution: Stanford University%\n")
	file1.write("% Date: 2014.06.11%\n")
	file1.write("% File Version 6.0.0 \"Falcon\"\n")
	
	###frame1
	file1.write("PHYSICAL_PROBLEM="+name5_chosen.get()+"\n")
	file1.write("MATH_PROBLEM ="+name6_chosen.get()+"\n")
	file1.write("RESTART_SOL ="+name7_chosen.get()+"\n")
	###frame2
	file1.write("MACH_NUMBER ="+spin_boxf11.get()+"\n")
	file1.write("AOA ="+spin_boxf12.get()+"\n")
	file1.write("FREESTREAM_PRESSURE ="+spin_boxf13.get()+"\n")
	file1.write("FREESTREAM_TEMPERATURE ="+spin_boxf14.get()+"\n")
	###frame3
	file1.write("GAMMA_VALUE ="+spin_boxf21.get()+"\n")
	file1.write("GAS_CONSTANT ="+spin_boxf22.get()+"\n")
	###frame4
	file1.write("REF_ORIGIN_MOMENT_X ="+name_entered1.get()+"\n")
	file1.write("REF_ORIGIN_MOMENT_Y ="+name_entered2.get()+"\n")
	file1.write("REF_ORIGIN_MOMENT_Z ="+name_entered3.get()+"\n")
	file1.write("REF_LENGTH ="+name_entered4.get()+"\n")
	file1.write("REF_AREA ="+name_entered5.get()+"\n")
	file1.write("REF_DIMENSIONALIZATION ="+name_chosen4.get()+"\n")
	###frame5
	file1.write("MARKER_EULER ="+name3_entered.get()+"\n")
	file1.write("MARKER_FAR ="+name4_entered.get()+"\n")
	###frame6
	file1.write("MARKER_PLOTTING ="+name5_entered.get()+"\n")
	file1.write("MARKER_MONITORING ="+name6_entered.get()+"\n")
	file1.write("MARKER_DESIGNING ="+name7_entered.get()+"\n")
	###frame7
	file1.write("NUM_METHOD_GRAD ="+name22_chosen.get()+"\n")
	file1.write("OBJECTIVE_FUNCTION ="+name21_chosen.get()+"\n")
	file1.write("CFL_NUMBER ="+spin_boxf71.get()+"\n")
	file1.write("EXT_ITER ="+spin_boxf72.get()+"\n")
	###frame8
	file1.write("LINEAR_SOLVER ="+name23_chosen.get()+"\n")
	file1.write("LINEAR_SOLVER_PREC ="+name24_chosen.get()+"\n")
	file1.write("LINEAR_SOLVER_ERROR ="+name25_entered.get()+"\n")
	file1.write("LINEAR_SOLVER_ITER ="+spin_boxf81.get()+"\n")
	###frame9
	file1.write("MGLEVEL ="+spin_boxf91.get()+"\n")
	file1.write("MGCYCLE ="+name30_chosen.get()+"\n")
	file1.write("MG_PRE_SMOOTH ="+listbox91.get(0)+"\n")
	file1.write("MG_POST_SMOOTH ="+listbox92.get(0)+"\n")
	file1.write("MG_CORRECTION_SMOOTH ="+listbox93.get(0)+"\n")
	file1.write("MG_DAMP_RESTRICTION ="+spin_boxf92.get()+"\n")
	file1.write("MG_DAMP_PROLONGATION ="+spin_boxf93.get()+"\n")
	###frame10
	file1.write("CONV_NUM_METHOD_FLOW ="+name31_chosen.get()+"\n")
	file1.write("MUSCL_FLOW ="+name32_chosen.get()+"\n")
	file1.write("SLOPE_LIMITER_FLOW ="+name33_chosen.get()+"\n")
	file1.write("JST_SENSOR_COEFF ="+listbox101.get(0)+"\n")
	file1.write("TIME_DISCRE_FLOW ="+name34_chosen.get()+"\n")
	###frame11
	file1.write("CONV_CRITERIA ="+name35_chosen.get()+"\n")
	file1.write("RESIDUAL_REDUCTION="+spin_box111.get()+"\n")
	file1.write("RESIDUAL_MINVAL="+spin_box112.get()+"\n")
	file1.write("STARTCONV_ITER ="+spin_box113.get()+"\n")
	file1.write("CAUCHY_ELEMS="+spin_box114.get()+"\n")
	file1.write("CAUCHY_EPS ="+name36_entered.get()+"\n")
	file1.write("CAUCHY_FUNC_FLOW ="+name37_chosen.get()+"\n")
	###frame12
	file1.write("MESH_FILENAME ="+entry_file1.get()+"\n")
	file1.write("MESH_FORMAT ="+name19_chosen.get()+"\n")
	file1.write("MESH_OUT_FILENAME ="+name16_entered.get()+"\n")
	file1.write("SOLUTION_FLOW_FILENAME ="+name8_entered.get()+"\n")
	file1.write("SOLUTION_ADJ_FILENAME ="+name9_entered.get()+"\n")
	file1.write("OUTPUT_FORMAT ="+name38_chosen.get()+"\n")
	file1.write("CONV_FILENAME ="+name12_entered.get()+"\n")
	file1.write("RESTART_FLOW_FILENAME ="+name13_entered.get()+"\n")
	file1.write("RESTART_ADJ_FILENAME ="+name14_entered.get()+"\n")
	file1.write("VOLUME_FLOW_FILENAME ="+name15_entered.get()+"\n")
	file1.write("VOLUME_ADJ_FILENAME ="+name17_entered.get()+"\n")
	file1.write("GRAD_OBJFUNC_FILENAME="+name18_entered.get()+"\n")
	file1.write("SURFACE_FLOW_FILENAME ="+name19_entered.get()+"\n")
	file1.write("SURFACE_ADJ_FILENAME ="+name20_entered.get()+"\n")
	file1.write("WRT_SOL_FREQ ="+spin_box121.get()+"\n")
	file1.write("WRT_CON_FREQ ="+spin_box122.get()+"\n")

upload_file=tk.Button(frame18,text="upload_to_create_cfg",command=upload_file,bg="green")
upload_file.grid(column=0,row=17)


def execute():
	filename="hello.cfg"
	#print(filename)
	#print("input file is::"+filename)
	fi="./SU2_CFD "+filename
	os.system(fi)
	#os.system("paraview")
action=ttk.Button(frame18,text="SOLVE_BUTTON",command=execute)
action.grid(column=4,row=17)

win.mainloop()
