import zipfile

zip_path = "/teamspace/studios/this_studio/MPV3D.zip"

print("Checking zip integrity...")
print(zipfile.is_zipfile(zip_path))  # must be True

with zipfile.ZipFile(zip_path, 'r') as z:
    z.extractall("/teamspace/studios/this_studio/M3D-VTON")

print("Done")
