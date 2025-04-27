## InterchangeTransformAnimationTrackNode Objects

```python
class InterchangeTransformAnimationTrackNode(InterchangeAnimationTrackNode)
```

Class to represent an animation on the transform of a camera, light, or scene node.

**C++ Source:**

- **Plugin**: Interchange
- **Module**: InterchangeNodes
- **File**: InterchangeAnimationTrackSetNode.h

<a id="unreal.InterchangeTransformAnimationTrackNode.set_custom_used_channels"></a>

#### set_custom_used_channels

```python
def set_custom_used_channels(attribute_value: int) -> bool
```

x.set_custom_used_channels(attribute_value) -> bool
Set which channels of this animation should be used. This is a bitwise mask.
Bits are interpreted as follow:
   None          = 0x000,
   TranslationX  = 0x001,
   TranslationY  = 0x002,
   TranslationZ  = 0x004,
   Translation   = TranslationX | TranslationY | TranslationZ,
   RotationX     = 0x008,
   RotationY     = 0x010,
   RotationZ     = 0x020,
   Rotation      = RotationX | RotationY | RotationZ,
   ScaleX        = 0x040,
   ScaleY        = 0x080,
   ScaleZ        = 0x100,
   Scale         = ScaleX | ScaleY | ScaleZ,
   AllTransform  = Translation | Rotation | Scale,
   Weight        = 0x200,
   All           = Translation | Rotation | Scale | Weight,

Args:
    attribute_value (int32): 

Returns:
    bool:

<a id="unreal.InterchangeTransformAnimationTrackNode.get_custom_used_channels"></a>

#### get_custom_used_channels

```python
def get_custom_used_channels() -> Optional[int]
```

x.get_custom_used_channels() -> int32 or None
Get which channels of this animation should be used. This is a bitmask.
See SetCustomUsedChannels for description of bitmask

Returns:
    int32 or None: 

    attribute_value (int32):

<a id="unreal.InterchangeSkeletalAnimationTrackNode"></a>