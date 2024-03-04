from tkinter import *
from tkinter import messagebox


# Настройки с окном программы
root = Tk()
root.title('Calculate')
root.geometry('290x360+500+100')
root.resizable(False, False)
# photo = PhotoImage(file='calc.png')
# root.iconphoto(False, photo)
root['bg'] = '#F08A5D'
# Основные кнопки калькулятора
column = Entry(root, justify=RIGHT, font=('Arial', 15), width=15)
column.insert(0, '0')
column.grid(row=0, column=0, columnspan=4, ipadx=60, ipady=10, sticky='we')


# Add zero in entry
def column_insert(insert):
    value = column.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    column.delete(0, END)
    column.insert(0, value+insert)


# Add opetation in calculate
def column_calc(calc):
    value = column.get()
    if value[-1] in '-/*+':
        value = value[-1]
    elif '+' in value or '-' or '*' or '/':
        calculate()
        value = column.get()
    column.delete(0, END)
    column.insert(0, value+calc)


# Equally result
def column_equally(equally):
    value = column.get() + str(equally)
    column.delete(0, END)
    column.insert(0, value)


def column_insert_make(insert):
    return Button(root, text=insert, bd=5, font=('Arial', 11), command=lambda: column_insert(insert))


def column_operation_make(calc):
    return Button(root, text=calc, bd=5, font=('Arial', 11), fg='#B83B5E', command=lambda: column_calc(calc))


def column_delete_make(delete):
    return Button(root, text=delete, bd=5, font=('Arial', 11), fg='#B83B5E', command=delete_all)


def delete_all():
    column.delete(0, END)
    column.insert(0, 0)


def calculate():
    value = column.get()
    if value[-1] in '*/-+':
        value = value+value[:-1]
    column.delete(0, END)
    try:
        column.insert(0, eval(value))
    except (NameError, SyntaxError):
        messagebox.showinfo('Внимание', 'Нужно вводить только цифры!')
        column.insert(0,0)
    except ZeroDivisionError:
        messagebox.showinfo('Внимание', 'На ноль делить нельзя!')
        column.insert(0, 0)




def column_equally_make(equally):
    return Button(root, text=equally, bd=5, font=('Arial', 11), fg='#B83B5E', command=calculate)


def press_key(event):
    print(repr(event.char))
    if event.char.isdigit():
        column_insert(event.char)
    elif event.char in '-*/+':
        column_calc(event.char)
    elif event.char in '\r':
        calculate()

column_insert_make('7') .grid(row=2, column=0, padx=1, pady=1, sticky='wens')
column_insert_make('8') .grid(row=2, column=1, padx=1, pady=1, sticky='wens')
column_insert_make('9') .grid(row=2, column=2, padx=1, pady=1, sticky='wens')
column_insert_make('4') .grid(row=3, column=0, padx=1, pady=1, sticky='wens')
column_insert_make('5') .grid(row=3, column=1, padx=1, pady=1, sticky='wens')
column_insert_make('6') .grid(row=3, column=2, padx=1, pady=1, sticky='wens')
column_insert_make('1') .grid(row=4, column=0, padx=1, pady=1, sticky='wens')
column_insert_make('2') .grid(row=4, column=1, padx=1, pady=1, sticky='wens')
column_insert_make('3') .grid(row=4, column=2, padx=1, pady=1, sticky='wens')
column_operation_make('+').grid(row=4, column=3, padx=1, pady=1, sticky='wens')
column_operation_make('0').grid(row=5, column=0, columnspan=2, padx=1, pady=1, sticky='wens')
column_operation_make(',').grid(row=5, column=2, padx=1, pady=1, sticky='wens')
column_equally_make('=').grid(row=5, column=3, padx=1, pady=1, sticky='wens')
column_operation_make('-').grid(row=3, column=3, padx=1, pady=1, sticky='wens')
column_delete_make('C').grid( row=1, column=0, padx=1, pady=1, columnspan=2, sticky ='wens')
column_operation_make('<').grid(row=1, column=2, padx=1, pady=1, sticky='wens')
column_operation_make('/').grid(row=1, column=3, padx=1, pady=1, sticky='wens')
column_operation_make('*').grid(row=2, column=3, padx=1, pady=1, sticky='wens')

root.grid_columnconfigure(0, minsize=60)
root.grid_columnconfigure(1, minsize=60)
root.grid_columnconfigure(2, minsize=60)
root.grid_columnconfigure(3, minsize=60)
root.grid_rowconfigure(0, minsize=60)
root.grid_rowconfigure(1, minsize=60)
root.grid_rowconfigure(2, minsize=60)
root.grid_rowconfigure(3, minsize=60)
root.grid_rowconfigure(4, minsize=60)
root.grid_rowconfigure(5, minsize=60)
root.grid_rowconfigure(6, minsize=60)

root.bind('<Key>', press_key)
root.mainloop()
