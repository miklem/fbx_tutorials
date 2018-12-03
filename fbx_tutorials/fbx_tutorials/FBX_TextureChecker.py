import fbx as fbx
from PIL import Image
import sys

filePath = r'E:\GoogleDrive\Dev\Code\fbx_tutorials\fbx_tutorials\fbx_tutorials\sample_model\cubeMan.fbx'

validTextureDimentions = [(256, 256), (512, 512)]
manager = fbx.FbxManager.Create()

importer = fbx.FbxImporter.Create(manager, 'fbxFileImporter')
status = importer.Initialize(filePath)
if not status:
    print "FbxImporter init failed."
    sys.exit()

scene = fbx.FbxScene.Create(manager, "FBXScene")
importer.Import(scene)
importer.Destroy()

textureArray = fbx.FbxTextureArray()

scene.FillTextureArray(textureArray)
invalidTextures = {}

for i in range(0, textureArray.GetCount()):
    texture = textureArray.GetAt(i)
    if texture.ClassId == fbx.FbxFileTexture.ClassId:
        textureFileName = texture.GetFileName()
        image = Image.open(textureFileName)
        width, height = image.size
        if (width, height) not in validTextureDimentions:
            invalidTextures[textureFileName] = (width, height)
            print "Invalid texture size (%s,%s) - %s" % (width, height, textureFileName)
