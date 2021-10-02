import os
import re
import sys
import json
import random
import string
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

password = "GBPAdmin123"

thankyou_lbl, ok_btn = "", ""
otp_num, vote_rad, vote_value = "", "", ""
aadhar_num, aadh_no, generate_pass = "", "", ""
radio_btn1, radio_btn2, radio_btn3 = "", "", ""
root, click_lbl, bg_img, parties_lbl = "", "", "", ""
head_lbl1, enter_lbl1, otp_entry, otp_sub = "", "", "", ""
head_lbl, enter_lbl, aadhar_entry, otp_btn = "", "", "", ""

mult = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 0, 6, 7, 8, 9, 5], [2, 3, 4, 0, 1, 7, 8, 9, 5, 6],
        [3, 4, 0, 1, 2, 8, 9, 5, 6, 7], [4, 0, 1, 2, 3, 9,
                                         5, 6, 7, 8], [5, 9, 8, 7, 6, 0, 4, 3, 2, 1],
        [6, 5, 9, 8, 7, 1, 0, 4, 3, 2], [7, 6, 5, 9, 8, 2,
                                         1, 0, 4, 3], [8, 7, 6, 5, 9, 3, 2, 1, 0, 4],
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]]

perm = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 5, 7, 6, 2, 8, 3, 0, 9, 4], [5, 8, 0, 3, 7, 9, 6, 1, 4, 2],
        [8, 9, 1, 6, 0, 4, 3, 5, 2, 7], [9, 4, 5, 3, 1, 2,
                                         6, 8, 7, 0], [4, 2, 8, 6, 5, 7, 3, 9, 0, 1],
        [2, 7, 9, 3, 8, 0, 6, 4, 1, 5], [7, 0, 4, 6, 9, 1, 3, 2, 5, 8]]


def onclosing():
    print("Window closed!")
    
    if messagebox.askyesnocancel("Info", "Are you sure you want to exit?"):
        sys.exit()


def destroy_result_win():
    result_head_lbl.destroy()
    bjp_head_lbl.destroy()
    aap_head_lbl.destroy()
    inc_head_lbl.destroy()
    bjp_vote_lbl.destroy()
    aap_vote_lbl.destroy()
    inc_vote_lbl.destroy()
    back_lbl.destroy()

    set_main_components()


def result_win():
    global result_head_lbl, bjp_head_lbl, aap_head_lbl, inc_head_lbl, bjp_vote_lbl, aap_vote_lbl, inc_vote_lbl, back_lbl

    admin_lbl.destroy()
    admin_pass_lbl.destroy()
    admin_entry.destroy()
    result_btn.destroy()

    result_head_lbl = Label(root, text="Voting Results", font=(
        "Times New Roman", 28, "bold"), height="2", bg="white", fg="#1031CB")
    result_head_lbl.place(x=550, y=260)

    bjp_head_lbl = Label(root, text="BJP", font=(
        "Times New Roman", 20, "bold"), height="2", bg="white", fg="orange")
    bjp_head_lbl.place(x=500, y=340)
    aap_head_lbl = Label(root, text="AAP", font=(
        "Times New Roman", 20, "bold"), height="2", bg="white", fg="blue")
    aap_head_lbl.place(x=500, y=390)
    inc_head_lbl = Label(root, text="INC", font=(
        "Times New Roman", 20, "bold"), height="2", bg="white", fg="green")
    inc_head_lbl.place(x=500, y=440)

    bjp_vote_lbl = Label(root, text=bjp_votes, font=(
        "Times New Roman", 20, "bold"), height="2", bg="white", fg="orange")
    bjp_vote_lbl.place(x=800, y=340)
    aap_vote_lbl = Label(root, text=aap_votes, font=(
        "Times New Roman", 20, "bold"), height="2", bg="white", fg="blue")
    aap_vote_lbl.place(x=800, y=390)
    inc_vote_lbl = Label(root, text=inc_votes, font=(
        "Times New Roman", 20, "bold"), height="2", bg="white", fg="green")
    inc_vote_lbl.place(x=800, y=440)

    back_lbl = Label(root, text="<< back", font=(
        "Times New Roman", 15, "italic"), fg="blue", bg="white")
    back_lbl.place(x=500, y=500)
    back_lbl.bind("<Button-1>", lambda e: destroy_result_win())


def calculate_votes():
    global bjp_votes, aap_votes, inc_votes

    vote_file = open("votes/votes.json", "r")
    read_votes = json.load(vote_file)

    bjp_votes = read_votes["BJP"]
    aap_votes = read_votes["AAP"]
    inc_votes = read_votes["INC"]

    result_win()


def check_admin_pass():
    admin = admin_pass.get()

    if admin != "":
        if admin == password:
            messagebox.showinfo("Success", "You're Welcome*")
            calculate_votes()
        else:
            messagebox.showerror("Error", "Incorrect Password*")
    else:
        messagebox.showerror("Error", "Password Required*")


def result_components():
    global admin_lbl, admin_pass_lbl, admin_entry, result_btn
    global admin_pass

    admin_pass = StringVar()

    admin_lbl = Label(root, text="Admin Details", font=(
        "Times New Roman", 28, "bold"), height="2", bg="white", fg="#1031CB")
    admin_lbl.place(x=530, y=260)

    admin_pass_lbl = Label(root, text="Admin Password", font=(
        "Times New Roman", 24, "bold"), bg="white", fg="springgreen4")
    admin_pass_lbl.place(x=360, y=360)

    admin_entry = Entry(root, textvariable=admin_pass, width="30", bg="white", font=(
        "Times New Roman", 18, "bold"), fg="Orange")
    admin_entry.place(x=630, y=370)
    admin_entry.focus_set()

    result_btn = Button(root, text="Get Result", width="26", height="2", bg="orange", font=(
        "Times New Roman", 12, "bold"), fg="white", command=check_admin_pass)
    result_btn.place(x=530, y=460)


def go_to_admin():
    head_lbl.destroy()
    enter_lbl.destroy()
    aadhar_entry.destroy()
    otp_btn.destroy()
    admin_btn.destroy()

    result_components()


def redirect_to_main():
    thankyou_lbl.destroy()
    ok_btn.destroy()

    set_main_components()


def thankyou_msg():
    global thankyou_lbl, ok_btn

    thankyou_lbl = Label(root, text="Thank you for your vote.", font=(
        "Times New Roman", 28, "bold"), bg="White", fg="orange")
    thankyou_lbl.place(x=390, y=300)

    ok_btn = Button(root, text="OK", bg="Orange", fg="springgreen4", font=(
        "Times New Roman", 15, "bold"), width="26", height="2", command=redirect_to_main)
    ok_btn.place(x=450, y=450)


def selected_btn():
    parties_lbl.destroy()
    radio_btn1.destroy()
    radio_btn2.destroy()
    radio_btn3.destroy()

    thankyou_msg()


def get_vote():
    global vote_value

    vote_value = vote_rad.get()

    if vote_value == 1:
        if "votes.json" in os.listdir("votes/"):
            vote_file = open("votes/"+"votes.json", "r")
            read_votes = json.load(vote_file)
            get_bjp_vote = read_votes["BJP"]
            vote_file.close()

            open_vote_file = open("votes/"+"votes.json", "w")
            read_votes["BJP"] = get_bjp_vote + 1
            json.dump(read_votes, open_vote_file)
            open_vote_file.close()

    elif vote_value == 2:
        if "votes.json" in os.listdir("votes/"):
            vote_file = open("votes/"+"votes.json", "r")
            read_votes = json.load(vote_file)
            get_aap_vote = read_votes["AAP"]
            vote_file.close()

            open_vote_file = open("votes/"+"votes.json", "w")
            read_votes["AAP"] = get_aap_vote + 1
            json.dump(read_votes, open_vote_file)
            open_vote_file.close()
    else:
        if "votes.json" in os.listdir("votes/"):
            vote_file = open("votes/"+"votes.json", "r")
            read_votes = json.load(vote_file)
            get_inc_vote = read_votes["INC"]
            vote_file.close()

            open_vote_file = open("votes/"+"votes.json", "w")
            read_votes["INC"] = get_inc_vote + 1
            json.dump(read_votes, open_vote_file)
            open_vote_file.close()

    read_obj = open("aadhars/"+"aadhar_numbers.json", "r")
    get_load = json.load(read_obj)
    read_obj.close()

    get_load[aadh_no] = TRUE
    write_obj = open("aadhars/"+"aadhar_numbers.json", "w")
    json.dump(get_load, write_obj)
    write_obj.close()

    selected_btn()


def vote_win():
    head_lbl1.destroy()
    enter_lbl1.destroy()
    otp_entry.destroy()
    otp_sub.destroy()

    global radio_btn1, radio_btn2, radio_btn3, parties_lbl
    global vote_rad

    vote_rad = IntVar()

    parties_lbl = Label(root, text="Give Your Support", font=(
        "times new roman", 30, "bold"), bg="white", fg="springgreen4")
    parties_lbl.place(x=470, y=300)

    radio_btn1 = Radiobutton(root, text="Bharatiya Janata Party", variable=vote_rad, bg="white", font=(
        "Times New Roman", 15, "bold"), fg="Orange", value=1, command=get_vote)
    radio_btn1.place(x=530, y=380)
    radio_btn2 = Radiobutton(root, text="Aam Aadmi Party", variable=vote_rad, bg="White", font=(
        "Times New Roman", 15, "bold"), fg="#1031CB", value=2, command=get_vote)
    radio_btn2.place(x=530, y=420)
    radio_btn3 = Radiobutton(root, text="Indian National Congress", variable=vote_rad, bg="white", font=(
        "Times New Roman", 15, "bold"), fg="springgreen4", value=3, command=get_vote)
    radio_btn3.place(x=530, y=460)


def check_empty_otp():
    num = otp_num.get()

    if num != "":
        if messagebox.showinfo("Success", "You're Welcome*"):
            vote_win()
    else:
        messagebox.showerror("Error", "OTP Required*")


def otp_win():
    head_lbl.destroy()
    enter_lbl.destroy()
    aadhar_entry.destroy()
    otp_btn.destroy()
    admin_btn.destroy()

    global head_lbl1, enter_lbl1, otp_entry, otp_sub
    global otp_num

    otp_num = StringVar()

    head_lbl1 = Label(root, text="OTP Details", font=(
        "Times New Roman", 28, "bold"), height="2", bg="white", fg="#1031CB")
    head_lbl1.place(x=530, y=260)

    enter_lbl1 = Label(root, text="OTP Number", font=(
        "Times New Roman", 24, "bold"), bg="White", fg="orange")
    enter_lbl1.place(x=360, y=360)

    otp_entry = Entry(root, textvariable=otp_num, width="30",  bg="white", font=(
        "Times New Roman", 18, "bold"), fg="Orange")
    otp_entry.place(x=630, y=370)
    otp_entry.focus_set()
    otp_entry.insert(END, generate_pass)

    otp_sub = Button(root, text="Submit", width="26", height="2", bg="springgreen4", font=(
        "Times New Roman", 12, "bold"), fg="white", command=check_empty_otp)
    otp_sub.place(x=530, y=460)


def create_otp(size):
    global generate_pass

    generate_pass = ''.join([random.choice(
        string.ascii_uppercase + string.ascii_lowercase + string.digits) for n in range(size)])

    if messagebox.showinfo("OTP", generate_pass):
        otp_win()


def final_checkup():
    if "aadhar_numbers.json" in os.listdir("aadhars/"):
        file1 = open("aadhars/"+"aadhar_numbers.json", "r")
        file2 = json.load(file1)
        file1.close()

        if file2[aadh_no] == FALSE:
            if messagebox.showinfo("Success", "Get Your OTP..."):
                create_otp(6)
        else:
            messagebox.showerror("Error", "Already Voted*")
    else:
        messagebox.showerror("Error", "File Not Exits*")


def Validate(aadharNum):
    try:
        i = len(aadharNum)
        j = 0
        x = 0

        while i > 0:
            i -= 1
            x = mult[x][perm[(j % 8)][int(aadharNum[i])]]
            j += 1

        if x == 0:
            messagebox.showinfo('Success', 'Valid Aadhar Number*')

            file_obj = open("aadhars/"+"aadhar_numbers.json", "r")
            loaded_file = json.load(file_obj)
            file_obj.close()

            if aadh_no not in loaded_file.keys():
                loaded_file[aadh_no] = FALSE
                filename_json = "aadhars/"
                file_obj = open(filename_json+"aadhar_numbers.json", "w")
                json.dump(loaded_file, file_obj)
                file_obj.close()

            final_checkup()

        else:
            messagebox.showerror('Error', 'Invalid Aadhar Number*')

    except ValueError:
        messagebox.showerror('Error', 'Invalid Aadhar Number*')

    except IndexError:
        messagebox.showerror('Error', 'Invalid Aadhar Number*')


def check_aadhar_num():
    global aadh_no

    aadh_no = aadhar_num.get()

    regex = "^([0-9]){12}$"

    if aadh_no != "":
        if re.search(regex, aadh_no):
            Validate(aadh_no)
        else:
            messagebox.showerror("Error", "Invalid Aadhar Number*")
    else:
        messagebox.showerror("Error", "Aadhar Number Required*")


def set_main_components():
    click_lbl.destroy()

    global head_lbl, enter_lbl, aadhar_entry, otp_btn, admin_btn, back_lbl
    global aadhar_num

    aadhar_num = StringVar()

    head_lbl = Label(root, text="Aadhar Details", font=(
        "Times New Roman", 28, "bold"), height="2", bg="white", fg="#1031CB")
    head_lbl.place(x=530, y=260)

    enter_lbl = Label(root, text="Aadhar Number", font=(
        "Times New Roman", 24, "bold"), bg="white", fg="springgreen4")
    enter_lbl.place(x=360, y=360)

    aadhar_entry = Entry(root, textvariable=aadhar_num, width="30", bg="white", font=(
        "Times New Roman", 18, "bold"), fg="Orange")
    aadhar_entry.place(x=630, y=370)
    aadhar_entry.focus_set()

    otp_btn = Button(root, text="Generate OTP", width="20", height="2", bg="orange", font=(
        "Times New Roman", 12, "bold"), fg="white", command=check_aadhar_num)
    otp_btn.place(x=450, y=460)

    admin_btn = Button(root, text="Admin", width="20", height="2", bg="Green", font=(
        "Times New Roman", 12, "bold"), fg="white", command=go_to_admin)
    admin_btn.place(x=700, y=460)


def main():
    global root
    global click_lbl, bg_img

    root = Tk()
    root.title("Election Survey")
    width = 1366
    height = 768
    root.geometry(f"{width}x{height}+0+0")
    root.iconbitmap("logo.ico")
    root.resizable(width=False, height=False)

    bg_img = Image.open("images/img.jpg")
    bg_img = bg_img.resize((width, height))
    bg_img = ImageTk.PhotoImage(bg_img)

    bg_lbl = Label(root, text="", image=bg_img)
    bg_lbl.image = bg_img
    bg_lbl.pack()

    click_lbl = Label(root, text="Go to Survey", fg="#1031CB", bg="white", font=(
        "Times New Roman", 40, "italic"), height="2", cursor="hand2")
    click_lbl.place(x=535, y=320)
    click_lbl.bind("<Button-1>", lambda e: set_main_components())

    root.mainloop()


if __name__ == "__main__":
    main()
