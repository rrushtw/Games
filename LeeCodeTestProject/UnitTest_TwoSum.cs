using LeeCode.TwoSum;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using Newtonsoft.Json;
using System.Collections.Generic;

namespace LeeCodeTestProject
{
    [TestClass]
    public class UnitTest_TwoSum
    {
        private ITwoSum Solution { get; set; }

        [TestMethod]
        public void TwoSum_Example1()
        {
            // arrange
            Solution = new TwoSumClass();

            // act
            List<int> list = new List<int>() { 2, 7, 11, 15 };
            int[] actual = Solution.TwoSum(list.ToArray(), 9);

            // assert
            int[] expected = new List<int>() { 0, 1 }.ToArray();
            Assert.AreEqual(JsonConvert.SerializeObject(expected), JsonConvert.SerializeObject(actual));
        }

        [TestMethod]
        public void TwoSum_Example2()
        {
            // arrange
            Solution = new TwoSumClass();

            // act
            List<int> list = new List<int>() { 3, 2, 4 };
            int[] actual = Solution.TwoSum(list.ToArray(), 6);

            // assert
            int[] expected = new List<int>() { 1, 2 }.ToArray();
            Assert.AreEqual(JsonConvert.SerializeObject(expected), JsonConvert.SerializeObject(actual));
        }

        [TestMethod]
        public void TwoSum_Example3()
        {
            // arrange
            Solution = new TwoSumClass();

            // act
            List<int> list = new List<int>() { 3, 3 };
            int[] actual = Solution.TwoSum(list.ToArray(), 6);

            // assert
            int[] expected = new List<int>() { 0, 1 }.ToArray();
            Assert.AreEqual(JsonConvert.SerializeObject(expected), JsonConvert.SerializeObject(actual));
        }
    }
}
