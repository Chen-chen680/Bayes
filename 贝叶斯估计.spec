# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['贝叶斯估计.py'],
             pathex=['C:\\Users\\12517\\Documents\\Tencent Files\\1251742511\\FileRecv\\大二下\\课程实验\\统计计算与软件\\数据\\《统计计算与软件》课程设计原始数据（8组）\\csv'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='贝叶斯估计',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
