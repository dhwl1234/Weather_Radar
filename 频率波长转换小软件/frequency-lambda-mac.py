import tkinter as tk
from tkinter import font


def convert():
    value = entry.get()
    unit = unit_var.get()
    conversion_type = conversion_var.get()
    c = c_entry.get()

    # 检查输入值是否为数字
    try:
        float(value)
    except ValueError:
        result_label.config(text="输入错误，请重新输入")
        return

    # 检查光速是否为数字
    try:
        float(c)
    except ValueError:
        result_label.config(text="光速输入错误，请重新输入")
        return

    c = float(c)  # 类型转化

    if conversion_type == "Frequency":
        if unit == "THz":
            result = f"Converted Wavelength: { c / (float(value) * 1e12)} m"
            result += f"\nConverted Wavelength: {c / (float(value) * 1e12) * 100} cm"
            result += f"\nConverted Wavelength: {c / (float(value) * 1e12) * 1000} mm"
            result += f"\nConverted Wavelength: {c / (float(value) * 1e12) * 1000000} um"
        elif unit == "GHz":
            result = f"Converted Wavelength: { c / (float(value) * 1e9)} m"
            result += f"\nConverted Wavelength: {c / (float(value) * 1e9) * 100} cm"
            result += f"\nConverted Wavelength: {c / (float(value) * 1e9) * 1000} mm"
            result += f"\nConverted Wavelength: {c / (float(value) * 1e9) * 1000000} um"
        elif unit == "MHz":
            result = f"Converted Wavelength: { c / (float(value) * 1e6)} m"
            result += f"\nConverted Wavelength: { c / (float(value) * 1e6) * 100} cm"
            result += f"\nConverted Wavelength: {c / (float(value) * 1e6) * 1000} mm"
            result += f"\nConverted Wavelength: {c / (float(value) * 1e6) * 1000000} um"
        elif unit == "Hz":
            result = f"Converted Wavelength: { c / float(value) } m"
            result += f"\nConverted Wavelength: { c / float(value) * 10} cm"
            result += f"\nConverted Wavelength: { c / float(value) * 100} mm"
            result += f"\nConverted Wavelength: {c / float(value) * 100000} um"
    else:
        if unit == "m":
            result = f"Converted Frequency: {c / float(value) / 1e12} THz"
            result += f"\nConverted Frequency: {c / float(value) /1e9} GHz"
            result += f"\nConverted Frequency: {c / float(value) / 1e6} MHz"
            result += f"\nConverted Frequency: {c / float(value)} Hz"
        elif unit == "cm":
            result = f"Converted Frequency: {c / (float(value)/100) / 1e12} THz"
            result += f"\nConverted Frequency: {c / (float(value)/100) / 1e9} GHz"
            result += f"\nConverted Frequency: {c / (float(value)/100) / 1e6} MHz"
            result += f"\nConverted Frequency: {c / (float(value)/100)} Hz"
        elif unit == "mm":
            result = f"Converted Frequency: {c / (float(value) / 1000) / 1e12} THz"
            result += f"\nConverted Frequency: {c / (float(value)/1000) / 1e9} GHz"
            result += f"\nConverted Frequency: {c / (float(value)/1000) / 1e6} MHz"
            result += f"\nConverted Frequency: {c / (float(value)/1000)} Hz"
        elif unit == "um":
            result = f"Converted Frequency: {c / (float(value) / 1000000) / 1e12} THz"
            result += f"\nConverted Frequency: {c / (float(value)/1000000) / 1e9} GHz"
            result += f"\nConverted Frequency: {c / (float(value)/1000000) / 1e6} MHz"
            result += f"\nConverted Frequency: {c / (float(value)/1000000)} Hz"

    result_label.config(text=result, font=custom_font)

def on_conversion_change(*args):
    conversion_type = conversion_var.get()
    if conversion_type == "Frequency":
        unit_dropdown['menu'].delete(0, 'end')
        for option in unit_options_freq:
            unit_dropdown['menu'].add_command(label=option, command=tk._setit(unit_var, option))
        unit_var.set("GHz")
    else:
        unit_dropdown['menu'].delete(0, 'end')
        for option in unit_options_wavelength:
            unit_dropdown['menu'].add_command(label=option, command=tk._setit(unit_var, option))
        unit_var.set("m")

# 创建主窗口
window = tk.Tk()
# 设置窗口标题
window.title("波长频率自动换算小软件")

# 运行主循环
# 设置窗口大小
window.geometry("600x400")

# 创建一个框架
frame = tk.Frame(window)
frame.pack(fill=tk.BOTH, expand=True)

# 添加标题
title_label = tk.Label(frame, text="波长频率自动换算小软件", font=("Arial", 30), pady=0)
title_label.grid(row=0, column=2, columnspan=1)  # 设置标题所在的单元格位置和跨列数量

# 创建输入框
entry = tk.Entry(frame)
entry.grid(row=1, column=2, padx=0, pady=10)

# 创建下拉选项
conversion_var = tk.StringVar()
conversion_var.set("Frequency")
conversion_options = ["Frequency", "Wavelength"]
conversion_dropdown = tk.OptionMenu(frame, conversion_var, *conversion_options, command=on_conversion_change)
conversion_dropdown.config(font=14)
conversion_dropdown.grid(row=1, column=1, padx=0, pady=10, sticky="e")
# 创建单位下拉选项
unit_var = tk.StringVar()
unit_var.set("GHz")
unit_options_freq = ["THz", "GHz", "MHz", "Hz"]
unit_options_wavelength = ["m", "cm", "mm", "um"]
unit_dropdown = tk.OptionMenu(frame, unit_var, *unit_options_freq)
unit_dropdown.config(font=14)
unit_dropdown.grid(row=1, column=3, padx=0, pady=10, sticky="w")

# 创建确定按钮
button = tk.Button(frame, text="确定", command=convert, font=14)
button.grid(row=2, column=3, padx=0, pady=10, sticky="w")

# 光速输入框
c_label = tk.Label(frame, text="光速 (m/s):", font=14)
c_label.grid(row=2, column=1, padx=0, pady=10)
c_entry = tk.Entry(frame)
c_entry.insert(0, "299792458")
c_entry.grid(row=2, column=2, padx=0, pady=10)

# 创建结果标签
result_label = tk.Label(frame, text="")
result_label.grid(row=3, column=1, columnspan=3, padx=10, pady=20)

# 自动调整内容布局
frame.grid_rowconfigure(0, weight=1)
frame.grid_rowconfigure(1, weight=1)
frame.grid_rowconfigure(3, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_columnconfigure(2, weight=1)
frame.grid_columnconfigure(3, weight=1)
# 创建自定义字体
custom_font = font.Font(family="Arial", size=20)  # 这里将字体设置为Arial，字体大小设置为16

# 运行主循环
window.mainloop()