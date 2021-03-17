using System.Collections.Generic;
using System.Linq;

namespace LeeCode.MedianSortedArrays
{
    public class MedianArraysClass : IMedianArrays
    {
        public double FindMedianSortedArrays(int[] nums1, int[] nums2)
        {
            double result;

            List<int> list = new List<int>();
            list.AddRange(nums1);
            list.AddRange(nums2);

            if (list.Count == 1)
            {
                result = list.FirstOrDefault();
                return result;
            }

            list = list.OrderBy(x => x).ToList();

            //is odd
            if (list.Count % 2 == 1)
            {
                result = list[(list.Count + 1) / 2 - 1];
            }
            else
            {
                result = (list[list.Count / 2 - 1] + list[list.Count / 2]) / 2.0d;
            }

            return result;
        }
    }
}
