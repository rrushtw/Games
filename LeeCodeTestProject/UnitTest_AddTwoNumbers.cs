using LeeCode.AddTwoNumbers;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using Newtonsoft.Json;

namespace LeeCodeTestProject
{
    [TestClass]
    public class UnitTest_AddTwoNumbers
    {
        private IAddTwoNumbers Solution { get; set; }

        [TestMethod]
        public void AddTwoNumbers_Example1()
        {
            // arrange
            Solution = new AddTwoNumbersClass();

            // act
            ListNode list1_3 = new ListNode(3);
            ListNode list1_4 = new ListNode(4, list1_3);
            ListNode list1_2 = new ListNode(2, list1_4);

            ListNode list2_4 = new ListNode(4);
            ListNode list2_6 = new ListNode(6, list2_4);
            ListNode list2_5 = new ListNode(5, list2_6);
            ListNode actual = Solution.AddTwoNumbers(list1_2, list2_5);

            // assert
            ListNode expected_8 = new ListNode(8);
            ListNode expected_0 = new ListNode(0, expected_8);
            ListNode expected_7 = new ListNode(7, expected_0);

            Assert.AreEqual(JsonConvert.SerializeObject(expected_7), JsonConvert.SerializeObject(actual));
        }

        [TestMethod]
        public void AddTwoNumbers_Example2()
        {
            // arrange
            Solution = new AddTwoNumbersClass();

            // act
            ListNode list1 = new ListNode(0);
            ListNode list2 = new ListNode(0);
            ListNode actual = Solution.AddTwoNumbers(list1, list2);

            // assert
            ListNode expected = new ListNode(0);
            Assert.AreEqual(JsonConvert.SerializeObject(expected), JsonConvert.SerializeObject(actual));
        }

        [TestMethod]
        public void AddTwoNumbers_Example3()
        {
            // arrange
            Solution = new AddTwoNumbersClass();

            // act
            ListNode list1_0 = new ListNode(9);
            ListNode list1_1 = new ListNode(9, list1_0);
            ListNode list1_2 = new ListNode(9, list1_1);
            ListNode list1_3 = new ListNode(9, list1_2);
            ListNode list1_4 = new ListNode(9, list1_3);
            ListNode list1_5 = new ListNode(9, list1_4);
            ListNode list1 = new ListNode(9, list1_5);

            ListNode list2_0 = new ListNode(9);
            ListNode list2_1 = new ListNode(9, list2_0);
            ListNode list2_2 = new ListNode(9, list2_1);
            ListNode list2 = new ListNode(9, list2_2);

            ListNode actual = Solution.AddTwoNumbers(list1, list2);

            // assert
            ListNode expected_0 = new ListNode(1);
            ListNode expected_1 = new ListNode(0, expected_0);
            ListNode expected_2 = new ListNode(0, expected_1);
            ListNode expected_3 = new ListNode(0, expected_2);
            ListNode expected_4 = new ListNode(9, expected_3);
            ListNode expected_5 = new ListNode(9, expected_4);
            ListNode expected_6 = new ListNode(9, expected_5);
            ListNode expected = new ListNode(8, expected_6);

            Assert.AreEqual(JsonConvert.SerializeObject(expected), JsonConvert.SerializeObject(actual));
        }
    }
}
