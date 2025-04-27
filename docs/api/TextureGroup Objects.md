## TextureGroup Objects

```python
class TextureGroup(EnumBase)
```

warning:: if this is changed: update BaseEngine.ini [SystemSettings] you might have to update the update Game's DefaultEngine.ini [SystemSettings] order and actual name can never change (order is important!) TEXTUREGROUP_Cinematic: should be used for Cinematics which will be baked out and want to have the highest settings

**C++ Source:**

- **Module**: Engine
- **File**: TextureDefines.h

<a id="unreal.TextureGroup.TEXTUREGROUP_WORLD"></a>

#### TEXTUREGROUP_WORLD

0

<a id="unreal.TextureGroup.TEXTUREGROUP_WORLD_NORMAL_MAP"></a>

#### TEXTUREGROUP_WORLD_NORMAL_MAP

1

<a id="unreal.TextureGroup.TEXTUREGROUP_WORLD_SPECULAR"></a>

#### TEXTUREGROUP_WORLD_SPECULAR

2

<a id="unreal.TextureGroup.TEXTUREGROUP_CHARACTER"></a>

#### TEXTUREGROUP_CHARACTER

3

<a id="unreal.TextureGroup.TEXTUREGROUP_CHARACTER_NORMAL_MAP"></a>

#### TEXTUREGROUP_CHARACTER_NORMAL_MAP

4

<a id="unreal.TextureGroup.TEXTUREGROUP_CHARACTER_SPECULAR"></a>

#### TEXTUREGROUP_CHARACTER_SPECULAR

5

<a id="unreal.TextureGroup.TEXTUREGROUP_WEAPON"></a>

#### TEXTUREGROUP_WEAPON

6

<a id="unreal.TextureGroup.TEXTUREGROUP_WEAPON_NORMAL_MAP"></a>

#### TEXTUREGROUP_WEAPON_NORMAL_MAP

7

<a id="unreal.TextureGroup.TEXTUREGROUP_WEAPON_SPECULAR"></a>

#### TEXTUREGROUP_WEAPON_SPECULAR

8

<a id="unreal.TextureGroup.TEXTUREGROUP_VEHICLE"></a>

#### TEXTUREGROUP_VEHICLE

9

<a id="unreal.TextureGroup.TEXTUREGROUP_VEHICLE_NORMAL_MAP"></a>

#### TEXTUREGROUP_VEHICLE_NORMAL_MAP

10

<a id="unreal.TextureGroup.TEXTUREGROUP_VEHICLE_SPECULAR"></a>

#### TEXTUREGROUP_VEHICLE_SPECULAR

11

<a id="unreal.TextureGroup.TEXTUREGROUP_CINEMATIC"></a>

#### TEXTUREGROUP_CINEMATIC

12

<a id="unreal.TextureGroup.TEXTUREGROUP_EFFECTS"></a>

#### TEXTUREGROUP_EFFECTS

13

<a id="unreal.TextureGroup.TEXTUREGROUP_EFFECTS_NOT_FILTERED"></a>

#### TEXTUREGROUP_EFFECTS_NOT_FILTERED

14

<a id="unreal.TextureGroup.TEXTUREGROUP_SKYBOX"></a>

#### TEXTUREGROUP_SKYBOX

15

<a id="unreal.TextureGroup.TEXTUREGROUP_UI"></a>

#### TEXTUREGROUP_UI

16

<a id="unreal.TextureGroup.TEXTUREGROUP_LIGHTMAP"></a>

#### TEXTUREGROUP_LIGHTMAP

17

<a id="unreal.TextureGroup.TEXTUREGROUP_RENDER_TARGET"></a>

#### TEXTUREGROUP_RENDER_TARGET

18

<a id="unreal.TextureGroup.TEXTUREGROUP_MOBILE_FLATTENED"></a>

#### TEXTUREGROUP_MOBILE_FLATTENED

19

<a id="unreal.TextureGroup.TEXTUREGROUP_PROC_BUILDING_FACE"></a>

#### TEXTUREGROUP_PROC_BUILDING_FACE

20: Obsolete - kept for backwards compatibility.

<a id="unreal.TextureGroup.TEXTUREGROUP_PROC_BUILDING_LIGHT_MAP"></a>

#### TEXTUREGROUP_PROC_BUILDING_LIGHT_MAP

21: Obsolete - kept for backwards compatibility.

<a id="unreal.TextureGroup.TEXTUREGROUP_SHADOWMAP"></a>

#### TEXTUREGROUP_SHADOWMAP

22

<a id="unreal.TextureGroup.TEXTUREGROUP_COLOR_LOOKUP_TABLE"></a>

#### TEXTUREGROUP_COLOR_LOOKUP_TABLE

23: No compression, no mips.

<a id="unreal.TextureGroup.TEXTUREGROUP_TERRAIN_HEIGHTMAP"></a>

#### TEXTUREGROUP_TERRAIN_HEIGHTMAP

24

<a id="unreal.TextureGroup.TEXTUREGROUP_TERRAIN_WEIGHTMAP"></a>

#### TEXTUREGROUP_TERRAIN_WEIGHTMAP

25

<a id="unreal.TextureGroup.TEXTUREGROUP_BOKEH"></a>

#### TEXTUREGROUP_BOKEH

26: Using this TextureGroup triggers special mip map generation code only useful for the BokehDOF post process.

<a id="unreal.TextureGroup.TEXTUREGROUP_IES_LIGHT_PROFILE"></a>

#### TEXTUREGROUP_IES_LIGHT_PROFILE

27: No compression, created on import of a .IES file.

<a id="unreal.TextureGroup.TEXTUREGROUP_PIXELS2D"></a>

#### TEXTUREGROUP_PIXELS2D

28: Non-filtered, useful for 2D rendering.

<a id="unreal.TextureGroup.TEXTUREGROUP_HIERARCHICAL_LOD"></a>

#### TEXTUREGROUP_HIERARCHICAL_LOD

29: Hierarchical LOD generated textures

<a id="unreal.TextureGroup.TEXTUREGROUP_IMPOSTOR"></a>

#### TEXTUREGROUP_IMPOSTOR

30: Impostor Color Textures

<a id="unreal.TextureGroup.TEXTUREGROUP_IMPOSTOR_NORMAL_DEPTH"></a>

#### TEXTUREGROUP_IMPOSTOR_NORMAL_DEPTH

31: Impostor Normal and Depth, use default compression

<a id="unreal.TextureGroup.TEXTUREGROUP_8_BIT_DATA"></a>

#### TEXTUREGROUP_8_BIT_DATA

32: 8 bit data stored in textures

<a id="unreal.TextureGroup.TEXTUREGROUP_16_BIT_DATA"></a>

#### TEXTUREGROUP_16_BIT_DATA

33: 16 bit data stored in textures

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT01"></a>

#### TEXTUREGROUP_PROJECT01

34: Project specific group, rename in Engine.ini, [EnumRemap] TEXTUREGROUP_Project**.DisplayName=My Fun Group

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT02"></a>

#### TEXTUREGROUP_PROJECT02

35

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT03"></a>

#### TEXTUREGROUP_PROJECT03

36

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT04"></a>

#### TEXTUREGROUP_PROJECT04

37

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT05"></a>

#### TEXTUREGROUP_PROJECT05

38

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT06"></a>

#### TEXTUREGROUP_PROJECT06

39

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT07"></a>

#### TEXTUREGROUP_PROJECT07

40

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT08"></a>

#### TEXTUREGROUP_PROJECT08

41

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT09"></a>

#### TEXTUREGROUP_PROJECT09

42

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT10"></a>

#### TEXTUREGROUP_PROJECT10

43

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT11"></a>

#### TEXTUREGROUP_PROJECT11

44

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT12"></a>

#### TEXTUREGROUP_PROJECT12

45

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT13"></a>

#### TEXTUREGROUP_PROJECT13

46

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT14"></a>

#### TEXTUREGROUP_PROJECT14

47

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT15"></a>

#### TEXTUREGROUP_PROJECT15

48

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT16"></a>

#### TEXTUREGROUP_PROJECT16

49

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT17"></a>

#### TEXTUREGROUP_PROJECT17

50

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT18"></a>

#### TEXTUREGROUP_PROJECT18

51

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT19"></a>

#### TEXTUREGROUP_PROJECT19

52

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT20"></a>

#### TEXTUREGROUP_PROJECT20

53

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT21"></a>

#### TEXTUREGROUP_PROJECT21

54

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT22"></a>

#### TEXTUREGROUP_PROJECT22

55

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT23"></a>

#### TEXTUREGROUP_PROJECT23

56

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT24"></a>

#### TEXTUREGROUP_PROJECT24

57

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT25"></a>

#### TEXTUREGROUP_PROJECT25

58

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT26"></a>

#### TEXTUREGROUP_PROJECT26

59

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT27"></a>

#### TEXTUREGROUP_PROJECT27

60

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT28"></a>

#### TEXTUREGROUP_PROJECT28

61

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT29"></a>

#### TEXTUREGROUP_PROJECT29

62

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT30"></a>

#### TEXTUREGROUP_PROJECT30

63

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT31"></a>

#### TEXTUREGROUP_PROJECT31

64

<a id="unreal.TextureGroup.TEXTUREGROUP_PROJECT32"></a>

#### TEXTUREGROUP_PROJECT32

65

<a id="unreal.TextureDownscaleOptions"></a>