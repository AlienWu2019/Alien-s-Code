# -*- mode: python -*-

block_cipher = None


a = Analysis(['baike.py'],
             pathex=['C:\\Users\\Œ‚‘Û¡º\\PycharmProjects\\untitled2\\PyQt\\image2'],
             binaries=[],
             datas=[],
             hiddenimports=['queue'],
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
          name='baike',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
