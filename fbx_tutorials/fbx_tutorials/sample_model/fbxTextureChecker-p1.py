import fbx
# import Image
import sys

filepath = r'E:\GoogleDrive\Dev\Code\fbx_sdk_tutorials\sample_model\cubeMan.fbx'

validTextureDimensions = [ (256, 256), (512, 512) ]

manager = fbx.FbxManager.Create()

importer = fbx.FbxImporter.Create( manager, 'myImporter' )

status = importer.Initialize( filepath )

if status == False:
    print 'FbxImporter initialization failed.'
    print 'Error: %s' % importer.GetLastErrorString()
    sys.exit()


scene = fbx.FbxScene.Create( manager, 'myScene' )

importer.Import( scene )

importer.Destroy()

textureArray = fbx.FbxTextureArray()

scene.FillTextureArray( textureArray )

invalidTextures = {}

for i in range( 0, textureArray.GetCount() ):
    
    texture = textureArray.GetAt( i )
    
    if texture.ClassId == fbx.FbxFileTexture.ClassId:
        
        textureFilename = texture.GetFileName()
        
        # image = Image.open( textureFilename )
        
         # width, height = image.size
        width, height = 800, 800
        if (width, height) not in validTextureDimensions:
            
            invalidTextures[ textureFilename ] = (width, height)
            
            print 'Invalid dimensions (%sx%s) - %s\n' % (width, height, textureFilename )









