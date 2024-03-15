import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		resources = System.Resources.ResourceManager("skateboarding485.MainForm", System.Reflection.Assembly.GetEntryAssembly())
		self._checkBox1 = System.Windows.Forms.CheckBox()
		self._checkBox2 = System.Windows.Forms.CheckBox()
		self._checkBox3 = System.Windows.Forms.CheckBox()
		self._checkBox4 = System.Windows.Forms.CheckBox()
		self._checkBox5 = System.Windows.Forms.CheckBox()
		self._checkBox6 = System.Windows.Forms.CheckBox()
		self._checkBox7 = System.Windows.Forms.CheckBox()
		self._checkBox8 = System.Windows.Forms.CheckBox()
		self._checkBox9 = System.Windows.Forms.CheckBox()
		self._checkBox10 = System.Windows.Forms.CheckBox()
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# checkBox1
		# 
		self._checkBox1.Location = System.Drawing.Point(37, 88)
		self._checkBox1.Name = "checkBox1"
		self._checkBox1.Size = System.Drawing.Size(127, 25)
		self._checkBox1.TabIndex = 0
		self._checkBox1.Text = "The Master Thrasher"
		self._checkBox1.UseVisualStyleBackColor = True
		# 
		# checkBox2
		# 
		self._checkBox2.Location = System.Drawing.Point(37, 119)
		self._checkBox2.Name = "checkBox2"
		self._checkBox2.Size = System.Drawing.Size(127, 24)
		self._checkBox2.TabIndex = 1
		self._checkBox2.Text = "The Dictator of Grind"
		self._checkBox2.UseVisualStyleBackColor = True
		# 
		# checkBox3
		# 
		self._checkBox3.Location = System.Drawing.Point(37, 149)
		self._checkBox3.Name = "checkBox3"
		self._checkBox3.Size = System.Drawing.Size(127, 24)
		self._checkBox3.TabIndex = 2
		self._checkBox3.Text = "The Street King"
		self._checkBox3.UseVisualStyleBackColor = True
		# 
		# checkBox4
		# 
		self._checkBox4.Location = System.Drawing.Point(37, 179)
		self._checkBox4.Name = "checkBox4"
		self._checkBox4.Size = System.Drawing.Size(127, 24)
		self._checkBox4.TabIndex = 3
		self._checkBox4.Text = "7.75 axle"
		self._checkBox4.UseVisualStyleBackColor = True
		# 
		# checkBox5
		# 
		self._checkBox5.Location = System.Drawing.Point(37, 209)
		self._checkBox5.Name = "checkBox5"
		self._checkBox5.Size = System.Drawing.Size(127, 24)
		self._checkBox5.TabIndex = 4
		self._checkBox5.Text = "8 axle"
		self._checkBox5.UseVisualStyleBackColor = True
		# 
		# checkBox6
		# 
		self._checkBox6.Location = System.Drawing.Point(191, 85)
		self._checkBox6.Name = "checkBox6"
		self._checkBox6.Size = System.Drawing.Size(87, 24)
		self._checkBox6.TabIndex = 5
		self._checkBox6.Text = "8.5 axle"
		self._checkBox6.UseVisualStyleBackColor = True
		# 
		# checkBox7
		# 
		self._checkBox7.Location = System.Drawing.Point(191, 114)
		self._checkBox7.Name = "checkBox7"
		self._checkBox7.Size = System.Drawing.Size(87, 29)
		self._checkBox7.TabIndex = 6
		self._checkBox7.Text = "checkBox7"
		self._checkBox7.UseVisualStyleBackColor = True
		# 
		# checkBox8
		# 
		self._checkBox8.Location = System.Drawing.Point(191, 144)
		self._checkBox8.Name = "checkBox8"
		self._checkBox8.Size = System.Drawing.Size(87, 29)
		self._checkBox8.TabIndex = 7
		self._checkBox8.Text = "checkBox8"
		self._checkBox8.UseVisualStyleBackColor = True
		# 
		# checkBox9
		# 
		self._checkBox9.Location = System.Drawing.Point(191, 175)
		self._checkBox9.Name = "checkBox9"
		self._checkBox9.Size = System.Drawing.Size(87, 29)
		self._checkBox9.TabIndex = 8
		self._checkBox9.Text = "checkBox9"
		self._checkBox9.UseVisualStyleBackColor = True
		# 
		# checkBox10
		# 
		self._checkBox10.Location = System.Drawing.Point(191, 206)
		self._checkBox10.Name = "checkBox10"
		self._checkBox10.Size = System.Drawing.Size(87, 29)
		self._checkBox10.TabIndex = 9
		self._checkBox10.Text = "checkBox10"
		self._checkBox10.UseVisualStyleBackColor = True
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.SystemColors.ActiveCaptionText
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(343, 73)
		self._label1.TabIndex = 10
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 266)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(82, 39)
		self._button1.TabIndex = 11
		self._button1.Text = "Claculate"
		self._button1.UseVisualStyleBackColor = True
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(138, 266)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(87, 39)
		self._button2.TabIndex = 12
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(271, 266)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(87, 39)
		self._button3.TabIndex = 13
		self._button3.Text = "EXIT"
		self._button3.UseVisualStyleBackColor = True
		# 
		# MainForm
		# 
		self.BackgroundImage = resources.GetObject("$this.BackgroundImage")
		self.ClientSize = System.Drawing.Size(370, 310)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._checkBox10)
		self.Controls.Add(self._checkBox9)
		self.Controls.Add(self._checkBox8)
		self.Controls.Add(self._checkBox7)
		self.Controls.Add(self._checkBox6)
		self.Controls.Add(self._checkBox5)
		self.Controls.Add(self._checkBox4)
		self.Controls.Add(self._checkBox3)
		self.Controls.Add(self._checkBox2)
		self.Controls.Add(self._checkBox1)
		self.Name = "MainForm"
		self.Text = "skateboarding485"
		self.ResumeLayout(False)

