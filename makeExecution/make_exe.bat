pyinstaller -D -i icon.ico --hiddenimport=pydicom.encoders.gdcm --hiddenimport=pydicom.encoders.pylibjpeg -w ../DicomConverter.py
