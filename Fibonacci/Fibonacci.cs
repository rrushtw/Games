using System.Collections.Generic;

namespace Fibonacci
{
    public class Fibonacci
    {
        public List<int> Sequence { get; private set; }

        public Fibonacci(int order)
        {
            Sequence = new List<int>();

            for (int i = 0; i < order; i++)
            {
                if (i == 0)
                {
                    Sequence.Add(0);
                    continue;
                }
                if (i == 1)
                {
                    Sequence.Add(1);
                    continue;
                }

                //next = the previous number + the one before previous;
                int count = Sequence.Count;
                int next = Sequence[count - 2] + Sequence[count - 1];

                Sequence.Add(next);
            }
        }
    }
}
