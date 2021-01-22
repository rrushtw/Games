namespace BullsAndCows.Model
{
    /// <summary>
    /// Input and result
    /// </summary>
    public class Record
    {
        /// <summary>
        /// Number between 0000 and 9999
        /// </summary>
        public int Input { get; set; } = -1;
        /// <summary>
        /// Correct number and correct position
        /// </summary>
        public int Bulls { get; set; } = 0;
        /// <summary>
        /// Correct number and incorrect postion
        /// </summary>
        public int Cows { get; set; } = 0;
    }
}
