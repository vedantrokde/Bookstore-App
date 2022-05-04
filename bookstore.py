# importing libraries
from tkinter import *
from books_service import Books

# utils function
def get_selected_row(event):
    try:
        global selected_tuple
        index = list_panel.curselection()[0]
        selected_tuple = list_panel.get(index)
        title_input.delete(0, END)
        title_input.insert(END, selected_tuple[1])
        author_input.delete(0, END)
        author_input.insert(END, selected_tuple[2])
        year_input.delete(0, END)
        year_input.insert(END, selected_tuple[3])
        isbn_input.delete(0, END)
        isbn_input.insert(END, selected_tuple[4])
    except IndexError:
        pass


def view_command():
    list_panel.delete(0, END)
    for row in books.view():
        list_panel.insert(END, row)


def search_command():
    list_panel.delete(0, END)
    for row in books.search(
        title_value.get(), author_value.get(), year_value.get(), isbn_value.get()
    ):
        list_panel.insert(END, row)


def add_command():
    books.insert(
        title_value.get(), author_value.get(), year_value.get(), isbn_value.get()
    )
    list_panel.delete(0, END)
    list_panel.insert(
        END, (title_value.get(), author_value.get(), year_value.get(), isbn_value.get())
    )


def delete_command():
    books.delete(selected_tuple[0])


def update_command():
    books.update(
        selected_tuple[0],
        title_value.get(),
        author_value.get(),
        year_value.get(),
        isbn_value.get(),
    )


# defining instances
root = Tk()
root.wm_title('Bookpedia')
books = Books()

# input field panel
title_value = StringVar()
title_label = Label(root, text="Title")
title_input = Entry(root, textvariable=title_value)
title_label.grid(row=0, column=0)
title_input.grid(row=0, column=1)

author_value = StringVar()
author_label = Label(root, text="Author")
author_input = Entry(root, textvariable=author_value)
author_label.grid(row=0, column=2)
author_input.grid(row=0, column=3)

year_value = StringVar()
year_label = Label(root, text="Year")
year_input = Entry(root, textvariable=year_value)
year_label.grid(row=1, column=0)
year_input.grid(row=1, column=1)

isbn_value = StringVar()
isbn_label = Label(root, text="ISBN")
isbn_input = Entry(root, textvariable=isbn_value)
isbn_label.grid(row=1, column=2)
isbn_input.grid(row=1, column=3)

# view list panel
list_panel = Listbox(root, height=6, width=35)
list_panel.bind('<<ListboxSelect>>', get_selected_row)
list_panel.grid(row=2, column=0, rowspan=6, columnspan=2)

scroll_bar = Scrollbar(root)
scroll_bar.configure(command=list_panel.yview)
list_panel.configure(yscrollcommand=scroll_bar.set)
scroll_bar.grid(row=2, column=2, rowspan=6)

# action panel
view_button = Button(root, text="View all", width=12, command=view_command)
search_button = Button(root, text="Search Book", width=12, command=search_command)
add_button = Button(root, text="Add Book", width=12, command=add_command)
update_button = Button(root, text="Update Book", width=12, command=update_command)
delete_button = Button(root, text="Delete Book", width=12, command=delete_command)
close_button = Button(root, text="Exit", width=12, command=root.destroy)
view_button.grid(row=2, column=3)
search_button.grid(row=3, column=3)
add_button.grid(row=4, column=3)
update_button.grid(row=5, column=3)
delete_button.grid(row=6, column=3)
close_button.grid(row=7, column=3)

# rendering the root
root.mainloop()
