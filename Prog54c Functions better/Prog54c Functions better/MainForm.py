import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		resources = System.Resources.ResourceManager("Prog54c_Functions_better.MainForm", System.Reflection.Assembly.GetEntryAssembly())
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.FromArgb(128, 64, 0)
		self._label1.Location = System.Drawing.Point(2, 59)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(158, 44)
		self._label1.TabIndex = 0
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.FromArgb(128, 64, 0)
		self._label2.Location = System.Drawing.Point(2, 137)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(158, 41)
		self._label2.TabIndex = 1
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.FromArgb(128, 64, 0)
		self._textBox1.ForeColor = System.Drawing.SystemColors.Window
		self._textBox1.Location = System.Drawing.Point(232, 109)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(211, 20)
		self._textBox1.TabIndex = 2
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.FromArgb(128, 64, 0)
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.Yellow
		self._button1.Location = System.Drawing.Point(2, 205)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(124, 54)
		self._button1.TabIndex = 3
		self._button1.Text = "Claculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.FromArgb(128, 64, 0)
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.FromArgb(0, 192, 0)
		self._button2.Location = System.Drawing.Point(195, 205)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(124, 54)
		self._button2.TabIndex = 4
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.FromArgb(128, 64, 0)
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 11.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.ForeColor = System.Drawing.Color.Red
		self._button3.Location = System.Drawing.Point(391, 205)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(135, 54)
		self._button3.TabIndex = 5
		self._button3.Text = "EXIT"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveCaption
		self.BackgroundImage = resources.GetObject("$this.BackgroundImage")
		self.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self.ClientSize = System.Drawing.Size(528, 261)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Prog54c Functions better"
		self.ResumeLayout(False)
		self.PerformLayout()


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
	

	def Button3Click(self, sender, e):
		Application.Exit()