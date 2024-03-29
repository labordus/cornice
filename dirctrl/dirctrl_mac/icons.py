import wx
import zlib, cStringIO

# ***************** Catalog starts here *******************

catalog = {}
index = []

class ImageClass: pass

#----------------------------------------------------------------------
def getfolderData():
    return zlib.decompress(
'x\xda\x01\xf9\x02\x06\xfd\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\
\x10\x00\x00\x00\x10\x08\x06\x00\x00\x00\x1f\xf3\xffa\x00\x00\x00\x04sBIT\
\x08\x08\x08\x08|\x08d\x88\x00\x00\x02\xb0IDATx\x9c}\x93\xcfkTW\x14\xc7?\xf7\
\xbe\xf7\x9c\xbcL\xe6G~t(\r\x86\xb4Q\xa2N$\xb1\x9a\x82\xabB\xa0\xd0\xae\xd3m\
\x05\xa1EE\xf0\x0f\xe9?0]$\xabYv\xdd]\xcc\xc2\x1f1(\x04\xb1-\x95"\x16c\xc14?\
\x1e3\xf3\xde\x9b{\xe7\xbew\xdf\xedb4\x06\x04?\x8bs8\x1c\xce\x97/\x87sD\xbd^\
\xe7\xee\xc6\x86\x03x\xb4\xbd\r\xc0\xd2\xd2\x12\x0b\x0b\x0b\xcc\xce\xce\n\
\x80v\xbb\xedx\xcb\xc3\xad-~i\xb5\xc4\xbbZ\xb4Z-766\xc6\xb9s\xe7i6/\x90\xa6)\
\x95J\x85\xb5\xb55\x84\x10\xcc\xcc\xcc\xb0|\xf9"\xd5z\x83c\x91\x07[\xfcv\xff\
17~\xba\x85h\xb7\xdbnuu\xf5\xb8\xa9\x94"\x0cCN\xb2\xb3\xb3\x03\xc0\xbd\xe71\
\xd6\xaf\x10\x8e\xcfR\x9dope\xdc\xc7\xdf\xdb\xdb\'\xcfs\xac\xb5D\x87\xfb\xbc\
\xfc\xe75\xfbG\x07\xd8\x0cdu\x8c \xac1\xfa\xc5el\xe6q\xf6\x8a\x87\xeei\xb4Rt\
w5\xe1T\x19\x1f\x1c\xe5r\x99\xed\xedG<\xfd\xe3o\xce7\x9b\xac,/\x13\x84!6\x08\
\x884\xbc\xda-\x88;)I\xdcg`\n\x84\'\xc9J\x92\xc6\xa8\xc0w\xce\x91\xa6\t\xbf\
\xff\xf5\x92k\xd7\x7f\xa0\x14\xf8\xa4@\xec\xa0\xd3\x87(r(\x93c\x01+}\xac\xc8\
q\x85\xc0I\x8f\xb9\xcf&\x84\x04A\xd2\xedR\x9d\x9aD\x06>{\x0e\x0c \x80\x02\
\xb0\xd6a\x81\xac\x00\x939\xf4\xa0\xa0\x10\x82\x1c\t0\x8ci\xa2\xd1\x9e\xa4\
\x0fH\x07\xa6\x00e\xc1X\xb0R\x92Y\x892`\x90\x14\x9e\xcf\xc08\xa4\xe7\x01\xe0\
# \x8e\x8f\x18\t\xcb\xa4\x0et\x01\x9e\x18fS@\x7f\xe0P\x99\xc5\x140\xc8\xc1\
\x98\x02|\x8fQ\x7fx\nR\x00\x87Q\x17J%\xba9X\x0b\x03\x01\x89\x818\x06e\x1d*\
\x97\xf4\x94Ee`\x9c\xa4\xab\x1c\xe5\x11\xf7\xd6\x01\x90$\x1a5Q\xa1?\x80<\x07\
i \xd1C\x17\xa9\x16\xc4\xda\x92\xe8\x82\xb4\x9f\xa3\xb4\xa52Y%\x95\xde{\x81\
\xbeJ\xc9N\xd59\xec\x81\x1f\x80\xc8\xa1\xd3\x83\xa3n\xc1Q\'\'N,\xa2R\xe3\xd3\
\xd3\x1e\x135G\xf4\xba\xc3\xe4\xfe\xab\xf7\x02z\x90\xd0\xd5\xa3x\x87\xc3\xb5\
j\x03\xc1\x08\x94&$\x8d\xda)\x1a6\xe0\xe0\xc5\x7f\xbc\xd9\xdc$U\xbb\\Z8\xcb\
\xcd\x1b?\n\x00\xdf\xe6\x16\nG\x94\x04\xd4\xc6a\xea\x13\xb09\xc4\x91\xe2\xc5\
\xd6\x9f\x1c<{\xc2\xe7u\xc3\xd5\xaf\x16\xf9\xfe\xe7\xdb\xc7O\xf4\x0e?\x89;,6\
\xe7\xd1\xa7\x1d\xbd\x7f\xdf\xf0\xf4\xd7{\xc8\xe89W\xbf\x9c\xe7\xce\xca\xd7\
\\\xb8\xfd\xcd\x07C\'\x11\xeb\xeb\xebn\xe3\xee&\x8b\x8b\xcb|\xf7\xed\ng\xce\
\xcc1==\xfd\xd1\xa1\x93\xfc\x0f\xfdVH\xfc\xf8\xd8?\x94\x00\x00\x00\x00IEND\
\xaeB`\x82\x07hfK' )

def getfolderBitmap():
    return wx.BitmapFromImage(getfolderImage())

def getfolderImage():
    stream = cStringIO.StringIO(getfolderData())
    return wx.ImageFromStream(stream)

def getfolderIcon():
    icon = wx.EmptyIcon()
    icon.CopyFromBitmap(getfolderBitmap())
    return icon

index.append('folder')
catalog['folder'] = ImageClass()
catalog['folder'].getData = getfolderData
catalog['folder'].getImage = getfolderImage
catalog['folder'].getBitmap = getfolderBitmap
catalog['folder'].getIcon = getfolderIcon


#----------------------------------------------------------------------
def getdesktopData():
    return zlib.decompress(
'x\xda\x01\xc0\x02?\xfd\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\
\x00\x00\x00\x10\x08\x06\x00\x00\x00\x1f\xf3\xffa\x00\x00\x00\x04sBIT\x08\
\x08\x08\x08|\x08d\x88\x00\x00\x02wIDATx\x9c\xa5\x93\xcdkTg\x14\x87\x9f\xf3~\
\xdc;wr3\xb9\xd18\xb6\xa8\x05SD\xb4Z\xdc\x08\xdaU+V(ucW\x82\xd0\xae\xbaTp\
\xd9\x7f\xa0P\\\xb8\xb4\xbb\xae\x04\xa5]u\xa1\x08\xd5\xd2}\x17\xb1Z\x13\xa5P\
\xf3Ad\xd2I\x9c&\x99\xc9\xcc\xbd\xf7}\x8f\x8b\xc9\x1f\xd0\xe2oq\x9e\xd5\xef\
\xc0y\xe0HQ\x14\xbcMdnnN\x17\x97V\xf9w\x10\x98\xce-\xd6\xfc\xf7\xb21\x06\xb7\
\xb0\xf0\x1c\x93\xcf\xb2\xd0{\x87\xab\x9f40\xc6\x02\n\n\x08\xc8x\x80*:\x06\
\xaaJ\xe2=\xf3\xf3\xf3\xb8N\xb7\xc7\xdf/\x9e\xf2d\xf1w\xee=\xd8bTC\x9aXZ\x13\
\x9ef\xd3\xe1\xbdE\x15\xea:\xd0}=\xa4\xae"*\xe0l\xca{\xd35.\xaa\xd0jM\xf1\
\xe1\xd16?>|\xc9\xf1\xd9\x822\x00\xbe\x81\xcb\x1duP\x00\xbc5L%\x15\xab\x9d\
\x01\xc7\x0f\xa6L\x15\x93lt;\x98\x18\x95\xfd{3n\\\xff\x88\xb6\xaf\xb8q\xf5\
\x0c\xdf\\9\xc2\xe6V\x9f\xd1\xb0$qJ+\xb7\xe4MC{o\x8a\x93\x9a\x8b\x1f\x1f\xe4\
\xf2\x97\xe7\xf1>\xc1\x89\x08\xaf\xd6\xfa\xdc\xba\xfb\x98\x9d\x91p\xfb\xa7\
\xc7\x8c\x9c\xa3?\x0c\x1c\x9eLh4<\x8a\xa2\nF\x84w\xf7\xe7\xdc\xf9e\x91\xf8\
\xdb:\x8d\xfe6&D\xc5{\xc3\x81\x99\x94t:c\xdf\xbe\x8c\xf5N\x0fg,Y\xc3\x11\xe3\
\xd8\xa6\x88`\x8c\x90f\x9e\xf3\xa7f\xf8\xea\xf3\x934\'\xf3\xf1\t\xdeZ.\x9c9\
\xc2\xa9c{\xf8\xec\xd3\x0f\xf8\xe2\xc2Q\xba\xddm\xd67\x86\x84\x18Q\x1d{\x88@\
\xe2\xc0\xb4\x9a\xac\x94)UU!\xdf\xdd\xfc^_nL\x90e)OV\x02\xc7\x0e9:\xbd\x92\
\x85WJ\xe6\x84V+e\xbah`\x9d\x00\x82\xb7BY\x96\xbc\xde\x0c\xcc\xa4}L\xac\x02\
\xed=M\xbe\xbdv\x0e\xca!__:\xcd\xe5s\xef\xb3\xd3\x1f1*\x03k\xff\x0cX\xeb\x0e\
(\xcb@\x88\x91\xa8J\xdeL\xc9\xf3\x0c\x01\\\x04\x96V{\xdc}\xf0\'\x83Q\xc5\xcf\
\xbf\xceSV\x01/\xe0D@\x94\xc1\xe6\x08\xd1HQ4\x105\x18\x04k\x1d\xd5N\x8dK\x92\
\x84\xbf\x96\xb6x\xf4\xc73\xb2\x89\x84\x1f\xee\xaf\xe0\xbc#of\x18g\xf0\xd6`\
\x9d\x01\x85\x10,\xde\'\xf8\xc4\x90d\t1x\xdc\xd9\xd3\'\x80gt\xd6\xb7\x10S\
\xee\x1a\x07\x91\xed]\x9a]\x821\x82s\x82\x11\x83(\xb4\x0f\xb7\x90\xa2(X^^\
\xd6\xba\xae\xff\xf7\'z\xef\xc7\x0b\xde&o\x00)m\xf6\xd98\x95\xf4\xc7\x00\x00\
\x00\x00IEND\xaeB`\x82m\x9aOK' )

def getdesktopBitmap():
    return wx.BitmapFromImage(getdesktopImage())

def getdesktopImage():
    stream = cStringIO.StringIO(getdesktopData())
    return wx.ImageFromStream(stream)

def getdesktopIcon():
    icon = wx.EmptyIcon()
    icon.CopyFromBitmap(getdesktopBitmap())
    return icon

index.append('desktop')
catalog['desktop'] = ImageClass()
catalog['desktop'].getData = getdesktopData
catalog['desktop'].getImage = getdesktopImage
catalog['desktop'].getBitmap = getdesktopBitmap
catalog['desktop'].getIcon = getdesktopIcon


#----------------------------------------------------------------------
def gethomeData():
    return zlib.decompress(
'x\xda\x01\xd9\x02&\xfd\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\
\x00\x00\x00\x10\x08\x06\x00\x00\x00\x1f\xf3\xffa\x00\x00\x00\x04sBIT\x08\
\x08\x08\x08|\x08d\x88\x00\x00\x02\x90IDATx\x9c\xa5\x93\xdfKSq\x18\xc6?\xdf\
\xb3s\xce\xce\xdc\xd6\xd6\xaa9\xd9\x8fLf\xa5\x12DY\xf6\x9b AJ\xc9\x8bn\xba\
\xce\x9b\xee\xfa\x0f\xfa\x13\xba)\x88 \xa1\x90\xd2\x8b\xa0 \x82\xba\xee\x17Q\
J\xce\xad\xc6R\xc9-5\xd4MS7\xed\x9c\x9d\xf3\xed*iY\xdd\xf4\xde\xbe\xcf\xf3\
\xe1\x85\xe7}D0\x18\xe4\x7fF\xfd\xdb"\x9d\xce\xc8\x17/_\xd1\xb2w\x0f\xad\xad\
-\xd8\xb6\xcd\xec\xec,~\xbf\x9fd2)\xfe\tH\xa73rpp\x90\xe17\xcfy\x11\x89s\xa9\
\xaf\x0f!\x1dr\x1fS\xa0\xa8LOO\xcbh4*\x00\x94\xdf\xcd\xa3\xa3)900\xc0\xa7\
\x0fo9{\xba\r\xa5Z\xa2\xffv?c\xa9\xf74l\xdfBey\x11\xcb\xb26\xf4\x1b\x80b\xb1\
(\xdf\r\x0f\xcb;w\xef2\xf5\xf1\x1d\xed\xbb\xb6S\xe7T9\x92\xac\xc7^\x98\xe4\
\xe9\x93\xc7\xe8\x86\x0fU\xad=Z\xf9i.\x14\n\xdc\xbbw\x9f\xf2\xf2\x1c]\xfb\
\x9b\xc9=|\xc4\x813\x17Y[X\'\xb10A[[\x92\xeb7\xfb)--\xe18N- \x9f\xcf344\xc4\
\xf2B\x81\xde\x9e.T\xd5\x8b.]\xd8\x81\x06\x84\xdb\x87\xb9Z\xa5\xbb\xbb\x9bH\
\xc8\xc3h*\xcb\xf8\xf8D-`l,\xcd\xe2\xfcW:O\x1e\xc2\xd0\xbd\xc4\x0f\x1ec\xcf\
\xf9\x1e\x9e\xdd\xb8\xcaze\x8e\x8e\xcbW0M\xc9\x85\xdes\xc4\xa3;\x18M\x8d\x91\
\xcf\xe7\xe5F\n\x1d\x1d\x87Y]^B\xf7z\xd9\xb6\xa3\x01Mw\xd3x\xaa\x87\x89\\\
\x86@ \xc8\xbe\x93\x9d\x94\xbf-b\x84\xc3D\xc7g8q\xfc(\x89DBl\x00\xc2\xe10\
\xf5\x91z|:x}\x01\x84K\xf0\xe0\xd65\xac\xcck\xca\xba\x87\xa6\xa6f\xa2;\x9b\
\xd15\x95\xba:/\x91Hd\xf3#)\x8a\x82\xc7c\xa0\n\x81#T\xda\xf76"\xcai*\xba\x1f\
\xb7\xdb@\xd5TT\x97\x0b\xdd0jRP\x01\xa4\x94\x08\xa1\xa0\xb9\r\x1c)\x91R\xe2\
\xf3\xd7\xb1\xb5\xa5\x89\xd2\x9a\x8d\xacZ A(\x02M\xd3\x91R\xd6\x02,\xcb\xa2Z\
\xb5\xd0T\x95\xc0\xd6\x00\xb84\xbc\xba\x82S\xfc\x82\xdb\x1d\xc4\xef\xf7\x12\
\x0c\x85\xb0m\x07\x01\x98\xe6\xf7\xcd\x00\xabj39\x95g2?\x83]\xb5)\x99\x1a\
\xfex;\x8b\xeb\x92W\xaf\xdf\x10\xfa\xfc\x15\xdd\xad\xb3R.c\x9aV- \x16\x8b\
\x89\x91\x91\x11\x99\xcb\xe50M\x8bJ\xa5L\xc9\x883\xafF\x10B\x10P<\xac\x99\
\x16\xa6#I\xeen\xe5\xd7\x06\x8b?\xd59\x9b\xcd\xca\x95\x95\x15\x1c\xc7A\x08\
\x81a\x18\x84B!b\xb1\x98\xf8]\xfb\x03\xcfg\x08\x14F\xf9P{\x00\x00\x00\x00IEN\
D\xaeB`\x82\r3U\xe5' )

def gethomeBitmap():
    return wx.BitmapFromImage(gethomeImage())

def gethomeImage():
    stream = cStringIO.StringIO(gethomeData())
    return wx.ImageFromStream(stream)

def gethomeIcon():
    icon = wx.EmptyIcon()
    icon.CopyFromBitmap(gethomeBitmap())
    return icon

index.append('home')
catalog['home'] = ImageClass()
catalog['home'].getData = gethomeData
catalog['home'].getImage = gethomeImage
catalog['home'].getBitmap = gethomeBitmap
catalog['home'].getIcon = gethomeIcon


#----------------------------------------------------------------------
def getvolumeData():
    return zlib.decompress(
'x\xda\x01\x1c\x03\xe3\xfc\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\
\x10\x00\x00\x00\x10\x08\x06\x00\x00\x00\x1f\xf3\xffa\x00\x00\x00\x04sBIT\
\x08\x08\x08\x08|\x08d\x88\x00\x00\x02\xd3IDATx\x9c\x8d\x92Mk\x1bW\x14\x86\
\x9f\xb9\xf3\xa1\xd1\xd8\x92=\xf1\xc8\xb2S\x1b\x07\x9cM\xc04`\n\x81\xd2lKV\
\xcd?h6Y\x86.\xd2]\x03\xa1?\xa0\xf4\xc7d\xd3\xa4\x86B6%\x85\xc6-\xa4\xe0EL\r\
\xa5B\x9a\xb1\xa4\x19Y\x9a\x19\xcd\xdc;\xf7v!\x83\xb7=\xebs\x1e\x1e\xde\xf7X\
\xc6\x18\xb3\\.y\xf7\xee7\x84\x10x\x9e\x87\xd6\x1ac\x00\x0c\x00Z\x1b\x94\x92\
h\xad\xd1Z\xe3\xba.\x0f\x1f~\x81m\xdb\x08\x80\xc1`\xc0\xd1\xd1\xa7\xbcz\xf5\
\x13\x83\xc1\x90\xe10&\x8e/\x19\x8f\xa7\x9c\x9f\xff\xcdp8bww\x9f\xfb\xf7\x1f\
\xf0\xe6\xcd/XV\x8b\xe9t\n\x80\x030\x9b\xcd\xd8\xda\xda\xe6\xf6\xed\x1d^\xbe\
\xfc\x8eV\xcb\xc7q\x1cl[\x90e3\xba\xdd\x0e\xcf\x9e}\xcb\xe1\xe1]\xd6\xd6\xda\
\x94eN\x9a\xa6\xf4z\xbd\x15`\xb1\xc81\xc6\xe6\xc9\x93\xafy\xfe\xfc\x1b\xb4\
\x06\xa54J\x19l\xdb\xa2(\x16\x9c\x9d\x9d\x91e\x19\xae\xebb\x0c\xa4izcPU\x15A\
\xe0\xf0\xfe\xfd_\x18#\xa8\xeb\x1a\xa5\x14JUH\xa9i\x1aI]\xd7ln\x86x\x9e\x87\
\x10\x82\xf9|\x01\xb0\xca\xa0(J^\xbc\xf8\x1e\xdf\xf7\x11\xc2 \x84@\x08\x03\
\xd8X\x16\xd8\xb6\xc0\xb6]\xf2<g}}\x83\x93\x93\x13\xe6\xf3\xf9\x8dA\xd3h\x1e\
?\xfe\x8a<\xcf\xaf\r\x96\xd8\xb6\x8d\xe3h\x8c\x11HiP\xaa@k\x0b\xdfo\xb1\xb7\
\xb7G\x9e\xe77\x00\xb3\xea\x0c\xc7iQ\x14\x05JI\xc6\xe3)`\x10\xc2&\x8eGt\xbb\
\x1d\x1c\xc7E\x08\xe8v7\xc8\xf3ruS\xd7\xf5\xf5R\xcc\xd6VD\xd3(\xaaJr\xef\xde\
]Z\xad\x80\xbaV\xb4\xdb>I\x92\x00\x16R6\xd7a\xda+\x801\x86\x8b\x8b\x0b\xa2h\
\x9b\xc9\xe4\x9c\xb2\xcc\xe9t:\xd4u\x85\xe7yT\xd5\x92<_bY\x16Y\x96\xd1n\xaf\
\xd1\xef\xf7\x19\x8f\x13\xaa\xaa\xc2)\xcb\x92\xa6\xd1\x14EA\x18\x86\xf4\xfb\
\x11\xa3QL\x9e\x97\x8cF\tJ)\\W\xe0\xba-\xee\xdc9\xa0\xaaj\xd24\xa5i4eY\xe2dY\
\xc6d2!\x8e\x13677\x08\xc3\x88~\xbf\xc7\xc1\xc1\xde\xf5[\xc3rY2\x18\x0c\x19\
\x0cF\xa4\xe9\x98,\x9b\xe186Y\x96\xe1H)\xf1\xfd6\x8f\x1e}\x89\x10>\xc6T()i\
\xb7\x03\xea\xba\x02\xc0\xf3\\vw\xb6\xd9\xdf\xff\x04\xcbj\xa1\xf5\x92\xd7\
\xaf\x7fFJ\x89\x13E\x11I2\xe1\xed\xdbS\x00.\xe3\x98\xdfO\x7f\xe5\xf8\xf8\x01\
\x1f>\x9c\xa2\xb5B)\x8deY|v\xfc9\x07\x87\x97\x14\x8b#\x92dB\x14E8A\x10p\xeb\
\xd6:\x1f?\xfe\t@]K\xa2h\x83\xc9\xe4_\xc20\xc0\x18q]\xb3!\x19\xff\xc3\x0f?\
\xfe\xc1\xd3\xa7\x8a\x9d\x9d\x1eA\x10`i\xadM\x9a\xa6\\]]!\x84\xe0\xff\x8c\
\xd6\x9an\xb7K\x18\x86\xfc\x07\xaa\x13\x7f\xa3\xd5\xe0fI\x00\x00\x00\x00IEND\
\xaeB`\x82\xe2EuY' )

def getvolumeBitmap():
    return wx.BitmapFromImage(getvolumeImage())

def getvolumeImage():
    stream = cStringIO.StringIO(getvolumeData())
    return wx.ImageFromStream(stream)

def getvolumeIcon():
    icon = wx.EmptyIcon()
    icon.CopyFromBitmap(getvolumeBitmap())
    return icon

index.append('volume')
catalog['volume'] = ImageClass()
catalog['volume'].getData = getvolumeData
catalog['volume'].getImage = getvolumeImage
catalog['volume'].getBitmap = getvolumeBitmap
catalog['volume'].getIcon = getvolumeIcon


#----------------------------------------------------------------------
def getcomputerData():
    return zlib.decompress(
'x\xda\x01(\x02\xd7\xfd\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x10\
\x00\x00\x00\x10\x08\x06\x00\x00\x00\x1f\xf3\xffa\x00\x00\x00\x04sBIT\x08\
\x08\x08\x08|\x08d\x88\x00\x00\x01\xdfIDATx\x9c\xa5\x92\xcdk\x13Q\x14\xc5\
\x7f\xefM\x92\xc9d\x92\xf4\x8d1M?\x14\xdc\x04\xdd\xb8\x10\x84n]\xd4E]\xba\
\xe9\xffb\xff\x0b\x8b\xff@\x17B\x91\xba\xcf\xb2\xb8\n]\x0b\x85,\xd2J\xc4\xb4\
`\xd21\x1f\x93\x99\xbc\xccu\xe1W\xd3\xd8\xaax\xe1\xf2\xb8p\xef\xe1\x9c\xf3\
\x8e2\xc6\xf0?\x95\xb9<\xec\xef\xef\xcb\xdf\x1cmoo\xab\x9f\x831\x06c\x0c\x8d\
FCz\xbd\x9e\x88\xcc.\xb5\x15\x91\xa9\xc8,\xf9\xd66\x910\x0c\xa5\xd1h\xc8\x8f\
\xbb9\x06A\x10Py\xfe\x86\xc0\xb8\xb8\xbeG\xb9R\xa2|\xabH\xb9\xe2S\xb9]\xc4q3\
\xbcz\x12\\/\x01\xa0\x9c\xd5\xe45\xf89\xc8)\x8b\r\x07H^\x18\xeb\x14\xd7+\xdc\
\xec\x01\x80d5Kw\x02\xc6g\x03\xac\x9d\x91/\xb9\xf4\xceg$\x91\xc5)\xc6\xc0\
\xea\xdc\xbe\xbe\n\x10\xf7#\x86\x9d\x0b\xd6\x1e\xae\xa33YldI\x861\xc3\xc1\
\x98Q\x18-0X\x00\xb0V\x18\xf4G\x9c\xb7?3:\x0f\xc9\x14]\xbc\x95%r~\x9e$\x89\
\xff,A\xe5\x1cP\x9a\x8bN\x8f\xbb\x8f\xef\xe18\x1a\xfb%"!E2\x1a\x90\xeb\x01\
\xce\xce>\xf1\xfa\xc5#\\7\x87\xd2\x1a%\x82\xd2\x1a\xc7uP\n\xe2i\xc2\x87\xd3S\
\xe2\xf8\x17\x13u9\x89{{{\xd2j\xb5\xb0\xd6\x12\x86!Q\x141\x99L\x08\x82\x80 \
\x08\xf0<\x8fz\xbd>\x17$\xf5\xbb(\xef\xec\xec\xc8\xe6\xe6S\x1e\xdc\xafsp\xf0\
\x96\xac\xd6\xbc?>\xe6\xe5\xee\xae\xba\xba\xbb\xe0\xc1\xd1\xd1\x91\xf8\x85\
\x02\xcb\xb5\x15&q\xc4\xd6\xb3-:\x9d\x0e\xdd\x8f\x1d\x9a\xcd\xa6lll\xcc\x81,\
\xfc\xc2I\xbb\x8d1\x06\xc7\xd1\xf8\x05\x1f\xcf\xf3(\x16J\xac\xae\xaf\xf1\xee\
\xf0p\x81\xed\x9c\x84n\xb7+\xfd~\x9f\xd1p\xc8,MI\xd3\x14\xf9\xfeN\xa7S\xaa\
\xd5*\xd5\xe5ej\xb5\xda\xcd\x1e\xfcK}\x05>\xe9\xd2\xb58\x9a%\xf7\x00\x00\x00\
\x00IEND\xaeB`\x82\xb4\xc1\x05\xd1' )

def getcomputerBitmap():
    return wx.BitmapFromImage(getcomputerImage())

def getcomputerImage():
    stream = cStringIO.StringIO(getcomputerData())
    return wx.ImageFromStream(stream)

def getcomputerIcon():
    icon = wx.EmptyIcon()
    icon.CopyFromBitmap(getcomputerBitmap())
    return icon

index.append('computer')
catalog['computer'] = ImageClass()
catalog['computer'].getData = getcomputerData
catalog['computer'].getImage = getcomputerImage
catalog['computer'].getBitmap = getcomputerBitmap
catalog['computer'].getIcon = getcomputerIcon


