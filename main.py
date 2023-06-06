import sys
import wx
import vlc


class VideoPlayer(wx.Frame):
    def __init__(self, title, video_path):
        wx.Frame.__init__(self, None, title=title, size=(600, 400))
        self.vlc_instance = vlc.Instance()
        self.vlc_media_player = self.vlc_instance.media_player_new()
        self.play_button = wx.Button(self, label="Play")
        self.play_button.Bind(wx.EVT_BUTTON, self.on_play)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.play_button, flag=wx.EXPAND)
        self.SetSizerAndFit(self.sizer)
        self.Show()
        media = self.vlc_instance.media_new(video_path)
        self.vlc_media_player.set_media(media)
        if sys.platform.startswith('linux'):  # for Linux using the X Server
            self.vlc_media_player.set_xwindow(self.GetHandle())
        elif sys.platform == "win32":  # for Windows
            self.vlc_media_player.set_hwnd(self.GetHandle())
        elif sys.platform == "darwin":  # for MacOS
            self.vlc_media_player.set_nsobject(self.GetHandle())

    def on_play(self, event):
        if not self.vlc_media_player.is_playing():
            self.vlc_media_player.play()
        else:
            self.vlc_media_player.pause()


app = wx.App(False)
frame = VideoPlayer("wxPython VLC Video Player",
                    "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4")
frame.Show()
app.MainLoop()
