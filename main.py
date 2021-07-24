import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("DATCOM-GUI")
root.iconbitmap("logo.ico")
root.geometry("900x500")
tabControl = ttk.Notebook(root)

control_cards = ttk.Frame(tabControl)

tabControl.add(control_cards,
			   text='Control Cards')
tabControl.pack(expand=1, fill="both")
tk.Label(control_cards,
		 text="Digital DATCOM Graphical User Interface",
		 font=('Arial', 25)).grid(column=1, row=0, sticky=tk.EW)
# Control Cards frames
# Dimensions unit

Dimensions = tk.Frame(control_cards,
				highlightbackground="black",
				highlightthickness=1)
Dimensions.grid(column=0, row=1, padx=10, pady=10, sticky=tk.W)
ttk.Label(Dimensions, text="Dimensions Unit:").grid(column=0, row=0, columnspan=2, sticky=tk.N)
dim_unit_var = tk.IntVar()
dim_unit_var.set(1)
tk.Radiobutton(Dimensions, text="Imperial", padx=20, variable=dim_unit_var, value=1).grid(column=0, row=1, sticky=tk.W)
tk.Radiobutton(Dimensions, text="Metric", padx=20, variable=dim_unit_var, value=2).grid(column=0, row=2, sticky=tk.W)

# Derivations unit
Derivations = tk.Frame(control_cards,
				highlightbackground="black",
				highlightthickness=1)
Derivations.grid(column=1, row=1, padx=10, pady=10, sticky=tk.W)
ttk.Label(Derivations, text="Derivations Unit:").grid(column=0, row=0, columnspan=2, sticky=tk.N)
der_unit_var = tk.IntVar()
der_unit_var.set(1)
tk.Radiobutton(Derivations, text="Degree", padx=20, variable=der_unit_var, value=1).grid(column=0, row=1, sticky=tk.W)
tk.Radiobutton(Derivations, text="Radian", padx=20, variable=der_unit_var, value=2).grid(column=0, row=2, sticky=tk.W)

# Other Options
Other_options = tk.Frame(control_cards,
				highlightbackground="black",
				highlightthickness=1)
Other_options.grid(column=0, row=2, columnspan=2, padx=10, pady=10, sticky=tk.W)
dyn_der_var = tk.IntVar()
dyn_der_var.set(1)
part_var = tk.IntVar()
part_var.set(0)
build_var = tk.IntVar()
build_var.set(0)
tk.Checkbutton(Other_options, text="Dynamic Derivation(Advice: make it on)",
			   variable=dyn_der_var).grid(column=0, row=0, sticky=tk.W)
tk.Checkbutton(Other_options, text="Part Module",
			   variable=part_var).grid(column=0, row=1, sticky=tk.W)
tk.Checkbutton(Other_options, text="Build Module",
			   variable=build_var).grid(column=0, row=2, sticky=tk.W)

# Flight Conditions frames
flight_condition = ttk.Frame(tabControl)

tabControl.add(flight_condition,
			   text='Flight Conditions')
tabControl.pack(expand=1, fill="both")
tk.Label(flight_condition, text="Take Off Weight").grid(column=0, row=0, padx=10, pady=10)
take_off_weight = tk.Entry(flight_condition)
take_off_weight.grid(column=1, row=0, padx=0, pady=10, sticky=tk.W)

# Mach
mach_number = tk.Frame(flight_condition,
				highlightbackground="black",
				highlightthickness=1)
mach_number.grid(column=0, row=1, columnspan=2, padx=10, pady=10, sticky=tk.W)
tk.Label(mach_number, text="Minimum Mach Number").grid(column=0, row=0, padx=10, pady=10, sticky=tk.W)
min_mach = tk.Entry(mach_number)
min_mach.grid(column=1, row=0, padx=10, pady=10, sticky=tk.E)
tk.Label(mach_number, text="Maximum Mach Number").grid(column=0, row=1, padx=10, pady=10, sticky=tk.W)
max_mach = tk.Entry(mach_number)
max_mach.grid(column=1, row=1, padx=10, pady=10, sticky=tk.E)
tk.Label(mach_number, text="Number of Mach number(max = 20)").grid(column=0, row=2, padx=10, pady=10, sticky=tk.W)
num_mach = tk.Entry(mach_number)
num_mach.grid(column=1, row=2, padx=10, pady=10, sticky=tk.E)
# Altitude
altitude = tk.Frame(flight_condition,
				highlightbackground="black",
				highlightthickness=1)
altitude.grid(column=3, row=1, columnspan=2, padx=10, pady=10, sticky=tk.EW)
tk.Label(altitude, text="Minimum Altitude").grid(column=0, row=0, padx=10, pady=10, sticky=tk.W)
min_alt = tk.Entry(altitude)
min_alt.grid(column=1, row=0, padx=10, pady=10, sticky=tk.E)
tk.Label(altitude, text="Maximum Altitude").grid(column=0, row=1, padx=10, pady=10, sticky=tk.W)
max_alt = tk.Entry(altitude)
max_alt.grid(column=1, row=1, padx=10, pady=10, sticky=tk.E)
tk.Label(altitude, text="Number of Altitude(max = 20)").grid(column=0, row=2, padx=10, pady=10, sticky=tk.W)
num_alt = tk.Entry(altitude)
num_alt.grid(column=1, row=2, padx=10, pady=10, sticky=tk.E)
# Angle
angle = tk.Frame(flight_condition,
				highlightbackground="black",
				highlightthickness=1)
angle.grid(column=0, row=2, columnspan=2, padx=10, pady=10, sticky=tk.EW)
tk.Label(angle, text="Minimum angle").grid(column=0, row=0, padx=38, pady=10, sticky=tk.W)
min_ang = tk.Entry(angle)
min_ang.grid(column=1, row=0, padx=0, pady=10, sticky=tk.E)
tk.Label(angle, text="Maximum angle").grid(column=0, row=1, padx=38, pady=10, sticky=tk.W)
max_ang = tk.Entry(angle)
max_ang.grid(column=1, row=1, padx=0, pady=10, sticky=tk.E)
tk.Label(angle, text="Number of angle(max = 20)").grid(column=0, row=2, padx=38, pady=10, sticky=tk.W)
num_ang = tk.Entry(angle)
num_ang.grid(column=1, row=2, padx=0, pady=10, sticky=tk.E)

# program looping control
looping = tk.Frame(flight_condition,
				highlightbackground="black",
				highlightthickness=1)
looping.grid(column=3, row=2, columnspan=2, padx=10, pady=10, sticky=tk.NSEW)
ttk.Label(looping, text="Program Looping Control").grid(column=0, row=0, columnspan=2, sticky=tk.E, pady=10)
looping_var = tk.IntVar()
looping_var.set(1)
tk.Radiobutton(looping, text="Vary Altitude and Mach together", padx=20,
			   variable=looping_var, value=1).grid(column=0, row=1, sticky=tk.W)
tk.Radiobutton(looping, text="Vary Mach at fixed Altitude", padx=20,
			   variable=looping_var, value=2).grid(column=0, row=2, sticky=tk.W)
tk.Radiobutton(looping, text="Vary Altitude at fixed Mach", padx=20,
			   variable=looping_var, value=3).grid(column=0, row=3, sticky=tk.W)
# options
options = ttk.Frame(tabControl)

tabControl.add(options,
			   text='Options')
tk.Label(options, text="Reference Area").grid(column=0, row=0, padx=10, pady=10)
reference_area = tk.Entry(options)
reference_area.grid(column=1, row=0, padx=0, pady=10, sticky=tk.W)

tk.Label(options, text="Mean Aerodynamic Chord").grid(column=0, row=1, padx=10, pady=10)
mean_aerodynamic_chord = tk.Entry(options)
mean_aerodynamic_chord.grid(column=1, row=1, padx=0, pady=10, sticky=tk.W)

tk.Label(options, text="Wing Span").grid(column=0, row=2, padx=10, pady=10)
wing_span = tk.Entry(options)
wing_span.grid(column=1, row=2, padx=0, pady=10, sticky=tk.W)

tk.Label(options, text="Surface Roughness").grid(column=0, row=3, padx=10, pady=10)
surface_roughness = tk.Entry(options)
surface_roughness.grid(column=1, row=3, padx=0, pady=10, sticky=tk.W)

# Synthesis
synthesis = ttk.Frame(tabControl)

tabControl.add(synthesis,
			   text='Synthesis')
tabControl.pack(expand=1, fill="both")

tk.Label(synthesis, text="XCG").grid(column=0, row=0, padx=10, pady=10)
XCG = tk.Entry(synthesis)
XCG.grid(column=1, row=0, padx=0, pady=10, sticky=tk.W)
tk.Label(synthesis, text="Longitudinal Location of CG").grid(column=2, row=0, padx=10, pady=10, sticky=tk.W)

tk.Label(synthesis, text="ZCG").grid(column=0, row=1, padx=10, pady=10)
ZCG = tk.Entry(synthesis)
ZCG.grid(column=1, row=1, padx=0, pady=10, sticky=tk.W)
tk.Label(synthesis, text="Vertical Location of CG relative to reference plane").grid(
	column=2, row=1, padx=10, pady=10, sticky=tk.W)

tk.Label(synthesis, text="XW").grid(column=0, row=2, padx=10, pady=10)
XW = tk.Entry(synthesis)
XW.grid(column=1, row=2, padx=0, pady=10, sticky=tk.W)
tk.Label(synthesis, text="Longitudinal Location of theoretical wing Apex").grid(
	column=2, row=2, padx=10, pady=10, sticky=tk.W)

tk.Label(synthesis, text="ZW").grid(column=0, row=3, padx=10, pady=10)
ZW = tk.Entry(synthesis)
ZW.grid(column=1, row=3, padx=0, pady=10, sticky=tk.W)
tk.Label(synthesis, text="Vertical Location of theoretical wing Apex relative to reference plane").grid(
	column=2, row=3, padx=10, pady=10, sticky=tk.W)

tk.Label(synthesis, text="ALIW").grid(column=0, row=4, padx=10, pady=10)
ALIW = tk.Entry(synthesis)
ALIW.grid(column=1, row=4, padx=0, pady=10, sticky=tk.W)
tk.Label(synthesis, text="Wing root chord incidence angle measured from reference plane").grid(
	column=2, row=4, padx=10, pady=10, sticky=tk.W)

tk.Label(synthesis, text="ALIH").grid(column=0, row=5, padx=10, pady=10)
ALIH = tk.Entry(synthesis)
ALIH.grid(column=1, row=5, padx=0, pady=10, sticky=tk.W)
tk.Label(synthesis, text="Horizontal tail root chord incidence angle measured from reference plane").grid(
	column=2, row=5, padx=10, pady=10, sticky=tk.W)

tk.Label(synthesis, text="XH").grid(column=0, row=6, padx=10, pady=10)
XH = tk.Entry(synthesis)
XH.grid(column=1, row=6, padx=0, pady=10, sticky=tk.W)
tk.Label(synthesis, text="Longitudinal Location of theoretical horizontal tail Apex").grid(
	column=2, row=6, padx=10, pady=10, sticky=tk.W)

tk.Label(synthesis, text="ZH").grid(column=0, row=7, padx=10, pady=10)
ZH = tk.Entry(synthesis)
ZH.grid(column=1, row=7, padx=0, pady=10, sticky=tk.W)
tk.Label(synthesis, text="Vertical Location of theoretical horizontal tail Apex relative to reference plane").grid(
	column=2, row=7, padx=10, pady=10, sticky=tk.W)

tk.Label(synthesis, text="XV").grid(column=0, row=8, padx=10, pady=10)
XV = tk.Entry(synthesis)
XV.grid(column=1, row=8, padx=0, pady=10, sticky=tk.W)
tk.Label(synthesis, text="Longitudinal Location of theoretical vertical tail Apex").grid(
	column=2, row=8, padx=10, pady=10, sticky=tk.W)

tk.Label(synthesis, text="ZV").grid(column=0, row=9, padx=10, pady=10)
ZV = tk.Entry(synthesis)
ZV.grid(column=1, row=9, padx=0, pady=10, sticky=tk.W)
tk.Label(synthesis, text="Vertical Location of theoretical vertical tail Apex").grid(
	column=2, row=9, padx=10, pady=10, sticky=tk.W)

vertup_frame = tk.Frame(synthesis,
				highlightbackground="black",
				highlightthickness=1)
vertup_frame.grid(column=3, row=0, padx=10, pady=10, rowspan=2, columnspan=2, sticky=tk.EW)
tk.Label(vertup_frame, text="Vertical plane above ref plane").grid(column=0, row=0)
vertup = tk.StringVar()
vertup.set(".TRUE.")
tk.Radiobutton(vertup_frame, text="True", padx=20,
			   variable=vertup, value=".TRUE.").grid(column=0, row=1, sticky=tk.W)
tk.Radiobutton(vertup_frame, text="False", padx=20,
			   variable=vertup, value=".FALSE.").grid(column=0, row=2, sticky=tk.W)

tk.Label(synthesis, text="Scale Factor").grid(column=3, row=2, padx=10, pady=10)
SCALE = tk.Entry(synthesis)
SCALE.grid(column=4, row=2, padx=0, pady=10, sticky=tk.EW)

# Wing
wing = ttk.Frame(tabControl)

tabControl.add(wing,
			   text='Wing')
tabControl.pack(expand=1, fill="both")

tk.Label(wing, text="CHRDTP").grid(column=0, row=0, padx=10, pady=10)
WCHRDTP = tk.Entry(wing)
WCHRDTP.grid(column=1, row=0, padx=0, pady=10, sticky=tk.W)
tk.Label(wing, text="Chord at the Tip").grid(
	column=2, row=0, padx=10, pady=10, sticky=tk.W)

tk.Label(wing, text="CHRDR").grid(column=0, row=1, padx=10, pady=10)
WCHRDR = tk.Entry(wing)
WCHRDR.grid(column=1, row=1, padx=0, pady=10, sticky=tk.W)
tk.Label(wing, text="Chord at the Root").grid(
	column=2, row=1, padx=10, pady=10, sticky=tk.W)

tk.Label(wing, text="SSPNE").grid(column=0, row=2, padx=10, pady=10)
WSSPNE = tk.Entry(wing)
WSSPNE.grid(column=1, row=2, padx=0, pady=10, sticky=tk.W)
tk.Label(wing, text="Semi Span (Exposed)").grid(
	column=2, row=2, padx=10, pady=10, sticky=tk.W)

tk.Label(wing, text="SSPN").grid(column=0, row=3, padx=10, pady=10)
WSSPN = tk.Entry(wing)
WSSPN.grid(column=1, row=3, padx=0, pady=10, sticky=tk.W)
tk.Label(wing, text="Semi Span (Theoretical)").grid(
	column=2, row=3, padx=10, pady=10, sticky=tk.W)

tk.Label(wing, text="SAVSI").grid(column=0, row=4, padx=10, pady=10)
WSAVSI = tk.Entry(wing)
WSAVSI.grid(column=1, row=4, padx=0, pady=10, sticky=tk.W)
tk.Label(wing, text="Sweep Angle").grid(
	column=2, row=4, padx=10, pady=10, sticky=tk.W)

tk.Label(wing, text="CHSTAT").grid(column=0, row=5, padx=10, pady=10)
WCHSTAT = tk.Entry(wing)
WCHSTAT.grid(column=1, row=5, padx=0, pady=10, sticky=tk.W)
tk.Label(wing, text="Reference chord station for inboard and outboard panel sweep angles, fraction of chord ").grid(
	column=2, row=5, padx=10, pady=10, sticky=tk.W)

tk.Label(wing, text="TWISTA").grid(column=0, row=6, padx=10, pady=10)
WTWISTA = tk.Entry(wing)
WTWISTA.grid(column=1, row=6, padx=0, pady=10, sticky=tk.W)
tk.Label(wing, text="Twist angle (negative L.E rotated down) ").grid(
	column=2, row=6, padx=10, pady=10, sticky=tk.W)

tk.Label(wing, text="DHDADI").grid(column=0, row=7, padx=10, pady=10)
WTWISTA = tk.Entry(wing)
WTWISTA.grid(column=1, row=7, padx=0, pady=10, sticky=tk.W)
tk.Label(wing, text="Dihedral Angle").grid(
	column=2, row=7, padx=10, pady=10, sticky=tk.W)

wing_type_frame = tk.Frame(wing,
				highlightbackground="black",
				highlightthickness=1)
wing_type_frame.grid(column=0, row=8, padx=10, pady=10, rowspan=2, columnspan=2, sticky=tk.EW)
tk.Label(wing_type_frame, text="Wing Type").grid(column=0, row=0)
wing_type = tk.IntVar()
wing_type.set(1)
tk.Radiobutton(wing_type_frame, text="straight tapered platform", padx=20,
			   variable=wing_type, value=1).grid(column=0, row=1, sticky=tk.W)
tk.Radiobutton(wing_type_frame, text="double delta platform AR<3", padx=20,
			   variable=wing_type, value=2).grid(column=0, row=2, sticky=tk.W)
tk.Radiobutton(wing_type_frame, text="Cranked platform AR>3", padx=20,
			   variable=wing_type, value=3).grid(column=0, row=3, sticky=tk.W)

# Horizontal Tail
horizontal_tail = ttk.Frame(tabControl)

tabControl.add(horizontal_tail,
			   text='Horizontal Tail')
tabControl.pack(expand=1, fill="both")

tk.Label(horizontal_tail, text="CHRDTP").grid(column=0, row=0, padx=10, pady=10)
HCHRDTP = tk.Entry(horizontal_tail)
HCHRDTP.grid(column=1, row=0, padx=0, pady=10, sticky=tk.W)
tk.Label(horizontal_tail, text="Chord at the Tip").grid(
	column=2, row=0, padx=10, pady=10, sticky=tk.W)

tk.Label(horizontal_tail, text="CHRDR").grid(column=0, row=1, padx=10, pady=10)
HCHRDR = tk.Entry(horizontal_tail)
HCHRDR.grid(column=1, row=1, padx=0, pady=10, sticky=tk.W)
tk.Label(horizontal_tail, text="Chord at the Root").grid(
	column=2, row=1, padx=10, pady=10, sticky=tk.W)

tk.Label(horizontal_tail, text="SSPNE").grid(column=0, row=2, padx=10, pady=10)
HSSPNE = tk.Entry(horizontal_tail)
HSSPNE.grid(column=1, row=2, padx=0, pady=10, sticky=tk.W)
tk.Label(horizontal_tail, text="Semi Span (Exposed)").grid(
	column=2, row=2, padx=10, pady=10, sticky=tk.W)

tk.Label(horizontal_tail, text="SSPN").grid(column=0, row=3, padx=10, pady=10)
HSSPN = tk.Entry(horizontal_tail)
HSSPN.grid(column=1, row=3, padx=0, pady=10, sticky=tk.W)
tk.Label(horizontal_tail, text="Semi Span (Theoretical)").grid(
	column=2, row=3, padx=10, pady=10, sticky=tk.W)

tk.Label(horizontal_tail, text="SAVSI").grid(column=0, row=4, padx=10, pady=10)
HSAVSI = tk.Entry(horizontal_tail)
HSAVSI.grid(column=1, row=4, padx=0, pady=10, sticky=tk.W)
tk.Label(horizontal_tail, text="Sweep Angle").grid(
	column=2, row=4, padx=10, pady=10, sticky=tk.W)

tk.Label(horizontal_tail, text="CHSTAT").grid(column=0, row=5, padx=10, pady=10)
HCHSTAT = tk.Entry(horizontal_tail)
HCHSTAT.grid(column=1, row=5, padx=0, pady=10, sticky=tk.W)
tk.Label(horizontal_tail,
		 text="Reference chord station for inboard and outboard panel sweep angles, fraction of chord ").grid(
	column=2, row=5, padx=10, pady=10, columnspan=2, sticky=tk.W)

tk.Label(horizontal_tail, text="TWISTA").grid(column=0, row=6, padx=10, pady=10)
HTWISTA = tk.Entry(horizontal_tail)
HTWISTA.grid(column=1, row=6, padx=0, pady=10, sticky=tk.W)
tk.Label(horizontal_tail, text="Twist angle (negative L.E rotated down) ").grid(
	column=2, row=6, padx=10, pady=10, sticky=tk.W)

tk.Label(horizontal_tail, text="DHDADI").grid(column=0, row=7, padx=10, pady=10)
HTWISTA = tk.Entry(horizontal_tail)
HTWISTA.grid(column=1, row=7, padx=0, pady=10, sticky=tk.W)
tk.Label(horizontal_tail, text="Dihedral Angle").grid(
	column=2, row=7, padx=10, pady=10, sticky=tk.W)

tk.Label(horizontal_tail, text="Airfoil").grid(column=0, row=8, padx=10, pady=10)
airfoil = tk.Entry(horizontal_tail)
airfoil.grid(column=1, row=8, padx=0, pady=10, sticky=tk.W)
tk.Label(horizontal_tail, text="Write airfoil name like: \"NACA-H-4-00012\"").grid(
	column=2, row=8, padx=10, pady=10, sticky=tk.W)

horizontal_tail_type_frame = tk.Frame(horizontal_tail,
				highlightbackground="black",
				highlightthickness=1)
horizontal_tail_type_frame.grid(column=3, row=8, padx=10, pady=10, rowspan=2, columnspan=2, sticky=tk.EW)
tk.Label(horizontal_tail_type_frame, text="Horizontal Tail Type").grid(column=0, row=0)
horizontal_tail_type = tk.IntVar()
horizontal_tail_type.set(1)
tk.Radiobutton(horizontal_tail_type_frame, text="straight tapered platform", padx=20,
			   variable=horizontal_tail_type, value=1).grid(column=0, row=1, sticky=tk.W)
tk.Radiobutton(horizontal_tail_type_frame, text="double delta platform AR<3", padx=20,
			   variable=horizontal_tail_type, value=2).grid(column=0, row=2, sticky=tk.W)
tk.Radiobutton(horizontal_tail_type_frame, text="Cranked platform AR>3", padx=20,
			   variable=horizontal_tail_type, value=3).grid(column=0, row=3, sticky=tk.W)

# Vertical Tail
vertical_tail = ttk.Frame(tabControl)

tabControl.add(vertical_tail,
			   text='Vertical Tail')
tabControl.pack(expand=1, fill="both")

tk.Label(vertical_tail, text="CHRDTP").grid(column=0, row=0, padx=10, pady=10)
VCHRDTP = tk.Entry(vertical_tail)
VCHRDTP.grid(column=1, row=0, padx=0, pady=10, sticky=tk.W)
tk.Label(vertical_tail, text="Chord at the Tip").grid(
	column=2, row=0, padx=10, pady=10, sticky=tk.W)

tk.Label(vertical_tail, text="CHRDR").grid(column=0, row=1, padx=10, pady=10)
VCHRDR = tk.Entry(vertical_tail)
VCHRDR.grid(column=1, row=1, padx=0, pady=10, sticky=tk.W)
tk.Label(vertical_tail, text="Chord at the Root").grid(
	column=2, row=1, padx=10, pady=10, sticky=tk.W)

tk.Label(vertical_tail, text="SSPNE").grid(column=0, row=2, padx=10, pady=10)
VSSPNE = tk.Entry(vertical_tail)
VSSPNE.grid(column=1, row=2, padx=0, pady=10, sticky=tk.W)
tk.Label(vertical_tail, text="Semi Span (Exposed)").grid(
	column=2, row=2, padx=10, pady=10, sticky=tk.W)

tk.Label(vertical_tail, text="SSPN").grid(column=0, row=3, padx=10, pady=10)
VSSPN = tk.Entry(vertical_tail)
VSSPN.grid(column=1, row=3, padx=0, pady=10, sticky=tk.W)
tk.Label(vertical_tail, text="Semi Span (Theoretical)").grid(
	column=2, row=3, padx=10, pady=10, sticky=tk.W)

tk.Label(vertical_tail, text="SAVSI").grid(column=0, row=4, padx=10, pady=10)
VSAVSI = tk.Entry(vertical_tail)
VSAVSI.grid(column=1, row=4, padx=0, pady=10, sticky=tk.W)
tk.Label(vertical_tail, text="Sweep Angle").grid(
	column=2, row=4, padx=10, pady=10, sticky=tk.W)

tk.Label(vertical_tail, text="CHSTAT").grid(column=0, row=5, padx=10, pady=10)
VCHSTAT = tk.Entry(vertical_tail)
VCHSTAT.grid(column=1, row=5, padx=0, pady=10, sticky=tk.W)
tk.Label(vertical_tail,
		 text="Reference chord station for inboard and outboard panel sweep angles, fraction of chord ").grid(
	column=2, row=5, padx=10, pady=10, columnspan=2, sticky=tk.W)

tk.Label(vertical_tail, text="TWISTA").grid(column=0, row=6, padx=10, pady=10)
VTWISTA = tk.Entry(vertical_tail)
VTWISTA.grid(column=1, row=6, padx=0, pady=10, sticky=tk.W)
tk.Label(vertical_tail, text="Twist angle (negative L.E rotated down) ").grid(
	column=2, row=6, padx=10, pady=10, sticky=tk.W)

tk.Label(vertical_tail, text="DHDADI").grid(column=0, row=7, padx=10, pady=10)
VTWISTA = tk.Entry(vertical_tail)
VTWISTA.grid(column=1, row=7, padx=0, pady=10, sticky=tk.W)
tk.Label(vertical_tail, text="Dihedral Angle").grid(
	column=2, row=7, padx=10, pady=10, sticky=tk.W)

tk.Label(vertical_tail, text="Airfoil").grid(column=0, row=8, padx=10, pady=10)
airfoil = tk.Entry(vertical_tail)
airfoil.grid(column=1, row=8, padx=0, pady=10, sticky=tk.W)
tk.Label(vertical_tail, text="Write airfoil name like: \"NACA-V-4-00012\"").grid(
	column=2, row=8, padx=10, pady=10, sticky=tk.W)

vertical_tail_type_frame = tk.Frame(vertical_tail,
									highlightbackground="black",
									highlightthickness=1)
vertical_tail_type_frame.grid(column=3, row=8, padx=10, pady=10, rowspan=2, columnspan=2, sticky=tk.W)
tk.Label(vertical_tail_type_frame, text="Vertical Tail Type").grid(column=0, row=0)
vertical_tail_type = tk.IntVar()
vertical_tail_type.set(1)
tk.Radiobutton(vertical_tail_type_frame, text="straight tapered platform", padx=20,
			   variable=vertical_tail_type, value=1).grid(column=0, row=1, sticky=tk.W)
tk.Radiobutton(vertical_tail_type_frame, text="double delta platform AR<3", padx=20,
			   variable=vertical_tail_type, value=2).grid(column=0, row=2, sticky=tk.W)
tk.Radiobutton(vertical_tail_type_frame, text="Cranked platform AR>3", padx=20,
			   variable=vertical_tail_type, value=3).grid(column=0, row=3, sticky=tk.W)

root.mainloop()
