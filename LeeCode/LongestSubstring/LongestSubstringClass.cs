using System.Collections.Generic;
using System.Linq;

namespace LeeCode.LongestSubstring
{
    public class LongestSubstringClass : ILongestSubstring
    {
        public int LengthOfLongestSubstring(string s)
        {
            int count = 0;
            List<int> countList = new List<int>() { 0 };
            List<char> charList = new List<char>();

            //Use double loop. If char duplicated, start from the next char.
            for (int i = 0; i < s.Length; i++)
            {
                //reset data
                count = 0;
                charList = new List<char>();

                for (int j = i; j < s.Length; j++)
                {
                    if (charList.Contains(s[j]))
                    {
                        //Add record
                        countList.Add(count);

                        break;
                    }

                    charList.Add(s[j]);
                    count++;
                }

                //Add record after ending loop
                countList.Add(count);

                //No cases could be longer
                if (count == s.Length)
                {
                    break;
                }
            }

            int result = countList.Max(x => x);
            return result;
        }
    }
}
