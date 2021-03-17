using LeeCode.ReverseInteger;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace LeeCodeTestProject
{
    [TestClass]
    public class UnitTest_ReverseInteger
    {
        private IReverseInteger Solution { get; set; }

        [TestMethod]
        public void ReverseInteger_Example1()
        {
            // arrange
            Solution = new ReverseIntegerClass();

            // act
            int actual = Solution.Reverse(123);

            // assert
            int expected = 321;
            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void ReverseInteger_Example2()
        {
            // arrange
            Solution = new ReverseIntegerClass();

            // act
            int actual = Solution.Reverse(-123);

            // assert
            int expected = -321;
            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void ReverseInteger_Example3()
        {
            // arrange
            Solution = new ReverseIntegerClass();

            // act
            int actual = Solution.Reverse(120);

            // assert
            int expected = 21;
            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void ReverseInteger_Example4()
        {
            // arrange
            Solution = new ReverseIntegerClass();

            // act
            int actual = Solution.Reverse(0);

            // assert
            int expected = 0;
            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void ReverseInteger_Example5()
        {
            // arrange
            Solution = new ReverseIntegerClass();

            // act
            int actual = Solution.Reverse(int.MaxValue - 1);

            // assert
            int expected = 0;
            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void ReverseInteger_Example6()
        {
            // arrange
            Solution = new ReverseIntegerClass();

            // act
            int actual = Solution.Reverse(int.MinValue);

            // assert
            int expected = 0;
            Assert.AreEqual(expected, actual);
        }
    }
}
