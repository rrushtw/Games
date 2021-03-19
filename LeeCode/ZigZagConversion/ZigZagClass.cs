using System.Collections.Generic;

namespace LeeCode.ZigZagConversion
{
    public class ZigZagClass : IZigZag
    {
        public string Convert(string s, int numRows)
        {
            if (s.Length <= numRows || numRows == 1)
            {
                return s;
            }

            List<string> table = new List<string>();
            for (int i = 0; i < numRows; i++)
            {
                table.Add(string.Empty);
            }

            for (int i = 0; i < s.Length; i++)
            {
                int quotient = i % (2 * numRows - 2);

                if (quotient < numRows)
                {
                    table[quotient] += s[i];
                    continue;
                }

                int index = (2 * numRows - 2) - quotient;
                table[index] += s[i];
            }

            string result = string.Empty;
            foreach (string text in table)
            {
                result += text;
            }

            return result;
        }
    }
}
