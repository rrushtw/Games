using LeeCode.TSMCTest;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using Newtonsoft.Json;
using System.Collections.Generic;

namespace LeeCodeTestProject
{
    [TestClass]
    public class UnitTest_TSMCTest2
    {
        private ISolution2 Solution { get; set; }

        [TestMethod]
        public void Example1()
        {
            //arrange
            Solution = new Solution2();

            //act
            var actaul = Solution.Order(new List<int>() { 1, 5, 2, 7, 8, 3});

            //assert
            var expected = new List<int>() { 1, 2, 8, 5, 3, 7 };
            Assert.AreEqual(JsonConvert.SerializeObject(expected), JsonConvert.SerializeObject(actaul));
        }

        [TestMethod]
        public void Example2()
        {
            //arrange
            Solution = new Solution2();

            //act
            var actaul = Solution.Order(new List<int>() { 3, 5, 3, 7, 8 });

            //assert
            var expected = new List<int>() { 3, 3, 8, 5, 7 };
            Assert.AreEqual(JsonConvert.SerializeObject(expected), JsonConvert.SerializeObject(actaul));
        }

        //[TestMethod]
        //public void Example3()
        //{
        //    //arrange
        //    Solution = new Solution1();

        //    //act
        //    var actaul = Solution.minNum(4, new List<int>() { 1, 3, 4, 7 });

        //    //assert
        //    var expected = 3;
        //    Assert.AreEqual(expected, actaul);
        //}

        //[TestMethod]
        //public void Example4()
        //{
        //    //arrange
        //    Solution = new Solution1();

        //    //act
        //    var actaul = Solution.minNum(650, new List<int>() { 82, 112, 134, 178, 206, 229, 238, 278, 293, 335 });

        //    //assert
        //    var expected = 10;
        //    Assert.AreEqual(expected, actaul);
        //}
    }
}
