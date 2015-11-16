import wx
import wx.xrc
#below are the variables that will be use to send information
ir_us=''
ir_pa=''
to_st=''
fr_st=''
da_of_jo=''
tr_no=''
cl=''
na_1=''
ag_1=''
ge_1=''
be_1=''
id_ty1=''
id_no1=''
na_2=''
ag_2=''
ge_2=''
be_2=''
id_ty2=''
id_no2=''
na_3=''
ag_3=''
ge_3=''
be_3=''
id_ty3=''
id_no3=''
na_4=''
ag_4=''
ge_4=''
be_4=''
id_ty4=''
id_no4=''
sm=''
sbi_us=''
sbi_pa=''
sbi_nb=0
#this class is for collecting information via gui
class Main_window ( wx.Frame ):
    
	def OnClick(self, event):
		self._done.SetLabel("Clicked")
		self.Close()	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Enter your information", pos = wx.Point( 100,100 ), size = wx.Size( 990,670 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 990,670 ), wx.Size( -1,-1 ) )#fixing minimium and maximum size of the
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_scrolledWindow1 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow1.SetScrollRate( 5, 5 )
		fgSizer1 = wx.FlexGridSizer( 0, 7, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
  
		self.irctc_username = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"IRCTC username", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_LEFT )
		self.irctc_username.Wrap( -1 )
		fgSizer1.Add( self.irctc_username, 0, wx.ALL, 5 )
		
		self._irctc_username = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self._irctc_username.SetMaxLength( 15 ) 
		fgSizer1.Add( self._irctc_username, 0, wx.ALL, 5 )
		
		self.m_staticText36 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText36.Wrap( -1 )
		fgSizer1.Add( self.m_staticText36, 0, wx.ALL, 5 )
		
		self.m_staticText37 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText37.Wrap( -1 )
		fgSizer1.Add( self.m_staticText37, 0, wx.ALL, 5 )
		
		self.m_staticText38 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText38.Wrap( -1 )
		fgSizer1.Add( self.m_staticText38, 0, wx.ALL, 5 )
		
		self.m_staticText39 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText39.Wrap( -1 )
		fgSizer1.Add( self.m_staticText39, 0, wx.ALL, 5 )
		
		self.m_staticText87 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText87.Wrap( -1 )
		fgSizer1.Add( self.m_staticText87, 0, wx.ALL, 5 )

		self.irctc_password = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"IRCTC password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.irctc_password.Wrap( -1 )
		fgSizer1.Add( self.irctc_password, 0, wx.ALL, 5 )
		
		self._irctc_password = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		self._irctc_password.SetMaxLength( 20 ) 
		fgSizer1.Add( self._irctc_password, 0, wx.ALL, 5 )
		
		self.m_staticText40 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText40.Wrap( -1 )
		fgSizer1.Add( self.m_staticText40, 0, wx.ALL, 5 )
		
		self.m_staticText41 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )
		fgSizer1.Add( self.m_staticText41, 0, wx.ALL, 5 )
		
		self.m_staticText42 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText42.Wrap( -1 )
		fgSizer1.Add( self.m_staticText42, 0, wx.ALL, 5 )
		
		self.m_staticText43 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText43.Wrap( -1 )
		fgSizer1.Add( self.m_staticText43, 0, wx.ALL, 5 )
				
		self.m_staticText88 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText88.Wrap( -1 )
		fgSizer1.Add( self.m_staticText88, 0, wx.ALL, 5 )
		
		self.m_staticline1 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer1.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline2 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer1.Add( self.m_staticline2, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline3 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer1.Add( self.m_staticline3, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline4 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer1.Add( self.m_staticline4, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline5 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer1.Add( self.m_staticline5, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline6 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer1.Add( self.m_staticline6, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline33 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer1.Add( self.m_staticline33, 0, wx.EXPAND |wx.ALL, 5 )		
		
		self.from_station = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"From Station", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.from_station.Wrap( -1 )
		fgSizer1.Add( self.from_station, 0, wx.ALL, 5 )
		
		self._from_station = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self._from_station.SetMaxLength( 30 ) 
		fgSizer1.Add( self._from_station, 0, wx.ALL, 5 )
		
		self.m_staticText44 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText44.Wrap( -1 )
		fgSizer1.Add( self.m_staticText44, 0, wx.ALL, 5 )
		
		self.m_staticText45 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText45.Wrap( -1 )
		fgSizer1.Add( self.m_staticText45, 0, wx.ALL, 5 )
		
		self.m_staticText46 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText46.Wrap( -1 )
		fgSizer1.Add( self.m_staticText46, 0, wx.ALL, 5 )
		
		self.m_staticText47 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText47.Wrap( -1 )
		fgSizer1.Add( self.m_staticText47, 0, wx.ALL, 5 )
		
		self.m_staticText89 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText89.Wrap( -1 )
		fgSizer1.Add( self.m_staticText89, 0, wx.ALL, 5 )
		  
		self.to_station = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"To Station", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.to_station.Wrap( -1 )
		fgSizer1.Add( self.to_station, 0, wx.ALL, 5 )
		
		self._to_station = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self._to_station.SetMaxLength( 30 ) 
		fgSizer1.Add( self._to_station, 0, wx.ALL, 5 )
		
		self.m_staticText48 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText48.Wrap( -1 )
		fgSizer1.Add( self.m_staticText48, 0, wx.ALL, 5 )
		
		self.m_staticText49 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText49.Wrap( -1 )
		fgSizer1.Add( self.m_staticText49, 0, wx.ALL, 5 )
		
		self.m_staticText50 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText50.Wrap( -1 )
		fgSizer1.Add( self.m_staticText50, 0, wx.ALL, 5 )
		
		self.m_staticText51 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText51.Wrap( -1 )
		fgSizer1.Add( self.m_staticText51, 0, wx.ALL, 5 )
		
		self.m_staticText90 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText90.Wrap( -1 )
		fgSizer1.Add( self.m_staticText90, 0, wx.ALL, 5 )
		  
		self.date_of_journey = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Date of Journey(dd-mm-yyyy)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.date_of_journey.Wrap( -1 )
		fgSizer1.Add( self.date_of_journey, 0, wx.ALL, 5 )
		
		self._date_of_journey = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self._date_of_journey.SetMaxLength( 10 ) 
		fgSizer1.Add( self._date_of_journey, 0, wx.ALL, 5 )

		self.m_staticText52 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText52.Wrap( -1 )
		fgSizer1.Add( self.m_staticText52, 0, wx.ALL, 5 )
		
		self.m_staticText53 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText53.Wrap( -1 )
		fgSizer1.Add( self.m_staticText53, 0, wx.ALL, 5 )
		
		self.m_staticText54 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText54.Wrap( -1 )
		fgSizer1.Add( self.m_staticText54, 0, wx.ALL, 5 )
		
		self.m_staticText55 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText55.Wrap( -1 )
		fgSizer1.Add( self.m_staticText55, 0, wx.ALL, 5 )
		
		self.m_staticText91 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText91.Wrap( -1 )
		fgSizer1.Add( self.m_staticText91, 0, wx.ALL, 5 )
		  
		self.m_staticline12 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer1.Add( self.m_staticline12, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline13 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer1.Add( self.m_staticline13, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline14 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer1.Add( self.m_staticline14, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline15 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer1.Add( self.m_staticline15, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline16 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer1.Add( self.m_staticline16, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline17 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer1.Add( self.m_staticline17, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline34 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer1.Add( self.m_staticline34, 0, wx.EXPAND |wx.ALL, 5 )
						
		self.train_no = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Train No.", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.train_no.Wrap( -1 )
		fgSizer1.Add( self.train_no, 0, wx.ALL, 5 )
		
		self._train_no = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self._train_no.SetMaxLength( 5 ) 
		fgSizer1.Add( self._train_no, 0, wx.ALL, 5 )
		
		self.m_staticText56 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText56.Wrap( -1 )
		fgSizer1.Add( self.m_staticText56, 0, wx.ALL, 5 )
		
		self.m_staticText57 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText57.Wrap( -1 )
		fgSizer1.Add( self.m_staticText57, 0, wx.ALL, 5 )
		
		self.m_staticText58 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText58.Wrap( -1 )
		fgSizer1.Add( self.m_staticText58, 0, wx.ALL, 5 )
		
		self.m_staticText59 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText59.Wrap( -1 )
		fgSizer1.Add( self.m_staticText59, 0, wx.ALL, 5 )
		
		self.m_staticText92 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText92.Wrap( -1 )
		fgSizer1.Add( self.m_staticText92, 0, wx.ALL, 5 )
		 
		self.class_of_j = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Class", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.class_of_j.Wrap( -1 )
		fgSizer1.Add( self.class_of_j, 0, wx.ALL, 5 )
		
		_class_of_jChoices = [ u"Select class", u"SL", u"3A", u"2A", u"1A" ]
		self._class_of_j = wx.Choice( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, _class_of_jChoices, 0 )
		self._class_of_j.SetSelection( 0 )
		fgSizer1.Add( self._class_of_j, 0, wx.ALL, 5 )

		self.m_staticText61 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText61.Wrap( -1 )
		fgSizer1.Add( self.m_staticText61, 0, wx.ALL, 5 )
		
		self.m_staticText62 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText62.Wrap( -1 )
		fgSizer1.Add( self.m_staticText62, 0, wx.ALL, 5 )
		
		self.m_staticText63 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText63.Wrap( -1 )
		fgSizer1.Add( self.m_staticText63, 0, wx.ALL, 5 )
		
		self.m_staticText64 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText64.Wrap( -1 )
		fgSizer1.Add( self.m_staticText64, 0, wx.ALL, 5 )
		
		self.m_staticText93 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText93.Wrap( -1 )
		fgSizer1.Add( self.m_staticText93, 0, wx.ALL, 5 )
		
		self.m_staticline19 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer1.Add( self.m_staticline19, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline20 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer1.Add( self.m_staticline20, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline21 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer1.Add( self.m_staticline21, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline22 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer1.Add( self.m_staticline22, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline23 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer1.Add( self.m_staticline23, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline24 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer1.Add( self.m_staticline24, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline35 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer1.Add( self.m_staticline35, 0, wx.EXPAND |wx.ALL, 5 )
				
		self.m_staticText12 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Passenger details", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		fgSizer1.Add( self.m_staticText12, 0, wx.ALL, 5 )
		
		self.name_1 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.name_1.Wrap( -1 )
		fgSizer1.Add( self.name_1, 0, wx.ALL, 5 )
		
		self.age_1 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Age", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.age_1.Wrap( -1 )
		fgSizer1.Add( self.age_1, 0, wx.ALL, 5 )
		
		self.gender_1 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Gender", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.gender_1.Wrap( -1 )
		fgSizer1.Add( self.gender_1, 0, wx.ALL, 5 )
		
		self.berth_preference = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Berth Preference", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.berth_preference.Wrap( -1 )
		fgSizer1.Add( self.berth_preference, 0, wx.ALL, 5 )
				
		self.id_card_type = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Id Card Type", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.id_card_type.Wrap( -1 )
		fgSizer1.Add( self.id_card_type, 0, wx.ALL, 5 )
		
		self.id_card_no = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Id Card number", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.id_card_no.Wrap( -1 )
		fgSizer1.Add( self.id_card_no, 0, wx.ALL, 5 )
		
		self.m_staticText65 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Passenger 1 details", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText65.Wrap( -1 )
		fgSizer1.Add( self.m_staticText65, 0, wx.ALL, 5 )
		
		self._name_1 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self._name_1.SetMaxLength( 40 ) 
		fgSizer1.Add( self._name_1, 0, wx.ALL, 5 )
		
		self._age_1 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self._age_1.SetMaxLength( 3 ) 
		fgSizer1.Add( self._age_1, 0, wx.ALL, 5 )
		
		_gender_1Choices = [ u"Select Gender", u"Male", u"Female" ]
		self._gender_1 = wx.Choice( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, _gender_1Choices, 0 )
		self._gender_1.SetSelection( 0 )
		fgSizer1.Add( self._gender_1, 0, wx.ALL, 5 )
		
		be_pr1Choices = [ u"No Preference", u"LOWER", u"MIDDLE", u"UPPER", wx.EmptyString, wx.EmptyString ]
		self.be_pr1 = wx.Choice( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, be_pr1Choices, 0 )
		self.be_pr1.SetSelection( 0 )
		fgSizer1.Add( self.be_pr1, 0, wx.ALL, 5 )
				
		_id_card_type1Choices = [ u"ID Card Type", u"Driving Licence", u"Passport", u"PAN Card", u"Voter ID-Card", u"Govt Issued ID-Card", u"Student ID-Card", u"Bank Passbook", u"Credit card with Photo", u"Aadhaar ID" ]
		self._id_card_type1 = wx.Choice( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, _id_card_type1Choices, 0 )
		self._id_card_type1.SetSelection( 0 )
		fgSizer1.Add( self._id_card_type1, 0, wx.ALL, 5 )
		
		self._id_card_no1 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self._id_card_no1.SetMaxLength( 30 ) 
		fgSizer1.Add( self._id_card_no1, 0, wx.ALL, 5 )
		
		self.m_staticText151 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Passenger 2 details", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText151.Wrap( -1 )
		fgSizer1.Add( self.m_staticText151, 0, wx.ALL, 5 )
		
		self._name_2 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self._name_2.SetMaxLength( 40 ) 
		fgSizer1.Add( self._name_2, 0, wx.ALL, 5 )
		
		self._age_2 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self._age_2.SetMaxLength( 3 ) 
		fgSizer1.Add( self._age_2, 0, wx.ALL, 5 )
		
		_gender_2Choices = [ u"Select Gender", u"Male", u"Female" ]
		self._gender_2 = wx.Choice( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, _gender_2Choices, 0 )
		self._gender_2.SetSelection( 0 )
		fgSizer1.Add( self._gender_2, 0, wx.ALL, 5 )
		
		be_pr2Choices = [ u"No Preference", u"LOWER", u"MIDDLE", u"UPPER", wx.EmptyString, wx.EmptyString ]
		self.be_pr2 = wx.Choice( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, be_pr2Choices, 0 )
		self.be_pr2.SetSelection( 0 )
		fgSizer1.Add( self.be_pr2, 0, wx.ALL, 5 )
				
		_id_card_type2Choices = [ u"ID Card Type", u"Driving Licence", u"Passport", u"PAN Card", u"Voter ID-Card", u"Govt Issued ID-Card", u"Student ID-Card", u"Bank Passbook", u"Credit card with Photo", u"Aadhaar ID" ]
		self._id_card_type2 = wx.Choice( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, _id_card_type2Choices, 0 )
		self._id_card_type2.SetSelection( 0 )
		fgSizer1.Add( self._id_card_type2, 0, wx.ALL, 5 )
		
		self._id_card_no2 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self._id_card_no2.SetMaxLength( 30 ) 
		fgSizer1.Add( self._id_card_no2, 0, wx.ALL, 5 )
		
		self.m_staticText66 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Passenger 3 details", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText66.Wrap( -1 )
		fgSizer1.Add( self.m_staticText66, 0, wx.ALL, 5 )
		
		self._name_3 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self._name_3.SetMaxLength( 40 ) 
		fgSizer1.Add( self._name_3, 0, wx.ALL, 5 )
		
		self._age_3 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self._age_3.SetMaxLength( 3 ) 
		fgSizer1.Add( self._age_3, 0, wx.ALL, 5 )
		
		_gender_3Choices = [ u"Select Gender", u"Male", u"Female" ]
		self._gender_3 = wx.Choice( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, _gender_3Choices, 0 )
		self._gender_3.SetSelection( 0 )
		fgSizer1.Add( self._gender_3, 0, wx.ALL, 5 )
		
		be_pr3Choices = [ u"No Preference", u"LOWER", u"MIDDLE", u"UPPER", wx.EmptyString, wx.EmptyString ]
		self.be_pr3 = wx.Choice( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, be_pr3Choices, 0 )
		self.be_pr3.SetSelection( 0 )
		fgSizer1.Add( self.be_pr3, 0, wx.ALL, 5 )
				
		_id_card_type3Choices = [ u"ID Card Type", u"Driving Licence", u"Passport", u"PAN Card", u"Voter ID-Card", u"Govt Issued ID-Card", u"Student ID-Card", u"Bank Passbook", u"Credit card with Photo", u"Aadhaar ID" ]
		self._id_card_type3 = wx.Choice( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, _id_card_type3Choices, 0 )
		self._id_card_type3.SetSelection( 0 )
		fgSizer1.Add( self._id_card_type3, 0, wx.ALL, 5 )
		
		self._id_card_no3 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self._id_card_no3.SetMaxLength( 30 ) 
		fgSizer1.Add( self._id_card_no3, 0, wx.ALL, 5 )
		
		self.m_staticText25 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Passenger 4 details", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )
		fgSizer1.Add( self.m_staticText25, 0, wx.ALL, 5 )
		
		self._name_4 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self._name_4.SetMaxLength( 40 ) 
		fgSizer1.Add( self._name_4, 0, wx.ALL, 5 )
		
		self._age_4 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self._age_4.SetMaxLength( 3 ) 
		fgSizer1.Add( self._age_4, 0, wx.ALL, 5 )
		
		_gender_4Choices = [ u"Select Gender", u"Male", u"Female" ]
		self._gender_4 = wx.Choice( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, _gender_4Choices, 0 )
		self._gender_4.SetSelection( 0 )
		fgSizer1.Add( self._gender_4, 0, wx.ALL, 5 )
		
		be_pr4Choices = [ u"No Preference", u"LOWER", u"MIDDLE", u"UPPER", wx.EmptyString, wx.EmptyString ]
		self.be_pr4 = wx.Choice( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, be_pr4Choices, 0 )
		self.be_pr4.SetSelection( 0 )
		fgSizer1.Add( self.be_pr4, 0, wx.ALL, 5 )
				
		_id_card_type4Choices = [ u"ID Card Type", u"Driving Licence", u"Passport", u"PAN Card", u"Voter ID-Card", u"Govt Issued ID-Card", u"Student ID-Card", u"Bank Passbook", u"Credit card with Photo", u"Aadhaar ID" ]
		self._id_card_type4 = wx.Choice( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, _id_card_type4Choices, 0 )
		self._id_card_type4.SetSelection( 0 )
		fgSizer1.Add( self._id_card_type4, 0, wx.ALL, 5 )
		
		self._id_card_no4 = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self._id_card_no4.SetMaxLength( 30 ) 
		fgSizer1.Add( self._id_card_no4, 0, wx.ALL, 5 )
		
		self.sms = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"Mobile no. for SMS", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.sms.Wrap( -1 )
		fgSizer1.Add( self.sms, 0, wx.ALL, 5 )
		
		self._sms = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self._sms.SetMaxLength( 10 ) 
		fgSizer1.Add( self._sms, 0, wx.ALL, 5 )
		
		self.m_staticText95 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText95.Wrap( -1 )
		fgSizer1.Add( self.m_staticText95, 0, wx.ALL, 5 )
				
		self.m_staticText67 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText67.Wrap( -1 )
		fgSizer1.Add( self.m_staticText67, 0, wx.ALL, 5 )
		
		self.m_staticText68 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText68.Wrap( -1 )
		fgSizer1.Add( self.m_staticText68, 0, wx.ALL, 5 )
		
		self.m_staticText69 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText69.Wrap( -1 )
		fgSizer1.Add( self.m_staticText69, 0, wx.ALL, 5 )
		
		self.m_staticText70 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText70.Wrap( -1 )
		fgSizer1.Add( self.m_staticText70, 0, wx.ALL, 5 )
		
		self.m_staticline26 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer1.Add( self.m_staticline26, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline36 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer1.Add( self.m_staticline36, 0, wx.EXPAND |wx.ALL, 5 )
				
		self.m_staticline27 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer1.Add( self.m_staticline27, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline28 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer1.Add( self.m_staticline28, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline29 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer1.Add( self.m_staticline29, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline30 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer1.Add( self.m_staticline30, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline31 = wx.StaticLine( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		fgSizer1.Add( self.m_staticline31, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.sbi = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"SBI Net Banking", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.sbi.Wrap( -1 )
		fgSizer1.Add( self.sbi, 0, wx.ALL, 5 )
		
		self._sbi = wx.CheckBox( self.m_scrolledWindow1, wx.ID_ANY, u"check if yes", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self._sbi, 0, wx.ALL, 5 )
		
		self.m_staticText73 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText73.Wrap( -1 )
		fgSizer1.Add( self.m_staticText73, 0, wx.ALL, 5 )
		
		self.m_staticText96 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText96.Wrap( -1 )
		fgSizer1.Add( self.m_staticText96, 0, wx.ALL, 5 )
				
		self.m_staticText74 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText74.Wrap( -1 )
		fgSizer1.Add( self.m_staticText74, 0, wx.ALL, 5 )
		
		self.m_staticText75 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText75.Wrap( -1 )
		fgSizer1.Add( self.m_staticText75, 0, wx.ALL, 5 )
		
		self.m_staticText76 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText76.Wrap( -1 )
		fgSizer1.Add( self.m_staticText76, 0, wx.ALL, 5 )
		
		self.sbi_username = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"SBI Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.sbi_username.Wrap( -1 )
		fgSizer1.Add( self.sbi_username, 0, wx.ALL, 5 )
		
		self._sbi_username = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self._sbi_username.SetMaxLength( 30 ) 
		fgSizer1.Add( self._sbi_username, 0, wx.ALL, 5 )
		
		self.m_staticText77 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText77.Wrap( -1 )
		fgSizer1.Add( self.m_staticText77, 0, wx.ALL, 5 )
		
		self.m_staticText78 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText78.Wrap( -1 )
		fgSizer1.Add( self.m_staticText78, 0, wx.ALL, 5 )
		
		self.m_staticText79 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText79.Wrap( -1 )
		fgSizer1.Add( self.m_staticText79, 0, wx.ALL, 5 )
		
		self.m_staticText80 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText80.Wrap( -1 )
		fgSizer1.Add( self.m_staticText80, 0, wx.ALL, 5 )
		self.m_staticText800 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText800.Wrap( -1 )
		fgSizer1.Add( self.m_staticText800, 0, wx.ALL, 5 )		
		self.sbi_password = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"SBI Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.sbi_password.Wrap( -1 )
		fgSizer1.Add( self.sbi_password, 0, wx.ALL, 5 )
		
		self._sbi_password = wx.TextCtrl( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_PASSWORD )
		fgSizer1.Add( self._sbi_password, 0, wx.ALL, 5 )
		
		self.m_staticText81 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText81.Wrap( -1 )
		fgSizer1.Add( self.m_staticText81, 0, wx.ALL, 5 )
		
		self.m_staticText781 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText781.Wrap( -1 )
		fgSizer1.Add( self.m_staticText781, 0, wx.ALL, 5 )
				
		self.m_staticText82 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText82.Wrap( -1 )
		fgSizer1.Add( self.m_staticText82, 0, wx.ALL, 5 )
		
		self.m_staticText83 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText83.Wrap( -1 )
		fgSizer1.Add( self.m_staticText83, 0, wx.ALL, 5 )
		
		self.m_staticText84 = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText84.Wrap( -1 )
		fgSizer1.Add( self.m_staticText84, 0, wx.ALL, 5 )
		
		self.done = wx.StaticText( self.m_scrolledWindow1, wx.ID_ANY, u"VERIFY details and click  'Done'", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.done.Wrap( -1 )
		fgSizer1.Add( self.done, 0, wx.ALL, 5 )
		
		self._done = wx.Button( self.m_scrolledWindow1, wx.ID_ANY, u"Done", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self._done, 0, wx.ALL, 5 )
		
		
		self.m_scrolledWindow1.SetSizer( fgSizer1 )
		self.m_scrolledWindow1.Layout()
		fgSizer1.Fit( self.m_scrolledWindow1 )
		bSizer3.Add( self.m_scrolledWindow1, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		self.Bind(wx.EVT_BUTTON, self.OnLaunchCommandOk, id=wx.ID_ANY)#when 'done' button is pressed execute the function mentioned
	def OnLaunchCommandOk(self, event):
		    	global ir_us
		    	global ir_pa
		    	global to_st
		    	global fr_st
		    	global da_of_jo
		    	global tr_no
		    	global cl
		    	global na_1
		    	global ag_1
		    	global ge_1
		    	global be_1
		    	global id_ty1
		    	global id_no1
		    	global na_2
		    	global ag_2
		    	global ge_2
		    	global be_2
		    	global id_ty2
		    	global id_no2
		    	global na_3
		    	global ag_3
		    	global ge_3
		    	global be_3
		    	global id_ty3
		    	global id_no3
		    	global na_4
		    	global ag_4
		    	global ge_4
		    	global be_4
		    	global id_ty4
		    	global id_no4
		    	global sm
		    	global sbi_nb       
		    	global sbi_us
		    	global sbi_pa
                 
		    	ir_us=self._irctc_username.GetValue()
		    	ir_pa=self._irctc_password.GetValue()
		    	to_st=self._to_station.GetValue()
		    	fr_st=self._from_station.GetValue()
		    	da_of_jo=self._date_of_journey.GetValue()
		    	tr_no=self._train_no.GetValue()
		    	cl=self._class_of_j.GetStringSelection()
		    	na_1=self._name_1.GetValue()
		    	ag_1=self._age_1.GetValue()
		    	ge_1=self._gender_1.GetStringSelection()
		    	be_1=self.be_pr1.GetStringSelection()
		    	id_ty1=self._id_card_type1.GetStringSelection()
		    	id_no1=self._id_card_no1.GetValue()
		    	na_2=self._name_2.GetValue()
		    	ag_2=self._age_2.GetValue()
		    	ge_2=self._gender_2.GetStringSelection()
		    	be_2=self.be_pr2.GetStringSelection()
		    	id_ty2=self._id_card_type2.GetStringSelection()
		    	id_no2=self._id_card_no2.GetValue()
		    	na_3=self._name_3.GetValue()
		    	ag_3=self._age_3.GetValue()
		    	ge_3=self._gender_3.GetStringSelection()
		    	be_3=self.be_pr3.GetStringSelection()
		    	id_ty3=self._id_card_type3.GetStringSelection()
		    	id_no3=self._id_card_no3.GetValue()
		    	na_4=self._name_4.GetValue()
		    	ag_4=self._age_4.GetValue()
		    	ge_4=self._gender_4.GetStringSelection()
		    	be_4=self.be_pr4.GetStringSelection()
		    	id_ty4=self._id_card_type4.GetStringSelection()
		    	id_no4=self._id_card_no4.GetValue()
		    	sm=self._sms.GetValue()
		    	sbi_nb=self._sbi.GetValue()
		    	sbi_us=self._sbi_username.GetValue()
		    	sbi_pa=self._sbi_password.GetValue()
		    	self.Close()    
        	
	def __del__( self ):
		pass
	

app=wx.App(False)
frame=Main_window(None)
frame.Show(True)
app.MainLoop()
##this code is to login at 9:59
from bs4 import *
from urllib2 import *
import time
url=urlopen('http://www.timeanddate.com/worldclock/india/new-delhi')
soup=BeautifulSoup(url)
a=0
i=soup.find(class_='h1')
s= i.get_text()
hr=int(s[:2])
mi=int(s[3:5])
se=int(s[6:])
h=9-hr
m=58-mi
s=40-se
t=s+60*m+3600*h
#if t>0:
#    time.sleep(t)

from selenium import webdriver
driver = webdriver.Firefox()
driver.get("https://www.irctc.co.in/eticketing/loginHome.jsf")
username = driver.find_element_by_id("usernameId")
username.send_keys(ir_us)#entering username
password = driver.find_element_by_class_name("loginPassword")


password.send_keys(ir_pa)#entering password


ir_ca=''
ID=1
#this class is gui for captcha
class MyFrame2 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Captcha", pos = wx.Point( 50,50 ), size = wx.Size( 400,150 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 400,150 ), wx.Size( 400,150 ) )
		
		fgSizer1 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.captcha_1 = wx.StaticText( self, wx.ID_ANY, u"Enter Captcha", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.captcha_1.Wrap( -1 )
		fgSizer1.Add( self.captcha_1, 0, wx.ALL, 5 )
		
		self._captcha_1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self._captcha_1, 0, wx.ALL, 5 )
		
		self.refresh_captcha = wx.Button( self, ID, u"Refresh Captcha", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.refresh_captcha, 0, wx.ALL, 5 )
		
		self.continue_1 = wx.StaticText( self, wx.ID_ANY, u"After typing,press Continue", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.continue_1.Wrap( -1 )
		fgSizer1.Add( self.continue_1, 0, wx.ALL, 5 )
		
		self._continue_1 = wx.Button( self, wx.ID_ANY, u"Continue", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self._continue_1, 0, wx.ALL, 5 )
		
		self.SetSizer( fgSizer1 )
		self.Layout()
		

		self.Centre( wx.HORIZONTAL )
		self.Bind(wx.EVT_BUTTON, self.OnLaunchCommandOk, id=wx.ID_ANY)
		self.Bind(wx.EVT_BUTTON, self.RefreshCaptcha, id=ID)
	def OnLaunchCommandOk(self, event):
		    	global ir_ca                 
		    	ir_ca=self._captcha_1.GetValue()
		    	self.Close()
	def RefreshCaptcha(self,event):
		    	driver.find_element_by_id('refresh').click()
	def __del__( self ):
		pass
app2=wx.App(False)
frame=MyFrame2(None)
frame.Show(True)
app2.MainLoop()	


cap=driver.find_element_by_class_name('loginCaptcha')
cap.send_keys(ir_ca)#entering captcha
login = driver.find_element_by_id("loginbutton").click()#auto login
#this part is to start booking by 10:00 
url=urlopen('http://www.timeanddate.com/worldclock/india/new-delhi')
soup=BeautifulSoup(url)
a=0
i=soup.find(class_='h1')
s= i.get_text()
hr=int(s[:2])
mi=int(s[3:5])
se=int(s[6:])
h=9-hr
m=59-mi
s=59-se
t=s+60*m+3600*h
#if t>0:
#    time.sleep(t)
from_station = driver.find_element_by_id("jpform:fromStation")
from_station.send_keys(fr_st)#entering from station
time.sleep(0.3)
from_station.send_keys("\n")
to_station = driver.find_element_by_id("jpform:toStation")
to_station.send_keys(to_st)#entering to station
time.sleep(0.3)
to_station.send_keys("\n")
journey_date = driver.find_element_by_id("jpform:journeyDateInputDate")
journey_date.send_keys(da_of_jo)#entering journey date
submit = driver.find_element_by_id("jpform:jpsubmit").click()#submit
css=driver.find_element_by_css_selector('tr>td>input[value="CK"]').click()#select tatkal

k='td>a[href*="javascript:availFareEnq($(\'#cllink-'+tr_no+'-'+cl+'"]'


selection = driver.find_element_by_css_selector(k).click()#selecting class of the given train
#this class is a gui which is used to confirm whether the tickets are available for the selected train
class MyFrame2 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Tickets availability", pos = wx.DefaultPosition, size = wx.Size( 515,138 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.book = wx.StaticText( self, wx.ID_ANY, u"If the tickets are available,click Book", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.book.Wrap( -1 )
		fgSizer2.Add( self.book, 0, wx.ALL, 5 )
		
		self._book = wx.Button( self, wx.ID_ANY, u"Book", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self._book, 0, wx.ALL, 5 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"If not,(1) select required train, and (2)click Book now in browser", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		fgSizer2.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"; and then", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		fgSizer2.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.m_staticText41 = wx.StaticText( self, wx.ID_ANY, u"(3)click Continue here", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText41.Wrap( -1 )
		fgSizer2.Add( self.m_staticText41, 0, wx.ALL, 5 )
		
		self._continue = wx.Button( self, ID, u"Continue", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self._continue, 0, wx.ALL, 5 )
		
		
		self.SetSizer( fgSizer2 )
		self.Layout()
		self.Bind(wx.EVT_BUTTON, self.OnLaunchCommandOk, id=wx.ID_ANY)
		self.Bind(wx.EVT_BUTTON, self.OnLaunchCommandOk2, id=ID)
		self.Centre( wx.HORIZONTAL )
	def OnLaunchCommandOk(self, event):
		    	driver.find_element_by_id('refid1').click()
		    	self.Close()	
	def OnLaunchCommandOk2(self, event):
		    	self.Close()
	def __del__( self ):
		pass
app4=wx.App(False)
frame=MyFrame2(None)
frame.Show(True)
app4.MainLoop()
#entering passenger details
p0name = driver.find_element_by_id("addPassengerForm:psdetail:0:psgnName")
p0name.send_keys(na_1)
p0age = driver.find_element_by_id("addPassengerForm:psdetail:0:psgnAge")
p0age.send_keys(ag_1)
p0gender = driver.find_element_by_id("addPassengerForm:psdetail:0:psgnGender")
p0gender.send_keys(ge_1)
p0berth=driver.find_element_by_id("addPassengerForm:psdetail:0:berthChoice")
p0berth.send_keys(be_1)
#p0idtype = driver.find_element_by_id("addPassengerForm:psdetail:0:idCardType")
#p0idtype.send_keys(id_ty1)
#p0idno = driver.find_element_by_id("addPassengerForm:psdetail:0:idCardNumber")
#p0idno.send_keys(id_no1)

p1name = driver.find_element_by_id("addPassengerForm:psdetail:1:psgnName")
p1name.send_keys(na_2)
p1age = driver.find_element_by_id("addPassengerForm:psdetail:1:psgnAge")
p1age.send_keys(ag_2)
p1gender = driver.find_element_by_id("addPassengerForm:psdetail:1:psgnGender")
p1gender.send_keys(ge_2)
p1berth=driver.find_element_by_id("addPassengerForm:psdetail:1:berthChoice")
p1berth.send_keys(be_2)
#p1idtype = driver.find_element_by_id("addPassengerForm:psdetail:1:idCardType")
#p1idtype.send_keys(id_ty2)
#p1idno = driver.find_element_by_id("addPassengerForm:psdetail:1:idCardNumber")
#p1idno.send_keys(id_no2)

p2name = driver.find_element_by_id("addPassengerForm:psdetail:2:psgnName")
p2name.send_keys(na_3)
p2age = driver.find_element_by_id("addPassengerForm:psdetail:2:psgnAge")
p2age.send_keys(ag_3)
p2gender = driver.find_element_by_id("addPassengerForm:psdetail:2:psgnGender")
p2gender.send_keys(ge_3)
p2berth=driver.find_element_by_id("addPassengerForm:psdetail:2:berthChoice")
p2berth.send_keys(be_3)
#p2idtype = driver.find_element_by_id("addPassengerForm:psdetail:2:idCardType")
#p2idtype.send_keys(id_ty3)
#p2idno = driver.find_element_by_id("addPassengerForm:psdetail:2:idCardNumber")
#p2idno.send_keys(id_no3)

p3name = driver.find_element_by_id("addPassengerForm:psdetail:3:psgnName")
p3name.send_keys(na_4)
p3age = driver.find_element_by_id("addPassengerForm:psdetail:3:psgnAge")
p3age.send_keys(ag_4)
p3gender = driver.find_element_by_id("addPassengerForm:psdetail:3:psgnGender")
p3gender.send_keys(ge_4)
p3berth=driver.find_element_by_id("addPassengerForm:psdetail:3:berthChoice")
p3berth.send_keys(be_4)
#p3idtype = driver.find_element_by_id("addPassengerForm:psdetail:3:idCardType")
#p3idtype.send_keys(id_ty4)
#p3idno = driver.find_element_by_id("addPassengerForm:psdetail:3:idCardNumber")
#p3idno.send_keys(id_no4)

mobile_number = driver.find_element_by_id("addPassengerForm:mobileNo")
mobile_number.clear()
mobile_number.send_keys(sm)
cap=driver.find_element_by_id('j_captcha')
cap.send_keys('')
ir_ca=''
ID=1
#this class is again for entering captcha via gui
class MyFrame3 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Captcha" , pos = wx.Point( 50,50 ), size = wx.Size( 600,150 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 600,150 ), wx.Size( 600,150 ) )
		
		fgSizer1 = wx.FlexGridSizer( 0, 3, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.captcha_1 = wx.StaticText( self, wx.ID_ANY, u"Enter Captcha", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.captcha_1.Wrap( -1 )
		fgSizer1.Add( self.captcha_1, 0, wx.ALL, 5 )
		
		self._captcha_1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self._captcha_1, 0, wx.ALL, 5 )
		
		self.refresh_captcha = wx.Button( self, ID, u"Refresh Captcha", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.refresh_captcha, 0, wx.ALL, 5 )
		
		self.continue_1 = wx.StaticText( self, wx.ID_ANY, u"Verify ticket details; After typing,press Continue", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.continue_1.Wrap( -1 )
		fgSizer1.Add( self.continue_1, 0, wx.ALL, 5 )
		
		self._continue_1 = wx.Button( self, wx.ID_ANY, u"Continue", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self._continue_1, 0, wx.ALL, 5 )
		
		self.SetSizer( fgSizer1 )
		self.Layout()
		

		self.Centre( wx.HORIZONTAL )
		self.Bind(wx.EVT_BUTTON, self.OnLaunchCommandOk, id=wx.ID_ANY)
		self.Bind(wx.EVT_BUTTON, self.RefreshCaptcha, id=ID)
	def OnLaunchCommandOk(self, event):
		    	global ir_ca                 
		    	ir_ca=self._captcha_1.GetValue()
		    	self.Close()
	def RefreshCaptcha(self,event):
		    	driver.find_element_by_id('addPassengerForm:refresh_captcha_image').click()
	def __del__( self ):
		pass
app3=wx.App(False)
frame=MyFrame3(None)
frame.Show(True)
app3.MainLoop()
cap=driver.find_element_by_id('j_captcha')
cap.send_keys(ir_ca)#entering capctha
validate = driver.find_element_by_id("validate").click()#going to next page
if (sbi_nb):#checking if sbi netbanking is selected, and going through it if it is true
    
    sb = driver.find_element_by_css_selector("input[type='radio'][value='1']").click()
    validate = driver.find_element_by_id("validate").click()
    username = driver.find_element_by_id("username")
    username.send_keys(sbi_us)#enter username
    password = driver.find_element_by_id("label2")


    password.send_keys(sbi_pa)#enter password


    driver.find_element_by_id('Button2').click()
    driver.find_element_by_id('Go').click()
    driver.find_element_by_id('confirmButton').click()










