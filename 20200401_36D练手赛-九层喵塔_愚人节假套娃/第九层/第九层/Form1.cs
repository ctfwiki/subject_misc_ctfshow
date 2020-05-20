using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Threading;

namespace 第九层
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            timer1.Start();
        }
        private int suijishu(int num)
        {
            Random rd = new Random();
            return rd.Next(num);
        }

        int dui = 10;
        int num1 = 0;
        int opt = 0;
        int num2 = 0;

        private int suan()
        {
            if(opt==0)
            {
                return num1 + num2;
            }
            else
            {
                return num1 - num2;
            }
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            if (textBox1.Text == suan().ToString())
            {
                if(--dui == 0)
                {
                    label1.Text = "flag提示：仔细观察第一个解压密码";
                    label1.ForeColor = Color.Red;
                    timer1.Stop();
                }
                else
                {
                    label1.Text = "十以内加减法，算对" + dui + "次就给你你想要的";
                }
            }
            num1 = suijishu(10);
            label2.Text = num1.ToString();
            Thread.Sleep(10);
            opt = suijishu(2);
            if (opt == 0)
            {
                label3.Text = "+";
            }
            else
            {
                label3.Text = "-";
            }
            Thread.Sleep(50);
            num2 = suijishu(10);
            label4.Text = num2.ToString();
        }
    }
}
