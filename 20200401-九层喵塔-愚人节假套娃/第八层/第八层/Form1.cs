using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace 第八层
{
    public partial class Form1 : Form
    {
        private static int num;
        //[0,num)
        private int suijishu(int num)
        {
            Random rd = new Random();
            return rd.Next(num);
        }

        public Form1()
        {
            InitializeComponent();
            num = suijishu(100);
        }

        private int count = 10;
        private void button1_Click(object sender, EventArgs e)
        {
            if(textBox1.Text == num.ToString())
            {
                label1.Text = "解压密码：flag倒数第二位是中文";
            }
            else
            {
                count--;
                if(count > 0)
                {
                    label1.Text = "猜错了，本轮你还有" + count + "次机会";
                }
                else
                {
                    label1.Text = "本轮随机数是" + num + "，但你的机会用尽，已重新生成随机数";
                    num = suijishu(100);
                    count = 10;
                }
            }
            textBox1.Text = "";
        }

        private void textBox1_KeyPress(object sender, KeyPressEventArgs e)
        {
            if (e.KeyChar != 8 && !Char.IsDigit(e.KeyChar))
            {
                e.Handled = true;
            }
        }
    }
}
