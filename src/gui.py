import tkinter as tk
from tkinter import ttk


class SuperResolutionApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Super-Resolution Comparison App")
        self.root.geometry("1000x650")
        self.root.minsize(900, 550)

        self.selected_method = tk.StringVar(value="Lanczos")
        self.selected_scale = tk.StringVar(value="4x")
        self.status_text = tk.StringVar(value="Ready")

        self._build_layout()

    def _build_layout(self):
        # Main container
        main_frame = ttk.Frame(self.root, padding=15)
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Title
        title_label = ttk.Label(
            main_frame,
            text="Image Super-Resolution Comparison App",
            font=("Arial", 18, "bold")
        )
        title_label.pack(pady=(0, 15))

        # Controls section
        controls_frame = ttk.LabelFrame(main_frame, text="Controls", padding=10)
        controls_frame.pack(fill=tk.X, pady=(0, 15))

        # Method selector
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

        # Scale selector
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

        # Buttons
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

        # Image preview section
        preview_frame = ttk.Frame(main_frame)
        preview_frame.pack(fill=tk.BOTH, expand=True)

        # Original image panel
        original_frame = ttk.LabelFrame(preview_frame, text="Original Image", padding=10)
        original_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 8))

        self.original_label = ttk.Label(
            original_frame,
            text="No image selected",
            anchor=tk.CENTER
        )
        self.original_label.pack(fill=tk.BOTH, expand=True)

        # Output image panel
        output_frame = ttk.LabelFrame(preview_frame, text="Output Image", padding=10)
        output_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(8, 0))

        self.output_label = ttk.Label(
            output_frame,
            text="No output yet",
            anchor=tk.CENTER
        )
        self.output_label.pack(fill=tk.BOTH, expand=True)

        # Status bar
        status_bar = ttk.Label(
            self.root,
            textvariable=self.status_text,
            relief=tk.SUNKEN,
            anchor=tk.W,
            padding=5
        )
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def select_image(self):
        self.status_text.set("Select image feature will be added in the next step.")

    def process_image(self):
        method = self.selected_method.get()
        scale = self.selected_scale.get()
        self.status_text.set(f"Process image feature not added yet. Selected: {method}, Scale: {scale}")

    def save_output(self):
        self.status_text.set("Save output feature will be added later.")

    def run(self):
        self.root.mainloop()