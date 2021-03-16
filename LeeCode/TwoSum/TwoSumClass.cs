using System.Collections.Generic;

namespace LeeCode.TwoSum
{
    public class TwoSumClass : ITwoSum
    {
        public int[] TwoSum(int[] nums, int target)
        {
            for (int i = 0; i < nums.Length; i++)
            {
                for (int j = i + 1; j < nums.Length; j++)
                {
                    if (nums[i] + nums[j] == target)
                    {
                        List<int> result = new List<int>() { i, j };

                        return result.ToArray();
                    }
                }
            }

            return null;
        }
    }
}
