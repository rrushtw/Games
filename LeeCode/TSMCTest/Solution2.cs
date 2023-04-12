using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace LeeCode.TSMCTest
{
    public class SinglyLinkedListNode
    {
        public int data { get; set; }
        public SinglyLinkedListNode next { get; set; }

        public SinglyLinkedListNode(int nodeData)
        {
            this.data = nodeData;
            this.next = null;
        }
    }

    public class SinglyLinkedList
    {
        public SinglyLinkedListNode head { get; set; }
        public SinglyLinkedListNode tail { get; set; }

        public SinglyLinkedList()
        {
            this.head = null;
            this.tail = null;
        }

        public void InsertNode(int nodeData)
        {
            SinglyLinkedListNode node = new SinglyLinkedListNode(nodeData);

            if (this.head == null)
            {
                this.head = node;
            }
            else
            {
                this.tail.next = node;
            }

            this.tail = node;
        }
    }

    public interface ISolution2
    {
        SinglyLinkedListNode createLinkedList(SinglyLinkedListNode head);
        List<int> Order(IEnumerable<int> list);
    }

    public class Solution2 : ISolution2
    {
        public SinglyLinkedListNode createLinkedList(SinglyLinkedListNode head)
        {
            List<int> list = new List<int>();
            SinglyLinkedListNode element = head;

            for (; ; )
            {
                list.Add(element.data);

                if (element.next == null) break;
                element = element.next;
            }

            list = Order(list);

            SinglyLinkedList linkedList = new SinglyLinkedList();
            foreach(int i in list)
            {
                linkedList.InsertNode(i);
            }

            return linkedList.head;
        }

        public List<int> Order(IEnumerable<int> list)
        {
            List<int> result = new List<int>();

            if (list.Count() <= 1)
            {
                result.AddRange(list);
                return result;
            }

            var evenList = list.Where((item, index) => index % 2 == 0);
            result.AddRange(evenList);

            var oddList = list.Where((item, index) => index % 2 != 0);
            result.AddRange(Order(oddList));

            return result;
        }
    }
}
