#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：project_python 
@File    ：code01.py
@Author  ：guotong
@Date    ：2021/8/26 15:43 
'''
import PyQt5 as Qt
def init_ui(self):
    global type
    self.setFixedSize(1025, 750)
    self.main_widget = QWidget()  # 创建窗口主部件
    self.main_layout = QGridLayout()  # 创建主部件的网格布局
    self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局

    self.close_widget = QWidget()  # 创建关闭侧部件
    self.close_widget.setObjectName('close_widget')
    self.close_layout = QGridLayout()  # 创建左侧部件的网格布局层
    self.close_widget.setLayout(self.close_layout)  # 设置左侧部件布局为网格

    self.left_widget = QWidget()  # 创建左边侧部件
    self.left_widget.setObjectName('left_widget')
    self.left_layout = QGridLayout()  # 创建左侧部件的网格布局层
    self.left_widget.setLayout(self.left_layout)  # 设置左侧部件布局为网格

    self.right_widget = QWidget()  # 创建右侧部件
    self.right_widget.setObjectName('right_widget')
    self.right_layout = QGridLayout()
    self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格

    self.down_widget = QWidget()  # 创建下面部件
    self.down_widget.setObjectName('down_widget')
    self.down_layout = QGridLayout()
    self.down_widget.setLayout(self.down_layout)  # 设置下侧部件布局为网格

    self.up_widget = QWidget()  # 创建下面部件
    self.up_widget.setObjectName('up_widget')
    self.up_layout = QGridLayout()
    self.up_widget.setLayout(self.up_layout)  # 设置下侧部件布局为网格

    self.label = QLabel(self)
    self.label.setText("还没有播放歌曲呢╰(*°▽°*)╯")
    self.label.setStyleSheet("color:white")
    self.label.setMaximumSize(310, 20)

    self.main_layout.addWidget(self.up_widget, 0, 0, 1, 115)

    self.main_layout.addWidget(self.left_widget, 1, 0, 90, 25)
    self.main_layout.addWidget(self.right_widget, 1, 25, 90, 90)  # 22右侧部件在第0行第3列，占8行9列
    self.main_layout.addWidget(self.down_widget, 100, 0, 10, 115)
    self.main_layout.addWidget(self.close_widget, 0, 110, 1, 5)  # 左侧部件在第0行第0列，占1行3列

    self.down_layout.addWidget(self.label, 1, 0, 1, 1)
    self.setCentralWidget(self.main_widget)  # 设置窗口主部件

    self.tabWidget = QTabWidget(self)
    self.tabWidget.setGeometry(QRect(33, 20, 716, 471))
    self.tab = QWidget()
    self.tab.setObjectName("tab")
    self.tab_layout = QGridLayout()
    self.tab.setLayout(self.tab_layout)
    self.listwidget = QListWidget(self.tab)
    self.listwidget.doubleClicked.connect(lambda: self.change_func(self.listwidget))
    self.listwidget.setContextMenuPolicy(Qt.CustomContextMenu)
    self.listwidget.customContextMenuRequested[QPoint].connect(self.myListWidgetContext)
    self.listwidget.setObjectName("listWidget")
    self.tab_layout.addWidget(self.listwidget, 0, 0, 1, 1)
    self.tabWidget.addTab(self.tab, "      搜索页      ")

    self.tab2 = QWidget()
    self.tab2.setObjectName("tab")
    self.tab2_layout = QGridLayout()
    self.tab2.setLayout(self.tab2_layout)
    self.listwidget2 = QListWidget(self.tab2)
    self.listwidget2.doubleClicked.connect(lambda: self.change_funcse(self.listwidget2))
    self.listwidget2.setContextMenuPolicy(Qt.CustomContextMenu)
    self.listwidget2.customContextMenuRequested[QPoint].connect(self.myListWidgetContext2)
    self.listwidget2.setObjectName("listWidget2")
    self.listwidget2.setContextMenuPolicy(3)
    self.tab2_layout.addWidget(self.listwidget2, 0, 0, 1, 1)
    self.tabWidget.addTab(self.tab2, "      最近播放      ")

    self.right_layout.addWidget(self.tabWidget, 3, 0, 100, 90)

    self.left_close = QPushButton("")  # 关闭按钮
    self.left_close.clicked.connect(self.close)
    self.left_visit = QPushButton("")  # 空白按钮
    self.left_visit.clicked.connect(self.big)
    self.left_mini = QPushButton("")  # 最小化按钮
    self.left_mini.clicked.connect(self.mini)
    self.close_layout.addWidget(self.left_mini, 0, 0, 1, 1)
    self.close_layout.addWidget(self.left_close, 0, 2, 1, 1)
    self.close_layout.addWidget(self.left_visit, 0, 1, 1, 1)
    self.left_close.setFixedSize(15, 15)  # 设置关闭按钮的大小
    self.left_visit.setFixedSize(15, 15)  # 设置按钮大小
    self.left_mini.setFixedSize(15, 15)  # 设置最小化按钮大小
    self.left_close.setStyleSheet(
        '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
    self.left_visit.setStyleSheet(
        '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
    self.left_mini.setStyleSheet(
        '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')


    self.button_123 = QLabel("")
    self.left_layout.addWidget(self.button_123, 0, 2, 2, 2)
    self.label2 = QLabel(self)
    self.label2.setText("当前为顺序播放")
    self.label2.setStyleSheet("color:green")
    self.left_layout.addWidget(self.label2, 4, 0, 2, 1)
    self.button_1234 = QPushButton(icon('fa.download', color='#3FC89C', font=24), "")
    self.button_1234.clicked.connect(self.down)
    self.button_1234.setStyleSheet(
        '''QPushButton{background:#222225;border-radius:5px;}QPushButton:hover{background:#3684C8;}''')
    self.left_layout.addWidget(self.button_1234, 4, 2, 2, 1)
    self.button_1234 = QPushButton(icon('fa.heart', color='#3FC89C', font=24), "")
    self.button_1234.clicked.connect(self.lovesong)
    self.button_1234.setStyleSheet(
        '''QPushButton{background:#222225;border-radius:5px;}QPushButton:hover{background:#3684C8;}''')
    self.left_layout.addWidget(self.button_1234, 4, 3, 2, 2)
    self.label3 = QLabel(self)
    self.label3.setText("")
    self.label3.setStyleSheet("color:white")
    self.down_layout.addWidget(self.label3, 1, 3, 1, 1)

    self.label7 = QLabel(self)
    self.label7.setText("")
    self.label7.setStyleSheet("color:white")
    self.label5 = QLabel(self)
    pix_img = QPixmap(str(data + '/backdown.png'))
    pix = pix_img.scaled(300, 300, Qt.KeepAspectRatio)
    self.label5.setPixmap(pix)
    # self.label5.setMaximumSize(1,1)
    self.left_layout.addWidget(self.label5, 2, 0, 2, 8)
    self.label6 = QLabel(self)
    self.label6.setText("")
    self.label6.setStyleSheet("color:#6DDF6D")
    self.left_layout.addWidget(self.label6, 2, 0, 2, 2)

    self.label23 = QLabel(self)
    self.label23.setText("                 ")
    self.label23.setStyleSheet("color:#6DDF6D")
    self.up_layout.addWidget(self.label23, 0, 100, 1, 20)

    self.shuru = QLineEdit("")
    self.up_layout.addWidget(self.shuru, 0, 120, 1, 40)
    self.shuru.returnPressed.connect(self.correct)

    self.label23 = QLabel(self)
    self.label23.setText("     软件")
    self.label23.setStyleSheet("color:#6DDF6D")
    self.up_layout.addWidget(self.label23, 0, 160, 1, 10)

    self.label61 = QLabel(self)
    self.label61.setText("")
    self.label61.setStyleSheet("color:#6DDF6D")
    self.up_layout.addWidget(self.label61, 0, 200, 1, 50)

    self.cb = QComboBox(self)
    self.cb.addItems(['网易云', '酷狗',  'qq'])
    self.up_layout.addWidget(self.cb, 0, 180, 1, 30)
    self.cb.currentIndexChanged[int].connect(self.print)
    self.button_1 = QPushButton(icon('fa.search', color='white'), "")
    self.button_1.clicked.connect(self.correct)
    self.button_1.setStyleSheet(
        '''
        QPushButton{color:white;border-radius:5px;}QPushButton:hover{background:green;}
        ''')
    self.up_layout.addWidget(self.button_1, 0, 155, 1, 5)

    self.right_process_bar = QProgressBar()  # 播放进度部件
    self.right_process_bar.setValue(49)
    self.right_process_bar.setFixedHeight(3)  # 设置进度条高度
    self.right_process_bar.setTextVisible(False)  # 不显示进度条文字
    self.right_process_bar.setRange(0, 10000)

    self.right_playconsole_widget = QWidget()  # 播放控制部件
    self.right_playconsole_layout = QGridLayout()  # 播放控制部件网格布局层
    self.right_playconsole_widget.setLayout(self.right_playconsole_layout)

    self.console_button_1 = QPushButton(icon('fa.backward', color='#3FC89C'), "")
    self.console_button_1.clicked.connect(self.last)
    self.console_button_1.setStyleSheet(
        '''QPushButton{background:#222225;border-radius:5px;}QPushButton:hover{background:#3684C8;}''')

    self.console_button_2 = QPushButton(icon('fa.forward', color='#3FC89C'), "")
    self.console_button_2.clicked.connect(self.nextion)
    self.console_button_2.setStyleSheet(
        '''QPushButton{background:#222225;border-radius:5px;}QPushButton:hover{background:#3684C8;}''')

    self.console_button_3 = QPushButton(icon('fa.pause', color='#3FC89C', font=18), "")
    self.console_button_3.clicked.connect(self.pause)
    self.console_button_3.setStyleSheet(
        '''QPushButton{background:#222225;border-radius:5px;}QPushButton:hover{background:#3684C8;}''')

    self.console_button_4 = QPushButton(icon('fa.volume-down', color='#3FC89C', font=18), "")
    self.console_button_4.clicked.connect(self.voicedown)
    self.console_button_4.setStyleSheet(
        '''QPushButton{background:#222225;border-radius:5px;}QPushButton:hover{background:#3684C8;}''')

    self.console_button_5 = QPushButton(icon('fa.volume-up', color='#3FC89C', font=18), "")
    self.console_button_5.clicked.connect(self.voiceup)
    self.console_button_5.setStyleSheet(
        '''QPushButton{background:#222225;border-radius:5px;}QPushButton:hover{background:#3684C8;}''')

    self.console_button_6 = QPushButton(icon('fa.align-center', color='#3FC89C', font=18), "")
    self.console_button_6.clicked.connect(self.playmode)
    self.console_button_6.setStyleSheet(
        '''QPushButton{background:#222225;border-radius:5px;}QPushButton:hover{background:#3684C8;}''')

    self.console_button_3.setIconSize(QSize(30, 30))

    self.right_playconsole_layout.addWidget(self.console_button_4, 0, 0)

    self.right_playconsole_layout.addWidget(self.console_button_1, 0, 1)
    self.right_playconsole_layout.addWidget(self.console_button_3, 0, 2)

    self.right_playconsole_layout.addWidget(self.console_button_2, 0, 3)

    self.right_playconsole_layout.addWidget(self.console_button_5, 0, 4)

    self.right_playconsole_layout.addWidget(self.console_button_6, 0, 5)
    self.right_playconsole_layout.setAlignment(Qt.AlignCenter)  # 设置布局内部件居中显示
    self.down_layout.addWidget(self.right_process_bar, 0, 0, 1, 4)  # 第0行第0列，占8行3列
    # 第0行第0列，占8行3列
    self.down_layout.addWidget(self.label7, 1, 2, 1, 1)
    self.down_layout.addWidget(self.right_playconsole_widget, 1, 0, 1, 4)
    self.setWindowOpacity(0.95)  # 设置窗口透明度
    self.setAttribute(Qt.WA_TranslucentBackground)
    self.setWindowFlag(Qt.FramelessWindowHint)  # 隐藏边框
    self.main_layout.setSpacing(0)

def run(self):
  qmut.lock()
  try:
      global paing
      global stop
      global lrcs
      global urls
      global songs
      global name
      global songid
      global proxies
      global pic
      global tryed
      paing = True

      print('搜索软件{}'.format(type))
      print('开始搜索')
      name = name
      headers = {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.110.430.128 Safari/537.36',
          'X-Requested-With': 'XMLHttpRequest'

      }
      urls = []
      songs = []
      pic = []
      lrcs = []
      pages = 5
      print(pages)
      for a in range(0, pages):
          if not stop:

              urlss = ['http://music.9q4.cn/', 'https://defcon.cn/dmusic/','http://www.xmsj.org/',
                      'http://music.laomao.me/']
              print (tryed)
              if tryed >3:

                  tryed = 0
                  url = urlss[tryed]
              else:
                  url = urlss[tryed]
              print (urlss[tryed])

              params = {'input': name,
                        'filter': 'name',
                        'type': type,
                        'page': a
                        }
              if not stop:
                  try:
                      res = post(url, params, headers=headers, proxies=proxies)
                      html = res.json()

                      for i in range(0, 10):

                              try:
                                  title = jsonpath(html, '$..title')[i]
                                  author = jsonpath(html, '$..author')[i]
                                  url1 = jsonpath(html, '$..url')[i]  # 取下载网址
                                  pick = jsonpath(html, '$..pic')[i]  # 取歌词
                                  lrc = jsonpath(html, '$..lrc')[i]
                                  print(title, author)
                                  lrcs.append(lrc)
                                  urls.append(url1)
                                  pic.append(pick)
                                  songs.append(str(title) + ' - ' + str(author))
                              except:
                                  pass
                  except:
                      stop = False
                      paing = False
                  self.trigger.emit(str('finish'))
              else:
                  self.trigger.emit(str('finish'))
          else:
              self.trigger.emit(str('clear'))
              pass

      stop = False
      paing = False
  except:
      print('爬取歌曲出错')
      self.trigger.emit(str('unfinish'))
      stop = False
      paing = False
  qmut.unlock()
