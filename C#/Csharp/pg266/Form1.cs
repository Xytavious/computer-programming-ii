using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace pg266
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void label5_Click(object sender, EventArgs e)
        {

        }

        private void label9_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            int b = int.Parse(textBox1.Text);
            int a = int.Parse(textBox2.Text);
            if (a == b)
                label1.Text = ("Value A and Value B are equal");
            else if (a < b)
                label1.Text = ("Value A is less than Value B");
            else if (a > b)
                label1.Text = ("Value A is greater than Value B ");
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
