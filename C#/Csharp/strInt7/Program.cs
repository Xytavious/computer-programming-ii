static void main(string[] args)
{
    Console.Write("enter a string: ");
    string word = Console.ReadLine().ToLower();

    int vow = 0;
    int cons = 0;

    for (int lcv =0; lcv < args.Length; lcv++)
    {
        char ltr = word[lcv];
        if (ltr == 'a' || ltr == 'e' || ltr == 'i' || ltr == 'o' || ltr == 'u')
            vow++;
        else if (ltr == 'a' && ltr <= 'z') cons++;

    }
    Console.WriteLine("$"{ word})

}