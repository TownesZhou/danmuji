# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['danmuji.py'],
             pathex=[],
             binaries=[],
             datas=[('bilibili-api\\bilibili_api\\data\\*.*', 'bilibili_api\\data'), ('bilibili-api\\bilibili_api\\data\\api\\*.*', 'bilibili_api\\data\\api'), ('asset\\*.*', 'asset\\')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
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
          name='弹幕抽奖姬',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='asset\\icon.ico')
