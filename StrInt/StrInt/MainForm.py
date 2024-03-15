import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.GhostWhite
		self._label1.Location = System.Drawing.Point(12, 100)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(360, 94)
		self._label1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.GhostWhite
		self._button1.Location = System.Drawing.Point(10, 218)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(90, 40)
		self._button1.TabIndex = 1
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.GhostWhite
		self._button2.Location = System.Drawing.Point(147, 218)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(90, 40)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.GhostWhite
		self._button3.Location = System.Drawing.Point(282, 218)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(90, 40)
		self._button3.TabIndex = 3
		self._button3.Text = "EXIT"
		self._button3.UseVisualStyleBackColor = False
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(50, 50)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(278, 20)
		self._textBox1.TabIndex = 4
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.MidnightBlue
		self.ClientSize = System.Drawing.Size(385, 281)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "StrInt"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		txt = self._textBox1.Text
		x = txt.index("m")
		self.label1.Text = x