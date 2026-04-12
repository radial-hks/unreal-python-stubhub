## FBXAnimationLengthImportType Objects

```python
class FBXAnimationLengthImportType(EnumBase)
```

Animation length type when importing

**C++ Source:**

- **Module**: UnrealEd
- **File**: FbxAnimSequenceImportData.h

<a id="unreal.FBXAnimationLengthImportType.FBXALIT_EXPORTED_TIME"></a>

#### FBXALIT\_EXPORTED\_TIME

0: This option imports animation frames based on what is defined at the time of export

<a id="unreal.FBXAnimationLengthImportType.FBXALIT_ANIMATED_KEY"></a>

#### FBXALIT\_ANIMATED\_KEY

1: Will import the range of frames that have animation. Can be useful if the exported range is longer than the actual animation in the FBX file

<a id="unreal.FBXAnimationLengthImportType.FBXALIT_SET_RANGE"></a>

#### FBXALIT\_SET\_RANGE

2: This will enable the Start Frame and End Frame properties for you to define the frames of animation to import

<a id="unreal.FbxExportCompatibility"></a>