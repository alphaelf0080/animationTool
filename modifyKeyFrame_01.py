import maya.cmds as cmds
import pymel.core as pm

###set start and end frame
startFrame = 1
endFrame =120
#singleObj = 'pSphere1'


objectList = pm.ls(sl=True,type= 'transform')
#for i in objectList:
  #  print i



###write dict from select obj and channel
objKeyFrameDict = {}

for singleObj in objectList:
    #print singleObj


    objKeyFrame = cmds.keyframe( '%s.rotateY'%singleObj ,t=(startFrame,endFrame),query=True )
    #print objKeyFrame

    singleObjByFrameDict= {}
    for byFrmae in objKeyFrame:
        atValue =  cmds.keyframe(str(singleObj),at=['translateX','translateY','translateZ','rotateX','rotateY','rotateZ'],t=(byFrmae,byFrmae),q=True,eval=True)
        singleObjByFrameDict.update({byFrmae:atValue})
    #fixNameA =  singleObj.split("u'") 
    #fixNameB =  fixNameA.split(("')")[0]
   # print fixNameA
    objKeyFrameDict.update({singleObj[0:]:singleObjByFrameDict})
    
for singleObj in objKeyFrameDict.keys():
   # print singleObj
   # print objKeyFrameDict[singleObj]
    
    

    cmds.cutKey(singleObj,at=['translateX','translateY','translateZ','rotateX','rotateY','rotateZ'],cl=True) ##clear key
    
    for byFrame in objKeyFrame:   
       # print byFrame 
       ###get key from dict
        translateX_value = objKeyFrameDict[singleObj][byFrame][0]
        translateY_value = objKeyFrameDict[singleObj][byFrame][1]
        translateZ_value = objKeyFrameDict[singleObj][byFrame][2]
        rotataX_value = objKeyFrameDict[singleObj][byFrame][3]
        rotataY_value = objKeyFrameDict[singleObj][byFrame][4]
        rotataZ_value = objKeyFrameDict[singleObj][byFrame][5]
       # print rotataY_value
        #cmds.select('pSphere10_2')
        ### switch or copy key to other channel
        cmds.setKeyframe(singleObj,at='translateX',v=translateX_value,t=byFrame,e=True)
        cmds.setKeyframe(singleObj,at='translateY',v=translateY_value,t=byFrame,e=True)
        cmds.setKeyframe(singleObj,at='translateZ',v=translateZ_value,t=byFrame,e=True)

        cmds.setKeyframe(singleObj,at='rotateX',v=rotataX_value,t=byFrame,e=True)
        cmds.setKeyframe(singleObj,at='rotateY',v=rotataZ_value*0,t=byFrame,e=True)
        cmds.setKeyframe(singleObj,at='rotateZ',v=rotataY_value*-1,t=byFrame,e=True)



              }
    
