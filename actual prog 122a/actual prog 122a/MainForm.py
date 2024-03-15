import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *
from math import sqrt

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._listBox1 = System.Windows.Forms.ListBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.AutoSize = True
		self._button1.BackColor = System.Drawing.SystemColors.ActiveCaptionText
		self._button1.Font = System.Drawing.Font("Old English Text MT", 9.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.FromArgb(192, 0, 0)
		self._button1.Location = System.Drawing.Point(12, 218)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(86, 51)
		self._button1.TabIndex = 0
		self._button1.Text = "Claculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.SystemColors.ActiveCaptionText
		self._button2.Font = System.Drawing.Font("Old English Text MT", 9.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.FromArgb(192, 0, 0)
		self._button2.Location = System.Drawing.Point(124, 218)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(86, 51)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.SystemColors.ActiveCaptionText
		self._button3.Font = System.Drawing.Font("Old English Text MT", 9.75, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.FromArgb(192, 0, 0)
		self._button3.Location = System.Drawing.Point(244, 218)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(80, 49)
		self._button3.TabIndex = 2
		self._button3.Text = "EXIT"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.SystemColors.InfoText
		self._listBox1.Font = System.Drawing.Font("Franklin Gothic Heavy", 8.25, System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.ForeColor = System.Drawing.Color.FromArgb(192, 0, 0)
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 15
		self._listBox1.Location = System.Drawing.Point(12, 26)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(312, 169)
		self._listBox1.TabIndex = 4
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ControlText
		self.ClientSize = System.Drawing.Size(336, 278)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "actual prog 122a"
		self.TransparencyKey = System.Drawing.Color.Transparent
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		for num in range (1, 51):
			numSqu = num**2
			root = sqrt(num)
			
			msg = str(num) + "\t\t" + str(numSqu) + "\t\t" + str(round(root, 4))
			self._listBox1.Items.Add(msg)
			
			
		

	def Button3Click(self, sender, e):
		application.EXIT()

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()