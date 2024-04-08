using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Enter your name: ");
            string name = Console.ReadLine();
            Console.WriteLine("hello, " + name);

            Console.Write("Enter your age: ");
            // int age 
            int age = int.Parse(Console.ReadLine());
            Console.WriteLine("you are " + age + " years old!");

            Console.ReadKey();
        }
    }
}
