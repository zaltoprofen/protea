JsOsaDAS1.001.00bplist00�Vscript_�app = Application("com.apple.itunes");
var retval;
if (app.playerState() == "playing"){
	track = app.currentTrack;
	retval = "Now Playing: " + track.name() + ' from "' + track.album() + '" (' + track.artist() + ")";
}
retval                            �jscr  ��ޭ