// See https://aka.ms/new-console-template for more information
Console.WriteLine("Hello, World!");

Console.Write("enter Num1;");
int n1 = int.Parse(Console.ReadLine());
Console.Write("enter Num2;");
int n2 = int.Parse(Console.ReadLine());
Console.Write("choose an option: add, sub, mul or div:");
string op = Console.ReadLine();
int res = 0;
if (op == "add") res = add(n1, n2);
else if (op == "sub") res = sub(n1, n2);
else if (op == "mul") res = mul(n1, n2);
else if (op == "div") res = div(n1, n2);
Console.WriteLine("result: " + res);
wait();


// ,access level. 
static void wait() { Console.ReadLine(); }


static int add(int x, int y)
{
    return x + y;
}
static int sub(int x, int y)
{
    return x - y;
}
static int mul(int x, int y)
{
    return x * y;
}
static int div(int x, int y)
{
    return x / y;
}