using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace lp4___2
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("enter weight ");
            int weight = int.Parse(Console.ReadLine());
            Console.Write("enter length ");
            int length = int.Parse(Console.ReadLine());
            Console.Write("enter width ");
            int width = int.Parse(Console.ReadLine());
            Console.Write("enter weight ");
            int hight = int.Parse(Console.ReadLine());
           
            int vol = length * width * hight;
            
            if (weight > 27 && vol > 100_000)
                Console.WriteLine("Package is too heavy and too large");
            else if (weight > 27)
                Console.WriteLine("Package is too heavy");
            else if (vol> 100_000)
            Console.WriteLine("package is too large ");
            else
            Console.WriteLine("package is ok ");
        }
    }
}
