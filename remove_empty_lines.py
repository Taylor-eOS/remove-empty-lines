import tkinter as tk

def remove_empty_lines():
    code = text.get("1.0", tk.END)
    lines = code.splitlines()
    prefixes = ["def ", "void ", "uint8_t ", "float "]
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
    text.focus_set()
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

root.bind_all("<Control-a>", select_all)
root.bind_all("<Control-A>", select_all)
root.bind_all("<Control-c>", copy_text)
root.bind_all("<Control-C>", copy_text)
root.bind_all("<Control-x>", cut_text)
root.bind_all("<Control-X>", cut_text)
root.bind_all("<Control-v>", paste_text)
root.bind_all("<Control-V>", paste_text)
root.bind_all("<Command-a>", select_all)
root.bind_all("<Command-c>", copy_text)
root.bind_all("<Command-x>", cut_text)
root.bind_all("<Command-v>", paste_text)

root.mainloop()

