# -*- mode: python -*-

block_cipher = None


a = Analysis(['memorama.py'],
             pathex=['C:\\Users\\seedi\\Desktop\\memorama'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)

a.datas += [('fondo.gif', 'C:\\Users\\seedi\\Desktop\\memorama\\images\\fondo.gif', "DATA"),
('1.gif', 'C:\\Users\\seedi\\Desktop\\memorama\\images\\1.gif', "DATA"),
('2.gif', 'C:\\Users\\seedi\\Desktop\\memorama\\images\\2.gif', "DATA"),
('3.gif', 'C:\\Users\\seedi\\Desktop\\memorama\\images\\3.gif', "DATA"),
('4.gif', 'C:\\Users\\seedi\\Desktop\\memorama\\images\\4.gif', "DATA"),
('5.gif', 'C:\\Users\\seedi\\Desktop\\memorama\\images\\5.gif', "DATA"),
('6.gif', 'C:\\Users\\seedi\\Desktop\\memorama\\images\\6.gif', "DATA"),
('7.gif', 'C:\\Users\\seedi\\Desktop\\memorama\\images\\7.gif', "DATA"),
('8.gif', 'C:\\Users\\seedi\\Desktop\\memorama\\images\\8.gif', "DATA")]

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='memorama',
          debug=False,
          strip=False,
          upx=True,
          console=False)