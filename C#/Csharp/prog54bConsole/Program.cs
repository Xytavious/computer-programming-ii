﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace prog54bConsole
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter Num1: ");
            int num1 = int.Parse(Console.ReadLine());
            Console.Write("Enter Num2: ");
            int num2 = int.Parse(Console.ReadLine());
            Console.Write("Enter Num3: ");
            int num3 = int.Parse(Console.ReadLine());
            Console.Write("Enter Num4: ");
            int num4 = int.Parse(Console.ReadLine());

            int sum = num1 + num2 + num3 + num4;
            double average = (double)sum / 4;
            Console.WriteLine("Average: " + Math.Round(average, 2));
            Console.ReadKey();
        }
    }
}
