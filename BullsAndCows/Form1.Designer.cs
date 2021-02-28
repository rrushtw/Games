
namespace BullsAndCows
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.Label_YourAns = new System.Windows.Forms.Label();
            this.TextBox_Input = new System.Windows.Forms.TextBox();
            this.Button_NewGame = new System.Windows.Forms.Button();
            this.Button_Quit = new System.Windows.Forms.Button();
            this.Button_Enter = new System.Windows.Forms.Button();
            this.TextBox_Display = new System.Windows.Forms.TextBox();
            this.Label_Records = new System.Windows.Forms.Label();
            this.Button_Help = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // Label_YourAns
            // 
            this.Label_YourAns.AutoSize = true;
            this.Label_YourAns.Location = new System.Drawing.Point(12, 66);
            this.Label_YourAns.Name = "Label_YourAns";
            this.Label_YourAns.Size = new System.Drawing.Size(98, 19);
            this.Label_YourAns.TabIndex = 0;
            this.Label_YourAns.Text = "Your Answer";
            // 
            // TextBox_Input
            // 
            this.TextBox_Input.Location = new System.Drawing.Point(12, 88);
            this.TextBox_Input.MaxLength = 4;
            this.TextBox_Input.Name = "TextBox_Input";
            this.TextBox_Input.Size = new System.Drawing.Size(225, 27);
            this.TextBox_Input.TabIndex = 1;
            this.TextBox_Input.KeyPress += new System.Windows.Forms.KeyPressEventHandler(this.TextBox_Input_PressEnter);
            // 
            // Button_NewGame
            // 
            this.Button_NewGame.Location = new System.Drawing.Point(12, 12);
            this.Button_NewGame.Name = "Button_NewGame";
            this.Button_NewGame.Size = new System.Drawing.Size(94, 29);
            this.Button_NewGame.TabIndex = 2;
            this.Button_NewGame.Text = "New Game";
            this.Button_NewGame.UseVisualStyleBackColor = true;
            this.Button_NewGame.Click += new System.EventHandler(this.Button_NewGame_Click);
            // 
            // Button_Quit
            // 
            this.Button_Quit.Location = new System.Drawing.Point(243, 12);
            this.Button_Quit.Name = "Button_Quit";
            this.Button_Quit.Size = new System.Drawing.Size(94, 29);
            this.Button_Quit.TabIndex = 3;
            this.Button_Quit.Text = "Quit";
            this.Button_Quit.UseVisualStyleBackColor = true;
            this.Button_Quit.Click += new System.EventHandler(this.Button_Quit_Click);
            // 
            // Button_Enter
            // 
            this.Button_Enter.Location = new System.Drawing.Point(243, 86);
            this.Button_Enter.Name = "Button_Enter";
            this.Button_Enter.Size = new System.Drawing.Size(94, 29);
            this.Button_Enter.TabIndex = 4;
            this.Button_Enter.Text = "Enter";
            this.Button_Enter.UseVisualStyleBackColor = true;
            this.Button_Enter.Click += new System.EventHandler(this.Button_Enter_Click);
            // 
            // TextBox_Display
            // 
            this.TextBox_Display.Location = new System.Drawing.Point(12, 163);
            this.TextBox_Display.Multiline = true;
            this.TextBox_Display.Name = "TextBox_Display";
            this.TextBox_Display.ReadOnly = true;
            this.TextBox_Display.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.TextBox_Display.Size = new System.Drawing.Size(325, 235);
            this.TextBox_Display.TabIndex = 5;
            // 
            // Label_Records
            // 
            this.Label_Records.AutoSize = true;
            this.Label_Records.Location = new System.Drawing.Point(12, 133);
            this.Label_Records.Name = "Label_Records";
            this.Label_Records.Size = new System.Drawing.Size(66, 19);
            this.Label_Records.TabIndex = 7;
            this.Label_Records.Text = "Records";
            // 
            // Button_Help
            // 
            this.Button_Help.Location = new System.Drawing.Point(143, 12);
            this.Button_Help.Name = "Button_Help";
            this.Button_Help.Size = new System.Drawing.Size(94, 29);
            this.Button_Help.TabIndex = 6;
            this.Button_Help.Text = "Help";
            this.Button_Help.UseVisualStyleBackColor = true;
            this.Button_Help.Click += new System.EventHandler(this.Button_Help_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 19F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(356, 410);
            this.Controls.Add(this.Label_Records);
            this.Controls.Add(this.Button_Help);
            this.Controls.Add(this.TextBox_Display);
            this.Controls.Add(this.Button_Enter);
            this.Controls.Add(this.Button_Quit);
            this.Controls.Add(this.Button_NewGame);
            this.Controls.Add(this.TextBox_Input);
            this.Controls.Add(this.Label_YourAns);
            this.Name = "Form1";
            this.Text = "Bulls and Cows";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label Label_YourAns;
        private System.Windows.Forms.TextBox TextBox_Input;
        private System.Windows.Forms.Button Button_NewGame;
        private System.Windows.Forms.Button Button_Quit;
        private System.Windows.Forms.Button Button_Enter;
        private System.Windows.Forms.TextBox TextBox_Display;
        private System.Windows.Forms.Label Label_Records;
        private System.Windows.Forms.Button Button_Help;
    }
}

