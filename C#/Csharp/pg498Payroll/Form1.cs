using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.VisualBasic;
using System.Windows.Forms;


namespace pg498Payroll
{
    const decimal drcHourly_pay_rate = 6.0m;
    const int intMax_Employees = 5;
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            //  calulate and display the gross pay rarned by employees
            int[] intHours = new int[intMax_Employees];
            // make a new int array of capacity intMax_Employees
            //capacity can never change, unlike lists in python 
            // explicicitly define an array with int[] thing = {}
            int intCount = 0;        // loop counter
            int intEmpHours = 0;     // Hours
            decimal decEmpPay = 0.0m;   // gross pay 

            // get the hours worked by the employees
            for (intCount = 0; intCount < intMax_Employees; intCount++)
            {
                Interaction.InputBox("enter the nuber of hours worked by Emploee #" + (intCount+1).ToString(),



            }
            listBox1.Items.Clear();
            for (intCount = 0; intCount < intMax_employees; intCount++)
            {
                decEmpPay = intHours[intCount] * decHourly_pay_rate;
                listBox1.Items.Add("empolyee " + (intCount + 1).ToString() + "earned " + decEmpPay.ToString("$.00"));
            }
        }
    }
}
