using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace MassNweight
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int mass = int.Parse(textBox1.Text);
            double weight = mass * 9.8;
            if (weight >= 1000)
                label1.Text = ("it is too heavy ");
            else if (weight <= 10)
                label1.Text = (" it is too light");
            else if (label1.Text = "the Weight is" + weight)
        }
    }
}
