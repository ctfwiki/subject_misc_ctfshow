# -*- coding: utf-8 -*-
# https://blog.csdn.net/sunny_xsc1994/article/details/78541079
# save from https://github.com/ruozhichen/rgb2Lab-rgb2hsl
import numpy as np
import os
from PIL import Image
import math

def hsl2rgb(inputColor):
    ''' Converts HSL colorspace (Hue/Saturation/Value) to RGB colorspace.
        Formula from http://www.easyrgb.com/math.php?MATH=M19#text19

        Input:
            h (float) : Hue (0...1, but can be above or below
                              (This is a rotation around the chromatic circle))
            s (float) : Saturation (0...1)    (0=toward grey, 1=pure color)
            l (float) : Lightness (0...1)     (0=black 0.5=pure color 1=white)

        Ouput:
            (r,g,b) (integers 0...255) : Corresponding RGB values

        Examples:
            >>> print HSL_to_RGB(0.7,0.7,0.6)
            (110, 82, 224)
            >>> r,g,b = HSL_to_RGB(0.7,0.7,0.6)
            >>> print g
            82
    '''
    h=inputColor[0]
    s=inputColor[1]
    l=inputColor[2]
    def hue2rgb( v1, v2, vH ):
        while vH<0.0: vH += 1.0
        while vH>1.0: vH -= 1.0
        if 6*vH < 1.0 : return v1 + (v2-v1)*6.0*vH
        if 2*vH < 1.0 : return v2
        if 3*vH < 2.0 : return v1 + (v2-v1)*((2.0/3.0)-vH)*6.0
        return v1

    if not (0 <= s <=1): raise ValueError("s (saturation) parameter must be between 0 and 1.")
    if not (0 <= l <=1): raise ValueError("l (lightness) parameter must be between 0 and 1.")

    r,b,g = (l*255,)*3
    if s!=0.0:
       	if l<0.5 : var_2 = l * ( 1.0 + s )
       	else     : var_2 = ( l + s ) - ( s * l )
       	var_1 = 2.0 * l - var_2
       	r = 255 * hue2rgb( var_1, var_2, h + ( 1.0 / 3.0 ) )
       	g = 255 * hue2rgb( var_1, var_2, h )
       	b = 255 * hue2rgb( var_1, var_2, h - ( 1.0 / 3.0 ) )
    r=max(min(r,255.0),0.0)
    g=max(min(g,255.0),0.0)
    b=max(min(b,255.0),0.0)
    return (int(round(r)),int(round(g)),int(round(b)))

def hue2rgb_matrix(v1,v2,vH):
    vH=np.where(vH<0.0,vH+1.0,vH)
    vH=np.where(vH>1.0,vH-1.0,vH)
    res=np.where(vH>=2.0/3,v1,0.0)
    res=np.where(vH<2.0/3,v1 + (v2-v1)*((2.0/3.0)-vH)*6.0,res)
    res=np.where(vH<1.0/2,v2,res)
    res=np.where(vH<1.0/6,v1+(v2-v1)*6.0*vH,res)
    return res

# colors size: n*3, when n is very large, it improves speed using matrix calculation
def hsl2rgb_matrix(colors):
    colors=np.array(colors)
    hs=colors[:,0]
    ss=colors[:,1]
    ls=colors[:,2]
    Rs,Gs,Bs=(ls*255,)*3
    #np.seterr(divide='ignore', invalid='ignore')

    var_2=np.where(ls<0.5,ls*(1.0+ss),(ls+ss)-(ss*ls))
    var_1=2.0*ls-var_2
    Rs=255*hue2rgb_matrix(var_1,var_2,hs+(1.0/3.0))
    Gs=255*hue2rgb_matrix(var_1,var_2,hs)
    Bs=255*hue2rgb_matrix(var_1,var_2,hs-(1.0/3.0))
    Rs=np.where(ss==0.0,ls*255,Rs)
    Gs=np.where(ss==0.0,ls*255,Gs)
    Bs=np.where(ss==0.0,ls*255,Bs)
    Rs=np.maximum(np.minimum(Rs,255),0)
    Gs=np.maximum(np.minimum(Gs,255),0)
    Bs=np.maximum(np.minimum(Bs,255),0)
    RGBs=np.vstack((Rs,Gs,Bs)).transpose()  # 3*n -> n*3
    RGBs=RGBs.astype('int')
    return RGBs


def rgb2hsl(inputColor):
    ''' Converts RGB colorspace to HSL (Hue/Saturation/Value) colorspace.
        Formula from http://www.easyrgb.com/math.php?MATH=M18#text18

        Input:
            (r,g,b) (integers 0...255) : RGB values

        Ouput:
            (h,s,l) (floats 0...1): corresponding HSL values

        Example:
            >>> print RGB_to_HSL(110,82,224)
            (0.69953051643192476, 0.69607843137254899, 0.59999999999999998)
            >>> h,s,l = RGB_to_HSL(110,82,224)
            >>> print s
            0.696078431373
    '''
    r=inputColor[0]
    g=inputColor[1]
    b=inputColor[2]
    if not (0 <= r <=255): raise ValueError("r (red) parameter must be between 0 and 255.")
    if not (0 <= g <=255): raise ValueError("g (green) parameter must be between 0 and 255.")
    if not (0 <= b <=255): raise ValueError("b (blue) parameter must be between 0 and 255.")

    var_R = r/255.0
    var_G = g/255.0
    var_B = b/255.0

    var_Min = min( var_R, var_G, var_B )    # Min. value of RGB
    var_Max = max( var_R, var_G, var_B )    # Max. value of RGB
    del_Max = var_Max - var_Min             # Delta RGB value

    l = ( var_Max + var_Min ) / 2.0
    h = 0.0
    s = 0.0
    if del_Max!=0.0:
       if l<0.5: s = del_Max / ( var_Max + var_Min )
       else:     s = del_Max / ( 2.0 - var_Max - var_Min )
       del_R = ( ( ( var_Max - var_R ) / 6.0 ) + ( del_Max / 2.0 ) ) / del_Max
       del_G = ( ( ( var_Max - var_G ) / 6.0 ) + ( del_Max / 2.0 ) ) / del_Max
       del_B = ( ( ( var_Max - var_B ) / 6.0 ) + ( del_Max / 2.0 ) ) / del_Max
       if    var_R == var_Max : h = del_B - del_G
       elif  var_G == var_Max : h = ( 1.0 / 3.0 ) + del_R - del_B
       elif  var_B == var_Max : h = ( 2.0 / 3.0 ) + del_G - del_R
       while h < 0.0: h += 1.0
       while h > 1.0: h -= 1.0

    return (h,s,l)

# colors size: n*3, when n is very large, it improves speed using matrix calculation
def rgb2hsl_matrix(colors):
    colors=np.array(colors)
    var_Rs=colors[:,0]/255.0
    var_Gs=colors[:,1]/255.0
    var_Bs=colors[:,2]/255.0
    var_Min=np.amin(colors/255.0,axis=1) # min(Ri,Gi,Bi) in each row
    var_Max=np.amax(colors/255.0,axis=1)
    del_Max=var_Max-var_Min
    ls=(var_Max+var_Min)/2.0
    hs=0.0
    ss=0.0
    # When del_Max=0,it may exist the situation that var_Max+var_Min or 2.0-var_Max-var_Min = 0
    # and the program would report error "invalid value encountered in divide"
    # However, at the end it will set zero when del_Max=0
    # so I ignore the error here
    # https://docs.scipy.org/doc/numpy/reference/generated/numpy.seterr.html
    np.seterr(divide='ignore', invalid='ignore')
    ss=np.where(ls<0.5,del_Max/(var_Max+var_Min),del_Max/(2.0-var_Max-var_Min))

    del_R=np.where(del_Max!=0.0,(((var_Max-var_Rs)/6.0)+(del_Max/2.0))/del_Max,0.0)
    del_G=np.where(del_Max!=0.0,(((var_Max-var_Gs)/6.0)+(del_Max/2.0))/del_Max,0.0)
    del_B=np.where(del_Max!=0.0,(((var_Max-var_Bs)/6.0)+(del_Max/2.0))/del_Max,0.0)

    hs=np.where(var_Rs==var_Max,del_B-del_G,hs)
    hs=np.where(var_Gs==var_Max,(1.0/3.0)+del_R-del_B,hs)
    hs=np.where(var_Bs==var_Max,(2.0/3.0)+del_G-del_R,hs)

    hs=np.where(del_Max!=0,hs,0.0)
    hs=np.where(hs<0.0,hs+1.0,hs)
    hs=np.where(hs>1.0,hs-1.0,hs)
    ss=np.where(del_Max!=0,ss,0.0)

    hsl=np.vstack((hs,ss,ls)).transpose()
    return hsl

#img = Image.open('input/test1.jpg')
#im = np.array(img)
#print im.shape

#for i in range(len(im[:,1])):
#    for j in range(len(im[1,:])):
#        h,s,l = RGB_to_HSL(im[i][j][0],im[i][j][1],im[i][j][2])
#        h = h+0.3
#        if h > 1:
#            h = h - 1
#        r,g,b = HSL_to_RGB(h,s,l)
#        im[i][j][0] = r
#        im[i][j][1] = g
#        im[i][j][2] = b
#scipy.misc.imsave('result.jpg', im)
