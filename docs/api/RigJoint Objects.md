## RigJoint Objects

```python
class RigJoint(RigBone)
```

deprecated: 'RigJoint' was renamed to 'RigBone'.

<a id="unreal.RigJoint.__init__"></a>

#### __init__

```python
def __init__(name: Name = "None",
             index: int = 0,
             parent_name: Name = "None",
             initial_transform: Transform = [[0.000000, 0.000000, 0.000000],
                                             [-0.000000, 0.000000, 0.000000],
                                             [1.000000, 1.000000, 1.000000]],
             global_transform: Transform = [[0.000000, 0.000000, 0.000000],
                                            [-0.000000, 0.000000, 0.000000],
                                            [1.000000, 1.000000, 1.000000]],
             local_transform: Transform = [[0.000000, 0.000000, 0.000000],
                                           [-0.000000, 0.000000, 0.000000],
                                           [1.000000, 1.000000, 1.000000]],
             type: RigBoneType = RigBoneType.IMPORTED) -> None
```

<a id="unreal.RigConnectionRule"></a>