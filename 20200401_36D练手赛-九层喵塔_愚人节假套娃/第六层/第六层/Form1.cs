using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace 第六层
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        int count = 233;
        private void button1_Click(object sender, EventArgs e)
        {
            count--;
            if(count > 0)
            {
                button1.Text = "点我" + count + "次";
            }else
            {
                MessageBox.Show("解压密码：(X[3]-X[4])^2=(X[7]-X[6])^2");
                count = 234;
            }
        }
    }
}
