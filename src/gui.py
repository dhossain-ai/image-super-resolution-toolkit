import tkinter as tk
from tkinter import ttk, filedialog, messagebox

from PIL import ImageTk

from src.image_utils import (
    load_preview_image,
    is_supported_image,
    get_filename,
    load_cv_image,
    create_preview_from_cv,
    get_scale_factor,
    create_output_path,
    save_cv_image,
)

from src.classical import (
    upscale_bicubic,
    upscale_lanczos,
    apply_mild_sharpening,
)


class SuperResolutionApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Super-Resolution Comparison App")
        self.root.geometry("1000x650")
        self.root.minsize(900, 550)

        self.selected_method = tk.StringVar(value="Lanczos")
        self.selected_scale = tk.StringVar(value="4x")
        self.status_text = tk.StringVar(value="Ready")

        self.selected_image_path = None
        self.original_photo = None
        self.output_photo = None
        self.output_image = None

        self._build_layout()

    def _build_layout(self):
        main_frame = ttk.Frame(self.root, padding=15)
        main_frame.pack(fill=tk.BOTH, expand=True)

        title_label = ttk.Label(
            main_frame,
            text="Image Super-Resolution Comparison App",
            font=("Arial", 18, "bold")
        )
        title_label.pack(pady=(0, 15))

        controls_frame = ttk.LabelFrame(main_frame, text="Controls", padding=10)
        controls_frame.pack(fill=tk.X, pady=(0, 15))

        method_label = ttk.Label(controls_frame, text="Method:")
        method_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

        method_combo = ttk.Combobox(
            controls_frame,
            textvariable=self.selected_method,
            values=["Bicubic", "Lanczos", "EDSR"],
            state="readonly",
            width=20
        )
        method_combo.grid(row=0, column=1, padx=5, pady=5)

        scale_label = ttk.Label(controls_frame, text="Scale:")
        scale_label.grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)

        scale_combo = ttk.Combobox(
            controls_frame,
            textvariable=self.selected_scale,
            values=["2x", "4x"],
            state="readonly",
            width=10
        )
        scale_combo.grid(row=0, column=3, padx=5, pady=5)

        select_button = ttk.Button(
            controls_frame,
            text="Select Image",
            command=self.select_image
        )
        select_button.grid(row=0, column=4, padx=10, pady=5)

        process_button = ttk.Button(
            controls_frame,
            text="Process Image",
            command=self.process_image
        )
        process_button.grid(row=0, column=5, padx=5, pady=5)

        save_button = ttk.Button(
            controls_frame,
            text="Save Output",
            command=self.save_output
        )
        save_button.grid(row=0, column=6, padx=5, pady=5)

        controls_frame.columnconfigure(7, weight=1)

        preview_frame = ttk.Frame(main_frame)
        preview_frame.pack(fill=tk.BOTH, expand=True)

        original_frame = ttk.LabelFrame(preview_frame, text="Original Image", padding=10)
        original_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 8))

        self.original_label = ttk.Label(
            original_frame,
            text="No image selected",
            anchor=tk.CENTER
        )
        self.original_label.pack(fill=tk.BOTH, expand=True)

        output_frame = ttk.LabelFrame(preview_frame, text="Output Image", padding=10)
        output_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(8, 0))

        self.output_label = ttk.Label(
            output_frame,
            text="No output yet",
            anchor=tk.CENTER
        )
        self.output_label.pack(fill=tk.BOTH, expand=True)

        status_bar = ttk.Label(
            self.root,
            textvariable=self.status_text,
            relief=tk.SUNKEN,
            anchor=tk.W,
            padding=5
        )
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def select_image(self):
        file_path = filedialog.askopenfilename(
            title="Select Image",
            filetypes=[
                ("Image Files", "*.jpg *.jpeg *.png *.bmp *.tif *.tiff *.webp"),
                ("JPEG Files", "*.jpg *.jpeg"),
                ("PNG Files", "*.png"),
                ("All Files", "*.*"),
            ]
        )

        if not file_path:
            self.status_text.set("Image selection cancelled.")
            return

        if not is_supported_image(file_path):
            messagebox.showerror(
                "Unsupported File",
                "Please select a valid image file."
            )
            self.status_text.set("Unsupported image file selected.")
            return

        try:
            preview_image = load_preview_image(file_path)
            self.original_photo = ImageTk.PhotoImage(preview_image)

            self.original_label.configure(
                image=self.original_photo,
                text=""
            )

            self.output_label.configure(
                image="",
                text="No output yet"
            )

            self.selected_image_path = file_path
            self.output_photo = None
            self.output_image = None

            self.status_text.set(f"Selected image: {get_filename(file_path)}")

        except Exception as error:
            messagebox.showerror(
                "Image Load Error",
                f"Could not load image.\n\nError: {error}"
            )
            self.status_text.set("Failed to load selected image.")

    def process_image(self):
        if not self.selected_image_path:
            messagebox.showwarning(
                "No Image Selected",
                "Please select an image first."
            )
            self.status_text.set("No image selected.")
            return

        method = self.selected_method.get()
        scale_factor = get_scale_factor(self.selected_scale.get())

        if method == "EDSR":
            messagebox.showinfo(
                "EDSR Not Added Yet",
                "EDSR deep learning support will be added in a later step."
            )
            self.status_text.set("EDSR support not added yet.")
            return

        try:
            image = load_cv_image(self.selected_image_path)

            if method == "Bicubic":
                processed_image = upscale_bicubic(image, scale_factor)
            elif method == "Lanczos":
                processed_image = upscale_lanczos(image, scale_factor)
            else:
                raise ValueError("Invalid method selected.")

            processed_image = apply_mild_sharpening(processed_image)

            self.output_image = processed_image

            preview_image = create_preview_from_cv(processed_image)
            self.output_photo = ImageTk.PhotoImage(preview_image)

            self.output_label.configure(
                image=self.output_photo,
                text=""
            )

            self.status_text.set(
                f"Processed using {method} interpolation at {scale_factor}x scale."
            )

        except Exception as error:
            messagebox.showerror(
                "Processing Error",
                f"Could not process image.\n\nError: {error}"
            )
            self.status_text.set("Image processing failed.")

    def save_output(self):
        if self.output_image is None:
            messagebox.showwarning(
                "No Output Image",
                "Please process an image before saving."
            )
            self.status_text.set("No output image to save.")
            return

        try:
            method = self.selected_method.get()
            scale_text = self.selected_scale.get()

            output_path = create_output_path(
                input_path=self.selected_image_path,
                method=method,
                scale_text=scale_text
            )

            save_cv_image(self.output_image, output_path)

            messagebox.showinfo(
                "Image Saved",
                f"Output image saved successfully:\n\n{output_path}"
            )

            self.status_text.set(f"Saved output: {output_path}")

        except Exception as error:
            messagebox.showerror(
                "Save Error",
                f"Could not save output image.\n\nError: {error}"
            )
            self.status_text.set("Failed to save output image.")

    def run(self):
        self.root.mainloop()