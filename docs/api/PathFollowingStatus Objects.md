## PathFollowingStatus Objects

```python
class PathFollowingStatus(EnumBase)
```

EPath Following Status

**C++ Source:**

- **Module**: AIModule
- **File**: PathFollowingComponent.h

<a id="unreal.PathFollowingStatus.IDLE"></a>

#### IDLE

0: No requests

<a id="unreal.PathFollowingStatus.WAITING"></a>

#### WAITING

1: Request with incomplete path, will start after UpdateMove()

<a id="unreal.PathFollowingStatus.PAUSED"></a>

#### PAUSED

2: Request paused, will continue after ResumeMove()

<a id="unreal.PathFollowingStatus.MOVING"></a>

#### MOVING

3: Following path

<a id="unreal.PathFollowingAction"></a>