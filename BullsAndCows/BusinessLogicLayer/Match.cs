using BullsAndCows.Interface;
using BullsAndCows.Model;
using System;
using System.Collections.Generic;

namespace BullsAndCows.BusinessLogicLayer
{
    public class Match : IMatch
    {
        public int Answer { get; set; } = -1;

        public Match()
        {
            for(; ; )
            {
                if (IsNotDuplicated4Digits(Answer))
                {
                    break;
                }

                Answer = new Random().Next(123, 9876);
            }
        }

        /// <summary>
        /// Validate input in none duplicated cases
        /// </summary>
        /// <param name="input"></param>
        /// <returns></returns>
        public bool IsNotDuplicated4Digits(int input)
        {
            if (input < 123 || input > 9876)
            {
                return false;
            }

            string inputString = input.ToString("D4");

            List<int> digits = new List<int>();
            foreach (char c in inputString)
            {
                int i = Convert.ToInt32(c);
                if (digits.Contains(i))
                {
                    return false;
                }

                digits.Add(i);
            }

            return true;
        }

        public Record Compare(int input)
        {
            Record record = new Record()
            {
                Input = input,
                Bulls = 0,
                Cows = 0
            };

            if (!IsNotDuplicated4Digits(input))
            {
                return null;
            }

            if (input == Answer)
            {
                record.Bulls = 4;
                record.Cows = 0;

                return record;
            }

            string inputString = input.ToString("D4");
            string answerString = Answer.ToString("D4");

            List<int> answerList = new List<int>();
            foreach (char c in answerString)
            {
                answerList.Add(Convert.ToInt32(c));
            }

            for (int i = 0; i < 4; i++)
            {
                if (inputString[i] == answerString[i])
                {
                    record.Bulls++;
                    continue;
                }

                if (answerString.Contains(inputString[i]))
                {
                    record.Cows++;
                    //continue;
                }
            }

            return record;
        }
    }
}
