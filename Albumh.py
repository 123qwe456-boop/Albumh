import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class PhotoAlbumApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Photo Album")
        self.root.geometry("500x650")
        self.root.configure(bg="#f0f0f0")

        # Photo details dictionary
        self.photo_info = {
            "Title": "Serene Mountain Landscape",
            "Author": "Jane Doe",
            "Date Taken": "October 24, 2026",
            "Location": "Banff National Park, Canada",
            "Camera": "Sony α7R V - 50mm f/1.8"
        }

        # 1. Main Window Title Label
        self.title_label = tk.Label(
            root, 
            text="My Photo Album", 
            font=("Arial", 20, "bold"), 
            bg="#f0f0f0", 
            fg="#333333"
        )
        self.title_label.pack(pady=15)

        # 2. Load and Display Image using Pillow
        self.image_label = tk.Label(root, bg="#dcdcdc")
        self.image_label.pack(pady=10)
        self.load_image("photo.jpg") # Change this to your image file path

        # 3. Create Interaction Buttons
        self.button_frame = tk.Frame(root, bg="#f0f0f0")
        self.button_frame.pack(pady=20)

        self.btn_details = tk.Button(
            self.button_frame, 
            text="View Details", 
            command=self.open_details_window,
            font=("Arial", 12),
            width=12,
            bg="#4CAF50",
            fg="white",
            relief="raised"
        )
        self.btn_details.grid(row=0, column=0, px=10)

        self.btn_like = tk.Button(
            self.button_frame, 
            text="❤️ Like", 
            command=self.show_like_message,
            font=("Arial", 12),
            width=12,
            bg="#008CBA",
            fg="white",
            relief="raised"
        )
        self.btn_like.grid(row=0, column=1, px=10)

        self.btn_exit = tk.Button(
            root, 
            text="Exit", 
            command=root.quit,
            font=("Arial", 10),
            bg="#f44336",
            fg="white"
        )
        self.btn_exit.pack(side="bottom", pady=20)

    def load_image(self, file_path):
        """Loads an image using PIL or creates a placeholder if the file is missing."""
        try:
            # Load the user's image
            pil_image = Image.open(file_path)
            # Resize image to fit the window safely
            pil_image = pil_image.resize((400, 400), Image.Resampling.LANCZOS)
            self.photo = ImageTk.PhotoImage(pil_image)
            self.image_label.config(image=self.photo)
        except FileNotFoundError:
            # Fallback placeholder if photo.jpg is not in the directory
            fallback_image = Image.new("RGB", (400, 400), color="#cccccc")
            self.photo = ImageTk.PhotoImage(fallback_image)
            self.image_label.config(
                image=self.photo, 
                text="[ Place 'photo.jpg' in this folder\nor change the path in load_image() ]",
                compound="center",
                font=("Arial", 10, "italic"),
                fg="#555555"
            )

    def show_like_message(self):
        """Shows a basic Tkinter messagebox popup."""
        messagebox.showinfo("Liked!", "You added this photo to your favorites!")

    def open_details_window(self):
        """Opens a new Toplevel window to display metadata details."""
        details_window = tk.Toplevel(self.root)
        details_window.title("Photo Details")
        details_window.geometry("350x250")
        details_window.configure(bg="#ffffff")
        
        # Make the details window modal (focuses user attention here)
        details_window.transient(self.root)
        details_window.grab_set()

        # Header in Toplevel window
        tk.Label(
            details_window, 
            text="Metadata Information", 
            font=("Arial", 14, "bold"), 
            bg="#ffffff", 
            fg="#333333"
        ).pack(pady=15)

        # Loop through the dictionary items to display them cleanly
        frame = tk.Frame(details_window, bg="#ffffff")
        frame.pack(padx=20, fill="both", expand=True)

        for i, (key, value) in enumerate(self.photo_info.items()):
            tk.Label(
                frame, 
                text=f"{key}:", 
                font=("Arial", 10, "bold"), 
                bg="#ffffff", 
                anchor="w"
            ).grid(row=i, column=0, sticky="w", pady=2)
            
            tk.Label(
                frame, 
                text=value, 
                font=("Arial", 10), 
                bg="#ffffff", 
                anchor="w"
            ).grid(row=i, column=1, sticky="w", pady=2, px=5)

if __name__ == "__main__":
    main_window = tk.Tk()
    app = PhotoAlbumApp(main_window)
    main_window.mainloop()
