from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from compas_fea2.model.elements import BeamElement
from compas_fea2.model.elements import MassElement
from compas_fea2.model.elements import MembraneElement
from compas_fea2.model.elements import ShellElement
from compas_fea2.model.elements import _Element3D
from compas_fea2.model.elements import SpringElement
from compas_fea2.model.elements import StrutElement
from compas_fea2.model.elements import TieElement
from compas_fea2.model.elements import TrussElement


class AnsysBeamElement(BeamElement):
    """Ansys implementation of :class:`compas_fea2.model.elements.BeamElement`.\n
    """
    __doc__ += BeamElement.__doc__

    def __init__(self, *, nodes, section, frame=None, part=None, name=None, **kwargs):
        super(AnsysBeamElement, self).__init__(nodes=nodes, section=section, frame=frame, part=part, name=name, **kwargs)
        raise NotImplementedError

    def _generate_jobdata(self):
        raise NotImplementedError


class AnsysMassElement(MassElement):
    """Ansys implementation of :class:`compas_fea2.model.elements.MassElement`.\n
    """
    __doc__ += MassElement.__doc__

    def __init__(self, *, nodes, section, frame=None, part=None, name=None, **kwargs):
        super(AnsysMassElement, self).__init__(nodes=nodes, section=section, frame=frame, part=part, name=name, **kwargs)
        raise NotImplementedError

    def _generate_jobdata(self):
        raise NotImplementedError


class AnsysSpringElement(SpringElement):
    """Ansys implementation of :class:`compas_fea2.model.elements.SpringElement`.\n
    """
    __doc__ += SpringElement.__doc__

    def __init__(self, *, nodes, section, frame=None, part=None, name=None, **kwargs):
        super(AnsysSpringElement, self).__init__(nodes=nodes,
                                                 section=section, frame=frame, part=part, name=name, **kwargs)
        raise NotImplementedError

    def _generate_jobdata(self):
        raise NotImplementedError


class AnsysStrutElement(StrutElement):
    """Ansys implementation of :class:`compas_fea2.model.elements.StrutElement`.\n
    """
    __doc__ += StrutElement.__doc__

    def __init__(self, *, nodes, section, frame=None, part=None, name=None, **kwargs):
        super(AnsysStrutElement, self).__init__(nodes=nodes, section=section, frame=frame, part=part, name=name, **kwargs)
        raise NotImplementedError

    def _generate_jobdata(self):
        raise NotImplementedError


class AnsysTieElement(TieElement):
    """Ansys implementation of :class:`compas_fea2.model.elements.TieElement`.\n
    """
    __doc__ += TieElement.__doc__

    def __init__(self, *, nodes, section, frame=None, part=None, name=None, **kwargs):
        super(AnsysTieElement, self).__init__(nodes=nodes, section=section, frame=frame, part=part, name=name, **kwargs)
        raise NotImplementedError

    def _generate_jobdata(self):
        raise NotImplementedError


class AnsysTrussElement(TrussElement):
    """Ansys implementation of :class:`compas_fea2.model.elements.TrussElement`.\n
    """
    __doc__ += TrussElement.__doc__

    def __init__(self, *, nodes, section, frame=None, part=None, name=None, **kwargs):
        super(AnsysTrussElement, self).__init__(nodes=nodes, section=section, frame=frame, part=part, name=name, **kwargs)
        raise NotImplementedError

    def _generate_jobdata(self):
        raise NotImplementedError


class AnsysMembraneElement(MembraneElement):
    """Ansys implementation of :class:`compas_fea2.model.elements.MembraneElement`.\n
    """
    __doc__ += MembraneElement.__doc__

    def __init__(self, *, nodes, section, frame=None, part=None, name=None, **kwargs):
        super(AnsysMembraneElement, self).__init__(nodes=nodes,
                                                   section=section, frame=frame, part=part, name=name, **kwargs)
        raise NotImplementedError

    def _generate_jobdata(self):
        raise NotImplementedError


class AnsysShellElement(ShellElement):
    """Ansys implementation of :class:`compas_fea2.model.elements.ShellElement`.\n
    """
    __doc__ += ShellElement.__doc__

    def __init__(self, *, nodes, section, frame=None, part=None, name=None, **kwargs):
        super(AnsysShellElement, self).__init__(nodes=nodes, section=section, frame=frame, part=part, name=name, **kwargs)
        raise NotImplementedError

    def _generate_jobdata(self):
        raise NotImplementedError


class _AnsysElement3D(_Element3D):
    """Ansys implementation of :class:`compas_fea2.model.elements._Element3D`.\n
    """
    __doc__ += _Element3D.__doc__

    def __init__(self, *, nodes, section, frame=None, part=None, name=None, **kwargs):
        super(_AnsysElement3D, self).__init__(nodes=nodes, section=section, frame=frame, part=part, name=name, **kwargs)
        raise NotImplementedError

    def _generate_jobdata(self):
        raise NotImplementedError
