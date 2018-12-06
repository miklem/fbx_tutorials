import fbx
import sys

filePath = r'E:\GoogleDrive\Dev\Code\fbx_tutorials\sample_model_2\cubeMan_UV.fbx'
# filePath = r'Y:\DVS_3D\PROJECTS\2018_Projects\09_SIBUR\Development\Models\data\PE_Extrusion.fbx'
# filePath = 'C:/Users/mmiroshnichenko/Desktop/test.fbx'


manager = fbx.FbxManager.Create()
importer = fbx.FbxImporter.Create(manager, 'fbxFileImporter')
status = importer.Initialize(filePath)
if not status:
    print "FbxImporter init failed."
    sys.exit()
scene = fbx.FbxScene.Create(manager, "FBXScene")
importer.Import(scene)
importer.Destroy()

root = scene.GetRootNode()

# for i in range(root.GetChildCount()):
#     print root.GetChild(i)

# child = root.GetChild(0)
# mesh = child.GetNodeAttribute()

# polyCount = mesh.GetPolygonCount()





def checkTranslation(node=None):
    # lTMPVector = node.GetGeometricTranslation(fbx.FbxNode.eSourcePivot)  # type: fbx.FbxVector4
    # position = [lTMPVector[0], lTMPVector[1], lTMPVector[2]]
    # # print position
    localMatrix = node.EvaluateLocalTranslation()  # type: fbx.FbxVector4
    localMatrix = [localMatrix[0], localMatrix[1], localMatrix[2]]
    if localMatrix and node:
        if any(val != 0 for val in localMatrix):
            print " found offset %s at: %s" % (localMatrix, node.GetName())


def checkUV01(node=None):
    layerCount = mesh.GetLayerCount()
    for z in range(layerCount):
        mesh_uvs = mesh.GetLayer(z).GetUVs()
        if not mesh_uvs:
            continue
        uvs_array = mesh_uvs.GetDirectArray()
        uvs_count = uvs_array.GetCount()
        if uvs_count == 0:
            continue
        uv_values = []
        uv_indices = []

        for l in range(uvs_count):
            uv = uvs_array.GetAt(l)
            uv = [uv[0], uv[1]]
            uv_values.append(uv)
        if node:
            checkUVs = [j for i in uv_values for j in i if (j > 1.0 or j < 0.0)]
            if len(checkUVs) > 0:
                print "UVs outside 0..1 at: %s" % node.GetName()


def getAllNodes(node=None):
    if node:
        nodes.append(node)
        for i in range(0, node.GetChildCount()):
            getAllNodes(node.GetChild(i))

            #TODO: if type(node.GetNodeAttribute())==fbx.FbxNull
            # which is group in Maya, then check if there is any child nodes inside.
            # if none then move this node to a list with "delete later if you want" nodes.


def cleanUpNodes(node=None):
    print node.GetNodeAttribute()

nodes = []  # type: List[fbx.FbxNode]

getAllNodes(root)
print nodes


#store all empty folders to delete later
emptyGrps = []
for node in nodes:  # type: fbx.FbxNode
    mesh = node.GetNodeAttribute()  # type: fbx.FbxNode
    if not mesh:
        continue
    if type(mesh) == fbx.FbxNull:
        #store empty folders to delete it later
        emptyGrps.append([node, node.GetName()])

        continue
    # geometry = fbx.FbxGeometryConverter(manager)
    # mesh = geometry.Triangulate(mesh, True)
    # print attribute
    # print node.GetNodeAttribute()
    #Translation
    checkTranslation(node)
    #UV
    checkUV01(node)

print emptyGrps








