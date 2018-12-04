import fbx
import sys


filePath = r'E:\GoogleDrive\Dev\Code\fbx_tutorials\sample_model_2\cubeMan_noFbm.fbx'

class FBXLoadModel(object):
    def __init__(self, filepath=None):
        if not filepath:
            filepath = r'E:\GoogleDrive\Dev\Code\fbx_tutorials\sample_model_2\cubeMan_noFbm.fbx'
        self.model = None
        self.manager = fbx.FbxManager.Create()
        self.importer = fbx.FbxImporter.Create(self.manager, 'fbxFileImporter')
        self.status = self.importer.Initialize(filepath)
        if not self.status:
            print "FbxImporter init failed."
            sys.exit()
        self.scene = fbx.FbxScene.Create(self.manager, "FBXScene")
        self.importer.Import(self.scene)
        self.importer.Destroy()
        self.allNodes = []

    def get_all_nodes(self, node, currentpath=[]):
        currentpath.append(node.GetName())
        print "Path: %s" % currentpath
        for i in range(0, node.GetChildCount()):
            self.allNodes.append(node.GetChild(i))
            self.get_all_nodes(node.GetChild(i), currentpath)

        currentpath.pop()

    def get_mesh(self):
        if False:
            root = fbx.FbxNode()
            child = fbx.FbxNode()
        root = self.scene.GetRootNode()
        child = root.GetChild(0)









test_fbx = FBXLoadModel(filePath)
test_fbx.get_all_nodes(test_fbx.scene.GetRootNode())
var = test_fbx.allNodes[:-1]    # remove root node
print var





