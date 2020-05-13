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

namespace 第二层
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private static int count = 0;

        private int suijishu(int num)
        {
            Random rd = new Random();
            return rd.Next(num);
        }
        
        private void label1_Click(object sender, EventArgs e)
        {
            MessageBox.Show("解压密码：flag的md5是0a9e4e1ac78b87485a4d23d49379aa5b");
        }

        private void label1_MouseEnter(object sender, EventArgs e)
        {
            if (count < 100)
            {
                int x = 0;
                int y = 0;
                while (true)
                {
                    x = suijishu(this.Width - label1.Width-20);
                    Thread.Sleep(10);
                    y = suijishu(this.Height - label1.Height-20);
                    if (Math.Abs(x - label1.Location.X) > label1.Width || Math.Abs(y - label1.Location.Y) > label1.Height)
                    {
                        break;
                    }
                }
                label2.Text = x + "," + y;
                label1.Location = new Point(x, y);
                count += 1;
            }
            else
            {
                label1.Text = "我跑不动了";
            }
        }
    }
}
