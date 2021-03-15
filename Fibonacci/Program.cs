using Newtonsoft.Json;
using System;
using System.Collections.Generic;
using System.Linq;

namespace Fibonacci
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Welcome to Fibonacci sequence.");

        InputNumber:
            Console.Write("Please input the order you want:");
            string inputValue = Console.ReadLine();

            if (!int.TryParse(inputValue, out int intValue))
            {
                goto InputNumber;
            }

            List<int> sequence = new Fibonacci(intValue).Sequence;

            Console.WriteLine($"\nThe result is {sequence.LastOrDefault()}");
            Console.WriteLine($"The whole sequence is {JsonConvert.SerializeObject(sequence)}");
            Console.WriteLine("\nPress any key to exit.");
            Console.ReadKey();
        }
    }
}
