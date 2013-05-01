"""
A simple programme for displaying text files
GitHub - https://github.com/anjanborah/Text_File_Viewer_Simple_Python
Author - Anjan Borah
Copyright ( c ) 2013 Anjan Borah
"""
try:
  import Tkinter
  import sys
  import os
except( ImportError ) as exception:
  print exception
class Application:
  
  def __init__( self ):
    
    # +----------------------------------------------------------------------+
    # |                      Creating the main window                        |
    # +----------------------------------------------------------------------+
    self.root_window = Tkinter.Tk()
    self.root_window.title( "Text file viewer" )
    self.root_window.geometry( "800x640" )
    
    self.create_the_layout()
    
    # +----------------------------------------------------------------------+
    # |                  The main loop of the application                    |
    # +----------------------------------------------------------------------+
    Tkinter.mainloop()
    
  def create_the_layout( self ):
    
    # Frame 1
    # This will contain,
    #   (a) Application name
    #   (b) File name input box
    #   (c) Button to display the file content
    #   (d) Button to clear the displayed data
    self.frame_1 = Tkinter.Frame( self.root_window, name = "frame_1" )
    self.frame_1.config( width = 800 )
    self.frame_1.config( height = 100 )
    self.frame_1.config( background = "#ffffff" )
    self.frame_1.place( x = 0, y = 0 )
    
    self.label_application_name = Tkinter.Label( self.frame_1, name = "label_application_name" )
    self.label_application_name.config( text = "Text file viewer" )
    self.label_application_name.config( font = ( "FreeSans", 40 ) )
    self.label_application_name.config( background = "#ffffff" )
    self.label_application_name.config( foreground = "#464646" )
    self.label_application_name.config( padx = 10, pady = 0 )
    self.label_application_name.place( x = 0, y = 0 )
    
    self.label_tkinter_is_not_ugly = Tkinter.Label( self.frame_1, name = "label_tkinter_is_not_ugly" )
    self.label_tkinter_is_not_ugly.config( text = "Tkinter is not ugly" )
    self.label_tkinter_is_not_ugly.config( font = ( "FreeSans", 8 ) )
    self.label_tkinter_is_not_ugly.config( background = "#ffffff" )
    self.label_tkinter_is_not_ugly.config( foreground = "#464646" )
    self.label_tkinter_is_not_ugly.config( padx = 20, pady = 0 )
    self.label_tkinter_is_not_ugly.place( x = 0, y = 60 )
    
    self.label_file_name = Tkinter.Label( self.frame_1, name = "label_file_name" )
    self.label_file_name.config( text = "File path" )
    self.label_file_name.config( font = ( "FreeSans", 8 ) )
    self.label_file_name.config( background = "#ffffff" )
    self.label_file_name.config( foreground = "#464646" )
    self.label_file_name.place( x = 500, y = 10 )
    
    self.entry_file_name = Tkinter.Entry( self.frame_1, name = "entry_file_name" )
    self.entry_file_name.config( borderwidth = "0.2" )
    self.entry_file_name.config( width = 35 )
    self.entry_file_name.config( font = ( "FreeSans", 8 ) )
    self.entry_file_name.config( foreground = "#464646" )
    self.entry_file_name.config( width = 46 )
    self.entry_file_name.place( x = 500, y = 30 )
    
    self.button_display_file = Tkinter.Button( self.frame_1, name = "button_display_file" )
    self.button_display_file.config( command = self.display_file )
    self.button_display_file.config( text = "Display" )
    self.button_display_file.config( font = ( "FreeSans", 8 ) )
    self.button_display_file.config( foreground = "#464646" )
    self.button_display_file.config( borderwidth = "0.2" )
    self.button_display_file.config( width = 19 )
    self.button_display_file.place( x = 500, y = 53 )
    
    self.button_reset_file = Tkinter.Button( self.frame_1, name = "button_reset_file" )
    self.button_reset_file.config( command = self.reset )
    self.button_reset_file.config( text = "Reset" )
    self.button_reset_file.config( font = ( "FreeSans", 8 ) )
    self.button_reset_file.config( foreground = "#464646" )
    self.button_reset_file.config( borderwidth = "0.2" )
    self.button_reset_file.config( width = 19 )
    self.button_reset_file.place( x = 640, y = 53 )
    
    # Frame2
    # This will contain
    #   (a) A text area, where the file content will be displayed
    #   (b) A horizontal and a vertical scrollbar for the text area
    self.frame_2 = Tkinter.Frame( self.root_window )
    self.frame_2.config( width = 800 )
    self.frame_2.config( height = 540 )
    self.frame_2.config( background = "#ffffff" )
    self.frame_2.config( padx = 10, pady = 10 )
    self.frame_2.place( x = 0, y = 100 )
    
    self.text_file_content = Tkinter.Text( self.frame_2, name = "text_file_content" )
    self.text_file_content.config( width = 126 )
    self.text_file_content.config( height = 33 )
    self.text_file_content.config( background = "#ffffff" )
    self.text_file_content.config( foreground = "#464646" )
    self.text_file_content.config( font = ( "FreeSans", 8 ) )
    self.text_file_content.config( borderwidth = "0.2" )
    self.text_file_content.config( highlightcolor = "gray" )
    self.text_file_content.place( x = 0, y = 0 )
    
    self.text_file_content_scroll_y = Tkinter.Scrollbar( self.frame_2, name = "text_file_content_scroll_y" )
    self.text_file_content_scroll_y.config( orient = Tkinter.VERTICAL )
    self.text_file_content_scroll_y.place( width = 10 )
    self.text_file_content_scroll_y.place( height = 499 )
    self.text_file_content_scroll_y.config( borderwidth = "0.0" )
    self.text_file_content_scroll_y.config( troughcolor = "#ffffff" )
    self.text_file_content_scroll_y.config( background = "#ffffff" )
    self.text_file_content_scroll_y.config( activebackground = "#ffffff" )
    self.text_file_content_scroll_y.config( command = self.text_file_content.yview )
    self.text_file_content_scroll_y.place( x = 760, y = 0 )
    
    self.text_file_content_scroll_x = Tkinter.Scrollbar( self.frame_2, name = "text_file_content_scroll_x" )
    self.text_file_content_scroll_x.config( orient = Tkinter.HORIZONTAL )
    self.text_file_content_scroll_x.place( width = 760 )
    self.text_file_content_scroll_x.place( height = 10 )
    self.text_file_content_scroll_x.config( borderwidth = "0.0" )
    self.text_file_content_scroll_x.config( troughcolor = "#ffffff" )
    self.text_file_content_scroll_x.config( background = "#ffffff" )
    self.text_file_content_scroll_x.config( activebackground = "#ffffff" )
    self.text_file_content_scroll_x.config( command = self.text_file_content.xview )
    self.text_file_content_scroll_x.place( x = 0, y = 499 )
    
    # Binding the scrollbars to the text area
    self.text_file_content.config( xscrollcommand = self.text_file_content_scroll_x.set )
    self.text_file_content.config( yscrollcommand = self.text_file_content_scroll_y.set )
    
  def display_file( self ):
    # +----------------------------------------------------------------------+
    # |                    This funciton reads the file                      |
    # +----------------------------------------------------------------------+
    
    self.text_file_content.delete( 1.0, Tkinter.END )
    file_name = str( self.entry_file_name.get() )
    try:
      if os.path.exists( file_name ) == True:
        self.text_file_content_scroll_y.config( troughcolor = "#B8B8B8" )
        self.text_file_content_scroll_x.config( troughcolor = "#B8B8B8" )
        self.text_file_content_scroll_y.config( activebackground = "#828282" )
        self.text_file_content_scroll_x.config( activebackground = "#828282" )
        file_content = open( file_name, "r" ).readlines()
        for line in file_content:
          self.text_file_content.insert( Tkinter.INSERT, line )
      else:
        self.text_file_content_scroll_y.config( troughcolor = "#B8B8B8" )
        self.text_file_content_scroll_x.config( troughcolor = "#B8B8B8" )
        self.text_file_content_scroll_y.config( activebackground = "#828282" )
        self.text_file_content_scroll_x.config( activebackground = "#828282" )
        self.text_file_content.insert( Tkinter.INSERT, "The file [ \" "+file_name+" \" ] does not exists \n\n" )
        files_in_the_current_directory = os.listdir( "." )
        self.text_file_content.insert( Tkinter.INSERT, "\tFiles in the current directory are...\n" )
        for item in files_in_the_current_directory:
          i = files_in_the_current_directory.index( item ) + 1
          self.text_file_content.insert( Tkinter.INSERT, "\t("+str(i)+") "+item+"\n" )
    except( Exception ) as exception:
      pass
    
  def reset( self ):
    # +----------------------------------------------------------------------+
    # |                 This function resets the display                     |
    # +----------------------------------------------------------------------+
    self.text_file_content.delete( 1.0, Tkinter.END )
    self.entry_file_name.delete( 0, Tkinter.END )
    self.text_file_content_scroll_y.config( troughcolor = "#ffffff" )
    self.text_file_content_scroll_y.config( background = "#ffffff" )
    self.text_file_content_scroll_y.config( activebackground = "#ffffff" )
    self.text_file_content_scroll_x.config( troughcolor = "#ffffff" )
    self.text_file_content_scroll_x.config( background = "#ffffff" )
    self.text_file_content_scroll_x.config( activebackground = "#ffffff" )
    
