using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace LeeCode.TSMCTest
{
    public interface ISolution1
    {
        int minNum(int threshold, List<int> points);
    }

    public class Solution1 : ISolution1
    {
        public int minNum(int threshold, List<int> points)
        {
            int firstPoint = points.First();
            points.RemoveRange(0, 1);

            int problemCount = 1;

            foreach (int point in points)
            {
                problemCount++;

                if (Math.Abs(point - firstPoint) >= threshold)
                {
                    break;
                }
            }

            if (problemCount >= points.Count && Math.Abs(points.Last() - firstPoint) < threshold)
            {
                return points.Count + 1;
            }

            problemCount = problemCount / 2 + 1;
            return problemCount;
        }
    }
}
