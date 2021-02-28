using BullsAndCows.BusinessLogicLayer;
using BullsAndCows.Model;
using System;
using System.Windows.Forms;

namespace BullsAndCows
{
    public partial class Form1 : Form
    {
        private Match Game { get; set; }
        private int TryCount { get; set; }

        public Form1()
        {
            InitializeComponent();

            Game = new Match();
            TryCount = 0;
        }

        private void Button_NewGame_Click(object sender, EventArgs e)
        {
            DialogResult result = MessageBox.Show(
                text: "Do you want to restart?",
                caption: "Confirm",
                buttons: MessageBoxButtons.YesNo
            );

            switch (result)
            {
                case DialogResult.Yes:
                    Game = new Match();
                    TryCount = 0;
                    TextBox_Display.Text = string.Empty;
                    TextBox_Input.Enabled = true;
                    Button_Enter.Enabled = true;
                    break;
                case DialogResult.No:
                default:
                    //do nothing
                    break;
            }
        }

        private void Button_Enter_Click(object sender, EventArgs e)
        {
            string inputString = TextBox_Input.Text;

            if (string.IsNullOrWhiteSpace(inputString)) return;

            //Remove space
            inputString = inputString.Replace(" ", string.Empty);

            if (!int.TryParse(inputString, out int inputInt))
            {
                MessageBox.Show("Please have 4 digits number");
                return;
            }

            bool isValid = Game.IsNotDuplicated4Digits(inputInt);

            if (!isValid)
            {
                MessageBox.Show("Please have none duplicated 4 digits");
                return;
            }

            TryCount++;

            Record record = Game.Compare(inputInt);

            string append = string.Empty;
            if (TryCount > 1) append += "\r\n";
            append += $"{TryCount}. {record.Input:D4}\t{record.Bulls}A{record.Cows}B";

            TextBox_Display.Text += append;
            TextBox_Input.Text = string.Empty;

            if (record.Bulls == 4)
            {
                MessageBox.Show(
                    text: $"Congratulations.\nThe correct answer is {Game.Answer:D4}.",
                    caption: "Victory",
                    buttons: MessageBoxButtons.OK
                );

                TextBox_Input.Enabled = false;
                Button_Enter.Enabled = false;
                return;
            }

            if (TryCount >= 10)
            {
                MessageBox.Show(
                    text: $"The correct answer is {Game.Answer:D4}.",
                    caption: "Defeat",
                    buttons: MessageBoxButtons.OK
                );

                TextBox_Input.Enabled = false;
                Button_Enter.Enabled = false;
                return;
            }
        }

        private void TextBox_Input_PressEnter(object sender, KeyPressEventArgs e)
        {
            if (e.KeyChar == (char)Keys.Return) Button_Enter_Click(sender, e);
        }

        private void Button_Quit_Click(object sender, EventArgs e)
        {
            DialogResult result = MessageBox.Show(
                text: "Do you want to quit this game?",
                caption: "Exit",
                buttons: MessageBoxButtons.YesNo
            );

            switch (result)
            {
                case DialogResult.Yes:
                    Close();
                    break;
                case DialogResult.No:
                default:
                    //do nothing
                    break;
            }
        }

        private void Button_Help_Click(object sender, EventArgs e)
        {
            DialogResult result = MessageBox.Show(
                text: "For more infomation, please check https://en.wikipedia.org/wiki/Bulls_and_Cows" + "\n(Press OK to copy link)",
                caption: "Infomation",
                buttons: MessageBoxButtons.OKCancel,
                icon: MessageBoxIcon.Asterisk
            );

            if (result == DialogResult.OK) Clipboard.SetText("https://en.wikipedia.org/wiki/Bulls_and_Cows");
        }
    }
}
