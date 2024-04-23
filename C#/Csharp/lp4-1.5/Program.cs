using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace lp4_1._5
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("enter # of copies to be printed: ");
            int copies = int.Parse(Console.ReadLine());
            double price = 0;
            double cost = 0;
            // && and,  || or Not !
            if (copies > 0 && copies <= 99) price = 0.30;
            else if (copies > 99 && copies <= 499) price = 0.28;
            else if (copies > 499 && copies <= 749) price = 0.27;
            else if (copies > 749 && copies <= 1000) price = 0.26;
            else if (copies > 1000) price = 0.25;
            else Console.WriteLine("Invalid number of Copies!");

            cost = price * copies;
            Console.WriteLine("price per copy is $" + price);
            Console.WriteLine("Total cost is $" + Math.Round(cost, 2));
            Console.ReadLine();

        }
    }
}
