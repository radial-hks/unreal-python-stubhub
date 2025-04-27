## HasCustomNavigableGeometry Objects

```python
class HasCustomNavigableGeometry(EnumBase)
```

Determines if, and how, a navigation element should export collision for AI navigation

**C++ Source:**

- **Module**: Engine
- **File**: NavRelevantInterface.h

<a id="unreal.HasCustomNavigableGeometry.NO"></a>

#### NO

0: Element custom geometry export callback is not called, but the default collision export is performed using its convex/trimesh collision.

<a id="unreal.HasCustomNavigableGeometry.YES"></a>

#### YES

1: The custom geometry export callback is called and indicates if the default collision export should also be performed.

<a id="unreal.HasCustomNavigableGeometry.EVEN_IF_NOT_COLLIDABLE"></a>

#### EVEN_IF_NOT_COLLIDABLE

2: The custom geometry export callback is called even if the mesh is non-collidable and wouldn't normally affect the navigation data.

<a id="unreal.HasCustomNavigableGeometry.DONT_EXPORT"></a>

#### DONT_EXPORT

3: Neither the custom geometry export delegate nor the default export will be called (can still add modifiers through the NavigationData export callback).

<a id="unreal.NavDataGatheringMode"></a>