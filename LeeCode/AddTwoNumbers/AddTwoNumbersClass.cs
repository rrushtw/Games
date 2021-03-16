using System.Collections.Generic;

namespace LeeCode.AddTwoNumbers
{
    public class AddTwoNumbersClass : IAddTwoNumbers
    {
        public ListNode AddTwoNumbers(ListNode l1, ListNode l2)
        {
            List<int> list = new List<int>();
            bool overflow = false;

            for (; ; )
            {
                int number = 0;

                if (overflow)
                {
                    number++;
                    overflow = false;
                }

                if (l1 is null && l2 is null && number == 0)
                {
                    break;
                }

                if (!(l1 is null))
                {
                    number += l1.val;
                    l1 = l1.next;
                }

                if (!(l2 is null))
                {
                    number += l2.val;
                    l2 = l2.next;
                }

                if (number > 9)
                {
                    overflow = true;
                    number -= 10;
                }

                list.Add(number);
            }

            ListNode result = ConvertToListNode(list);
            return result;
        }

        private ListNode ConvertToListNode(List<int> list)
        {
            ListNode result = null;

            for (int i = list.Count; i > 0; i--)
            {
                result = new ListNode(list[i - 1], result);
            }

            return result;
        }
    }
}
