using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace LeeCode.TSMCTest
{
    public interface ISolution5
    {
        int TimeOfBuffering(int arrivalRate, List<int> packets);
    }

    public class Solution5 : ISolution5
    {
        public int TimeOfBuffering(int arrivalRate, List<int> packets)
        {
            int upperlimit = packets.Max();
            List<int> buffer = new List<int>();

            for (int i = 0; i < upperlimit; i++)
            {
                if (!buffer.Any(x => x == i + 1) && packets.FirstOrDefault() != (i + 1))
                {
                    return i + 1;
                }

                if (packets.Count > 0)
                {
                    buffer.AddRange(packets.Take(arrivalRate).Where(x => x > i));

                    if (packets.Count < arrivalRate)
                    {
                        packets.Clear();
                        continue;
                    }

                    packets.RemoveRange(0, arrivalRate);
                }
            }

            return -1;
        }
    }
}
