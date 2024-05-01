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
            int x = label1.Text;
            label1.Text = (" input nuber of books in the Text Box");

            int b = textBox1.Text;
            if b => 0
                x = (" your Total points = ", b);
        }
    }
}
