from dal import forward


class Function(forward.Forward):

    type = "const"

    def __init__(self, func, dst):
        """Instantiate a forwarded constant value."""
        self.func = func
        self.dst = dst

    def to_dict(self):
        """Convert to dictionary which will be rendered as JSON."""
        d = super(Function, self).to_dict()

        d.update(val=self.func())
        d.update(dst=self.dst)

        return d


class Nested(forward.Forward):

    type = "nested"

    def __init__(self, val, dst):
        """Instantiate a forwarded constant value."""
        self.val = val
        self.dst = dst

    def to_dict(self):
        """Convert to dictionary which will be rendered as JSON."""
        d = super().to_dict()

        d.update(val=self.val)
        if isinstance(self.dst, forward.Forward):
            d.update(dst=self.dst.to_dict())

        return d


class Field(forward.Field):

    type = "field"

    def __init__(self, src, dst=None, default=None):
        """Instantiate a forwarded field value."""
        self.src = src
        self.dst = dst
        self.default = None

    def to_dict(self):
        """Convert to dictionary which will be rendered as JSON."""
        d = super(Field, self).to_dict()

        d.update(src=self.src)
        if self.dst is not None:
            d.update(dst=self.dst)

        return d
