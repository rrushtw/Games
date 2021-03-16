using LeeCode.LongestSubstring;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace LeeCodeTestProject
{
    [TestClass]
    public class UnitTest_LongestSubstring
    {
        private ILongestSubstring Solution { get; set; }

        [TestMethod]
        public void LongestSubstring_Example1()
        {
            //arrange
            Solution = new LongestSubstringClass();

            //act
            int actual = Solution.LengthOfLongestSubstring("abcabcbb");

            //assert
            int expected = 3;
            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void LongestSubstring_Example2()
        {
            //arrange
            Solution = new LongestSubstringClass();

            //act
            int actual = Solution.LengthOfLongestSubstring("bbbbb");

            //assert
            int expected = 1;
            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void LongestSubstring_Example3()
        {
            //arrange
            Solution = new LongestSubstringClass();

            //act
            int actual = Solution.LengthOfLongestSubstring("pwwkew");

            //assert
            int expected = 3;
            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void LongestSubstring_Example4()
        {
            //arrange
            Solution = new LongestSubstringClass();

            //act
            int actual = Solution.LengthOfLongestSubstring(string.Empty);

            //assert
            int expected = 0;
            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void LongestSubstring_Example5()
        {
            //arrange
            Solution = new LongestSubstringClass();

            //act
            int actual = Solution.LengthOfLongestSubstring(" ");

            //assert
            int expected = 1;
            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void LongestSubstring_Example6()
        {
            //arrange
            Solution = new LongestSubstringClass();

            //act
            int actual = Solution.LengthOfLongestSubstring("dvdf");

            //assert
            int expected = 3;
            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void LongestSubstring_Example7()
        {
            //arrange
            Solution = new LongestSubstringClass();

            //act
            int actual = Solution.LengthOfLongestSubstring("asjrgapa");

            //assert
            int expected = 6;
            Assert.AreEqual(expected, actual);
        }
    }
}
