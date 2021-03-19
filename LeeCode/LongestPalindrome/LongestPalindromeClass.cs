using System.Collections.Generic;
using System.Linq;

namespace LeeCode.LongestPalindrome
{
    public class LongestPalindromeClass : ILongestPalindrome
    {
        public string LongestPalindrome(string s)
        {
            if (s.Length == 1) return s;

            List<string> resultList = new List<string>();
            string word = string.Empty;

            for (int i = 0; i < s.Length; i++)
            {
                word = Expand_Even(s, i);
                if (!(word is null))
                {
                    resultList.Add(word);
                }

                word = Expand_Odd(s, i);
                if (!(word is null))
                {
                    resultList.Add(word);
                }
            }

            word = resultList.OrderByDescending(x => x.Length).FirstOrDefault();
            return word;
        }

        private string Expand_Even(string input, int position)
        {
            //int position1 = position;
            int position2 = position + 1;
            int border = new List<int>()
            {
                position + 1,
                input.Length - position2
            }.Min();

            string result = null;

            for (int i = 0; i < border; i++)
            {
                if (input[position - i] == input[position2 + i])
                {
                    result = input.Substring(position - i, 2 * (i + 1));
                    continue;
                }

                break;
            }

            return result;
        }

        private string Expand_Odd(string input, int position)
        {
            int border = new List<int>()
            {
                position + 1,
                input.Length - position
            }.Min();

            string result = null;

            for (int i = 0; i < border; i++)
            {
                if (input[position - i] == input[position + i])
                {
                    result = input.Substring(position - i, 2 * i + 1);
                    continue;
                }

                break;
            }

            return result;
        }
    }
}
