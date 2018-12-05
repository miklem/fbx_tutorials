import fbx
import sys

filePath = r'E:\GoogleDrive\Dev\Code\fbx_tutorials\sample_model_2\cubeMan_UV.fbx'

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
print root.GetChildCount()
for i in range(root.GetChildCount()):
    print root.GetChild(i)

child = root.GetChild(0)
print child.GetName()  # chest
mesh = child.GetNodeAttribute()

polyCount = mesh.GetPolygonCount()

layerCount = mesh.GetLayerCount()
print layerCount


def checkTranslation(matrix=None, node=None):
    if matrix and node:
        if any(val != 0 for val in matrix):
            print " found offset %s at: %s" % (matrix, node.GetName())


# def checkUV01(node=None):
#     if node:
#         checkUVs = [j for i in uv_values for j in i if (j > 1.0 or j < 0.0)]
#         if len(checkUVs) > 0:
#             print checkUVs


def get_all_nodes(node):
    nodes.append(node)
    for i in range(0, node.GetChildCount()):
        get_all_nodes(node.GetChild(i))


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
    # print uv_values

    # #classical for cycle
    # checkUVs = []
    # for i in uv_values:
    #     for j in i:
    #         if j > 1.0 or j < 0.0:
    #             checkUVs.append(j)
    #
    # print checkUVs

    checkUVs = [j for i in uv_values for j in i if (j > 1.0 or j < 0.0)]
    print checkUVs
    if len(checkUVs) > 0:
        print checkUVs



nodes = []  # type: List[fbx.FbxNode]


get_all_nodes(root)
print nodes




#
#transformation
#
for node in nodes:  # type: fbx.FbxNode
    mesh = node.GetNodeAttribute()
    geometry = fbx.FbxGeometryConverter(manager)
    mesh = geometry.Triangulate(mesh, True)
    # print attribute
    # print node.GetNodeAttribute()
    lTMPVector = node.GetGeometricTranslation(fbx.FbxNode.eSourcePivot)  # type: fbx.FbxVector4
    position = [lTMPVector[0], lTMPVector[1], lTMPVector[2]]
    # print position
    localMatrix = node.EvaluateLocalTranslation()  # type: fbx.FbxVector4
    localMatrix = [localMatrix[0], localMatrix[1], localMatrix[2]]
    checkTranslation(localMatrix, node)











