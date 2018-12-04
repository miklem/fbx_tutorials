import fbx as fbx
from PIL import Image
import sys

filePath = r'E:\GoogleDrive\Dev\Code\fbx_tutorials\sample_model_2\cubeMan_noFbm.fbx'
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
def findTextureOnNodes( node, textureDictionary, currentPath = []):
    if False:
        node = fbx.FbxNode()
        mesh = fbx.FbxMesh()

    currentPath.append(node.GetName())
    #print "Path: %s" %currentPath

    for materialIndex in range(0, node.GetMaterialCount()):
        material = node.GetMaterial(materialIndex)
        #print '\material: %s'% material.GetName()
        for propertyIndex in range(0, fbx.FbxLayerElement.sTypeTextureCount()):
            property = material.FindProperty( fbx.FbxLayerElement.sTextureChannelNames(propertyIndex))
            if property.GetName() != '':
                pass
                #print "Property: %s" % property.GetName()
            for textureIndex in range(0, property.GetSrcObjectCount()):
                texture = property.GetSrcObject(textureIndex)
                #print "Texture: %s" % texture.GetFileName()
                print 'Texture (%sx%s) found at: %s > %s > %s > "%s"' % (width, height, currentPath, material.GetName(), property.GetName(), textureFileName )



    print ''

    for i in range(0, node.GetChildCount()):
        findTextureOnNodes(node.GetChild(i), textureDictionary, currentPath)
    currentPath.pop()

findTextureOnNodes(scene.GetRootNode(), invalidTextures)


def getUV(node, allNodes = [] ):
    if False:
        node = fbx.FbxNode()
        mesh = fbx.FbxMesh()
    allNodes.append(node.GetName())
    if mesh.GetElementUVCount()>0:
        container = mesh.GetElementUV(0)
        print container

    for i in range(0, node.GetChildCount()):
        getUV(node.GetChild(i), allNodes)
    allNodes.pop()




