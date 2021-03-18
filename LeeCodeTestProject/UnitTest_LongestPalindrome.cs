using LeeCode.LongestPalindrome;
using Microsoft.VisualStudio.TestTools.UnitTesting;
using System.Collections.Generic;
using System.Linq;

namespace LeeCodeTestProject
{
    [TestClass]
    public class UnitTest_LongestPalindrome
    {
        private ILongestPalindrome Solution { get; set; }

        [TestMethod]
        public void Example1()
        {
            //arrange
            Solution = new LongestPalindromeClass();

            //act
            var actual = Solution.LongestPalindrome("babad");

            //assert
            List<string> expected = new List<string>()
            {
                "aba",
                "bab"
            };

            Assert.IsTrue(expected.Any(x => x.Equals(actual)));
        }

        [TestMethod]
        public void Example2()
        {
            //arrange
            Solution = new LongestPalindromeClass();

            //act
            var actual = Solution.LongestPalindrome("cbbd");

            //assert
            var expected = "bb";
            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void Example3()
        {
            //arrange
            Solution = new LongestPalindromeClass();

            //act
            var actual = Solution.LongestPalindrome("a");

            //assert
            var expected = "a";
            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void Example4()
        {
            //arrange
            Solution = new LongestPalindromeClass();

            //act
            var actual = Solution.LongestPalindrome("ac");

            //assert
            List<string> expected = new List<string>()
            {
                "a",
                "c"
            };

            Assert.IsTrue(expected.Any(x => x.Equals(actual)));
        }

        [TestMethod]
        public void Example5()
        {
            //arrange
            Solution = new LongestPalindromeClass();

            //act
            var actual = Solution.LongestPalindrome("aba12321");

            //assert
            var expected = "12321";
            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void Example6()
        {
            //arrange
            Solution = new LongestPalindromeClass();

            //act
            var actual = Solution.LongestPalindrome("abba123321");

            //assert
            var expected = "123321";
            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void Example7()
        {
            //arrange
            Solution = new LongestPalindromeClass();

            //act
            var actual = Solution.LongestPalindrome("zudfweormatjycujjirzjpyrmaxurectxrtqedmmgergwdvjmjtstdhcihacqnothgttgqfywcpgnuvwglvfiuxteopoyizgehkwuvvkqxbnufkcbodlhdmbqyghkojrgokpwdhtdrwmvdegwycecrgjvuexlguayzcammupgeskrvpthrmwqaqsdcgycdupykppiyhwzwcplivjnnvwhqkkxildtyjltklcokcrgqnnwzzeuqioyahqpuskkpbxhvzvqyhlegmoviogzwuiqahiouhnecjwysmtarjjdjqdrkljawzasriouuiqkcwwqsxifbndjmyprdozhwaoibpqrthpcjphgsfbeqrqqoqiqqdicvybzxhklehzzapbvcyleljawowluqgxxwlrymzojshlwkmzwpixgfjljkmwdtjeabgyrpbqyyykmoaqdambpkyyvukalbrzoyoufjqeftniddsfqnilxlplselqatdgjziphvrbokofvuerpsvqmzakbyzxtxvyanvjpfyvyiivqusfrsufjanmfibgrkwtiuoykiavpbqeyfsuteuxxjiyxvlvgmehycdvxdorpepmsinvmyzeqeiikajopqedyopirmhymozernxzaueljjrhcsofwyddkpnvcvzixdjknikyhzmstvbducjcoyoeoaqruuewclzqqqxzpgykrkygxnmlsrjudoaejxkipkgmcoqtxhelvsizgdwdyjwuumazxfstoaxeqqxoqezakdqjwpkrbldpcbbxexquqrznavcrprnydufsidakvrpuzgfisdxreldbqfizngtrilnbqboxwmwienlkmmiuifrvytukcqcpeqdwwucymgvyrektsnfijdcdoawbcwkkjkqwzffnuqituihjaklvthulmcjrhqcyzvekzqlxgddjoir");

            //assert
            var expected = "gykrkyg";
            Assert.AreEqual(expected, actual);
        }
    }
}
