import sys
import vlc
import wx


class VideoPlayerFrame(wx.Frame):
    def __init__(self, title, video_path):
        wx.Frame.__init__(self, None, title=title, size=(600, 400))
        self.video_path = video_path
        self.video_panel = wx.Panel(self, -1)
        self.vlc_instance = vlc.Instance()
        self.vlc_media_player = self.vlc_instance.media_player_new()
        self.url_text = wx.TextCtrl(self, size=(400, -1))
        self.url_text.SetValue(self.video_path)
        self.play_button = wx.Button(self, label="Play")
        self.play_button.Bind(wx.EVT_BUTTON, self.on_play)
        controls_sizer = wx.BoxSizer(wx.HORIZONTAL)
        controls_sizer.Add(self.url_text, proportion=1, flag=wx.RIGHT, border=5)
        controls_sizer.Add(self.play_button, proportion=0)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(controls_sizer, 0, wx.EXPAND | wx.ALL, 5)
        self.sizer.Add(self.video_panel, 1, wx.EXPAND | wx.ALL, 5)
        self.SetSizerAndFit(self.sizer)
        self.Show()
        if sys.platform.startswith("linux"):
            self.vlc_media_player.set_xwindow(self.video_panel.GetHandle())
        elif sys.platform == "win32":
            self.vlc_media_player.set_hwnd(self.video_panel.GetHandle())
        elif sys.platform == "darwin":
            self.vlc_media_player.set_nsobject(self.video_panel.GetHandle())

    def on_play(self, event):
        if not self.vlc_media_player.is_playing():
            media = self.vlc_instance.media_new(self.url_text.GetValue())
            self.vlc_media_player.set_media(media)
            self.vlc_media_player.play()
            self.play_button.SetLabel("Pause")
        else:
            self.vlc_media_player.pause()
            self.play_button.SetLabel("Play")


app = wx.App()
frame = VideoPlayerFrame(
    "wxpython-vlc",
    "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4",
)
frame.Show()
app.MainLoop()
