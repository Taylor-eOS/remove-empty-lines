import tkinter as tk

def remove_empty_lines():
    code = text.get("1.0", tk.END)
    lines = code.splitlines()
    prefixes = ["def ", "void ", "uint8_t ", "float ", "int ", "class ", "if __name__ "]
    out = []
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        if line.strip() == "":
            j = i
            while j < n and lines[j].strip() == "":
                j += 1
            if j < n:
                next_line = lines[j].lstrip()
                if any(next_line.startswith(p) for p in prefixes):
                    out.append("")
            i = j
        else:
            out.append(line)
            i += 1
    cleaned = "\n".join(out)
    if code.endswith("\n"):
        cleaned += "\n"
    text.delete("1.0", tk.END)
    text.insert("1.0", cleaned)

def select_all(event=None):
    text.focus_set()
    text.tag_add("sel", "1.0", "end-1c")
    return "break"

def copy_text(event=None):
    if text.tag_ranges("sel"):
        sel = text.get("sel.first", "sel.last")
        root.clipboard_clear()
        root.clipboard_append(sel)
    else:
        root.bell()
    return "break"

def cut_text(event=None):
    if text.tag_ranges("sel"):
        sel = text.get("sel.first", "sel.last")
        root.clipboard_clear()
        root.clipboard_append(sel)
        text.delete("sel.first", "sel.last")
    else:
        root.bell()
    return "break"

def paste_text(event=None):
    try:
        content = root.clipboard_get()
    except tk.TclError:
        root.bell()
        return "break"
    text.insert("insert", content)
    return "break"

root = tk.Tk()
root.title("Remove Empty Lines")
frame = tk.Frame(root)
frame.pack(fill="both", expand=True)
text = tk.Text(frame, wrap="none", undo=True)
vsb = tk.Scrollbar(frame, orient="vertical", command=text.yview)
hsb = tk.Scrollbar(frame, orient="horizontal", command=text.xview)
text.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
vsb.pack(side="right", fill="y")
hsb.pack(side="bottom", fill="x")
text.pack(fill="both", expand=True)
button = tk.Button(root, text="Remove Empty Lines", command=remove_empty_lines)
button.pack(fill="x")
text.unbind_class("Text", "<Control-a>")
text.unbind_class("Text", "<Control-A>")
text.unbind_class("Text", "<Command-a>")
text.bind("<Control-a>", select_all)
text.bind("<Control-A>", select_all)
text.bind("<Command-a>", select_all)
text.unbind_class("Text", "<Control-c>")
text.unbind_class("Text", "<Control-C>")
text.unbind_class("Text", "<Command-c>")
text.bind("<Control-c>", copy_text)
text.bind("<Control-C>", copy_text)
text.bind("<Command-c>", copy_text)
text.unbind_class("Text", "<Control-x>")
text.unbind_class("Text", "<Control-X>")
text.unbind_class("Text", "<Command-x>")
text.bind("<Control-x>", cut_text)
text.bind("<Control-X>", cut_text)
text.bind("<Command-x>", cut_text)
text.unbind_class("Text", "<Control-v>")
text.unbind_class("Text", "<Control-V>")
text.unbind_class("Text", "<Command-v>")
text.bind("<Control-v>", paste_text)
text.bind("<Control-V>", paste_text)
text.bind("<Command-v>", paste_text)
root.bind("<Control-q>", lambda e: root.destroy())
root.mainloop()

