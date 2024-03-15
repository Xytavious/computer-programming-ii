import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label2 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(42, 190)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(91, 41)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label1.Location = System.Drawing.Point(42, 88)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 1
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(167, 190)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(89, 41)
		self._button2.TabIndex = 2
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(299, 190)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(91, 41)
		self._button3.TabIndex = 3
		self._button3.Text = "EXIT"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.ButtonHighlight
		self._label2.Location = System.Drawing.Point(42, 131)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 4
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(190, 115)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(161, 20)
		self._textBox1.TabIndex = 6
		self._textBox1.TextAlign = System.Windows.Forms.HorizontalAlignment.Center
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveCaption
		self.ClientSize = System.Drawing.Size(431, 271)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "prog54c"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button3Click(self, sender, e):
		Application.Exit()

	def Button1Click(self, sender, e):
		rad = float(self._textBox1.Text)
		Area = rad ** 2 * 3.14159 
		Cir = 2 * 3.14159 * rad
		Di = rad * 2
		self._label1.Text = str(round( Area,3))
		self._label2.Text = str(round( Cir,3))

	def Button2Click(self, sender, e):
		self._label1.Text =""
		self._label2.Text =""
		self._textBox1.Text =""
	