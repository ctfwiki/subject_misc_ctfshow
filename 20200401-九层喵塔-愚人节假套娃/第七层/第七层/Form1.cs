using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Reflection;

namespace 第七层
{
    public partial class Form1 : Form
    {
        // 隐藏鼠标
        [DllImport("user32.dll", EntryPoint = "ShowCursor", CharSet = CharSet.Auto)]
        public static extern void ShowCursor(int status);
        // 修改鼠标指针图片
        [DllImport("user32.dll")]
        static extern IntPtr LoadCursorFromFile(string fileName);

        public Form1()
        {
            InitializeComponent();
            ShowCursor(0);
        }

        // 超大窗口
        //private static extern int GetWindowRect(IntPtr hwnd, out Rect lpRect);
        private void Form1_Load(object sender, EventArgs e)
        {
            // 全屏黑
            int SW = Screen.PrimaryScreen.Bounds.Width;
            int SH = Screen.PrimaryScreen.Bounds.Height;
            this.Width = SW;
            this.Height = SH;
            this.Location = new Point(0,0);// -5 * SW, -5 * SH);
            label1.Location = new Point((SW - label1.Width)/2, (SH - label1.Height) / 2);
            // 自定义鼠标图片（全黑）
            Cursor customCursor = new Cursor(Cursor.Current.Handle);
            IntPtr customCursorHandle = LoadCursorFromFile("你的自定义鼠标指针的路径");
            customCursor.GetType().InvokeMember("handle", BindingFlags.Public |
            BindingFlags.NonPublic | BindingFlags.Instance |
            BindingFlags.SetField, null, customCursor,
            new object[] { customCursorHandle });
            this.Cursor = customCursor;
        }
        static bool flag = false;
        protected override void WndProc(ref Message m)
        {
            base.WndProc(ref m);
            /*switch (m.Msg)
            {
                case 0x0200: //WM_MOUSEMOVE
                    if (flag)
                    {
                        PostMessage(this.Handle, 0x00A1, new IntPtr(2), m.LParam);
                    }
                    break;
                case 0x201://WM_LBUTTONDOWN
                    flag = true;
                    break;
                case 0x202://WM_LBUTTONUP
                    flag = false;
                    break;
                default:
                    base.WndProc(ref m);
                    break;
            }*/
        }
        // 窗体拖动
        [DllImport("user32.dll", CharSet = CharSet.Unicode)]
        public static extern IntPtr PostMessage(IntPtr hwnd, int wMsg, IntPtr wParam, IntPtr lParam);

        private void Form1_KeyDown(object sender, KeyEventArgs e)
        {
            // 屏蔽Alt+F4
            /*if ((e.KeyCode == Keys.F4) && (e.Alt == true))
            {
                e.Handled = true;
            }*/
            e.Handled = true;
        }
    }
}
