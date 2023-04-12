using LeeCode.TSMCTest;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using Newtonsoft.Json;
using System.Collections.Generic;

namespace LeeCodeTestProject
{
    [TestClass]
    public class UnitTest_TSMCTest5
    {
        private ISolution5 Solution { get; set; }

        [TestMethod]
        public void Example1()
        {
            //arrange
            Solution = new Solution5();

            //act
            var actaul = Solution.TimeOfBuffering(2, new List<int>() { 1, 3, 2, 1, 2, 3, 3, 4 });

            //assert
            var expected = 4;
            Assert.AreEqual(expected, actaul);
        }

        [TestMethod]
        public void Example2()
        {
            //arrange
            Solution = new Solution5();

            //act
            var actaul = Solution.TimeOfBuffering(3, new List<int>() { 1, 2, 2, 2 });

            //assert
            var expected = -1;
            Assert.AreEqual(expected, actaul);
        }

        [TestMethod]
        public void Example3()
        {
            //arrange
            Solution = new Solution5();

            //act
            var actaul = Solution.TimeOfBuffering(1, new List<int>() { 1, 2, 3, 4 });

            //assert
            var expected = -1;
            Assert.AreEqual(expected, actaul);
        }

        [TestMethod]
        public void Example4()
        {
            //arrange
            Solution = new Solution5();

            //act
            var actaul = Solution.TimeOfBuffering(1, new List<int>() { 1, 2, 3, 4 });

            //assert
            var expected = -1;
            Assert.AreEqual(expected, actaul);
        }
    }
}
