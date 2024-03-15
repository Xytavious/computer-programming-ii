import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._listBox1 = System.Windows.Forms.ListBox()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ControlLightLight
		self._label1.Location = System.Drawing.Point(149, 15)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(49, 23)
		self._label1.TabIndex = 0
		self._label1.Text = "Hours"
		self._label1.Click += self.Label1Click
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.SystemColors.ControlLightLight
		self._label2.Location = System.Drawing.Point(285, 15)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(54, 23)
		self._label2.TabIndex = 1
		self._label2.Text = "Pay"
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 324)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(97, 42)
		self._button1.TabIndex = 3
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(194, 324)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(104, 46)
		self._button2.TabIndex = 4
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(366, 324)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(94, 46)
		self._button3.TabIndex = 5
		self._button3.Text = "EXIT"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# listBox1
		# 
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(84, 53)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(335, 225)
		self._listBox1.TabIndex = 6
		self._listBox1.SelectedIndexChanged += self.ListBox1SelectedIndexChanged
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.Highlight
		self.ClientSize = System.Drawing.Size(488, 386)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "prog122b"
		self.ResumeLayout(False)


	def Label1Click(self, sender, e):
		pass

	def Button3Click(self, sender, e):
		Appliaction.Exit()

	def Button1Click(self, sender, e):
		for num in range (1, 41):
			hour = num*4
			
			
			msg = str(num) + "\t\t" + str(hour)
			self._listBox1.Items.Add(msg)
			

	def ListBox1SelectedIndexChanged(self, sender, e):
		pass

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()