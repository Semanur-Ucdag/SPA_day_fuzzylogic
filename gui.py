import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk, ImageSequence   # <-- Pillow eklendi
from fuzzy_controller import bakim_ctrl, cilt, yorgunluk, plan, ruh_hali, hava, süre, bakim_tipi
import skfuzzy.control as ctrl
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg




class SpaAssistantApp:

    def __init__(self, root):
        self.root = root
        root.title("💆‍♀️ SPA Günü Asistanı")
        root.geometry("1200x800")

        # --- JPEG Arka Plan ---
        self.bg_image = Image.open("pngtree-beautiful-pink-orchid-on-white-towel-in-spa-salon-image_15938759.jpg")  # JPEG dosya yolunu buraya yaz
        self.bg_image = self.bg_image.resize((1200, 800), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        self.bg_label = tk.Label(root, image=self.bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Tam pencereyi kaplar

        # --- GIF Animasyon Canvas ---
        self.gif_canvas = tk.Canvas(root, width=300, height=200, highlightthickness=0, bg="white") 
        self.gif_canvas.place(x=850, y=550)  # İstersen konumu değiştir

        self.gif = Image.open("spa-day.gif")  # GIF dosya yolunu buraya yaz
        self.frames = [ImageTk.PhotoImage(frame.copy().resize((300, 200), Image.Resampling.LANCZOS)) for frame in ImageSequence.Iterator(self.gif)]
        self.gif_frame_index = 0
        self.animate_gif()

        # --- Scrollable Canvas ve Frame ---
          
        self.canvas = tk.Canvas(root, bg="#ffe6f0", highlightthickness=0)
        self.scroll_y = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.scroll_x = tk.Scrollbar(root, orient="horizontal", command=self.canvas.xview)  # <--- yatay scrollbar
        self.scrollable_frame = tk.Frame(self.canvas, bg="#ffe6f0")

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scroll_y.set, xscrollcommand=self.scroll_x.set)

        self.canvas.place(x=50, y=50, width=700, height=700)
        self.scroll_y.place(x=750, y=50, height=700)
        self.scroll_x.place(x=50, y=750, width=700)

        # ... (Buraya mevcut combo ve buton widget kodların aynen gelecek)

        # Her değişkene özgü dilsel değerleri belirle
        self.combo_labels = [
            ("Yorgunluk", ["düşük", "orta", "yüksek"]),
            ("Ruh Hali", ["stresli", "orta", "çok iyi"]),
            ("Cilt Yağlılığı", ["kuru", "normal", "yağlı"]),
            ("Hava Durumu", ["Kapalı", "orta", "Güneşli"]),
            ("Plan Yoğunluğu", ["boş", "orta", "yoğun"]),
        ]

        self.linguistic_to_numeric = {
            "düşük": 2.5, "orta": 5.0, "yüksek": 7.5,
            "stresli": 2.5, "çok iyi": 7.5,
            "kuru": 2.5, "normal": 5.0, "yağlı": 7.5,
            "Kapalı": 2.5, "Güneşli": 7.5,
            "boş": 2.5, "yoğun": 7.5
        }

        self.entries = {}

        for i, (label, options) in enumerate(self.combo_labels):
            tk.Label(self.scrollable_frame, text=label, bg="#ffe6f0", font=("Comic Sans MS", 10, "bold")).grid(row=i, column=0, padx=10, pady=10, sticky="w")
            combo = ttk.Combobox(self.scrollable_frame, values=options, font=("Arial", 10), state="readonly")
            combo.grid(row=i, column=1, padx=10, pady=10)
            combo.set(options[1])  # varsayılan: orta
            self.entries[label] = combo

        # Butonlar
        self.calc_btn = tk.Button(self.scrollable_frame, text="🌸 SPA Rutini Hesapla 🌸", bg="#ff99cc", fg="white", font=("Arial", 10, "bold"), command=self.hesapla)
        self.calc_btn.grid(row=6, column=0, columnspan=2, pady=10)

        self.graph_btn = tk.Button(self.scrollable_frame, text="📊 Grafikleri Göster 📊", bg="#ff99cc", fg="white", font=("Arial", 10, "bold"), command=self.toggle_graphs)
        self.graph_btn.grid(row=7, column=0, columnspan=2, pady=10)

        # Sonuç Etiketleri
        self.result1 = tk.Label(self.scrollable_frame, text="Önerilen Süre: ", font=("Arial", 12, "bold"), bg="#ffe6f0", fg="#99004d")
        self.result1.grid(row=8, column=0, columnspan=2, pady=5)

        self.result2 = tk.Label(self.scrollable_frame, text="Bakım Tipi Skoru: ", font=("Arial", 12, "bold"), bg="#ffe6f0", fg="#99004d")
        self.result2.grid(row=9, column=0, columnspan=2, pady=5)

        # Grafik alanı
        self.graph_frame = tk.Frame(self.scrollable_frame, bg="#ffe6f0")
        self.graph_frame.grid(row=0, column=2, rowspan=20, padx=10, pady=10, sticky="nsew")
        self.graph_frame.grid_remove()

        self.fig = None
        self.canvas_graph = None


    def animate_gif(self):
        frame = self.frames[self.gif_frame_index]
        self.gif_canvas.create_image(0, 0, anchor=tk.NW, image=frame)
        self.gif_frame_index = (self.gif_frame_index + 1) % len(self.frames)
        self.root.after(100, self.animate_gif)  # 100 ms hızında oynat


    def hesapla(self):
        # Aynen mevcut kodun
        try:
            values = [self.linguistic_to_numeric[entry.get()] for entry in self.entries.values()]
            bakim_sim = ctrl.ControlSystemSimulation(bakim_ctrl)

            bakim_sim.input["yorgunluk"] = values[0]
            bakim_sim.input["ruh_hali"] = values[1]
            bakim_sim.input["cilt"] = values[2]
            bakim_sim.input["hava"] = values[3]
            bakim_sim.input["plan"] = values[4]

            bakim_sim.compute()

            süre_val = bakim_sim.output["süre"]
            tip_skor = bakim_sim.output["bakim_tipi"]

            if tip_skor <= 1:
                öneri = "Esans ve hafif bir banyo önerilir."
            elif tip_skor <= 2:
                öneri = "Yüz maskesi ve cilt bakımı yapılabilir."
            elif tip_skor <= 3:
                öneri = "Masaj ve saç bakımı gibi rutinler uygundur."
            else:
                öneri = "Meditasyon ve tam SPA günü önerilir."

            self.result1.config(text=f"Önerilen Süre: {süre_val:.2f} dakika")
            self.result2.config(text=f"Bakım Tipi Skoru: {tip_skor:.2f} → {öneri}")

        except Exception as e:
            messagebox.showerror("Hata", f"Beklenmedik bir hata oluştu: {e}")

    def toggle_graphs(self):
        # Aynen mevcut kodun
        if self.graph_frame.winfo_ismapped():
            self.graph_frame.grid_remove()
            self.graph_btn.config(text="📊 Grafikleri Göster 📊")
            if self.canvas_graph:
                self.canvas_graph.get_tk_widget().destroy()
                self.canvas_graph = None
            if self.fig:
                plt.close(self.fig)
                self.fig = None
        else:
            self.graph_frame.grid()
            self.graph_btn.config(text="📊 Grafikleri Gizle 📊")
            self.draw_graphs()

    def draw_graphs(self):
        # Aynen mevcut kodun
        if self.canvas_graph:
            self.canvas_graph.get_tk_widget().destroy()
        if self.fig:
            plt.close(self.fig)

        self.fig, axs = plt.subplots(4, 2, figsize=(8, 10))
        axs = axs.flatten()

        vars = [yorgunluk, ruh_hali, cilt, hava, plan, süre, bakim_tipi]
        for i, var in enumerate(vars):
            for term in var.terms:
                mf = var.terms[term].mf
                axs[i].plot(var.universe, mf, label=term)
            axs[i].set_title(var.label, fontsize=10)
            axs[i].legend(fontsize=8)
            axs[i].tick_params(axis="both", labelsize=8)

        if len(vars) < len(axs):
            for i in range(len(vars), len(axs)):
                self.fig.delaxes(axs[i])

        self.fig.tight_layout(pad=3.0)

        self.canvas_graph = FigureCanvasTkAgg(self.fig, master=self.graph_frame)
        self.canvas_graph.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        self.canvas_graph.draw()


if __name__ == "__main__":
    root = tk.Tk()
    app = SpaAssistantApp(root)
    root.mainloop()
