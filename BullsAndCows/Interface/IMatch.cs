using BullsAndCows.Model;

namespace BullsAndCows.Interface
{
    public interface IMatch
    {
        bool IsNotDuplicated4Digits(int input);

        public Record Compare(int input);
    }
}
