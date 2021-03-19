using System;

namespace LeeCode.ReverseInteger
{
    public class ReverseIntegerClass : IReverseInteger
    {
        public int Reverse(int x)
        {
            bool isMinus = x < 0;

            string intString = x.ToString().Replace("-", "");
            intString = ReverseString(intString);

            if (isMinus)
            {
                intString = $"-{intString}";
            }

            int.TryParse(intString, out int result);

            return result;
        }

        private string ReverseString(string input)
        {
            char[] charArray = input.ToCharArray();
            Array.Reverse(charArray);
            return new string(charArray);
        }
    }
}
