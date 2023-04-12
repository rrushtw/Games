using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace LeeCode.TSMCTest
{
    public class Node
    {
        public Node Parent { get; set; }

        public int Position { get; set; }
        public int Value { get; set; }
    }

    public interface ISolution3
    {
        int bestSumDownwardTreePath(List<int> parent, List<int> values);
    }

    public class Solution3 : ISolution3
    {
        public int bestSumDownwardTreePath(List<int> parent, List<int> values)
        {

        }
    }
}
