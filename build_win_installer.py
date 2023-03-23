import os
import urllib.request
import zipfile
import subprocess

def download_wix(source_url, destination_path):
    wix_folder = os.path.join(os.getcwd(), "wix")

    try:
        if os.path.exists(destination_path):
            print(f"WiX already downloaded at: {destination_path}")
        else:
            if not os.path.exists(wix_folder):
                os.makedirs(wix_folder)

            print(f"Downloading {source_url}...")
            urllib.request.urlretrieve(source_url, destination_path)
            print("Download finished")

            print(f"Extracting {destination_path}...")
            with zipfile.ZipFile(destination_path, 'r') as zip_ref:
                zip_ref.extractall(wix_folder)
            print("Extraction finished")
    except Exception as e:
        print(e)
        exit(1)

def build_installer(wix_folder_path):
    candle_tool_path = os.path.join(wix_folder_path, "candle.exe")
    light_tool_path = os.path.join(wix_folder_path, "light.exe")

    try:
        if not os.path.exists(wix_folder_path):
            raise Exception(f"Folder {wix_folder_path} does not exist. Start DownloadAndExtractWix.ps1 script to create it.")

        if not (os.path.exists(candle_tool_path) and os.path.exists(light_tool_path)):
            raise Exception("Tools required to build installer (candle.exe and light.exe) do not exist in wix folder.")

        wxs_file_name = "Product.wxs"
        wixobj_file_name = "build/Product.wixobj"
        msi_file_name = "build/matexecutable.msi"

        # compiling wxs file into wixobj
        subprocess.run([candle_tool_path, wxs_file_name, "-out", wixobj_file_name], check=True)

        # linking wixobj into msi
        subprocess.run([light_tool_path, wixobj_file_name, "-out", msi_file_name, "-ext", "WixUIExtension"], check=True)
    except Exception as e:
        print(e)
        exit(1)

download_wix("https://github.com/wixtoolset/wix3/releases/download/wix3112rtm/wix311-binaries.zip", "wix.zip")
build_installer(os.path.join(os.getcwd(), "wix"))