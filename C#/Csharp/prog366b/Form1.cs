using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace prog366b
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {

            listBox1.Items.Clear();
            listBox1.Items.Add("The following numvers generated" + "by the formula x^2 -x + 41 are:");

            int x = 1
                while (true)
            {
                int num = f(x);
                if (isPrime(num, 2))
                    listBox1.Items.Add(num + "\tprime");
                else {
                    int fac = FindSmallestFac(num);
                    listBox1.Items.Add(num + "\ttest fails/factor=" + fac);
                    return;

                x++;
            }
                // for (int x = 1; ; x++)

            public int f(int x) => (int)Math.Pow(x, 2) - x + 41;

            public bool isPrime(int n, int f) {
                if (n <= 1) return false;
                if (n == 2) || f * f > n) return true;
            if (n % f == 0) return false;
            return isPrime(n, f + 1);
                    }
            public int FindSmallestFac(int n)
        {
            for (int lcv = 2; lcv <= Math.Sqrt(n); lcv++)
                if (n % lcv == 0) return lcv;
            return n;

        }

        }
    }
}
