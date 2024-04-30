using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Prog310a
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e)
        {

        }

        private void button1_Click(object sender, EventArgs e)
        {
            Random rand = new Random();

            // in lcv =0; while (lcv< ...){lcv++; }
            // clcv++ means lcv += 1
            for (int lcv = 0; lcv < rand.Next(5, 11); lcv++)
            {
                double freq = rand.Next(0, 21) + rand.NextDouble();
                string msg = "";
                int max = (int)Math.Round(freq);
                for (int lcv2 = 0; lcv2 < max; lcv2++)
                    msg += "*";
                msg += " " + Math.Round(freq, 2);
                listBox1.Items.Add(msg);
            }
        }
    }
}
