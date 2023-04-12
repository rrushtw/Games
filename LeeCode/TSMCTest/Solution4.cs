using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace LeeCode.TSMCTest
{
    public interface ISolution4
    {
        List<int> minChairs(List<string> simulations);
    }

    public class Solution4 : ISolution4
    {
        public List<int> minChairs(List<string> simulations)
        {
            List<int> result = new List<int>();

            foreach (string c in simulations)
            {
                int takenChairs = 0;
                int availibleChairs = 0;

                foreach (char action in c)
                {
                    if (action == 'C' || action == 'U')
                    {
                        if (availibleChairs == 0)
                        {
                            takenChairs++;
                            continue;
                        }

                        availibleChairs--;
                        takenChairs++;
                        continue;
                    }

                    if (action == 'R' || action == 'L')
                    {
                        takenChairs--;
                        availibleChairs++;
                    }

                    continue;
                }

                result.Add(takenChairs + availibleChairs);
            }

            return result;
        }
    }
}
