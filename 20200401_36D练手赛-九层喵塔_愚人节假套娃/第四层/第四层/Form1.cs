using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace 第四层
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            int SW = Screen.PrimaryScreen.Bounds.Width;
            int SH = Screen.PrimaryScreen.Bounds.Height;
            this.Location = new Point(SW, SH);
        }
    }
}
