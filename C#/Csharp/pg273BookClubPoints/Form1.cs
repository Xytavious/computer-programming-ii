using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace pg273BookClubPoints
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            
            int p = 0;
            
            int b = int.Parse(textBox1.Text);

            if (b == 0)
                p = 0;

            else if (b == 1)
                p = 5;

            else if (b == 2)
                p = 15;

            else if (b == 3)
                p = 30;
            else if (b >= 4)
                p = 60;
            label1.Text = (" your Total points = " + p);

        }

        private void button2_Click(object sender, EventArgs e)
        {
            label1.Text
        }
    }
}
