import wx
import vlc


class VideoPlayer(wx.Frame):
    def __init__(self, title, video_path):
        wx.Frame.__init__(self, None, title=title, size=(600, 400))
        self.panel = wx.Panel(self)
        self.vlc_media_player = vlc.MediaPlayer()
        self.vlc_media_player.set_mrl(video_path)
        self.play_button = wx.Button(self.panel, label="Play")
        self.play_button.Bind(wx.EVT_BUTTON, self.on_play)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.play_button, 1, flag=wx.EXPAND)
        self.panel.SetSizer(self.sizer)

    def on_play(self, event):
        if not self.vlc_media_player.is_playing():
            self.vlc_media_player.play()
        else:
            self.vlc_media_player.pause()


app = wx.App(False)
frame = VideoPlayer("wxPython VLC Video Player", "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/BigBuckBunny.mp4")
frame.Show()
app.MainLoop()
