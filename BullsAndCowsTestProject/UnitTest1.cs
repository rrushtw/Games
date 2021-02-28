using BullsAndCows.BusinessLogicLayer;
using BullsAndCows.Interface;
using BullsAndCows.Model;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace BullsAndCowsTestProject
{
    [TestClass]
    public class UnitTest1
    {
        public IMatch Match { get; set; }

        [TestMethod]
        public void IsNotDuplicated4Digits_true()
        {
            // arrange
            Match = new Match();

            // act
            bool actual = Match.IsNotDuplicated4Digits(1234);

            // assert
            bool expected = true;
            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void IsNotDuplicated4Digits_false()
        {
            // arrange
            Match = new Match();

            // act
            bool actual = Match.IsNotDuplicated4Digits(9999);

            // assert
            bool expected = false;
            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void IsNotDuplicated4Digits_Over4()
        {
            // arrange
            Match = new Match();

            // act
            bool actual = Match.IsNotDuplicated4Digits(12345);

            // assert
            bool expected = false;
            Assert.AreEqual(expected, actual);
        }

        [TestMethod]
        public void Compare_4B()
        {
            // arrange
            Match = new Match
            {
                Answer = 4321
            };

            // act
            Record actual = Match.Compare(1234);

            // assert
            Record expected = new Record()
            {
                Input = 1234,
                Bulls = 0,
                Cows = 4
            };
            Assert.AreEqual(actual.Cows, expected.Cows);
        }
    }
}
