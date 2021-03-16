using System.Diagnostics.CodeAnalysis;

namespace LeeCode.AddTwoNumbers
{
    public class ListNode
    {
        [SuppressMessage("Style", "IDE1006:命名樣式", Justification = "<暫止>")]
        public int val { get; set; }

        [SuppressMessage("Style", "IDE1006:命名樣式", Justification = "<暫止>")]
        public ListNode next { get; set; }

        public ListNode(int val = 0, ListNode next = null)
        {
            this.val = val;
            this.next = next;
        }
    }
}
