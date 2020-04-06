# Developed By: Utsab Sen
# Developed In: INDIA

from tkinter import *
from tkinter import messagebox
import math
import time

class global_var:
    flag_deg_red = "d"

glb_var = global_var


t = int(time.ctime()[11:13])

root = Tk()
root.geometry("362x407")
root.title("SCIENTIFIC CALCULATOR")

# frame_0 = Frame(root)
#
# frame_0.grid(row=0, column=0)

# ___Frame zero___
frame_1 = Frame(root)

entry = Entry(frame_1, justify="right", font=("Calibri 26"),  # expand=True, fill="both",
              relief=FLAT)
entry.grid()

frame_1.grid(row=0, column=1, columnspan=2)


def Frame_2():
    def Frame_2_Destroy():
        root.geometry("362x407")
        frame_0.destroy()
        frame_2.destroy()
        btn_max_min.config(text=">>", command=Frame_2)

    def fn_first_fn():
        btn_squareroot_or_cuberoot.config(text="\t__\n     /\n v", command=None)
        btn_sin_or_sin_inverse.config(text="sin", command=None)
        btn_cos_or_cos_inverse.config(text="cos", command=None)
        btn_tan_or_tan_inverse.config(text="tan", command=None)
        btn_ln_or_sinh.config(text="ln", command=None)
        btn_log_or_cosh.config(text="log", command=None)
        btn_x_inverse_or_tanh.config(text="1/x", command=None)
        btn_e_power_x_or_sinh_inverse.config(text="e^x", command=None)
        btn_x_squared_or_cosh_inverse.config(text="x^2", command=None)
        btn_x_power_y_or_tanh_inverse.config(text="x^y", command=None)
        btn_mod_x_or_2_power_x.config(text="|x|", command=None)
        btn_Pi_or_x_cube.config(text="Pi", command=None)
        btn_exponential_or_x_factorial.config(text="e", command=None)
        btn_second_fn_swap.config(text="2nd", command=fn_second_fn)

    def fn_second_fn():
        btn_squareroot_or_cuberoot.config(text="\t__\n3   /\n v", command=None)
        btn_sin_or_sin_inverse.config(text="sin^-1", command=None)
        btn_cos_or_cos_inverse.config(text="cos^-1", command=None)
        btn_tan_or_tan_inverse.config(text="tan^-1", command=None)
        btn_ln_or_sinh.config(text="sinh", command=None)
        btn_log_or_cosh.config(text="cosh", command=None)
        btn_x_inverse_or_tanh.config(text="tanh", command=None)
        btn_e_power_x_or_sinh_inverse.config(text="sinh^-1", command=None)
        btn_x_squared_or_cosh_inverse.config(text="cosh^-1", command=None)
        btn_x_power_y_or_tanh_inverse.config(text="tanh^-1", command=None)
        btn_mod_x_or_2_power_x.config(text="2^x", command=None)
        btn_Pi_or_x_cube.config(text="x^3", command=None)
        btn_exponential_or_x_factorial.config(text="x!", command=None)
        btn_second_fn_swap.config(text="1st", command=fn_first_fn)

    root.geometry("632x407")

    frame_0 = Frame(root)
    label = Label(frame_0,text="Scientific mode on")
    label.pack()
    frame_0.grid(row=0, column=0)

    # __Frame 2__
    frame_2 = Frame(root)

    def btn_second_fn_swap_on_enter(e):
        btn_second_fn_swap.config(bg="#eeeeee", fg="#00cc00") if (9 <= t <= 18) else btn_second_fn_swap.config(
            bg="#444444", fg="#00cc00")

    def btn_second_fn_swap_on_leave(e):
        btn_second_fn_swap.config(bg="white", fg="black") if (9 <= t <= 18) else btn_second_fn_swap.config(bg="black",
                                                                                                           fg="white")

    def btn_radian_on_enter(e):
        btn_degree_radian.config(bg="#eeeeee", fg="#00cc00") if (9 <= t <= 18) else btn_degree_radian.config(bg="#444444",
                                                                                               fg="#00cc00")

    def btn_radian_on_leave(e):
        btn_degree_radian.config(bg="white", fg="black") if (9 <= t <= 18) else btn_degree_radian.config(bg="black", fg="white")

    def btn_squareroot_or_cuberoot_on_enter(e):
        btn_squareroot_or_cuberoot.config(bg="#eeeeee", fg="#00cc00") if (
                9 <= t <= 18) else btn_squareroot_or_cuberoot.config(bg="#444444", fg="#00cc00")

    def btn_squareroot_or_cuberoot_on_leave(e):
        btn_squareroot_or_cuberoot.config(bg="white", fg="black") if (
                9 <= t <= 18) else btn_squareroot_or_cuberoot.config(bg="black", fg="white")

    def btn_sin_or_sin_inverse_on_enter(e):
        btn_sin_or_sin_inverse.config(bg="#eeeeee", fg="#00cc00") if (9 <= t <= 18) else btn_sin_or_sin_inverse.config(
            bg="#444444", fg="#00cc00")

    def btn_sin_or_sin_inverse_on_leave(e):
        btn_sin_or_sin_inverse.config(bg="white", fg="black") if (9 <= t <= 18) else btn_sin_or_sin_inverse.config(
            bg="black", fg="white")

    def btn_cos_or_cos_inverse_on_enter(e):
        btn_cos_or_cos_inverse.config(bg="#eeeeee", fg="#00cc00") if (9 <= t <= 18) else btn_cos_or_cos_inverse.config(
            bg="#444444", fg="#00cc00")

    def btn_cos_or_cos_inverse_on_leave(e):
        btn_cos_or_cos_inverse.config(bg="white", fg="black") if (9 <= t <= 18) else btn_cos_or_cos_inverse.config(
            bg="black", fg="white")

    def btn_tan_or_tan_inverse_on_enter(e):
        btn_tan_or_tan_inverse.config(bg="#eeeeee", fg="#00cc00") if (9 <= t <= 18) else btn_tan_or_tan_inverse.config(
            bg="#444444", fg="#00cc00")

    def btn_tan_or_tan_inverse_on_leave(e):
        btn_tan_or_tan_inverse.config(bg="white", fg="black") if (9 <= t <= 18) else btn_tan_or_tan_inverse.config(
            bg="black", fg="white")

    def btn_ln_or_sinh_on_enter(e):
        btn_ln_or_sinh.config(bg="#eeeeee", fg="#00cc00") if (9 <= t <= 18) else btn_ln_or_sinh.config(bg="#444444",
                                                                                                       fg="#00cc00")

    def btn_ln_or_sinh_on_leave(e):
        btn_ln_or_sinh.config(bg="white", fg="black") if (9 <= t <= 18) else btn_ln_or_sinh.config(bg="black",
                                                                                                   fg="white")

    def btn_log_or_cosh_on_enter(e):
        btn_log_or_cosh.config(bg="#eeeeee", fg="#00cc00") if (9 <= t <= 18) else btn_log_or_cosh.config(bg="#444444",
                                                                                                         fg="#00cc00")

    def btn_log_or_cosh_on_leave(e):
        btn_log_or_cosh.config(bg="white", fg="black") if (9 <= t <= 18) else btn_log_or_cosh.config(bg="black",
                                                                                                     fg="white")

    def btn_x_inverse_or_tanh_on_enter(e):
        btn_x_inverse_or_tanh.config(bg="#eeeeee", fg="#00cc00") if (9 <= t <= 18) else btn_x_inverse_or_tanh.config(
            bg="#444444", fg="#00cc00")

    def btn_x_inverse_or_tanh_on_leave(e):
        btn_x_inverse_or_tanh.config(bg="white", fg="black") if (9 <= t <= 18) else btn_x_inverse_or_tanh.config(
            bg="black", fg="white")

    def btn_e_power_x_or_sinh_inverse_on_enter(e):
        btn_e_power_x_or_sinh_inverse.config(bg="#eeeeee", fg="#00cc00") if (
                9 <= t <= 18) else btn_e_power_x_or_sinh_inverse.config(bg="#444444", fg="#00cc00")

    def btn_e_power_x_or_sinh_inverse_on_leave(e):
        btn_e_power_x_or_sinh_inverse.config(bg="white", fg="black") if (
                9 <= t <= 18) else btn_e_power_x_or_sinh_inverse.config(bg="black", fg="white")

    def btn_x_squared_or_cosh_inverse_on_enter(e):
        btn_x_squared_or_cosh_inverse.config(bg="#eeeeee", fg="#00cc00") if (
                9 <= t <= 18) else btn_x_squared_or_cosh_inverse.config(bg="#444444", fg="#00cc00")

    def btn_x_squared_or_cosh_inverse_on_leave(e):
        btn_x_squared_or_cosh_inverse.config(bg="white", fg="black") if (
                9 <= t <= 18) else btn_x_squared_or_cosh_inverse.config(bg="black", fg="white")

    def btn_x_power_y_or_tanh_inverse_on_enter(e):
        btn_x_power_y_or_tanh_inverse.config(bg="#eeeeee", fg="#00cc00") if (
                9 <= t <= 18) else btn_x_power_y_or_tanh_inverse.config(bg="#444444", fg="#00cc00")

    def btn_x_power_y_or_tanh_inverse_on_leave(e):
        btn_x_power_y_or_tanh_inverse.config(bg="white", fg="black") if (
                9 <= t <= 18) else btn_x_power_y_or_tanh_inverse.config(bg="black", fg="white")

    def btn_mod_x_or_2_power_x_on_enter(e):
        btn_mod_x_or_2_power_x.config(bg="#eeeeee", fg="#00cc00") if (9 <= t <= 18) else btn_mod_x_or_2_power_x.config(
            bg="#444444", fg="#00cc00")

    def btn_mod_x_or_2_power_x_on_leave(e):
        btn_mod_x_or_2_power_x.config(bg="white", fg="black") if (9 <= t <= 18) else btn_mod_x_or_2_power_x.config(
            bg="black", fg="white")

    def btn_Pi_or_x_cube_on_enter(e):
        btn_Pi_or_x_cube.config(bg="#eeeeee", fg="#00cc00") if (9 <= t <= 18) else btn_Pi_or_x_cube.config(bg="#444444",
                                                                                                           fg="#00cc00")

    def btn_Pi_or_x_cube_on_leave(e):
        btn_Pi_or_x_cube.config(bg="white", fg="black") if (9 <= t <= 18) else btn_Pi_or_x_cube.config(bg="black",
                                                                                                       fg="white")

    def btn_exponential_or_x_factorial_on_enter(e):
        btn_exponential_or_x_factorial.config(bg="#eeeeee", fg="#00cc00") if (
                9 <= t <= 18) else btn_exponential_or_x_factorial.config(bg="#444444", fg="#00cc00")

    def btn_exponential_or_x_factorial_on_leave(e):
        btn_exponential_or_x_factorial.config(bg="white", fg="black") if (
                9 <= t <= 18) else btn_exponential_or_x_factorial.config(bg="black", fg="white")

    def btn_nCr_on_enter(e):
        btn_nCr.config(bg="#eeeeee", fg="#00cc00") if (9 <= t <= 18) else btn_nCr.config(bg="#444444",
                                                                                                           fg="#00cc00")

    def btn_nCr_on_leave(e):
        btn_nCr.config(bg="white", fg="black") if (9 <= t <= 18) else btn_nCr.config(bg="black",
                                                                                                       fg="white")

    def btn_nPr_on_enter(e):
        btn_nPr.config(bg="#eeeeee", fg="#00cc00") if (9 <= t <= 18) else btn_nPr.config(bg="#444444",
                                                                                                           fg="#00cc00")

    def btn_nPr_on_leave(e):
        btn_nPr.config(bg="white", fg="black") if (9 <= t <= 18) else btn_nPr.config(bg="black",
                                                                                                       fg="white")

    def btn_calc_on_enter(e):
        btn_calc.config(bg="#eeeeee", fg="#00cc00") if (9 <= t <= 18) else btn_calc.config(bg="#444444",
                                                                                                           fg="#00cc00")

    def btn_calc_on_leave(e):
        btn_calc.config(bg="white", fg="black") if (9 <= t <= 18) else btn_calc.config(bg="black",
                                                                                                       fg="white")


    btn_second_fn_swap = Button(frame_2, text="2nd", width=10, height=3, bg="#FFFFFF", relief=FLAT,
                                font=('Helvetica', '10', 'bold'), command=fn_second_fn)
    btn_second_fn_swap.grid(row=0, column=0)


    def deg_rad():
        if (glb_var.flag_deg_red == 'd'):
            global_var.flag_deg_red = 'r'
            btn_degree_radian.config(text="Rad On")

        elif (glb_var.flag_deg_red == 'r'):
            global_var.flag_deg_red = 'd'
            btn_degree_radian.config(text="Deg On")

    btn_degree_radian = Button(frame_2, text="Deg On", width=10, height=3, bg="#FFFFFF", relief=FLAT,
                        font=('Helvetica', '10', 'bold'), command= deg_rad)

    btn_degree_radian.grid(row=0, column=1)

    def squareroot_or_cuberoot():

        None

    btn_squareroot_or_cuberoot = Button(frame_2, text="\t__\n     /\n v", width=10, height=3, bg="#FFFFFF", relief=FLAT,
                                        font=('Helvetica', '10', 'bold'), command=None)
    btn_squareroot_or_cuberoot.grid(row=0, column=2)

    btn_sin_or_sin_inverse = Button(frame_2, text="sin", width=10, height=3, bg="#FFFFFF", relief=FLAT,
                                    font=('Helvetica', '10', 'bold'), command=None)
    btn_sin_or_sin_inverse.grid(row=1, column=0)

    btn_cos_or_cos_inverse = Button(frame_2, text="cos", width=10, height=3, bg="#FFFFFF", relief=FLAT,
                                    font=('Helvetica', '10', 'bold'), command=None)
    btn_cos_or_cos_inverse.grid(row=1, column=1)

    btn_tan_or_tan_inverse = Button(frame_2, text="tan", width=10, height=3, bg="#FFFFFF", relief=FLAT,
                                    font=('Helvetica', '10', 'bold'), command=None)
    btn_tan_or_tan_inverse.grid(row=1, column=2)

    btn_ln_or_sinh = Button(frame_2, text="ln", width=10, height=3, bg="#FFFFFF", relief=FLAT,
                            font=('Helvetica', '10', 'bold'), command=None)
    btn_ln_or_sinh.grid(row=2, column=0)

    btn_log_or_cosh = Button(frame_2, text="log", width=10, height=3, bg="#FFFFFF", relief=FLAT,
                             font=('Helvetica', '10', 'bold'), command=None)
    btn_log_or_cosh.grid(row=2, column=1)

    btn_x_inverse_or_tanh = Button(frame_2, text="1/x", width=10, height=3, bg="#FFFFFF", relief=FLAT,
                                   font=('Helvetica', '10', 'bold'), command=None)
    btn_x_inverse_or_tanh.grid(row=2, column=2)

    btn_e_power_x_or_sinh_inverse = Button(frame_2, text="e^x", width=10, height=3, bg="#FFFFFF", relief=FLAT,
                                           font=('Helvetica', '10', 'bold'), command=None)
    btn_e_power_x_or_sinh_inverse.grid(row=3, column=0)

    btn_x_squared_or_cosh_inverse = Button(frame_2, text="x^2", width=10, height=3, bg="#FFFFFF", relief=FLAT,
                                           font=('Helvetica', '10', 'bold'), command=None)
    btn_x_squared_or_cosh_inverse.grid(row=3, column=1)

    btn_x_power_y_or_tanh_inverse = Button(frame_2, text="x^3", width=10, height=3, bg="#FFFFFF", relief=FLAT,
                                           font=('Helvetica', '10', 'bold'), command=None)
    btn_x_power_y_or_tanh_inverse.grid(row=3, column=2)

    btn_mod_x_or_2_power_x = Button(frame_2, text="|x|", width=10, height=3, bg="#FFFFFF", relief=FLAT,
                                    font=('Helvetica', '10', 'bold'), command=None)
    btn_mod_x_or_2_power_x.grid(row=4, column=0)

    btn_Pi_or_x_cube = Button(frame_2, text="Pi", width=10, height=3, bg="#FFFFFF", relief=FLAT,
                              font=('Helvetica', '10', 'bold'), command=None)
    btn_Pi_or_x_cube.grid(row=4, column=1)

    btn_exponential_or_x_factorial = Button(frame_2, text="e", width=10, height=3, bg="#FFFFFF", relief=FLAT,
                                            font=('Helvetica', '10', 'bold'), command=None)
    btn_exponential_or_x_factorial.grid(row=4, column=2)

    btn_nCr = Button(frame_2, text="nCr", width=10, height=3, bg="#FFFFFF", relief=FLAT,
                     font=('Helvetica', '10', 'bold'), command=None)
    btn_nCr.grid(row=5, column=0)

    btn_nPr = Button(frame_2, text="nPr", width=10, height=3, bg="#FFFFFF", relief=FLAT,
                     font=('Helvetica', '10', 'bold'), command=None)
    btn_nPr.grid(row=5, column=1)

    btn_calc = Button(frame_2, text="Calc", width=10, height=3, bg="#FFFFFF", relief=FLAT,
                     font=('Helvetica', '10', 'bold'), command=None)
    btn_calc.grid(row=5, column=2)

    btn_max_min.config(text="<<", command=Frame_2_Destroy)

    btn_second_fn_swap.bind("<Enter>", btn_second_fn_swap_on_enter)
    btn_second_fn_swap.bind("<Leave>", btn_second_fn_swap_on_leave)

    btn_degree_radian.bind("<Enter>", btn_radian_on_enter)
    btn_degree_radian.bind("<Leave>", btn_radian_on_leave)

    btn_squareroot_or_cuberoot.bind("<Enter>", btn_squareroot_or_cuberoot_on_enter)
    btn_squareroot_or_cuberoot.bind("<Leave>", btn_squareroot_or_cuberoot_on_leave)

    btn_sin_or_sin_inverse.bind("<Enter>", btn_sin_or_sin_inverse_on_enter)
    btn_sin_or_sin_inverse.bind("<Leave>", btn_sin_or_sin_inverse_on_leave)

    btn_cos_or_cos_inverse.bind("<Enter>", btn_cos_or_cos_inverse_on_enter)
    btn_cos_or_cos_inverse.bind("<Leave>", btn_cos_or_cos_inverse_on_leave)

    btn_tan_or_tan_inverse.bind("<Enter>", btn_tan_or_tan_inverse_on_enter)
    btn_tan_or_tan_inverse.bind("<Leave>", btn_tan_or_tan_inverse_on_leave)

    btn_ln_or_sinh.bind("<Enter>", btn_ln_or_sinh_on_enter)
    btn_ln_or_sinh.bind("<Leave>", btn_ln_or_sinh_on_leave)

    btn_log_or_cosh.bind("<Enter>", btn_log_or_cosh_on_enter)
    btn_log_or_cosh.bind("<Leave>", btn_log_or_cosh_on_leave)

    btn_x_inverse_or_tanh.bind("<Enter>", btn_x_inverse_or_tanh_on_enter)
    btn_x_inverse_or_tanh.bind("<Leave>", btn_x_inverse_or_tanh_on_leave)

    btn_e_power_x_or_sinh_inverse.bind("<Enter>", btn_e_power_x_or_sinh_inverse_on_enter)
    btn_e_power_x_or_sinh_inverse.bind("<Leave>", btn_e_power_x_or_sinh_inverse_on_leave)

    btn_x_squared_or_cosh_inverse.bind("<Enter>", btn_x_squared_or_cosh_inverse_on_enter)
    btn_x_squared_or_cosh_inverse.bind("<Leave>", btn_x_squared_or_cosh_inverse_on_leave)

    btn_x_power_y_or_tanh_inverse.bind("<Enter>", btn_x_power_y_or_tanh_inverse_on_enter)
    btn_x_power_y_or_tanh_inverse.bind("<Leave>", btn_x_power_y_or_tanh_inverse_on_leave)

    btn_mod_x_or_2_power_x.bind("<Enter>", btn_mod_x_or_2_power_x_on_enter)
    btn_mod_x_or_2_power_x.bind("<Leave>", btn_mod_x_or_2_power_x_on_leave)

    btn_Pi_or_x_cube.bind("<Enter>", btn_Pi_or_x_cube_on_enter)
    btn_Pi_or_x_cube.bind("<Leave>", btn_Pi_or_x_cube_on_leave)

    btn_exponential_or_x_factorial.bind("<Enter>", btn_exponential_or_x_factorial_on_enter)
    btn_exponential_or_x_factorial.bind("<Leave>", btn_exponential_or_x_factorial_on_leave)

    btn_nCr.bind("<Enter>", btn_nCr_on_enter)
    btn_nCr.bind("<Leave>", btn_nCr_on_leave)

    btn_nPr.bind("<Enter>", btn_nPr_on_enter)
    btn_nPr.bind("<Leave>", btn_nPr_on_leave)

    btn_calc.bind("<Enter>", btn_calc_on_enter)
    btn_calc.bind("<Leave>", btn_calc_on_leave)

    def dark_expend():
        btn_second_fn_swap.config(bg="black", fg="white")
        btn_degree_radian.config(bg="black", fg="white")
        btn_squareroot_or_cuberoot.config(bg="black", fg="white")
        btn_sin_or_sin_inverse.config(bg="black", fg="white")
        btn_cos_or_cos_inverse.config(bg="black", fg="white")
        btn_tan_or_tan_inverse.config(bg="black", fg="white")
        btn_ln_or_sinh.config(bg="black", fg="white")
        btn_log_or_cosh.config(bg="black", fg="white")
        btn_x_inverse_or_tanh.config(bg="black", fg="white")
        btn_e_power_x_or_sinh_inverse.config(bg="black", fg="white")
        btn_x_squared_or_cosh_inverse.config(bg="black", fg="white")
        btn_x_power_y_or_tanh_inverse.config(bg="black", fg="white")
        btn_mod_x_or_2_power_x.config(bg="black", fg="white")
        btn_Pi_or_x_cube.config(bg="black", fg="white")
        btn_exponential_or_x_factorial.config(bg="black", fg="white")
        btn_nCr.config(bg="black", fg="white")
        btn_nPr.config(bg="black", fg="white")
        btn_calc.config(bg="black", fg="white")

    def light_expend():
        btn_second_fn_swap.config(bg="white", fg="black")
        btn_degree_radian.config(bg="white", fg="black")
        btn_squareroot_or_cuberoot.config(bg="white", fg="black")
        btn_sin_or_sin_inverse.config(bg="white", fg="black")
        btn_cos_or_cos_inverse.config(bg="white", fg="black")
        btn_tan_or_tan_inverse.config(bg="white", fg="black")
        btn_ln_or_sinh.config(bg="white", fg="black")
        btn_log_or_cosh.config(bg="white", fg="black")
        btn_x_inverse_or_tanh.config(bg="white", fg="black")
        btn_e_power_x_or_sinh_inverse.config(bg="white", fg="black")
        btn_x_squared_or_cosh_inverse.config(bg="white", fg="black")
        btn_x_power_y_or_tanh_inverse.config(bg="white", fg="black")
        btn_mod_x_or_2_power_x.config(bg="white", fg="black")
        btn_Pi_or_x_cube.config(bg="white", fg="black")
        btn_exponential_or_x_factorial.config(bg="white", fg="black")
        btn_nCr.config(bg="white", fg="black")
        btn_nPr.config(bg="white", fg="black")
        btn_calc.config(bg="white", fg="black")






    if (9 <= t <= 18):
        light_expend()
    else:
        dark_expend()
    frame_2.grid(row=1, column=0)


# def entryDestroy()


# ___Frame 1___
def btn_max_min_on_enter(e):
    btn_max_min.config(bg="#eeeeee", fg= "blue") if (9 <= t <= 18) else btn_max_min.config(bg="#444444", fg="blue")  #"#00cc00"


def btn_max_min_on_leave(e):
    btn_max_min.config(bg="white", fg="black") if (9 <= t <= 18) else btn_max_min.config(bg="black", fg="white")


def btn_clear_on_enter(e):
    btn_clear.config(bg="orange")


def btn_clear_on_leave(e):
    btn_clear.config(bg="red", fg="black") if (9 <= t <= 18) else btn_clear.config(bg="black", fg="red")


def btn_modulus_on_enter(e):
    btn_modulus.config(bg="#eeeeee", fg="#00cc00") if (9 <= t <= 18) else btn_modulus.config(bg="#444444", fg="#00cc00")


def btn_modulus_on_leave(e):
    btn_modulus.config(bg="white", fg="black") if (9 <= t <= 18) else btn_modulus.config(bg="black", fg="white")


def btn_backspace_on_enter(e):
    btn_backspace.config(bg="orange", fg="red") if (9 <= t <= 18) else btn_backspace.config(bg="orange",
                                                                                                 fg="red")


def btn_backspace_on_leave(e):
    btn_backspace.config(bg="white", fg="black") if (9 <= t <= 18) else btn_backspace.config(bg="black",
                                                                                                 fg="orange")

def btn_history_on_enter(e):
    btn_history.config(bg="#eeeeee", fg="#00cc00") if (9 <= t <= 18) else btn_history.config(bg="#444444", fg="orange")


def btn_history_on_leave(e):
    btn_history.config(bg="white", fg="black") if (9 <= t <= 18) else btn_history.config(bg="black", fg="white")


def btn_parenthesis_start_on_enter(e):
    btn_parenthesis_start.config(bg="#eeeeee", fg="#00cc00") if (9 <= t <= 18) else btn_parenthesis_start.config(bg="#444444", fg="#00cc00")


def btn_parenthesis_start_on_leave(e):
    btn_parenthesis_start.config(bg="white", fg="black") if (9 <= t <= 18) else btn_parenthesis_start.config(bg="black", fg="white")


def btn_parenthesis_end_on_enter(e):
    btn_parenthesis_end.config(bg="#eeeeee", fg="#00cc00") if (9 <= t <= 18) else btn_parenthesis_end.config(bg="#444444", fg="#00cc00")


def btn_parenthesis_end_on_leave(e):
    btn_parenthesis_end.config(bg="white", fg="black") if (9 <= t <= 18) else btn_parenthesis_end.config(bg="black", fg="white")


def btn_division_on_enter(e):
    btn_division.config(bg="#eeeeee", fg="#00cc00") if (9 <= t <= 18) else btn_division.config(bg="#444444",
                                                                                               fg="#00cc00")


def btn_division_on_leave(e):
    btn_division.config(bg="white", fg="black") if (9 <= t <= 18) else btn_division.config(bg="black", fg="white")


def btn_7_on_enter(e):
    btn_7.config(bg="#eeeeee", fg="#00cc00") if (9 <= t <= 18) else btn_7.config(bg="#444444", fg="#00cc00")


def btn_7_on_leave(e):
    btn_7.config(bg="white", fg="black") if (9 <= t <= 18) else btn_7.config(bg="black", fg="white")


def btn_8_on_enter(e):
    btn_8.config(bg="#eeeeee", fg="#00cc00") if (9 <= t <= 18) else btn_8.config(bg="#444444", fg="#00cc00")


def btn_8_on_leave(e):
    btn_8.config(bg="white", fg="black") if (9 <= t <= 18) else btn_8.config(bg="black", fg="white")


def btn_9_on_enter(e):
    btn_9.config(bg="#eeeeee", fg="#00cc00") if (9 <= t <= 18) else btn_9.config(bg="#444444", fg="#00cc00")


def btn_9_on_leave(e):
    btn_9.config(bg="white", fg="black") if (9 <= t <= 18) else btn_9.config(bg="black", fg="white")


def btn_multiplication_on_enter(e):
    btn_multiplication.config(bg="#eeeeee", fg="#00cc00") if (9 <= t <= 18) else btn_multiplication.config(bg="#444444",
                                                                                                           fg="#00cc00")


def btn_multiplication_on_leave(e):
    btn_multiplication.config(bg="white", fg="black") if (9 <= t <= 18) \
        else btn_multiplication.config(bg="black", fg="white")


def btn_4_on_enter(e):
    btn_4.config(bg="#eeeeee", fg="#00cc00") if (9 <= t <= 18) else btn_4.config(bg="#444444", fg="#00cc00")


def btn_4_on_leave(e):
    btn_4.config(bg="white", fg="black") if (9 <= t <= 18) else btn_4.config(bg="black", fg="white")


def btn_5_on_enter(e):
    btn_5.config(bg="#eeeeee", fg="#00cc00") if (9 <= t <= 18) else btn_5.config(bg="#444444", fg="#00cc00")


def btn_5_on_leave(e):
    btn_5.config(bg="white", fg="black") if (9 <= t <= 18) else btn_5.config(bg="black", fg="white")


def btn_6_on_enter(e):
    btn_6.config(bg="#eeeeee", fg="#00cc00") if (9 <= t <= 18) else btn_6.config(bg="#444444", fg="#00cc00")


def btn_6_on_leave(e):
    btn_6.config(bg="white", fg="black") if (9 <= t <= 18) else btn_6.config(bg="black", fg="white")


def btn_subtraction_on_enter(e):
    btn_subtraction.config(bg="#eeeeee", fg="#00cc00") if (9 <= t <= 18) else btn_subtraction.config(bg="#444444",
                                                                                                     fg="#00cc00")


def btn_subtraction_on_leave(e):
    btn_subtraction.config(bg="white", fg="black") if (9 <= t <= 18) else btn_subtraction.config(bg="black", fg="white")


def btn_1_on_enter(e):
    btn_1.config(bg="#eeeeee", fg="#00cc00") if (9 <= t <= 18) else btn_1.config(bg="#444444", fg="#00cc00")


def btn_1_on_leave(e):
    btn_1.config(bg="white", fg="black") if (9 <= t <= 18) else btn_1.config(bg="black", fg="white")


def btn_2_on_enter(e):
    btn_2.config(bg="#eeeeee", fg="#00cc00") if (9 <= t <= 18) else btn_2.config(bg="#444444", fg="#00cc00")


def btn_2_on_leave(e):
    btn_2.config(bg="white", fg="black") if (9 <= t <= 18) else btn_2.config(bg="black", fg="white")


def btn_3_on_enter(e):
    btn_3.config(bg="#eeeeee", fg="#00cc00") if (9 <= t <= 18) else btn_3.config(bg="#444444", fg="#00cc00")


def btn_3_on_leave(e):
    btn_3.config(bg="white", fg="black") if (9 <= t <= 18) else btn_3.config(bg="black", fg="white")


def btn_addition_on_enter(e):
    btn_addition.config(bg="#eeeeee", fg="#00cc00") if (9 <= t <= 18) else btn_addition.config(bg="#444444",
                                                                                               fg="#00cc00")


def btn_addition_on_leave(e):
    btn_addition.config(bg="white", fg="black") if (9 <= t <= 18) else btn_addition.config(bg="black", fg="white")


def btn_pos_neg_on_enter(e):
    btn_pos_neg.config(bg="#eeeeee", fg="#00cc00") if (9 <= t <= 18) else btn_pos_neg.config(bg="#444444", fg="#00cc00")


def btn_pos_neg_on_leave(e):
    btn_pos_neg.config(bg="white", fg="black") if (9 <= t <= 18) else btn_pos_neg.config(bg="black", fg="white")


def btn_0_on_enter(e):
    btn_0.config(bg="#eeeeee", fg="#00cc00") if (9 <= t <= 18) else btn_0.config(bg="#444444", fg="#00cc00")


def btn_0_on_leave(e):
    btn_0.config(bg="white", fg="black") if (9 <= t <= 18) else btn_0.config(bg="black", fg="white")


def btn_decimal_on_enter(e):
    btn_decimal.config(bg="#eeeeee", fg="#00cc00") if (9 <= t <= 18) else btn_decimal.config(bg="#444444", fg="#00cc00")


def btn_decimal_on_leave(e):
    btn_decimal.config(bg="white", fg="black") if (9 <= t <= 18) else btn_decimal.config(bg="black", fg="white")


def btn_equals_on_enter(e):
    btn_equals.config(bg="#00aa00", fg="white")


def btn_equals_on_leave(e):
    btn_equals.config(bg="#00cc00", fg="black") if (9 <= t <= 18) else btn_equals.config(bg="black", fg="#00cc00")


frame_3 = Frame(root)

btn_max_min = Button(frame_3, text=">>", width=10, height=3, bg="#FFFFFF", fg="black", relief=FLAT,
                     font=('Helvetica', '10', 'bold'), command=Frame_2)
btn_max_min.grid(row=0, column=0)


def entry_clear():
    entry.delete(0, END)
    entry.insert(0, "")
    #btn_backspace.config(state=DISABLED)


def entry_modulus():
    try:
        if (type(int(entry.get()[-1])) == type(1)):
            entry.insert(entry.index(INSERT), "%")
    except:
        None
    if (entry.get() == ""):
        entry.insert(0, '')
    if (entry.get() == "("):
        None
    elif (entry.get()[-1] == "+" or entry.get()[-1] == "-" or entry.get()[-1] == "*" or entry.get()[-1] == "/" or
          entry.get()[-1] == "%"):
        if(entry.get()[-2] == "("):
            None
        elif (entry.get()[-2] == ")"):
            backspace()
            entry.insert(entry.index(INSERT), "%")
        else:
            try:
                if (type(int(entry.get()[-2])) == type(1)):
                    backspace()
                    entry.insert(entry.index(INSERT), "%")
            except:
                result = entry.get()
                if (result[-1] == '('):
                    entry.insert(entry.index(INSERT), "%")
                elif (entry.get()[-2] == "("):
                    None
                elif (result[0] == '('):
                    entry.insert(entry.index(INSERT), "%")
                else:
                    backspace()
                    entry.insert(entry.index(INSERT), "%")
    elif (entry.get()[-1] == ")"):
        entry.insert(entry.index(INSERT), "%")


def backspace():
    entry.delete(entry.index(INSERT) - 1)


btn_clear = Button(frame_3, text="C", width=10, height=3, bg="red", fg="black", relief=FLAT,
                   font=('Helvetica', '10', 'bold'), command=entry_clear)
btn_clear.grid(row=0, column=1)

btn_modulus = Button(frame_3, text="%", width=10, height=3, bg="#FFFFFF", fg="black", relief=FLAT,
                     font=('Helvetica', '10', 'bold'), command=entry_modulus)
btn_modulus.grid(row=0, column=2)

btn_backspace = Button(frame_3, text="<-", width=10, height=3, bg="#FFFFFF", relief=FLAT,
                       font=('Helvetica', '10', 'bold'), command=backspace)
btn_backspace.grid(row=0, column=3)


def history():
    None


def entry_paranthesis_start():
    try:
        result = entry.get()
        if(result == "" or result[-1] == "(" or entry.get()[-1] == "+" or entry.get()[-1] == "-" or entry.get()[-1] == "*" or entry.get()[-1] == "/" or entry.get()[-1] == "%"):
            entry.insert(entry.index(INSERT), "(")
        elif(type(int(entry.get()[-1])) == type(1)):
            entry.insert(entry.index(INSERT), "*(")
    except:
        entry.insert(entry.index(INSERT), "*(")
    # entry.insert(entry.index(INSERT),"(")

def entry_paranthesis_end():
    result = entry.get()
    if(result == "" or result[-1] == "(" or entry.get()[-1] == "+" or entry.get()[-1] == "-" or entry.get()[-1] == "*" or entry.get()[-1] == "/" or entry.get()[-1] == "%"):
        None
    elif(int(result.count("(")) > int(result.count(")"))):
        try:
            if(type(int(result[-1])) == type(1)):
                result += ")"
                entry.delete(0, END)
                entry.insert(0, result)
        except:
            if(result[-1] == ")"):
                result += ")"
                entry.delete(0, END)
                entry.insert(0, result)

    # entry.insert(entry.index(INSERT),")")


def entry_division():
    try:
        if(type(int(entry.get()[-1])) == type(1)):
            entry.insert(entry.index(INSERT), "/")
    except:
        None
    if (entry.get() == ""):
        entry.insert(0, '')
    if(entry.get()=="("):
        None
    elif (entry.get()[-1] == "+" or entry.get()[-1] == "-" or entry.get()[-1] == "*" or entry.get()[-1] == "/" or
          entry.get()[-1] == "%"):
        if(entry.get()[-2] == "(" ):
            None
        elif(entry.get()[-2] == ")"):
            backspace()
            entry.insert(entry.index(INSERT), "/")
        else:
            try:
                if(type(int(entry.get()[-2])) == type(1)):
                    backspace()
                    entry.insert(entry.index(INSERT), "/")
            except:
                result = entry.get()
                if (result[-1] == '('):
                    entry.insert(entry.index(INSERT), "/")
                elif (entry.get()[-2] == "("):
                    None
                elif (result[0] == '('):
                    entry.insert(entry.index(INSERT), "/")
                else:
                    backspace()
                    entry.insert(entry.index(INSERT), "/")
    elif(entry.get()[-1] == ")"):
        entry.insert(entry.index(INSERT), "/")


btn_history = Button(frame_3, text="H", width=10, height=3, bg="#FFFFFF", fg="black", relief=FLAT,
                     font=('Helvetica', '10', 'bold'), command=history)
btn_history.grid(row=1, column=0)

btn_parenthesis_start = Button(frame_3, text="(", width=10, height=3, bg="#FFFFFF", fg="black", relief=FLAT,
                               font=('Helvetica', '10', 'bold'), command=entry_paranthesis_start)
btn_parenthesis_start.grid(row=1, column=1)

btn_parenthesis_end = Button(frame_3, text=")", width=10, height=3, bg="#FFFFFF", fg="black", relief=FLAT,
                             font=('Helvetica', '10', 'bold'), command=entry_paranthesis_end)
btn_parenthesis_end.grid(row=1, column=2)

btn_division = Button(frame_3, text="÷", width=10, height=3, bg="#FFFFFF", fg="black", relief=FLAT,
                      font=('Helvetica', '10', 'bold'), command=entry_division)
btn_division.grid(row=1, column=3)


def entry_7():
    if(entry.get() == ""):
        entry.insert(entry.index(INSERT), "7")
    elif(entry.get()[-1] == ")"):
        entry.insert(entry.index(INSERT), "*7")
    else:
        entry.insert(entry.index(INSERT), "7")


def entry_8():
    if (entry.get() == ""):
        entry.insert(entry.index(INSERT), "8")
    elif (entry.get()[-1] == ")"):
        entry.insert(entry.index(INSERT), "*8")
    else:
        entry.insert(entry.index(INSERT), "8")


def entry_9():
    if (entry.get() == ""):
        entry.insert(entry.index(INSERT), "9")
    elif (entry.get()[-1] == ")"):
        entry.insert(entry.index(INSERT), "*9")
    else:
        entry.insert(entry.index(INSERT), "9")


def entry_multiplication():
    try:
        if(type(int(entry.get()[-1])) == type(1)):
            entry.insert(entry.index(INSERT), "*")
    except:
        None
    if (entry.get() == ""):
        entry.insert(0, '')
    if(entry.get()=="("):
        None
    elif (entry.get()[-1] == "+" or entry.get()[-1] == "-" or entry.get()[-1] == "*" or entry.get()[-1] == "/" or
          entry.get()[-1] == "%"):
        if(entry.get()[-2] == "(" ):#or entry.get()[-2] == ")"):
            None
        elif(entry.get()[-2] == ")"):
            backspace()
            entry.insert(entry.index(INSERT), "*")
        else:
            try:
                if(type(int(entry.get()[-2])) == type(1)):
                    backspace()
                    entry.insert(entry.index(INSERT), "*")
            except:
                result = entry.get()
                if (result[-1] == '('):
                    entry.insert(entry.index(INSERT), "*")
                elif (entry.get()[-2] == "("):
                    None
                elif (result[0] == '('):
                    entry.insert(entry.index(INSERT), "*")
                else:
                    backspace()
                    entry.insert(entry.index(INSERT), "*")
    elif(entry.get()[-1] == ")"):
        entry.insert(entry.index(INSERT), "*")
    # else:
    #     try:
    #         result = entry.get()
    #         result = eval(result)
    #         entry.delete(0, END)
    #         entry.insert(0, result)
    #         entry.insert(entry.index(INSERT), "*")
    #     except:
    #         result = entry.get()
    #         if(result[-1] == '('):
    #             entry.insert(entry.index(INSERT), "*")
    #         elif(result[0] == '('):
    #             entry.insert(entry.index(INSERT), "*")


btn_7 = Button(frame_3, text="7", width=10, height=3, bg="#FFFFFF", fg="black", relief=FLAT,
               font=('Helvetica', '10', 'bold'), command=entry_7)
btn_7.grid(row=2, column=0)

btn_8 = Button(frame_3, text="8", width=10, height=3, bg="#FFFFFF", fg="black", relief=FLAT,
               font=('Helvetica', '10', 'bold'), command=entry_8)
btn_8.grid(row=2, column=1)

btn_9 = Button(frame_3, text="9", width=10, height=3, bg="#FFFFFF", fg="black", relief=FLAT,
               font=('Helvetica', '10', 'bold'), command=entry_9)
btn_9.grid(row=2, column=2)

btn_multiplication = Button(frame_3, text="×", width=10, height=3, fg="black", bg="#FFFFFF", relief=FLAT,
                            font=('Helvetica', '10', 'bold'), command=entry_multiplication)
btn_multiplication.grid(row=2, column=3)


def entry_4():
    if (entry.get() == ""):
        entry.insert(entry.index(INSERT), "4")
    elif (entry.get()[-1] == ")"):
        entry.insert(entry.index(INSERT), "*4")
    else:
        entry.insert(entry.index(INSERT), "4")


def entry_5():
    if (entry.get() == ""):
        entry.insert(entry.index(INSERT), "5")
    elif (entry.get()[-1] == ")"):
        entry.insert(entry.index(INSERT), "*5")
    else:
        entry.insert(entry.index(INSERT), "5")


def entry_6():
    if (entry.get() == ""):
        entry.insert(entry.index(INSERT), "6")
    elif (entry.get()[-1] == ")"):
        entry.insert(entry.index(INSERT), "*6")
    else:
        entry.insert(entry.index(INSERT), "6")


def entry_subtraction():
    try:
        if(type(int(entry.get()[-1])) == type(1)):
            entry.insert(entry.index(INSERT), "-")
    except:
        None
    if (entry.get() == ""):
        entry.insert(0, '')
    if(entry.get()=="("):
        None
    elif (entry.get()[-1] == "+" or entry.get()[-1] == "-" or entry.get()[-1] == "*" or entry.get()[-1] == "/" or
          entry.get()[-1] == "%"):
        if(entry.get()[-2] == "("):
            None
        elif (entry.get()[-2] == ")"):
            backspace()
            entry.insert(entry.index(INSERT), "-")
        else:
            try:
                if(type(int(entry.get()[-2])) == type(1)):
                    backspace()
                    entry.insert(entry.index(INSERT), "-")
            except:
                result = entry.get()
                if (result[-1] == '('):
                    entry.insert(entry.index(INSERT), "-")
                elif (entry.get()[-2] == "("):
                    None
                elif (result[0] == '('):
                    entry.insert(entry.index(INSERT), "-")
                elif(entry.get()[-1] == "+" or entry.get()[-1] == "-" or entry.get()[-1] == "*" or entry.get()[-1] == "/" or entry.get()[-1] == "%"):
                    None
                else:
                    backspace()
                    entry.insert(entry.index(INSERT), "-")
    elif(entry.get()[-1] == ")"):
        entry.insert(entry.index(INSERT), "-")


btn_4 = Button(frame_3, text="4", width=10, height=3, bg="#FFFFFF", fg="black", relief=FLAT,
               font=('Helvetica', '10', 'bold'), command=entry_4)
btn_4.grid(row=3, column=0)

btn_5 = Button(frame_3, text="5", width=10, height=3, bg="#FFFFFF", fg="black", relief=FLAT,
               font=('Helvetica', '10', 'bold'), command=entry_5)
btn_5.grid(row=3, column=1)

btn_6 = Button(frame_3, text="6", width=10, height=3, bg="#FFFFFF", fg="black", relief=FLAT,
               font=('Helvetica', '10', 'bold'), command=entry_6)
btn_6.grid(row=3, column=2)

btn_subtraction = Button(frame_3, text="-", width=10, height=3, bg="#FFFFFF", fg="black",
                         font=('Helvetica', '10', 'bold'), relief=FLAT, command=entry_subtraction)
btn_subtraction.grid(row=3, column=3)


def entry_1():
    if (entry.get() == ""):
        entry.insert(entry.index(INSERT), "1")
    elif (entry.get()[-1] == ")"):
        entry.insert(entry.index(INSERT), "*1")
    else:
        entry.insert(entry.index(INSERT), "1")


def entry_2():
    if (entry.get() == ""):
        entry.insert(entry.index(INSERT), "2")
    elif (entry.get()[-1] == ")"):
        entry.insert(entry.index(INSERT), "*2")
    else:
        entry.insert(entry.index(INSERT), "2")


def entry_3():
    if (entry.get() == ""):
        entry.insert(entry.index(INSERT), "3")
    elif (entry.get()[-1] == ")"):
        entry.insert(entry.index(INSERT), "*3")
    else:
        entry.insert(entry.index(INSERT), "3")


def entry_addition():
    try:
        if(type(int(entry.get()[-1])) == type(1)):
            entry.insert(entry.index(INSERT), "+")
    except:
        None
    if (entry.get() == ""):
        entry.insert(0, '')
    if(entry.get()=="("):
        None
    elif (entry.get()[-1] == "+" or entry.get()[-1] == "-" or entry.get()[-1] == "*" or entry.get()[-1] == "/" or
          entry.get()[-1] == "%"):
        if(entry.get()[-2] == "("):
            None
        elif (entry.get()[-2] == ")"):
            backspace()
            entry.insert(entry.index(INSERT), "+")
        else:
            try:
                if(type(int(entry.get()[-2])) == type(1)):
                    backspace()
                    entry.insert(entry.index(INSERT), "+")
            except:
                result = entry.get()
                if (result[-1] == '('):
                    entry.insert(entry.index(INSERT), "+")
                elif (entry.get()[-2] == "(" or entry.get()[-2] == ")"):
                    None
                elif (result[0] == '('):
                    entry.insert(entry.index(INSERT), "+")
                elif(entry.get()[-1] == "+" or entry.get()[-1] == "-" or entry.get()[-1] == "*" or entry.get()[-1] == "/" or entry.get()[-1] == "%"):
                    None
                else:
                    backspace()
                    entry.insert(entry.index(INSERT), "+")
    elif(entry.get()[-1] == ")"):
        entry.insert(entry.index(INSERT), "+")

btn_1 = Button(frame_3, text="1", width=10, height=3, bg="#FFFFFF", fg="black", relief=FLAT,
               font=('Helvetica', '10', 'bold'), command=entry_1)
btn_1.grid(row=4, column=0)

btn_2 = Button(frame_3, text="2", width=10, height=3, bg="#FFFFFF", fg="black", relief=FLAT,
               font=('Helvetica', '10', 'bold'), command=entry_2)
btn_2.grid(row=4, column=1)

btn_3 = Button(frame_3, text="3", width=10, height=3, bg="#FFFFFF", fg="black", relief=FLAT,
               font=('Helvetica', '10', 'bold'), command=entry_3)
btn_3.grid(row=4, column=2)

btn_addition = Button(frame_3, text="+", width=10, height=3, bg="#FFFFFF", fg="black", relief=FLAT,
                      font=('Helvetica', '10', 'bold'), command=entry_addition)
btn_addition.grid(row=4, column=3)


def entry_pos_neg():
    if(entry.get()==""):
        entry.insert(0,'-')
    elif(entry.get()[0] == '-'):
        entry.delete(0,1)
        entry.insert(0,"+")
    elif(entry.get()[0] == '+'):
        entry.delete(0, 1)
        entry.insert(0,"-")
    else:
        entry.insert(0, "-")


def entry_0():
    if (entry.get() == ""):
        entry.insert(entry.index(INSERT), "0")
    elif (entry.get()[-1] == ")"):
        entry.insert(entry.index(INSERT), "*0")
    else:
        entry.insert(entry.index(INSERT), "0")


def entry_decimal():
    result = entry.get()
    if(result == "" or result[-1] == "("):
        entry.insert(entry.index(INSERT), "0.")
    elif(result[-1] == "."):
        None
    elif(result[-1] == ")"):
        entry.insert(entry.index(INSERT), "*0.")
    elif(48 > ord(result[-1]) or ord(result[-1]) > 57):
        entry.insert(entry.index(INSERT), "0.")
    else:
        temp = result[::-1]
        valid = True
        for i in range(len(temp)):
            if(temp[i] == "."):
                valid = False
                break
            elif(48 > ord(temp[i]) or ord(temp[i]) > 57):
                break
        entry.insert(entry.index(INSERT),".") if(valid) else None


def entry_result():
    try:
        result = eval(entry.get())
        entry.delete(0,END)
        entry.insert(0,result)
    except:
        None


btn_pos_neg = Button(frame_3, text="+/-", width=10, height=3, bg="#FFFFFF", fg="black", relief=FLAT,
                     font=('Helvetica', '10', 'bold'), command=entry_pos_neg)
btn_pos_neg.grid(row=5, column=0)

btn_0 = Button(frame_3, text="0", width=10, height=3, bg="#FFFFFF", fg="black", relief=FLAT,
               font=('Helvetica', '10', 'bold'), command=entry_0)
btn_0.grid(row=5, column=1)

btn_decimal = Button(frame_3, text=".", width=10, height=3, bg="#FFFFFF", fg="black", relief=FLAT,
                     font=('Helvetica', '10', 'bold'), command=entry_decimal)
btn_decimal.grid(row=5, column=2)

btn_equals = Button(frame_3, text="=", width=10, height=3, bg="#00cc00", fg="black", relief=FLAT,
                    font=('Helvetica', '10', 'bold'), command=entry_result)
btn_equals.grid(row=5, column=3)

btn_max_min.bind("<Enter>", btn_max_min_on_enter)
btn_max_min.bind("<Leave>", btn_max_min_on_leave)

btn_clear.bind("<Enter>", btn_clear_on_enter)
btn_clear.bind("<Leave>", btn_clear_on_leave)

btn_modulus.bind("<Enter>", btn_modulus_on_enter)
btn_modulus.bind("<Leave>", btn_modulus_on_leave)

btn_backspace.bind("<Enter>",btn_backspace_on_enter)
btn_backspace.bind("<Leave>",btn_backspace_on_leave)

btn_history.bind("<Enter>",btn_history_on_enter)
btn_history.bind("<Leave>",btn_history_on_leave)

btn_parenthesis_start.bind("<Enter>",btn_parenthesis_start_on_enter)
btn_parenthesis_start.bind("<Leave>",btn_parenthesis_start_on_leave)

btn_parenthesis_end.bind("<Enter>",btn_parenthesis_end_on_enter)
btn_parenthesis_end.bind("<Leave>",btn_parenthesis_end_on_leave)

btn_division.bind("<Enter>", btn_division_on_enter)
btn_division.bind("<Leave>", btn_division_on_leave)

btn_7.bind("<Enter>", btn_7_on_enter)
btn_7.bind("<Leave>", btn_7_on_leave)

btn_8.bind("<Enter>", btn_8_on_enter)
btn_8.bind("<Leave>", btn_8_on_leave)

btn_9.bind("<Enter>", btn_9_on_enter)
btn_9.bind("<Leave>", btn_9_on_leave)

btn_multiplication.bind("<Enter>", btn_multiplication_on_enter)
btn_multiplication.bind("<Leave>", btn_multiplication_on_leave)

btn_4.bind("<Enter>", btn_4_on_enter)
btn_4.bind("<Leave>", btn_4_on_leave)

btn_5.bind("<Enter>", btn_5_on_enter)
btn_5.bind("<Leave>", btn_5_on_leave)

btn_6.bind("<Enter>", btn_6_on_enter)
btn_6.bind("<Leave>", btn_6_on_leave)

btn_subtraction.bind("<Enter>", btn_subtraction_on_enter)
btn_subtraction.bind("<Leave>", btn_subtraction_on_leave)

btn_1.bind("<Enter>", btn_1_on_enter)
btn_1.bind("<Leave>", btn_1_on_leave)

btn_2.bind("<Enter>", btn_2_on_enter)
btn_2.bind("<Leave>", btn_2_on_leave)

btn_3.bind("<Enter>", btn_3_on_enter)
btn_3.bind("<Leave>", btn_3_on_leave)

btn_addition.bind("<Enter>", btn_addition_on_enter)
btn_addition.bind("<Leave>", btn_addition_on_leave)

btn_pos_neg.bind("<Enter>", btn_pos_neg_on_enter)
btn_pos_neg.bind("<Leave>", btn_pos_neg_on_leave)

btn_0.bind("<Enter>", btn_0_on_enter)
btn_0.bind("<Leave>", btn_0_on_leave)

btn_decimal.bind("<Enter>", btn_decimal_on_enter)
btn_decimal.bind("<Leave>", btn_decimal_on_leave)

btn_equals.bind("<Enter>", btn_equals_on_enter)
btn_equals.bind("<Leave>", btn_equals_on_leave)

frame_3.grid(row=1, column=1)


def dark_main():
    root["bg"] = "black"
    entry.config(bg="black", fg="white")
    btn_max_min.config(bg="black", fg="white")
    btn_clear.config(bg="black", fg="red")
    btn_modulus.config(bg="black", fg="white")
    btn_backspace.config(bg="black", fg="orange")
    btn_history.config(bg="black", fg="white")
    btn_parenthesis_start.config(bg="black", fg="white")
    btn_parenthesis_end.config(bg="black", fg="white")
    btn_division.config(bg="black", fg="white")
    btn_7.config(bg="black", fg="white")
    btn_8.config(bg="black", fg="white")
    btn_9.config(bg="black", fg="white")
    btn_multiplication.config(bg="black", fg="white")
    btn_4.config(bg="black", fg="white")
    btn_5.config(bg="black", fg="white")
    btn_6.config(bg="black", fg="white")
    btn_subtraction.config(bg="black", fg="white")
    btn_1.config(bg="black", fg="white")
    btn_2.config(bg="black", fg="white")
    btn_3.config(bg="black", fg="white")
    btn_addition.config(bg="black", fg="white")
    btn_pos_neg.config(bg="black", fg="white")
    btn_0.config(bg="black", fg="white")
    btn_decimal.config(bg="black", fg="white")
    btn_equals.config(bg="black", fg="green")
    #entry.configure(cursor="dotbox green")


def light_main():
    root.config(bg="white")
    entry.config(bg="white", fg="black")
    btn_max_min.config(bg="white", fg="black")
    btn_clear.config(bg="red", fg="white")
    btn_modulus.config(bg="white", fg="black")
    btn_backspace.config(bg="white", fg="orange")
    btn_history.config(bg="white", fg="black")
    btn_parenthesis_start.config(bg="white", fg="black")
    btn_parenthesis_end.config(bg="white", fg="black")
    btn_division.config(bg="white", fg="black")
    btn_7.config(bg="white", fg="black")
    btn_8.config(bg="white", fg="black")
    btn_9.config(bg="white", fg="black")
    btn_multiplication.config(bg="white", fg="black")
    btn_4.config(bg="white", fg="black")
    btn_5.config(bg="white", fg="black")
    btn_6.config(bg="white", fg="black")
    btn_subtraction.config(bg="white", fg="black")
    btn_1.config(bg="white", fg="black")
    btn_2.config(bg="white", fg="black")
    btn_3.config(bg="white", fg="black")
    btn_addition.config(bg="white", fg="black")
    btn_pos_neg.config(bg="white", fg="black")
    btn_0.config(bg="white", fg="black")
    btn_decimal.config(bg="white", fg="black")
    btn_equals.config(bg="#00cc00", fg="white")


if (9 <= t <= 18):
    light_main()
else:
    dark_main()

root.config(bg="blue")
root.mainloop()
