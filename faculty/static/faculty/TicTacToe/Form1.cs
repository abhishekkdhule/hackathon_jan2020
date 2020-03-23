using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace TicTacToe
{
    public partial class FrmMain : Form
    {
        Random myRandom;
        int turn,counter=0;
        bool winner = false;
        public FrmMain()
        {
            InitializeComponent();
            myRandom = new Random();
            turn = myRandom.Next(2);
        }

        private void btn_Click(object sender, EventArgs e)
        {
            counter++;
            Button btn = (Button)sender;

            if (turn == 0)
            {
                btn.Text = "X";
                if (checkWinner("X"))
                {
                    MessageBox.Show("Player 1 wins");
                    StopGame();
                }
                rad1.ForeColor = Color.Black;
                rad2.ForeColor = Color.Blue;
                rad2.Checked = true;
                turn = 1;
            }
            else
            {
                btn.Text = "O";
                if (checkWinner("O"))
                {
                    MessageBox.Show("Player 2 wins");
                    StopGame();
                }
                rad1.ForeColor = Color.Blue;
                rad2.ForeColor = Color.Black;
                rad1.Checked = true;
                turn = 0;
            }
            btn.Enabled = false;
            if (winner == false && counter == 9)
            {
                MessageBox.Show("It's a Draw");
                StopGame();
                btn.Enabled = true;
            }
        }
        void StopGame()
        {
            btn0.Enabled = false;
            btn1.Enabled = false;
            btn2.Enabled = false;
            btn3.Enabled = false;
            btn4.Enabled = false;
            btn5.Enabled = false;
            btn6.Enabled = false;
            btn7.Enabled = false;
            btn8.Enabled = false;
            btnRestart.Enabled = true;
            
        }
        void ResetALL()
        {
            btn0.Enabled = true;
            btn1.Enabled = true;
            btn2.Enabled = true;
            btn3.Enabled = true;
            btn4.Enabled = true;
            btn5.Enabled = true;
            btn6.Enabled = true;
            btn7.Enabled = true;
            btn8.Enabled = true;
            turn = myRandom.Next(2);
            btn0.Text = "";
            btn1.Text = "";
            btn2.Text = "";
            btn3.Text = "";
            btn4.Text = "";
            btn5.Text = "";
            btn6.Text = "";
            btn7.Text = "";
            btn8.Text = "";

            counter = 0;
            SwitchTrun();

        }
        void SwitchTrun()
        {
            if (turn == 0)
            {
                rad1.Checked = true;
                rad1.ForeColor = Color.BlueViolet;
                rad2.ForeColor = Color.Black;
            }
            else
            {
                rad2.Checked = true;
                rad2.ForeColor = Color.BlueViolet;
                rad1.ForeColor = Color.Black;
            }
        }
        private void FrmMain_Load(object sender, EventArgs e)
        {
            SwitchTrun();
            btnRestart.Enabled = false;
        }

        bool checkWinner(String val)
        {
            if (btn0.Text.Equals(val) && btn1.Text.Equals(val) && btn2.Text.Equals(val))
            {
                winner = true;
                return true;
            }
            else if (btn3.Text.Equals(val) && btn4.Text.Equals(val) && btn5.Text.Equals(val))
            {
                winner = true;
                return true;
            }
            else if (btn6.Text.Equals(val) && btn7.Text.Equals(val) && btn8.Text.Equals(val))
            {
                winner = true;
                return true;
            }
            else if (btn0.Text.Equals(val) && btn3.Text.Equals(val) && btn6.Text.Equals(val))
            {
                winner = true;
                return true;
            }
            else if (btn1.Text.Equals(val) && btn4.Text.Equals(val) && btn7.Text.Equals(val))
            {
                winner = true;
                return true;
            }
            else if (btn2.Text.Equals(val) && btn5.Text.Equals(val) && btn8.Text.Equals(val))
            {
                winner = true;
                return true;
            }
            else if (btn0.Text.Equals(val) && btn4.Text.Equals(val) && btn8.Text.Equals(val))
            {
                winner = true;
                return true;
            }
            else if (btn2.Text.Equals(val) && btn4.Text.Equals(val) && btn6.Text.Equals(val))
            {
                winner = true;
                return true;
            }
            else
                return false;
        }

        private void btnRestart_Click(object sender, EventArgs e)
        {
            if (MessageBox.Show("Do you want to restart the game", "Continue", MessageBoxButtons.OKCancel) == DialogResult.OK)
            {
                ResetALL();
                btnRestart.Enabled = false;
            }
            else
            {
                MessageBox.Show("Thank you for playing!!!");
                this.Close();
            }
        }
    }
}
