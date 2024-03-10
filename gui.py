import customtkinter as cus
from tkinter import Frame
import numpy as np
from recode_Stacking import Stacking
def create_main_window(accuracy_score, precision_score, recall_score, f1_score, model1, model2, model3):
    stacking = Stacking()
    # tạo cửa sổ chương trình
    root = cus.CTk()
    # đặt tiêu đề cho chương trình
    root.title("Phân loại giới tính dựa vào các đặc điểm cá nhân")

    # Tính toán tọa độ trung tâm của màn hình
    width = 700
    height = 700  # Đặt chiều cao mong muốn
    x = (root.winfo_screenwidth() - width) // 2
    y = (root.winfo_screenheight() - height) // 4
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))

    # tạo label tiêu đề
    cus.CTkLabel(root,
                 text="Phân loại giới tính dựa vào các đặc điểm cá nhân\n sử dụng Stacking",
                 text_color="#03a9fc",
                 font=("Time New Roman", 20, "bold")).pack(pady=20)

    # đặt khoảng cách giữa các widget
    cpadx = 20

    # hàm tạo custom label ngoài root
    def root_label(ctext="", font_size=15, color="#000000"):
        cfont = ("Time New Roman", font_size)
        return cus.CTkLabel(root, text=ctext, font=cfont, text_color=color).pack(anchor="w", padx=cpadx)

    # tạo label thông tin về dữ liệu và độ đo phân cụm
    root_label("Độ đo Accuracy: " + str("%.3f" % (accuracy_score)), color="#00FF00")
    root_label("Độ đo Precision: " + str("%.3f" % (precision_score)), color="#00FF00")
    root_label("Độ đo Recall: " + str("%.3f" % (recall_score)), color="#00FF00")
    root_label("Độ đo F1: " + str("%.3f" % (f1_score)), color="#00FF00")

    # tạo frame chứa các widget nhập liệu
    fr = cus.CTkFrame(root)
    fr.pack(pady=20)

    # hàm tạo custom label cho frame
    def fr_label(ctext="", crow=0, font_size=15):
        cfont = ("Time New Roman", font_size)
        return cus.CTkLabel(fr, text=ctext, font=cfont).grid(column=0, row=crow, sticky="w", padx=cpadx, pady=10)
    fr_label("long_hair:", 1)
    child_mort = cus.CTkEntry(fr, width=60)
    child_mort.grid(column=1, row=1, padx=20)

    fr_label("forehead_width_cm:", 2)
    exports = cus.CTkEntry(fr, width=60)
    exports.grid(column=1, row=2, padx=20)

    fr_label("forehead_height_cm:", 3)
    health = cus.CTkEntry(fr, width=60)
    health.grid(column=1, row=3, padx=20)

    fr_label("nose_wide:", 4)
    imports = cus.CTkEntry(fr, width=60)
    imports.grid(column=1, row=4, padx=20)

    fr_label("nose_long:", 5)
    income = cus.CTkEntry(fr, width=60)
    income.grid(column=1, row=5, padx=20)

    fr_label("lips_thin:", 6)
    inflation = cus.CTkEntry(fr, width=60)
    inflation.grid(column=1, row=6, padx=20)

    fr_label("distance_nose_to_lip_long:", 7)
    life_expec = cus.CTkEntry(fr, width=60)
    life_expec.grid(column=1, row=7, padx=20)

    # hàm dự đoán, in ra kết quả
    def get_data():
        try:
            data = np.array([[float(child_mort.get()), float(exports.get()), float(health.get()), float(imports.get()),
                              float(income.get()), float(inflation.get()), float(life_expec.get())]])
            y_pred_test = stacking.predict(model1, model2, model3,data)

            if y_pred_test[0] == 1:
                label_pre.configure(text="Giới tính dự đoán: Female", text_color="#00FF00")
            else:
                label_pre.configure(text="Giới tính dự đoán: Male", text_color="#00FF00")
        except ValueError:
            label_pre.configure(text="Lỗi: Hãy nhập số cho tất cả các trường", text_color="red")

    # Hàm xóa dữ liệu đầu vào
    def clear_data():
        for entry in [child_mort, exports, health, imports, income, inflation, life_expec]:
            entry.delete(0, 'end')

    bg_color = root.cget('bg')
    button_frame = Frame(root, background=bg_color)
    button_frame.pack()

    predict_btn = cus.CTkButton(button_frame, text="Dự đoán", command=get_data, width=50)
    predict_btn.pack(side="left", padx=10)
    clear_btn = cus.CTkButton(button_frame, text="Xóa giá trị", command=clear_data, width=50)
    clear_btn.pack(side="left")

    # tạo label dự đoán
    label_pre = cus.CTkLabel(root,
                             text="Dự đoán: ",
                             text_color="#00FF00",
                             font=("Time New Roman", 15))
    label_pre.pack(anchor="w", padx=cpadx, pady=10)
    root.mainloop()

def create_id3_window(accuracy_score, precision_score, recall_score, f1_score, model):
    # tạo cửa sổ chương trình
    root = cus.CTk()
    # đặt tiêu đề cho chương trình
    root.title("Phân loại giới tính dựa vào các đặc điểm cá nhân")

    # Tính toán tọa độ trung tâm của màn hình
    width = 700
    height = 700  # Đặt chiều cao mong muốn
    x = (root.winfo_screenwidth() - width) // 2
    y = (root.winfo_screenheight() - height) // 4
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))

    # tạo label tiêu đề
    cus.CTkLabel(root,
                 text="Phân loại giới tính dựa vào các đặc điểm cá nhân\nsử dụng ID3",
                 text_color="#03a9fc",
                 font=("Time New Roman", 20, "bold")).pack(pady=20)

    # đặt khoảng cách giữa các widget
    cpadx = 20

    # hàm tạo custom label ngoài root
    def root_label(ctext="", font_size=15, color="#000000"):
        cfont = ("Time New Roman", font_size)
        return cus.CTkLabel(root, text=ctext, font=cfont, text_color=color).pack(anchor="w", padx=cpadx)

    # tạo label thông tin về dữ liệu và độ đo phân cụm
    root_label("Độ đo Accuracy: " + str("%.3f" % (accuracy_score)), color="#00FF00")
    root_label("Độ đo Precision: " + str("%.3f" % (precision_score)), color="#00FF00")
    root_label("Độ đo Recall: " + str("%.3f" % (recall_score)), color="#00FF00")
    root_label("Độ đo F1: " + str("%.3f" % (f1_score)), color="#00FF00")

    # tạo frame chứa các widget nhập liệu
    fr = cus.CTkFrame(root)
    fr.pack(pady=20)

    # hàm tạo custom label cho frame
    def fr_label(ctext="", crow=0, font_size=15):
        cfont = ("Time New Roman", font_size)
        return cus.CTkLabel(fr, text=ctext, font=cfont).grid(column=0, row=crow, sticky="w", padx=cpadx, pady=10)

    fr_label("long_hair:", 1)
    child_mort = cus.CTkEntry(fr, width=60)
    child_mort.grid(column=1, row=1, padx=20)

    fr_label("forehead_width_cm:", 2)
    exports = cus.CTkEntry(fr, width=60)
    exports.grid(column=1, row=2, padx=20)

    fr_label("forehead_height_cm:", 3)
    health = cus.CTkEntry(fr, width=60)
    health.grid(column=1, row=3, padx=20)

    fr_label("nose_wide:", 4)
    imports = cus.CTkEntry(fr, width=60)
    imports.grid(column=1, row=4, padx=20)

    fr_label("nose_long:", 5)
    income = cus.CTkEntry(fr, width=60)
    income.grid(column=1, row=5, padx=20)

    fr_label("lips_thin:", 6)
    inflation = cus.CTkEntry(fr, width=60)
    inflation.grid(column=1, row=6, padx=20)

    fr_label("distance_nose_to_lip_long:", 7)
    life_expec = cus.CTkEntry(fr, width=60)
    life_expec.grid(column=1, row=7, padx=20)

    # hàm dự đoán, in ra kết quả
    def get_data():
        try:
            data = np.array([[float(child_mort.get()), float(exports.get()), float(health.get()), float(imports.get()),
                              float(income.get()), float(inflation.get()), float(life_expec.get())]])
            y_pred_test = model.predict(data)
            if y_pred_test[0] == 1:
                label_pre.configure(text="Giới tính dự đoán: Female", text_color="#00FF00")
            else:
                label_pre.configure(text="Giới tính dự đoán: Male", text_color="#00FF00")
        except ValueError:
            label_pre.configure(text="Lỗi: Hãy nhập số cho tất cả các trường", text_color="red")

    # Hàm xóa dữ liệu đầu vào
    def clear_data():
        for entry in [child_mort, exports, health, imports, income, inflation, life_expec]:
            entry.delete(0, 'end')

    bg_color = root.cget('bg')
    button_frame = Frame(root, background=bg_color)
    button_frame.pack()

    predict_btn = cus.CTkButton(button_frame, text="Dự đoán", command=get_data, width=50)
    predict_btn.pack(side="left", padx=10)
    clear_btn = cus.CTkButton(button_frame, text="Xóa giá trị", command=clear_data, width=50)
    clear_btn.pack(side="left")

    # tạo label dự đoán
    label_pre = cus.CTkLabel(root,
                             text="Dự đoán: ",
                             text_color="#00FF00",
                             font=("Time New Roman", 15))
    label_pre.pack(anchor="w", padx=cpadx, pady=10)
    root.mainloop()