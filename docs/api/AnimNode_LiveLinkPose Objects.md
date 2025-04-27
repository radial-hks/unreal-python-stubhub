## AnimNode_LiveLinkPose Objects

```python
class AnimNode_LiveLinkPose(AnimNode_Base)
```

Anim Node Live Link Pose

**C++ Source:**

- **Module**: LiveLinkAnimationCore
- **File**: AnimNode_LiveLinkPose.h

**Editor Properties:** (see get_editor_property/set_editor_property)

- ``do_live_link_evaluation`` (bool):  [Read-Write]
- ``input_pose`` (PoseLink):  [Read-Write]
- ``live_link_subject_name`` (LiveLinkSubjectName):  [Read-Write]
- ``retarget_asset`` (type(Class)):  [Read-Write]

<a id="unreal.AnimNode_LiveLinkPose.__init__"></a>

#### __init__

```python
def __init__(input_pose: PoseLink = [],
             live_link_subject_name: LiveLinkSubjectName = ["None"],
             do_live_link_evaluation: bool = False,
             retarget_asset: Class = None) -> None
```

<a id="unreal.AnimNode_LiveLinkPose.input_pose"></a>

#### input_pose

```python
@property
def input_pose() -> PoseLink
```

(PoseLink):  [Read-Write]

<a id="unreal.AnimNode_LiveLinkPose.input_pose"></a>

#### input_pose

```python
@input_pose.setter
def input_pose(value: PoseLink) -> None
```

<a id="unreal.AnimNode_LiveLinkPose.live_link_subject_name"></a>

#### live_link_subject_name

```python
@property
def live_link_subject_name() -> LiveLinkSubjectName
```

(LiveLinkSubjectName):  [Read-Write]

<a id="unreal.AnimNode_LiveLinkPose.live_link_subject_name"></a>

#### live_link_subject_name

```python
@live_link_subject_name.setter
def live_link_subject_name(value: LiveLinkSubjectName) -> None
```

<a id="unreal.AnimNode_LiveLinkPose.do_live_link_evaluation"></a>

#### do_live_link_evaluation

```python
@property
def do_live_link_evaluation() -> bool
```

(bool):  [Read-Write]

<a id="unreal.AnimNode_LiveLinkPose.do_live_link_evaluation"></a>

#### do_live_link_evaluation

```python
@do_live_link_evaluation.setter
def do_live_link_evaluation(value: bool) -> None
```

<a id="unreal.AnimNode_LiveLinkPose.retarget_asset"></a>

#### retarget_asset

```python
@property
def retarget_asset() -> Class
```

(type(Class)):  [Read-Write]

<a id="unreal.AnimNode_LiveLinkPose.retarget_asset"></a>

#### retarget_asset

```python
@retarget_asset.setter
def retarget_asset(value: Class) -> None
```

<a id="unreal.LiveLinkInnerTestInternal"></a>