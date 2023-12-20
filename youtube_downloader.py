from pytube import YouTube
import customtkinter as ctk


class YoutubeDownloader(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.geometry("500x300")
        self.title("YouTube Downloader")
        self.minsize(500, 300)
        self.init_gui_elements()

    def init_gui_elements(self):
        self.url_entry = ctk.CTkEntry(
            self, 
            placeholder_text="Enter YouTube URL",
            width=400)
        self.url_entry.pack(pady=20)

         # Label for displaying selected quality
        self.selected_quality_label = ctk.CTkLabel(self, text="Selected Quality: 720p")
        self.selected_quality_label.pack(pady=10)

        # Quality selection slider
        self.quality_slider = ctk.CTkSlider(self, 
                                            from_=0, to=3, 
                                            number_of_steps=3,
                                            command=self.update_quality_label)
        self.quality_slider.set(2)  # Default position for 720p
        self.quality_slider.pack(pady=10)

        self.download_button = ctk.CTkButton(
            self, text="Download", command=self.download_video
        )
        self.download_button.pack(pady=10)

        self.status_label = ctk.CTkLabel(self, text="")
        self.status_label.pack(pady=10)

        # Quality labels mapping
        self.quality_labels = {0: "360p", 1: "480p", 2: "720p", 3: "1080p"}
    
    def update_quality_label(self, event=None):
        slider_value = int(self.quality_slider.get())
        selected_quality = self.quality_labels[slider_value]
        self.selected_quality_label.configure(text=f"Selected Quality: {selected_quality}")

    def download_video(self):
        """
        Download the video from the URL provided in the GUI.
        """
        url = self.url_entry.get()  # Get the URL from the entry widget
        slider_value = self.quality_slider.get()
        selected_quality = self.quality_labels[slider_value]
        try:
            ytObject = YouTube(url)
            video = ytObject.streams.get_by_resolution(selected_quality)
            if video:
                video.download()
                self.status_label.configure(text="Download completed!")
            else:
                self.status_label.configure(text="Requested quality not available.")
        except Exception as e:
            self.status_label.configure(text=f"Error: {e}")


app = YoutubeDownloader()
app.mainloop()