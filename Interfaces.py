import curses
class ConsoleInterface:
    def __init__(self):
        pass

    def set_board(self, inputstr):
        '''
        Takes board info as an inputstr
        and prints it to the console.
        '''
        print(inputstr)

    def set_msg(self, inputstr, **kwargs):
        '''
        Takes an inputstr and prints it
        to the console.
        '''
        if "end" in kwargs:
          ending = kwargs["end"]
          print(inputstr, end = ending)
        else:
          print(inputstr)

    def get_player_input(self, msgstr):
        '''
        Prompts the user with a msgstr,
        returns their input as str.
        '''
        value = input(msgstr)
        return value

class TextInterface:
  def __init__(self):
    self.stdscr = curses.initscr()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    y, x = 0, 0
    self.boardwin = curses.newwin(11, 40, y , x)
    self.drawborder(self.boardwin, (0,2), "Board")
    y += 11
    self.msgwin = curses.newwin(5, 40, y, x)
    self.drawborder(self.msgwin, (0,2), "Messages")
    y += 5
    self.inputwin = curses.newwin(3, 40, y, x)
    self.drawborder(self.inputwin, (0,2), "Player")
  
  @staticmethod
  def drawborder(window, position:tuple, label:str):
    window.clear()
    window.border()
    y, x = position
    window.addstr(y, x, label)

  
  def set_board(self, inputstr):
    self.drawborder(self.boardwin, (0,2), "Board")
    lines = inputstr.split("\n")
    for i in range(len(lines)-1):
      self.boardwin.addstr(i + 1, 10, lines[i])
    self.boardwin.refresh()

  def set_msg(self, inputstr, status=None):
    self.drawborder(self.msgwin, (0,2), "Messages")
    if status in ["error", "check", "checkmate"]:
      self.msgwin.addstr(1, 1, inputstr, curses.color_pair(1))
    else: 
      self.msgwin.addstr(1, 1, inputstr)
    self.msgwin.refresh()

  def get_player_input(self, msg):
    self.drawborder(self.inputwin, (0,2), "Player")
    self.inputwin.addstr(1, 1,msg)
    value = self.inputwin.getstr()
    value = value.decode("utf-8")
    return value

