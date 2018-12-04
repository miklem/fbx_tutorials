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
print polyCount  # 6
layerCount = mesh.GetLayerCount()
print layerCount

# UV
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
    print uv_values

    #classical for cycle
    checkUVs = []
    for i in uv_values:
        for j in i:
            if j > 1.0 or j < 0.0:
                checkUVs.append(j)
    #
    print checkUVs
    #same result
    checkUVs = [j for i in uv_values for j in i if (j > 1.0 or j < 0.0)]
    print checkUVs


def get_all_nodes(node, currentpath=[]):
    currentpath.append(node.GetName())
    print "Path: %s" % currentpath
    for i in range(0, node.GetChildCount()):
        get_all_nodes(node.GetChild(i), currentpath)
    currentpath.pop()


print get_all_nodes(root)

