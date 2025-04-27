## RigVMCommentNode Objects

```python
class RigVMCommentNode(RigVMNode)
```

Comment Nodes can be used to annotate a Graph by adding
colored grouping as well as user provided text.
Comment Nodes are purely cosmetic and don't contribute
to the runtime result of the Graph / Function.

**C++ Source:**

- **Plugin**: RigVM
- **Module**: RigVMDeveloper
- **File**: RigVMCommentNode.h

<a id="unreal.RigVMCommentNode.get_comment_text"></a>

#### get_comment_text

```python
def get_comment_text() -> str
```

x.get_comment_text() -> str
Returns the current user provided text of this comment.

Returns:
    str:

<a id="unreal.RigVMCommentNode.get_comment_font_size"></a>

#### get_comment_font_size

```python
def get_comment_font_size() -> int
```

x.get_comment_font_size() -> int32
Returns the current user provided font size of this comment.

Returns:
    int32:

<a id="unreal.RigVMCommentNode.get_comment_color_bubble"></a>

#### get_comment_color_bubble

```python
def get_comment_color_bubble() -> bool
```

x.get_comment_color_bubble() -> bool
Returns the current user provided bubble color inheritance of this comment.

Returns:
    bool:

<a id="unreal.RigVMCommentNode.get_comment_bubble_visible"></a>

#### get_comment_bubble_visible

```python
def get_comment_bubble_visible() -> bool
```

x.get_comment_bubble_visible() -> bool
Returns the current user provided bubble visibility of this comment.

Returns:
    bool:

<a id="unreal.RigVMDispatchNode"></a>