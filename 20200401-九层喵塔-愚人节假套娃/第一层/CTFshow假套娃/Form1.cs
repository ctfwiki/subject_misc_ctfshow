using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CTFshow假套娃
{
    public partial class Form1 : Form
    {
        public static Int64 endTime; 
        public Form1()
        {
            InitializeComponent();
            endTime = GetTimeStamp()+60*60;
            updateTime();
            timer1.Start();
        }
        /// <summary>
        /// 获取时间戳
        /// </summary>
        /// <returns></returns>
        private Int64 GetTimeStamp()
        {
            TimeSpan ts = DateTime.Now - new DateTime(1970, 1, 1, 0, 0, 0, 0);
            return Convert.ToInt64(ts.TotalSeconds);
        }

        private string calc(Int64 duration)
        {
            TimeSpan ts = new TimeSpan(0, 0, Convert.ToInt32(duration));
            string str = "";
            if (ts.Hours > 0)
            {
                str = ts.Hours.ToString() + "小时 " + ts.Minutes.ToString() + "分钟 " + ts.Seconds + "秒";
            }
            if (ts.Hours == 0 && ts.Minutes > 0)
            {
                str = ts.Minutes.ToString() + "分钟 " + ts.Seconds + "秒";
            }
            if (ts.Hours == 0 && ts.Minutes == 0)
            {
                str = ts.Seconds + "秒";
            }
            return str;
        }

        private void updateTime()
        {
            Int64 rest = endTime - GetTimeStamp();
            if(rest >= 0)
            {
                label2.Text = calc(rest);
            }
            else
            {
                label2.Text = "解压密码：flag是flag{XXX-XXX-XXX}格式的";
            }
        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            updateTime();
        }
    }
}
