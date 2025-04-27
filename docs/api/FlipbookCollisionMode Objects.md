## FlipbookCollisionMode Objects

```python
class FlipbookCollisionMode(EnumBase)
```

EFlipbook Collision Mode

**C++ Source:**

- **Plugin**: Paper2D
- **Module**: Paper2D
- **File**: PaperFlipbook.h

<a id="unreal.FlipbookCollisionMode.NO_COLLISION"></a>

#### NO_COLLISION

0: The flipbook has no collision

<a id="unreal.FlipbookCollisionMode.FIRST_FRAME_COLLISION"></a>

#### FIRST_FRAME_COLLISION

1: The flipbook has non-animated collision based on the first frame of the animation

<a id="unreal.FlipbookCollisionMode.EACH_FRAME_COLLISION"></a>

#### EACH_FRAME_COLLISION

2: The flipbook changes collision each frame based on the animation (Note: This setting is not recommended and is very expensive, recreating the physics state every frame)

<a id="unreal.SpriteCollisionMode"></a>