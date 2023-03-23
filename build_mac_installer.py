import os

app_name = "matexecutable"
app_path = "build/bin/matexecutable"
dmg_name = "build/matexecutable.dmg"

os.system(f"hdiutil create -volname {app_name} -srcfolder {app_path} -ov -format UDZO {dmg_name}")