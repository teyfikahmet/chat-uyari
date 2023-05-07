// Arat class ChatLine(ui.EditLine) içinde
def OnIMEUpdate(self):
// Üstüne Ekle
def CheckPlaceholder(self):
	if len(self.GetText()) > 0:
		self.placeholderTextLine.Hide()
	else:
		self.placeholderTextLine.Show()
		
// Arat def __init__(self) içinde
self.overTextLine = ui.TextLine()
self.overTextLine.SetParent(self)
self.overTextLine.SetPosition(-1, 0)
self.overTextLine.SetFontColor(1.0, 1.0, 0.0)
self.overTextLine.SetOutline()
self.overTextLine.Hide()
// Bloğun altına ekle
self.placeholderTextLine = ui.TextLine()
self.placeholderTextLine.SetParent(self)
self.placeholderTextLine.SetPosition(-1, 0)
self.placeholderTextLine.SetFontColor(1.73, 1.72, 1.72)
self.placeholderTextLine.SetOutline()
self.placeholderTextLine.Show()
self.placeholderTextLine.SetText("  Görünecek yazi.")

// Arat class ChatInputSet(ui.Window) içinde
def OnRender(self):
// Altına Ekle
def OnUpdate(self):
	self.chatLine.CheckPlaceholder()
