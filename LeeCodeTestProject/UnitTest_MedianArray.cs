using LeeCode.MedianSortedArrays;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using System;
using System.Collections.Generic;

namespace LeeCodeTestProject
{
    [TestClass]
    public class UnitTest_MedianArray
    {
        private IMedianArrays Solution { get; set; }

        [TestMethod]
        public void Example1()
        {
            //arrange
            Solution = new MedianArraysClass();

            //act
            List<int> list1 = new List<int>() { 1, 3 };
            List<int> list2 = new List<int>() { 2 };
            var actual = Solution.FindMedianSortedArrays(list1.ToArray(), list2.ToArray());

            //assert
            var expected = (double)2;
            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void Example2()
        {
            //arrange
            Solution = new MedianArraysClass();

            //act
            List<int> list1 = new List<int>() { 1, 2 };
            List<int> list2 = new List<int>() { 3, 4 };
            var actual = Solution.FindMedianSortedArrays(list1.ToArray(), list2.ToArray());

            //assert
            var expected = (double)2.5;
            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void Example3()
        {
            //arrange
            Solution = new MedianArraysClass();

            //act
            List<int> list1 = new List<int>() { 0, 0 };
            List<int> list2 = new List<int>() { 0, 0 };
            var actual = Solution.FindMedianSortedArrays(list1.ToArray(), list2.ToArray());

            //assert
            var expected = (double)0;
            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void Example4()
        {
            //arrange
            Solution = new MedianArraysClass();

            //act
            List<int> list1 = new List<int>() { };
            List<int> list2 = new List<int>() { 1 };
            var actual = Solution.FindMedianSortedArrays(list1.ToArray(), list2.ToArray());

            //assert
            var expected = (double)1;
            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void Example5()
        {
            //arrange
            Solution = new MedianArraysClass();

            //act
            List<int> list1 = new List<int>() { 2 };
            List<int> list2 = new List<int>() { };
            var actual = Solution.FindMedianSortedArrays(list1.ToArray(), list2.ToArray());

            //assert
            var expected = (double)2;
            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void Example6()
        {
            //arrange
            Solution = new MedianArraysClass();

            //act
            List<int> list1 = new List<int>() { 10 ^ 6 };
            List<int> list2 = new List<int>() { 10 ^ 6 };
            var actual = Solution.FindMedianSortedArrays(list1.ToArray(), list2.ToArray());

            //assert
            var expected = Convert.ToDouble(10 ^ 6);
            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void Example7()
        {
            //arrange
            Solution = new MedianArraysClass();

            //act
            List<int> list1 = new List<int>() { 0 };
            List<int> list2 = new List<int>() { 1_000_000 };
            var actual = Solution.FindMedianSortedArrays(list1.ToArray(), list2.ToArray());

            //assert
            var expected = Convert.ToDouble(500_000);
            Assert.AreEqual(expected, actual);
        }
    }
}
